######  `zip`简化循环语句
>比如这个问题：
问题:有两个列表，分别是`a=[1,2,3,4,5]`,`b=[9,8,7,6,5]`,求这两个列表相对应元素的和
解析:由于`a``b`长度相等，可以使用其索引进行运算，求出结果
`c = [a[i]+b[i] for i in range(len(a)) ]`
当然可以使用另外一种方法`zip`来进行计算
先看一下`zip`的文档，是这样描述的
```python
zip(iter1 [,iter2 [...]]) --> zip object
Return a zip object whose .__next__() method returns a tuple where the i-th element comes from the i-th iterable argument.
The .__next__() method continues until the shortest iterable in the argument sequence is exhausted and then it raises StopIteration.
```
`zip`生成的是一个`zip`对象，作用的是1到多个可迭代对象，生成的是一个一一对应的`tuple`,匹配的是最短的值
>
>```python
>In [260]: a
>Out[260]: [1, 2, 3, 4, 5]
>
>In [261]: b
>Out[261]: [9, 8, 7, 6, 5]
>#生成一一对应的zip对象
>In [262]: list(zip(a,b))
>Out[262]: [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
>#作用与字典时，只会作用与键
>In [263]: s = {'lang':'python','name':'Jack'}
>
>In [264]: list(zip(s))
>Out[264]: [('name',), ('lang',)]
>#不等长时，以最短为依据
>In [265]: a1 = [1,2,3]
>
>In [266]: b1 = [1,12,3,223,232]
>
>In [267]: list(zip(a1,b1))
>Out[267]: [(1, 1), (2, 12), (3, 3)]
>```
>对于上一个问题，`zip`的解法
>```python
>In [276]: d = [ x+y for x,y in list(zip(a,b))]
>In [277]: d
>Out[277]: [10, 10, 10, 10, 10]
>```
>解释一下为什么x,y可以直接代替list(zip(a,b))这个列表中的元组的两个值，这个来源也是，解压序列赋值给多个变量
>
>```python
>In [271]: l1,l2,l3=[1,2,(1,2)]
>
>In [272]: print(l1,l2,l3)
>1 2 (1, 2)
>In [274]: ll1,ll2,(ll3,ll4) =[1,2,(1,2)]
>
>In [275]: print(ll1,ll2,ll3,ll4)
>1 2 1 2
>```
>走向图
>![图解](./解压可迭代对象图解.png)
>对于`zip`而言它还可以解包
>```python
>In [295]: result
>Out[295]: [(2, 11), (4, 13), (6, 15), (8, 17)]
>
>In [296]: list(zip(*result))
>Out[296]: [(2, 4, 6, 8), (11, 13, 15, 17)]
>```
>根据解压可迭代对象给多个变量
>![图解](./result图解.png)
>```python
>In [290]: result
>Out[290]: [(2, 11), (4, 13), (6, 15), (8, 17)]
>
>In [291]: print(*result)
>(2, 11) (4, 13) (6, 15) (8, 17)
>
>In [292]: name1,name2,name3,name4 = result
>
>In [293]: print(name1,name2,name3,name4)
>(2, 11) (4, 13) (6, 15) (8, 17)
>
>In [294]: list(zip(name1,name2,name3,name4))
>Out[294]: [(2, 4, 6, 8), (11, 13, 15, 17)]
>```
>延伸一个问题：有一个字典，`myinfor = {"name":"xiaoming", "site":"xiaoming.github.io", "lang":"python"}`，将这个字典变换成：`infor = {"xiaoming":"name", "xiaoming.github.io":"site", "python":"lang"}`
>```python
> dict(zip(myinfor.values(), myinfor.keys()))
>{'python': 'lang', 'xiaoming.github.io': 'site', 'xiaoming': 'name'}`
>```
######`enumerate`简化循环
>```python
>>  enumerate(iterable[, start]) -> iterator for index, value of iterable Return an enumerate object.
>iterable must be another object that supports iteration.
>The enumerate object yields pairs containing a
> count (from start, which defaults to zero) and
>a value yielded by the iterable argument.enumerate
>is useful for obtaining an indexed list:(0, seq[0]), (1, seq[1]), (2, seq[2]), ...
>```
