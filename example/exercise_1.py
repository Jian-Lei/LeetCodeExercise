#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
https://leetcode-cn.com/problems/two-sum/
"""


def two_sum_1(nums, target):
    """
    通过两次for循环
    :param nums:
    :param target:
    :return:
    """
    length = len(nums)
    for x in range(0, length):
        for y in range(x+1, length):
            if nums[x] + nums[y] == target:
                return [x, y]
    return None


def two_sum_2(nums, target):
    """
    通过字典的方式
    :param nums: list[int]
    :param target: int
    :return:
    """
    num_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in num_dict:
            return [num_dict[target - nums[i]], i]
        else:
            num_dict[nums[i]] = i
    else:
        return None


def two_sum_3(nums, target):
    """
    通过列表切片
    :param nums: list[int]
    :param target: int
    :return:
    """
    n = 0
    for i in range(0, len(nums) - 1):
        n += 1
        if (target - nums[i]) in nums[i + 1:]:
            return [i, nums[i + 1:].index(target - nums[i]) + n]
    else:
        return None


if __name__ == "__main__":
    list_1 = [2, 7, 8, 9, 24, 4, 6]
    tar_sum = 32
    print(two_sum_1(list_1, tar_sum))
    print(two_sum_2(list_1, tar_sum))
    print(two_sum_3(list_1, tar_sum))

