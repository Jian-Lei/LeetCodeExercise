#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
https://leetcode-cn.com/problems/valid-anagram/
"""


def is_anagram_1(s, t):
    """
    :param s:
    :param t:
    :return:
    """
    result = True
    if len(s) != len(t):
        result = False
    else:
        s_s = set(s)
        if s_s == set(t):
            for i in s_s:
                result = result and (s.count(i) == t.count(i))
        else:
            result = False
    return result


def is_anagram_2(s, t):
    """
    :param s:
    :param t:
    :return:
    """
    from collections import Counter
    c1 = Counter(s)
    c2 = Counter(t)
    if c1 == c2:
        return True
    else:
        return False


if __name__ == "__main__":
    num_1 = "banagram"
    num_2 = "mnagabra"
    num_3 = "rat"
    num_4 = "car"
    print(is_anagram_1(num_1, num_2))
    print(is_anagram_1(num_3, num_4))
    print(is_anagram_1(num_1, num_3))

    print(is_anagram_2(num_1, num_2))
    print(is_anagram_2(num_3, num_4))
    print(is_anagram_2(num_1, num_3))
