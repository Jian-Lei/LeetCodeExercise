#!/usr/bin/env python
# coding=utf-8
"""
Auther: jian.lei
Email: leijian0907@163.com

给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
https://leetcode-cn.com/problems/add-two-numbers/
"""
import copy


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers_0(l1, l2):
    """
    列表倒序， join成一个字符串， 转int相加， 拆分为列表，倒序返回
    :param l1: list[int]
    :param l2: list[int]
    :return:
    """
    # 使用deepcopy防止直接修改了源数据
    ll1 = copy.deepcopy(l1)
    ll2 = copy.deepcopy(l2)
    ll1.reverse()
    ll2.reverse()
    ll1 = [str(i) for i in ll1]
    ll2 = [str(i) for i in ll2]
    rl = [int(i) for i in list(str(int("".join(ll1)) + int("".join(ll2))))]
    rl.reverse()
    return rl


def add_two_numbers_1(l1, l2):
    """
    不直接使用列表的功能
    :param l1: ListNode
    :param l2: ListNode
    :return:
    """
    first = 0
    res = ListNode(0)
    res_temp = res
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        cur_sum = x + y + first
        first = cur_sum // 10
        res_temp.next = ListNode(cur_sum % 10)
        res_temp = res_temp.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if first != 0:
        res_temp.next = ListNode(first)
    return res.next


def string_to_list_node(l_data):
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in l_data:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummy_root.next
    return ptr


def list_node_to_string(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == "__main__":
    list1 = [1, 8, 7, 9]
    list2 = [3, 4, 5, 9]
    print(add_two_numbers_0(list1, list2))
    print(list_node_to_string(add_two_numbers_1(string_to_list_node(list1), string_to_list_node(list2))))
