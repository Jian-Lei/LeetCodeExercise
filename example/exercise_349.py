#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定两个数组，编写一个函数来计算它们的交集。
https://leetcode-cn.com/problems/intersection-of-two-arrays/
"""


def intersection_1(nums1, nums2):
    """
    给定两个数组，编写一个函数来计算它们的交集。
    :param nums1: list
    :param nums2: list
    :return:
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1
    return [v for v in nums1 if v in nums2]


def intersection_2(nums1, nums2):
    """
    给定两个数组，编写一个函数来计算它们的交集。
    :param nums1: list
    :param nums2: list
    :return:
    """
    return list(set(nums1).intersection(set(nums2)))


def intersection_3(nums1, nums2):
    """
    给定两个数组，编写一个函数来计算它们的交集。
    :param nums1: list
    :param nums2: list
    :return:
    """
    return list(set(nums1) & set(nums2))


if __name__ == "__main__":
    print(intersection_1([1, 2, 2, 1], [2, 2]))
    print(intersection_2([1, 2, 2, 1], [2, 2]))
    print(intersection_3([1, 2, 2, 1], [2, 2]))



