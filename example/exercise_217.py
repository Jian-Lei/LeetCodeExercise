#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
https://leetcode-cn.com/problems/contains-duplicate/
"""


def contains_duplicate(nums):
    """
    :param nums: list
    :return:
    """
    if len(nums) != len(set(nums)):
        return True
    else:
        return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))



