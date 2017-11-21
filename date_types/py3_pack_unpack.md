###打包，解包
####1.`*`
>`*`可以用来打包解包序列(`list`,`tuple`,`string`)

####2.`**`
>`**`可以用来打包解包字典

####3.打包

####4.解包
>参见语句中的的 解压可迭代对象赋值给多个变量 *args 其实相当于多个变量名
>常见语句中的`zip`简化循环，可以清楚看到 变量的走向
>```python
>In [77]: str1 = 'Python'
>
>In [78]: print(*str1)
>P y t h o n
>>
>In [79]: tuple1=(1,2,3)
>>
>In [81]: print(*tuple1)
>1 2 3
>>
>In [82]: range(3,6)
>Out[82]: range(3, 6)
>>
>In [83]: list1 = [3,6]
>>
>In [84]: print(range(*list1))
>range(3, 6)
>>
>In [85]: def jibao1(*args):
>    ...:     for item in args:
>    ...:         print(item)
>    ...:
>>
>In [87]: jibao1(list1)
>[3, 6]
>>
>In [95]: def print_key_args(**kwargs):
>    ...:     for key,value in kwargs.items():
>    ...:         print("%s = %s"%(key,value) )
>    ...:         
>>
>In [96]: print_key_args(**d1)
>name = xiaoming
>age = 5
>>```
