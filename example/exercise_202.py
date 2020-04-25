#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。
https://leetcode-cn.com/problems/happy-number/
"""


def is_happy(n):
    """
    :param n: int
    :return:
    """
    l_1 = [i for i in str(n)]
    sum_num_list = []
    result = False
    while not result:
        sum_num = sum([int(i) * int(i) for i in l_1])
        if sum_num == 1:
            result = True
        else:
            l_1 = [i for i in str(sum_num)]
            if sum_num in sum_num_list:
                break
            sum_num_list.append(sum_num)
    return result


if __name__ == "__main__":
    print(is_happy(19))



