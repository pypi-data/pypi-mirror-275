# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @author  : Tanyu
# @file    : decorators.py
# @time    : 2024/5/24 下午15:46

import inspect
from functools import wraps


class TestMark(object):
    def __init__(self, mark=None):
        self.mark = mark

    def __call__(self, obj):
        if inspect.isclass(obj):
            # 如果装饰的是类，为类和类中所有方法添加标记属性
            setattr(obj, "__test_case_mark__", self.mark)
            for name, method in inspect.getmembers(obj, inspect.isfunction):
                if name.startswith('test') or name.endswith('test'):
                    existing_marks = getattr(method, "__test_case_mark__", [])
                    if not isinstance(existing_marks, list):
                        existing_marks = [existing_marks]
                    existing_marks.append(self.mark)
                    setattr(method, "__test_case_mark__", existing_marks)
            return obj
        else:
            # 如果装饰的是方法，为方法添加标记属性
            @wraps(obj)
            def wrapper(*args, **kwargs):
                return obj(*args, **kwargs)

            existing_marks = getattr(obj, "__test_case_mark__", [])
            if not isinstance(existing_marks, list):
                existing_marks = [existing_marks]
            existing_marks.append(self.mark)
            setattr(wrapper, "__test_case_mark__", existing_marks)
            return wrapper

# 示例用法
# @TestMark(mark="example_class_mark")
# class TestExample:
#     def test_method1(self):
#         pass
#
#     @TestMark(mark="example_method_mark")
#     def test_method2(self):
#         pass

# TestExample 类现在拥有 __test_case_mark__ 属性
# TestExample.test_method1 方法现在拥有 __test_case_mark__ 属性 (继承自类的标记)
# TestExample.test_method2 方法现在拥有 __test_case_mark__ 属性 (继承自类的标记以及自己定义的标记)
