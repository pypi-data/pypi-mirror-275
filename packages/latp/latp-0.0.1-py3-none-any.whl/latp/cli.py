# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @author  : Tanyu
# @file    : cli.py
# @time    : 2024/5/24 下午15:46

from __future__ import absolute_import
import argparse
import os
import sys
import yaml
from latp import __description__, __version__, __pro_name__
from latp import runner


def load_config(config_file):
    if not os.path.exists(config_file):
        # 如果指定的配置文件不存在，则使用默认配置文件
        config_file = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(prog=__pro_name__, description=__description__)
    parser.add_argument(
        "-V", "--version", dest="version", action="store_true", help="show version")
    parser.add_argument("-k", default=None, action="store", help="run tests which match the given substring expression")
    parser.add_argument("-m", default=None, action="store", help="run tests with same marks")
    parser.add_argument("-c", "--config", default=None, action="store", help="path to config file")
    parser.add_argument("path", nargs='?', help="please input test folder", action="store")

    args = parser.parse_args()

    config = load_config(args.config if args.config else 'config.yaml')

    if args.version:
        print(f"{__version__}")
        sys.exit(0)

    test_path = args.path if args.path else config['tests']['test_path']

    if not test_path:
        print("请提供测试文件夹路径，或者在配置文件中指定测试路径。")
        sys.exit(0)

    if not os.path.exists(test_path):
        print(f'输入的路径不存在: {test_path}')
        sys.exit(0)

    if args.k:
        print(f"测试路径: {test_path}")
        print(f"用例过滤表达式: {args.k}")
    if args.m:
        print(f"测试路径: {test_path}")
        print(f"用例标签: {args.m}")

    runner.run(args, test_path)


if __name__ == "__main__":
    main()
