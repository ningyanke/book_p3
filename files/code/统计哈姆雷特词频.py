#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:ning
@file:统计哈姆雷特词频.py
@time:12/26/20178:14 AM
"""

import string


# 返回所有标点符号替换称为 空格
def strclear(text, newsign=""):
    signtext = string.punctuation + newsign
    signrepl = "@" * len(signtext)
    signtable = str.maketrans(signtext, signrepl)
    return text.translate(signtable).replace("@", "")


# 返回所有大写字母替换称为小写
def strlower(text):
    return text.lower()


counts = {}


# 分割成包含每个单词的列表
def strlist(sttr):
    list_str = sttr.split()
    return list_str


# 将每个单词保存在字典中
def strword(list_dict):
    for word in list_dict:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1


# 统计最后的字数排序
def sortstr(dict_sort):
    # list1 = [value for value in dict_sort.values()]
    # list2 = sorted(list1, reverse=True)
    list2 = list(counts.items())
    list2.sort(key=lambda x: x[1], reverse=True)
    return list2


# 打印出前10
def printstr(str_list):
    # lit = ["{}:{}".format(k, v) for k, v in counts.items() for x in str_list if v == x]
    # for k, v in counts.items
    # for x in str_list[0:11]:
    #    lit = ["{}:{}".format(k, v) for k, v in counts.items() if v == x]
    lit = str_list[0:11]
    return lit


if __name__ == '__main__':
    # 测试 strlower
    a = "SDFDFGDSFlkjl"
    print(strlower(a))
    # 测试单词保存在字典中
    a = "today is a good day  i am living  in  china i am 19 years old i am chinese hello world"
    list1 = strlist(a)
    print(list1)
    strword(list1)
    print(counts)
    # 测试字数统计排序
    test_list = sortstr(counts)
    print(test_list)
    print(printstr(test_list))

    with open("./hamlet1.txt", 'r') as f:
        temp = f.read()
        strlower(temp)
        strclear(temp)
        list_test = strlist(temp)
        for i in list_test:
            strword(i)
        list_test2 = sortstr(counts)
        print(printstr(list_test2))
