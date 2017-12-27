#!/usr/bin/env python 
# coding=utf-8

file1 = open("teleaddressbook.txt")
file2 = open("emaladdressbook.txt")
file3 = open("addressbook.txt", "w")

list1 = file1.readlines()
list2 = file2.readlines()

mum = 0
if len(list1) > len(list2):
    num = len(list1)
else:
    num = len(list1)

for i in range(num):
    b = list2[i].split(" ")[1:]
    bb = " ".join(b)
    srt = list1[i].strip("\n") + bb

    print(srt)
    file3.writelines(iter(srt))

file1.close()
file2.close()
file3.close()


