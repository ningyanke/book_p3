#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
这个模块用于返回需要统计的txt文档中出现次数最多的10个单词
面向对象:
需求是返回一个txt文档中的前10个词频
首先,每个txt文档都是一个对象
这个文档应该具有方法 Print_txt 来打印出10个词频
面向对象也包含面向对象,但是更是工厂.
对于文件对象来说;
行为
方法:
打开文件得到全文字符串,
操作文件,
    得到一个可操作字符串:
        去除标点符号
        去除大小写
    生成单词和个数的对照表(字典)
        对可操作字符串生成列表
        对生成的列表统计到字典
        字典是无序序列,转换为有序列表
    对列表中的前10个元素取出

关闭文件,
"""
import string


class Cipin:
    """
    用于打开/关闭 需要读取的文件
    """

    def __init__(self, text):
        """
        打开文件
        :param text:
        """
        self.text = open(text, 'r')

    def openfile(self):
        return self.text

    def fileread(self):
        """
        返回全部文档的一个字符串
        :return:
        """
        fileread = self.text.read()
        return fileread

    def closefile(self):
        """
        关闭文件
        :return:
        """
        return self.text.close()

        # def __all__(self):
        #    return ['pptxt']


class Cipin_str(Cipin):
    """
    用于处理文件: 移除标点符号,转换大小写,和同时移除标点转换大小写
    """

    def remove_biaodian(self, newsign=""):
        """
        移除标点
        :param newsign:
        :return:
        """
        signtext = string.punctuation + newsign
        signrepl = "@" * len(signtext)
        signtable = str.maketrans(signtext, signrepl)
        return self.fileread().translate(signtable).replace("@", "")

    def changecaptital(self):
        """
        转换大小写
        :return:
        """
        return self.fileread().lower()

    def biaodiancapital(self, newsign=""):
        """
        同时移除大小写和标点
        :param newsign:
        :return:
        """
        return self.remove_biaodian(newsign="").lower()


class Dict_txt(Cipin_str):
    """
    生成单词和出现次数的字典
    """
    counts = {}

    def __init__(self, text):
        self.counts = Dict_txt.counts
        super(Dict_txt, self).__init__(text)

    def word_dict(self):
        """
        返回生成的字典
        :return:
        """
        list_str = self.biaodiancapital(newsign="").split()
        for word in list_str:
            if word in Dict_txt.counts:
                Dict_txt.counts[word] += 1
            else:
                Dict_txt.counts[word] = 1
        return self.counts

    def paixu_dict(self):
        """
        对生成的字典排序
        :return:
        """
        a = list(self.word_dict().items())
        print(a)
        b = sorted(a, key=lambda x: x[1], reverse=True)
        return b
        # return list(Dict_txt.counts.items()).sort(key=lambda x: x[1], reverse=True)


class Print_txt(Dict_txt):
    """
    取出字典中的前10个
    """

    def __init__(self, text):
        super(Print_txt, self).__init__(text)

    def pptxt(self):
        """
        返回前10个高发词频
        :return:
        """
        # self.word_dict()
        return "前10个高发词频为:", self.paixu_dict()[0:11]


if __name__ == '__main__':
    #    test1 = Cipin_str("./test1.txt")
    #    print(test1.changecaptital())
    #    test1.closefile()
    #    test2 = Cipin_str("./test1.txt")
    #    print(test2.biaodiancapital())
    #    test2.closefile()
    #    test3 = Dict_txt("./test1.txt")
    #    print(test3.word_dict())
    #    # test1.closefile()
    #    # test1= Dict_txt("./test1.txt")
    #    print("test3", test3.paixu_dict())
    #    test3.closefile()

    test4 = Print_txt("./test1.txt")
    print(Dict_txt.counts)
    print(test4.pptxt())
    test4.closefile()
    # test5 = Print_txt("./hamlet1.txt")
    # print("test5", test5.pptxt())
    # test5.closefile()
