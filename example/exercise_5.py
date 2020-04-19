#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为 1000。
https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


def longest_palindrome_1(s):
    """

    :param s: str
    :return:
    """
    is_palindromic_string = lambda s: s == s[::-1]  # 回文串判定函数
    max_len, max_substr = 0, ''

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            cur_substr = s[i:j]  # 取当前子串
            if is_palindromic_string(cur_substr):
                cur_len = len(cur_substr)  # 当前子串长度
                if cur_len > max_len:
                    max_len = cur_len
                    max_substr = cur_substr  # 当前最长子串
    return max_substr


def longest_palindrome_2(s):
    """

    :param s: str
    :return:
    """
    dp = [[False] * len(s) for _ in range(len(s))]
    max_start, max_len = 0, 0  # 最长回文子串开始位置及长度
    for right in range(len(s)):  # 右指针先走
        for left in range(right + 1):  # 左指针跟着右指针
            if right - left < 2:  # 前两种情况
                dp[left][right] = (s[left] == s[right])
            else:  # 最后一种情况
                dp[left][right] = (s[left] == s[right]) and dp[left + 1][right - 1]
            # cur_substr = s[left:right+1]          # 当前考察的子串
            cur_len = right + 1 - left  # 当前子串长度为 right + 1 - left
            if dp[left][right] and max_len < cur_len:
                max_start = left
                max_len = cur_len

    return s[max_start:max_start + max_len]


def longest_palindrome_3(s):
    """

    :param s: str
    :return:
    """

    def extend(start_idx, end_idx, max_start, max_len):
        """
        扩展函数，用于得到向左向右同步扩展后的最长回文子串
        :param start_idx: 向左扩展的起始位置
        :param end_idx: 向右扩展的起始位置
        :param max_start: 当前最长回文子串的左指针
        :param max_len: 当前最大长度
        :return: 当前最长回文子串的起始位置和长度
        """

        while 0 <= start_idx <= end_idx < len(s):  # 子串起止下标合法时
            if s[start_idx] == s[end_idx]:  # 如果新增的两端字符相等
                cur_str = s[start_idx:end_idx]  # 当前子串是回文串
                cur_len = end_idx + 1 - start_idx  # 当前子串长度
                if max_len < cur_len:
                    max_len = cur_len
                    max_start = start_idx
                start_idx -= 1  # 左指针向左移动一位
                end_idx += 1  # 右指针向右移动一位
            else:
                break
        return max_start, max_len

    max_start, max_len = 0, 0  # 初始化最长回文子串开始位置及长度

    for i in range(len(s)):  # 进行一次遍历
        left = right = i  # 判断长度为奇数的回文子串开始和结束位置
        # 从i位置向两边扩展，搜寻可以得到的最大回文子串
        max_start, max_len = extend(left, right, max_start, max_len)

        left, right = i, i + 1  # 判断长度为偶数的回文子串开始和结束位置
        # 从i位置向左扩展，从i+1位置向右扩展，搜寻可以得到的最大回文子串
        max_start, max_len = extend(left, right, max_start, max_len)

    return s[max_start:max_start + max_len]


def longest_palindrome_4(s):
    """

    :param s: str
    :return:
    """
    is_palindromic_string = lambda s: s == s[::-1]
    cur_length = 0
    start_index = 0
    for i in range(len(s)):

        cur_start_index = i - cur_length - 1                                # 向左扩展一个字符
        cur_substr = s[cur_start_index: cur_start_index+cur_length+2]       # 向右扩展一个字符，获得子串

        if cur_start_index >= 0 and is_palindromic_string(cur_substr):      # 判断扩展后的子串是否回文
            start_index = cur_start_index                                   # 更新子串起始下标
            cur_length += 2                                                 # 更新当前最长子串长度

        else:
            cur_start_index = i - cur_length                                # 向左不扩展
            cur_substr = s[cur_start_index: cur_start_index+cur_length+1]   # 向右扩展一个字符，获得子串
            if cur_start_index >= 0 and is_palindromic_string(cur_substr):  # 判断扩展后的子串是否回文
                start_index = cur_start_index                               # 更新子串起始下标
                cur_length += 1                                             # 更新当前最长子串长度

    return s[start_index: start_index + cur_length]


def longest_palindrome_5(s):
    """

    :param s: str
    :return:
    """

    def get_length(string, index):
        # 循环求出index为中心的最长回文字串
        start, length = index // 2, 0
        r_ = len(string)
        for i in range(1, index + 1):
            if index + i < r_ and string[index - i] == string[index + i]:
                start = (index - i) // 2
                length += 1
            else:
                break
        return start, length

    s_list = [c for c in s]
    new_s = '#' + '#'.join(s_list) + '#'  # 形成新串

    max_start = max_length = 0
    length = len(new_s)
    for index in range(0, length):
        start, r_length = get_length(new_s, index)
        if max_length < r_length:
            max_start, max_length = start, r_length
    return s[max_start: max_start + max_length]


if __name__ == "__main__":
    s1 = "abcdcbaferdjjjk"
    print(longest_palindrome_4(s1))
