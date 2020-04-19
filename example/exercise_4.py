#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定两个大小为m和n的有序数组nums1和nums2。请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。假设 nums1 和 nums2 不会同时为空。
https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""


def median_of_two_sorted_arrays(nums1, nums2):
    """

    :param nums1: list[int]
    :param nums2: list[int]
    :return:
    """
    sum_list = sorted(nums1 + nums2)
    length = len(sum_list)
    if length % 2 == 0:
        return float(sum_list[length // 2 - 1] + sum_list[length // 2]) / 2
    else:
        return float(sum_list[length // 2])


if __name__ == "__main__":
    nums_1 = [-3, -6]
    nums_2 = [4, 5, 7]
    print(median_of_two_sorted_arrays(nums_1, nums_2))
