#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给你一个整数 x ，如果 x 是一个回文整数，返回 ture ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

https://leetcode-cn.com/problems/palindrome-number

"""


def is_palindrome(x):
    result = False
    if -1 < x < 2 ** 31 - 1:
        y = int(str(x)[::-1])
        if x == y:
            result = True
    return result


def is_palindrome_1(x):
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    print(is_palindrome(0))
    print(is_palindrome(121))
    print(is_palindrome(122))

    print(is_palindrome_1(0))
    print(is_palindrome_1(121))
    print(is_palindrome_1(122))
    print(is_palindrome_1(-122))
