#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com
"""

import pytest
import allure
from example.exercise_1 import *
from example.exercise_2 import *
from example.exercise_3 import *


@allure.feature("测试练习题")
class TestExerciseOne(object):

    @allure.story("测试练习题1")
    def test_exercise_1(self):
        """
        测试练习题1
        :return:
        """
        t_list_1 = [2, 7, 8, 9, 24, 4, 6]
        t_tar_sum = 32
        result_1 = two_sum_1(t_list_1, t_tar_sum)
        result_2 = two_sum_2(t_list_1, t_tar_sum)
        result_3 = two_sum_3(t_list_1, t_tar_sum)
        assert [2, 4] == result_1
        assert [2, 4] == result_2
        assert [2, 4] == result_3

    @allure.story("测试练习题2")
    def test_exercise_2(self):
        """
        测试练习题2
        :return:
        """
        t_list_1 = [1, 8, 7, 9]
        t_list_2 = [3, 4, 5, 9]
        result_1 = add_two_numbers_0(t_list_1, t_list_2)
        result_2 = list_node_to_string(add_two_numbers_1(string_to_list_node(t_list_1), string_to_list_node(t_list_2)))
        assert [4, 2, 3, 9, 1] == result_1
        assert '[4, 2, 3, 9, 1]' == result_2

    @allure.story("测试练习题3")
    def test_exercise_3(self):
        """
        测试练习题3
        :return:
        """
        t_str_1 = "wergthyjkkkfg"
        t_str_2 = "bbbbb"
        t_str_3 = "abcabcbbb"
        result_1 = length_of_longest_substring_0(t_str_1)
        result_2 = length_of_longest_substring_0(t_str_2)
        result_3 = length_of_longest_substring_0(t_str_3)
        result_4 = length_of_longest_substring_1(t_str_1)
        result_5 = length_of_longest_substring_1(t_str_2)
        result_6 = length_of_longest_substring_1(t_str_3)
        assert 9 == result_1
        assert 1 == result_2
        assert 3 == result_3
        assert 9 == result_4
        assert 1 == result_5
        assert 3 == result_6


if __name__ == "__main__":
    pytest.main(["-s", "-q", "--alluredir", "../report/xml"])
    # pytest -s -q test_main.py --alluredir ../report/xml
    # allure generate --clean ../report/xml/ -o ../report/html

