#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定两个数组，编写一个函数来计算它们的交集。
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
"""


def intersect_1(nums1, nums2):
    """
    :param nums1:
    :param nums2:
    :return:
    """
    m = len(nums1)
    n = len(nums2)

    if m == 0 or n == 0:
        return []

    dicts = {}
    for i in nums1:
        if i in dicts:
            dicts[i] += 1
        else:
            dicts[i] = 1

    ret = []
    for j in nums2:
        if j in dicts and dicts[j] > 0:
            ret.append(j)
            dicts[j] -= 1

    return ret


def intersect_2(nums1, nums2):
    """
    :param nums1:
    :param nums2:
    :return:
    """
    inter = set(nums1) & set(nums2)
    nums = []
    for i in inter:
        nums += [i] * min(nums1.count(i), nums2.count(i))
    return nums


if __name__ == "__main__":
    num_1 = [1, 2, 2, 2, 1]
    num_2 = [2, 2]
    print(intersect_1(num_1, num_2))
    print(intersect_2(num_1, num_2))
