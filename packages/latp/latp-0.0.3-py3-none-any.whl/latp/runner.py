# runner.py
# !/usr/bin/python3
# -*- coding: utf-8 -*-
import inspect
import os
import sys
import glob
import pytest
import importlib.util
import logging
import yaml
import re


def configure_logging(level, log_file, log_format):
    """
    配置日志记录。

    Args:
        level: 日志级别。
        log_file: 日志文件路径。
        log_format: 日志格式。
    """
    logging.basicConfig(level=level, format=log_format, filename=log_file, encoding='utf-8', filemode='w')
    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def load_config(config_file):
    """
    加载配置文件。

    Args:
        config_file: 配置文件路径。

    Returns:
        配置字典。
    """
    if not os.path.exists(config_file):
        config_file = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def find_modules_from_folder(folder, module_pattern):
    """
    从指定文件夹中查找符合模式的模块。

    Args:
        folder: 文件夹路径。
        module_pattern: 模块名称匹配模式（正则表达式）。

    Returns:
        模块名称和路径的列表。
    """
    absolute_f = os.path.abspath(folder)
    print(f"文件夹路径为: {absolute_f}")
    modules = glob.glob(os.path.join(absolute_f, "**", "*.py"), recursive=True)
    pattern = re.compile(module_pattern)
    return [(os.path.relpath(f, start=absolute_f)[:-3].replace(os.sep, '.'), f) for f in modules if
            os.path.isfile(f) and not f.endswith('__init__.py') and pattern.match(os.path.basename(f)[:-3])]


def import_modules_dynamically(module, file_path):
    """
    动态导入模块。

    Args:
        module: 模块名称。
        file_path: 文件路径。

    Returns:
        导入的模块对象。
    """
    spec = importlib.util.spec_from_file_location(module, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(args, test_path):
    """
    运行测试。

    Args:
        args: 命令行参数。
        test_path: 测试路径。
    """
    config_path = args.config if args.config else os.path.join(os.path.dirname(__file__), 'config.yaml')
    config = load_config(config_path)
    configure_logging(config['logging']['level'], config['logging']['file'], config['logging']['format'])
    logger = logging.getLogger(__name__)

    logger.info(f"加载的配置文件: {config_path}")
    logger.info(f"测试路径: {test_path}")

    keyword = args.k if args.k is not None else config['tests']['keyword_expression']
    mark = args.m if args.m is not None else config['tests']['mark_expression']

    module_pattern = config['tests']['module_pattern']
    class_pattern = config['tests']['class_pattern']
    function_pattern = config['tests']['function_pattern']

    logger.info(f"关键字过滤表达式: {keyword}")
    logger.info(f"标记过滤表达式: {mark}")
    logger.info(f"模块匹配模式: {module_pattern}")
    logger.info(f"类匹配模式: {class_pattern}")
    logger.info(f"函数/方法匹配模式: {function_pattern}")

    module_list = find_modules_from_folder(test_path, module_pattern)
    logger.info(f"找到的模块: {[module[0] for module in module_list]}")

    test_case_list = []
    for module in module_list:
        module_name, module_file = module
        logger.info(f"正在导入模块: {module_name}，路径: {module_file}")
        _module = import_modules_dynamically(module_name, module_file)
        collect_test_cases(_module, test_case_list, module_file, class_pattern, function_pattern)

    logger.info(f"所有找到的测试用例: {test_case_list}")

    filtered_test_cases = filter_test_cases(test_case_list, keyword, mark)

    if filtered_test_cases:
        logger.info(f"过滤后的测试用例: {filtered_test_cases}")
        sys.exit(run_test_case(filtered_test_cases))
    else:
        logger.info("未找到任何匹配的测试用例。")


def collect_test_cases(_module, test_case_list, module_file, class_pattern, function_pattern):
    """
    收集测试用例。

    Args:
        _module: 导入的模块对象。
        test_case_list: 测试用例列表。
        module_file: 模块文件路径。
        class_pattern: 类匹配模式（正则表达式）。
        function_pattern: 函数/方法匹配模式（正则表达式）。
    """
    module_file_path = os.path.relpath(module_file)
    class_re = re.compile(class_pattern)
    function_re = re.compile(function_pattern)

    for func_name, func in inspect.getmembers(_module, inspect.isfunction):
        if function_re.match(func_name):
            test_case = f"{module_file_path}::{func_name}"
            test_case_list.append((test_case, func))

    for cls_name, cls in inspect.getmembers(_module, inspect.isclass):
        if class_re.match(cls_name):
            for func_name, func in inspect.getmembers(cls, inspect.isfunction):
                if function_re.match(func_name):
                    test_case = f"{module_file_path}::{cls_name}::{func_name}"
                    test_case_list.append((test_case, func))


def filter_test_cases(test_case_list, keyword, mark):
    """
    过滤测试用例。

    Args:
        test_case_list: 测试用例列表。
        keyword: 关键字过滤表达式。
        mark: 标记过滤表达式。

    Returns:
        过滤后的测试用例列表。
    """
    logger = logging.getLogger(__name__)
    filtered_cases = []

    for test_case, func in test_case_list:
        if keyword and keyword not in test_case:
            continue
        if mark:
            func_marks = getattr(func, "__test_case_mark__", [])
            if not isinstance(func_marks, list):
                func_marks = [func_marks]
            if mark not in func_marks:
                continue
        filtered_cases.append(test_case)

    return filtered_cases


def run_test_case(test_case_list):
    """
    运行测试用例。

    Args:
        test_case_list: 测试用例列表。

    Returns:
        pytest 的运行结果。
    """
    logger = logging.getLogger(__name__)
    logger.info(f"本次执行用例的数量为: {len(test_case_list)}")
    extra_args_list = ["-vs", "--tb=short"] + test_case_list
    logger.info(f"运行的参数列表：{extra_args_list}")
    return pytest.main(extra_args_list)


def count_test_cases(test_path):
    """
    统计测试用例数量。

    Args:
        test_path: 测试用例路径。

    Returns:
        测试用例数量。
    """
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    config = load_config(config_path)
    module_list = find_modules_from_folder(test_path, config['tests']['module_pattern'])
    test_case_count = 0
    for module in module_list:
        module_name, module_file = module
        _module = import_modules_dynamically(module_name, module_file)
        test_case_list = []
        collect_test_cases(_module, test_case_list, module_file, config['tests']['class_pattern'],
                           config['tests']['function_pattern'])
        test_case_count += len(test_case_list)
    return test_case_count


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Test Runner")
    parser.add_argument('test_path', type=str, help="Path to the test files")
    parser.add_argument('-k', type=str, help="Only run tests that match the given substring expression")
    parser.add_argument('-m', type=str, help="Only run tests that have the given mark expression")
    parser.add_argument('-c', '--config', type=str, default='config.yaml', help="Path to the config file")
    args = parser.parse_args()

    run(args, args.test_path)
