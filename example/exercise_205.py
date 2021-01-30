#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身
https://leetcode-cn.com/problems/isomorphic-strings
"""


def is_isomorphic(s, t):
    """

    :param s: str
    :param t: str
    :return:
    """
    map_s = {}
    map_t = {}
    for i in range(len(s)):
        if s[i] not in map_s and t[i] not in map_t:
            map_s[s[i]] = i
            map_t[t[i]] = i
        else:
            if map_s.get(s[i]) is None or map_t.get(t[i]) is None:
                return False
            else:
                if map_s.get(s[i]) != map_t.get(t[i]):
                    return False
    return True


print(is_isomorphic("eff", "foo"))



