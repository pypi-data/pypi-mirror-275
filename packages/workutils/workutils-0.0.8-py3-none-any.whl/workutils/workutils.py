# coding=utf-8
"""
@File    : workutils.py
@Time    : 2024/3/9 15:50
@Author  : MengYue Sun
@Description : A tool to solve daily work
"""
import os
import argparse
import re
import chardet
from tqdm import tqdm


def get_files_path(folder_path, file_suffix=None, all_files=False):
    """
    获取指定文件夹中的所有文件路径，默认所有文件，如传递参数，只处理指定后缀的文件

    Args:
        folder_path: 文件夹路径
        file_suffix: 文件后缀，默认为None表示所有文件
        all_files: 是否遍历所有文件，包括隐藏文件，默认为False

    Returns:
        包含所有文件路径的列表
    """

    log_files = []  # 用于存储所有文件路径
    file_types = {}  # 用于统计文件类型和数量

    try:
        for root, dirs, files in os.walk(folder_path):
            if not all_files:
                # 检查是否传递了-a参数，如果没有，去除隐藏文件夹
                dirs[:] = [d for d in dirs if not d.startswith('.')]
                files = [f for f in files if not f.startswith('.')]

            for file in files:
                if file_suffix is None or file.lower().endswith(f".{file_suffix}"):
                    # 如果没有指定后缀或文件后缀匹配指定的后缀，处理文件
                    file_path = os.path.join(root, file)
                    log_files.append(file_path)

                    # 获取文件类型
                    file_extension = os.path.splitext(file)[1].lower()
                    if file_extension not in file_types:
                        file_types[file_extension] = 1
                    else:
                        file_types[file_extension] += 1

        # 返回包含所有文件路径、文件类型和数量的列表
        return log_files, file_types
    except Exception as e:
        print(
            f'Error in get_files_path(folder_path, file_suffix="{file_suffix}", all_files={all_files}):{str(e)}'
        )


# 获取指定文件的编码格式
def get_file_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
            encoding = result['encoding']
            return encoding
    except Exception as e:
        print(f"Error in get_file_encoding(file_path): {str(e)}")


def show_file_counts(file_types, total_files=0):
    """
    打印每种类型的文件和数量，以及文件的总数。

    Args:
        file_types (dict): 包含文件类型和数量的字典。
        total_files (int): 文件总数。
    """
    print("=" * 50)
    print("{:<20}{}".format("Suffix", "Counts"))
    print("-" * 50)
    for file_type, count in file_types.items():
        print("{:<20}{}".format(file_type, count))
    print("-" * 50)
    print("{:<20}{}".format("Total", total_files))
    print("=" * 50)
    print()


def show_keyword_files(files, results):
    """
    打印每个文件名以及关键词匹配数量。

    Args:
        files (list): 文件路径列表。
        results (list): 含有每个文件关键词匹配数量的字典列表。
    """
    print("=" * 50)
    print("{:<20}{:<20}{}".format("Keyword", "Matches", "File Name"))
    print("-" * 50)
    for file, result in zip(files, results):
        file_name = os.path.basename(file)  # 获取文件名
        for keyword, matches in result.items():
            if matches > 0:
                print("{:<20}{:<20}{}".format(keyword, matches, file_name))
    print("-" * 50)
    print("=" * 50)
    print()


def get_key_words(file_path, keywords):
    list_results = []
    dict_keyword_counts = {keyword: 0 for keyword in keywords}

    try:
        encode = get_file_encoding(file_path)
        with open(file_path, "r", encoding=encode) as file:
            for line in file:
                for keyword in keywords:
                    escaped_keyword = re.escape(keyword)
                    matches = re.finditer(escaped_keyword, line, flags=re.IGNORECASE)
                    dict_keyword_counts[keyword] += len(list(matches))
            list_results.append(dict_keyword_counts)
        return list_results, dict_keyword_counts
    except FileNotFoundError:
        print(f"Error File {file_path} not found.")
        return [], {}
    except PermissionError:
        print(f"Error No permission to read file {file_path}.")
        return [], {}
    except Exception as e:
        print(f'Error in reading file: {e}')
        return [], {}


def convert_encoding(directory, extension, target_encoding):
    """
    递归处理指定目录及其子目录下所有指定后缀的文件，将文件编码转换为目标编码。
    :param directory: 指定目录路径
    :param extension: 指定文件后缀名，例如“.txt”
    :param target_encoding: 目标编码格式，例如 "utf-8"
    """
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                file_path = os.path.join(dirpath, filename)
                try:
                    original_encoding = get_file_encoding(file_path)
                    if original_encoding is None:
                        print(f"无法检测文件 {file_path} 的编码格式，跳过。")
                        continue

                    with open(file_path, 'r', encoding=original_encoding) as file:
                        content = file.read()

                    with open(file_path, 'w', encoding=target_encoding) as file:
                        file.write(content)

                    print(f"{file_path} 已成功从 {original_encoding} 转换为 {target_encoding} 编码格式。")

                except Exception as e:
                    print(f"处理文件 {file_path} 时出错: {e}")


def main():
    parser = argparse.ArgumentParser(description="A tool for daily work")
    subparsers = parser.add_subparsers(dest='action', required=True, help="选择操作类型：'convert', 'query' 或 'analyze'")

    # convert 子解析器
    parser_convert = subparsers.add_parser('convert', help='转换指定目录及其子目录中所有指定后缀的文件的编码格式')
    parser_convert.add_argument("directory", type=str, help="指定目录路径")
    parser_convert.add_argument("target_encoding", type=str, help="目标编码格式，例如 ‘utf-8’")
    parser_convert.add_argument("-s", "--suffix", type=str, required=True, help="指定文件后缀，例如 ‘.txt’")

    # query 子解析器
    parser_query = subparsers.add_parser('query', help='查询文件的编码格式')
    parser_query.add_argument("directory", type=str, help="指定文件路径")

    # analyze 子解析器
    parser_analyze = subparsers.add_parser('analyze', help='分析目录中的文件类型和关键词匹配情况')
    parser_analyze.add_argument("directory", type=str, help="指定目录路径")
    parser_analyze.add_argument("-s", "--suffix", type=str, help="指定文件后缀")
    parser_analyze.add_argument("-k", "--keywords", type=str, help="在所有文件中统计关键词，如 'key word1','key word2'")
    parser_analyze.add_argument("-a", "--all-files", action="store_true", help="遍历所有文件，包括隐藏文件")
    parser_analyze.add_argument("-o", "--output", type=str, help="保存结果文件路径")

    args = parser.parse_args()

    # Convert the incoming directory to an absolute path
    directory = os.path.abspath(args.directory)

    if args.action == 'convert':
        convert_encoding(directory, args.suffix, args.target_encoding)
    elif args.action == 'query':
        encoding = get_file_encoding(directory)
        if encoding:
            print(f"文件 {directory} 的编码格式是 {encoding}")
        else:
            print(f"无法检测文件 {directory} 的编码格式。")
    elif args.action == 'analyze':
        file_suffix = args.suffix
        list_keywords = [keyword.strip() for keyword in args.keywords.split(",")] if args.keywords else []
        all_files = args.all_files
        result_file = os.path.abspath(args.output) if args.output else None

        # Check if the specified path is a folder
        if not os.path.isdir(directory):
            print("指定的路径不是文件夹。")
            return

        files, types = get_files_path(directory, file_suffix, all_files)
        for file in files:
            print(file)

        # Calculate the total number of files
        total_files = len(files)

        # Print each type of file and quantity
        show_file_counts(types, total_files)

        keyword_results = []  # List to save keyword match results
        if list_keywords:  # Check if keyword parameters are passed
            with tqdm(total=total_files) as pbar:
                for file_path in files:
                    results, counts = get_key_words(file_path=file_path, keywords=list_keywords)
                    keyword_results.append((file_path, counts))
                    pbar.update(1)

            # Print keyword match results
            show_keyword_files([os.path.basename(file[0]) for file in keyword_results],
                                [file[1] for file in keyword_results])

        # Save the result to a file if output file is specified
        if result_file:
            try:
                with open(result_file, "w") as f:
                    for file in files:
                        f.write(file + "\n")
                    if list_keywords:
                        f.write("\nKeyword             Matches           File Name\n")
                        f.write("-" * 50)
                        f.write("\n")
                        for file_path, counts in keyword_results:
                            file_name = os.path.basename(file_path)
                            for keyword, matches in counts.items():
                                if matches > 0:
                                    f.write(f"{keyword:<20}{matches:<20}{file_name}\n")
                        f.write("-" * 50)
                print(f"The result has been saved to the {result_file} file.")
            except Exception as e:
                print(f"An error occurred while saving the result to the file: {e}")

if __name__ == "__main__":
    # Get the directory path of the current script file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Change the working directory to the directory where the script file is located
    os.chdir(script_dir)
    main()