#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


def length_of_longest_substring_0(s):
    """
    窗口滑动
    :param s:
    :return:
    """
    max_len, i = 0, -1
    for x, y in enumerate(s):
        if y in s[i + 1:x]:
            max_len = max(max_len, x - i - 1)
            i = s[i + 1:x].index(y) + i + 1
    return max(max_len, len(s) - 1 - i)


def length_of_longest_substring_1(s):
    """
    遍历算法
    :param s:
    :return:
    """
    longest_str = []
    cur_len = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] in longest_str:
            cur_index = longest_str.index(s[i])
            longest_str = longest_str[cur_index + 1:]
            cur_len -= cur_index
        else:
            cur_len += 1
        longest_str.append(s[i])
        if max_len < cur_len:
            max_len = cur_len
    return max_len


if __name__ == "__main__":
    str_1 = "wergthyjkkkfg"
    str_2 = "bbbbb"
    str_3 = "abcabcbbb"
    print(length_of_longest_substring_0(str_1))
    print(length_of_longest_substring_0(str_2))
    print(length_of_longest_substring_0(str_3))
    print(length_of_longest_substring_1(str_1))
    print(length_of_longest_substring_1(str_2))
    print(length_of_longest_substring_1(str_3))

