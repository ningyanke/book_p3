## itertools

[TOC]

### 1.官网

> [python3.5-itertools](http://python.usyiyi.cn/translate/python_352/library/itertools.html)
>
> 迭代器的特点是：**惰性求值**（Lazy evaluation），即只有当迭代至某个值时，它才会被计算，这个特点使得迭代器特别适合于遍历大文件或无限集合等，因为我们不用一次性将它们存储在内存中。
>
> Python 内置的 itertools 模块包含了一系列用来产生不同类型迭代器的函数或类，这些函数的返回都是一个迭代器，我们可以通过 for 循环来遍历取值，也可以使用 `next()` 来取值。
>
> itertools 模块提供的迭代器函数有以下几种类型：
>
> * 无限迭代器：生成一个无限序列，比如自然数序列 `1, 2, 3, 4, ...`；
> * 有限迭代器：接收一个或多个序列（sequence）作为参数，进行组合、分组和过滤等；
> * 组合生成器：序列的排列、组合，求序列的笛卡儿积等；

### 2.组成分类

> #### 无限迭代器
>
> | 迭代器     | 参数                | 结果                                       | 例子                               |
> | ------- | ----------------- | ---------------------------------------- | -------------------------------- |
> | count() | `(start [,step])` | start,<br>start+step,<br>start+2*step..... | count(10)<br>10,<br>11,....      |
> | cycle() | P                 | P0,P1,...Plast,p0,p1..                   | cycle('abc')<br>abcabcabc        |
> | repeat  | elem[,n]          | elem,elem....(endlessly<br />or up to n times) | repeat('abc',3)<br />abc abc abc |
>
> #### 有限的迭代器
>
> | 迭代器                     | 参数                          | 结果                                       | 例                                        |
> | ----------------------- | --------------------------- | ---------------------------------------- | ---------------------------------------- |
> | `accumulate()`          | p [,func]                   | p0，p0 + p1，p0 + p1 + p2，...              | `accumulate([1,2,3,4,5]) --> 1 3 6 10 15` |
> | `chain()`               | p, q, ...                   | p0，p1，... plast，q0，q1，...                | `chain('ABC', 'DEF') --> A B C D E F`    |
> | `chain.from_iterable()` | iterable                    | p0，p1，... plast，q0，q1，...                | `chain.from_iterable(['ABC', 'DEF']) --> A B C D E F` |
> | `compress()`            | data, selectors             | (d[0] if s[0]), (d[1] if s[1]), ...      | `compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F` |
> | `dropwhile()`           | pred, seq                   | seq[n], seq[n+1], starting when pred fails | `dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1` |
> | `filterfalse()`         | pred, seq                   | elements of seq where pred(elem) is false | `filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8` |
> | `groupby()`             | iterable[, keyfunc]         | sub-iterators grouped by value of keyfunc(v) |                                          |
> | `islice()`              | seq, [start,] stop [, step] | elements from seq[start:stop:step]       | `islice('ABCDEFG', 2, None) --> C D E F G` |
> | `starmap()`             | func, seq                   | func(*seq[0]), func(*seq[1]), ...        | `starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000` |
> | `takewhile()`           | pred, seq                   | seq[0], seq[1], until pred fails         | `takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4` |
> | `tee()`                 | it, n                       | it1, it2, ... itn splits one iterator into n |                                          |
> | `zip_longest()`         | p, q, ...                   | (p[0], q[0]), (p[1], q[1]), ...          | `zip_longest('ABCD', 'xy', fillvalue='-') --> Ax ByC- D-` |
>
> #### 组合生成器
>
> | 迭代器                                      | 参数                   | 结果                                       |
> | ---------------------------------------- | -------------------- | ---------------------------------------- |
> | `product()`                              | p, q, ... [repeat=1] | 笛卡尔积，相当于嵌套for循环                          |
> | `permutations()`                         | p[, r]               | r长度元组，所有可能的顺序，没有重复的元素                    |
> | `combinations()`                         | p, r                 | r长度元组，按排序顺序，没有重复的元素                      |
> | `combinations_with_replacement()`        | p, r                 | r长度元组，按排序顺序，重复元素                         |
> | `product('ABCD', repeat=2)`              |                      | `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD` |
> | `permutations('ABCD', 2)`                |                      | `AB AC AD BA BC BD CA CB CD DA DB DC`    |
> | `combinations('ABCD', 2)`                |                      | `AB AC AD BC BD CD`                      |
> | `combinations_with_replacement('ABCD', 2)` |                      | `AA AB AC AD BB BC BD CC CD DD`          |

### 3.无限迭代器

#### 3.1count(start=0, step=1) 

> 创建一个迭代器，生成从n开始的连续的数，如果忽略n，则从0开始计算(可以是整数,可以是浮点数)
>
> ##### 定义参考
>
> ```python
> def count(start=0, step=1):
>     # count(10) --> 10 11 12 13 14 ...
>     # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
>     n = start
>     while True:
>         yield n
>         n += step
> ```
>
> ##### 实例
>
> ```python
> import itertools
>
> # 整数
> nums = itertools.count()
> for i in nums:
>     if i > 6:
>         break
>     else:
>         print(i,end='')
>  '''
> 0123456
>  '''
>
>
> nums1 = itertools.count(10, 2)
> for i in nums1:
>     if i > 20:
>         break
>     else:
>         print(i,end='')
> '''
> 101214161820
> '''
>
> # 浮点数
> num2 = itertools.count(2.5, 0.5)
>
> for i in num2:
>     if i >8:
>         break
>     else:
>         print(i,end=' ,')
> '''
> 2.5 ,3.0 ,3.5 ,4.0 ,4.5 ,5.0 ,5.5 ,6.0 ,6.5 ,7.0 ,7.5 ,8.0 
> '''
>
> # 与 zip 结合使用
> for i in zip(itertools.count(1), ['a','b','c']):
>     print(i, end='')
> '''
> (1, 'a')(2, 'b')(3, 'c')
> '''
> ```

#### 3.2 itertools.cytle(iterable)

> 用于对 iterable 中的元素反复周期执行循环
>
> ##### 定义参考
>
> ```python
> def cycle(iterable):
>     # cycle('ABCD') --> A B C D A B C D A B C D ...
>     saved = []
>     for element in iterable:
>         yield element
>         saved.append(element)
>     while saved:
>         for element in saved:
>               yield element
> ```
>
> ##### 实例
>
> ```python
> cycle_string = itertools.cycle('ABC')
> i = 1
> for string in cycle_string:
>     if i == 10:
>         break
>     else:
>         print(i,string)
>         i += 1
> '''
> 1 A
> 2 B
> 3 C
> 4 A
> 5 B
> 6 C
> 7 A
> 8 B
> 9 C
> '''        
> ```

#### 3.3 itertools.repeat(*object*[, *times*])

> 创建一个迭代器，重复生成object，times（如果已提供）指定重复计数，如果未提供times，将无止尽返回该对象。
>
> ##### 定义参考
>
> ```python
> def repeat(object, times=None):
>     # repeat(10, 3) --> 10 10 10
>     if times is None:
>         while True:
>             yield object
>     else:
>         for i in range(times):
>             yield object
> ```
>
> 实例:
>
> ```python
> for item in itertools.repeat('Hello world', 3):
>     print(item)
> '''
> Hello world
> Hello world
> Hello world
> ''' 
> # 最常用在 map 中
> list(map(pow, range(10), itertools.repeat(2)))
>
> '''map可以加载多个可迭代对象
> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> '''
> ```

### 4.有限的迭代器

#### 4.1 itertools.accumulate(iterable [,func])

> 首先运算的是一个二元函数,func只能接受2个参数,func作用于iterable中的元素,进行累计预案算,默认是加法,如果输入的iterable 为空,那么输出的iterable也为空.
>
> 二元函数,用途很多
>
> ##### 定义参考
>
> ```python
> def accumulate(iterable, func=operator.add):
>     'Return running totals'
>     # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
>     # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
>     it = iter(iterable)
>     try:
>         total = next(it)
>     except StopIteration:
>         return
>     yield total
>     for element in it:
>         total = func(total, element)
>         yield total
> ```
>
> ##### 实例
>
> ```python
> list(itertools.accumulate(range(10)))
> #[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
>
> >>> data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
> >>> list(accumulate(data, operator.mul))     # running product
> [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
> >>> list(accumulate(data, max))              # running maximum
> [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
>
> # Amortize a 5% loan of 1000 with 4 annual payments of 90
> >>> cashflows = [1000, -90, -90, -90, -90]
> >>> list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
> [1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
>
> # Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
> >>> logistic_map = lambda x, _:  r * x * (1 - x)
> >>> r = 3.8
> >>> x0 = 0.4
> >>> inputs = repeat(x0, 36)     # only the initial value is used
> >>> [format(x, '.2f') for x in accumulate(inputs, logistic_map)]
> ['0.40', '0.91', '0.30', '0.81', '0.60', '0.92', '0.29', '0.79', '0.63',
>  '0.88', '0.39', '0.90', '0.33', '0.84', '0.52', '0.95', '0.18', '0.57',
>  '0.93', '0.25', '0.71', '0.79', '0.63', '0.88', '0.39', '0.91', '0.32',
>  '0.83', '0.54', '0.95', '0.20', '0.60', '0.91', '0.30', '0.80', '0.60']
> ```

#### 4.2 itertools.chain(*iterables) 

> 接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回
>
> ##### 定义参考
>
> ```python
> def chain(*iterables):
>     # chain('ABC', 'DEF') --> A B C D E F
>     for it in iterables:
>         for element in it:
>             yield element
> ```
>
> ##### 实例
>
> ```python
> for item in itertools.chain([1,2,3], ['a','b','c']):
>     print(item)
> '''
> 1
> 2
> 3
> a
> b
> c
> '''
> ```

#### 4.3 chain.from_iterable(iterable)  ---> (classmethod)

> 接收一个可迭代对象作为参数，返回一个迭代器
>
> ##### 参考定义
>
> ```python
> def from_iterable(iterables):
>     # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
>     for it in iterables:
>         for element in it:
>             yield element
> ```
>
> ##### 实例
>
> ```python
> # 接受一个可迭代对象作为参数,返回一个迭代器
> string = itertools.chain.from_iterable('abcd')
> next(string)
> next(string)
> # 'a'
> # 'b'
> ```

#### 4.4 itertools.compress(data, selectors)

> 可用于对数据进行筛选，当 selectors 的某个元素为 true 时，则保留 data 对应位置的元素，否则去除
>
> ##### 定义参考
>
> ```python
> def compress(data, selectors):
>     # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
>     return (d for d, s in zip(data, selectors) if s)
> ```
>
> ##### 实例
>
> ```python
> list(itertools.compress('abcdef', [1,1,0,1,0,0]))
> '''
> 'a', 'b', 'd']
> '''
> ```

#### 4.5 itertools.dropwhile(predicate, iterable)

> predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则丢弃该元素，否则返回该项及所有后续项
>
> ##### 定义参考
>
> ```python
> def dropwhile(predicate, iterable):
>     # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
>     iterable = iter(iterable)
>     for x in iterable:
>         if not predicate(x):
>             yield x
>             break
>     for x in iterable:
>         yield x
> ```
>
> ##### 实例
>
> ```python
> list(itertools.dropwhile(lambda x: x < 5, [1,3,6,7,9]))
> # 如果为True 就丢弃,如果为False,就保留本身和后续的项,不管大小
> list(itertools.dropwhile(lambda x: x < 5, [1,3,6,1,3]))
> ```

#### 4.6  itertools.filterfalse(*predicate*, *iterable*) 

> predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 False,则保留输出
>
> ##### 参考定义
>
> ```python
> def filterfalse(predicate, iterable):
>     # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
>     if predicate is None:
>         predicate = bool
>     for x in iterable:
>         if not predicate(x):
>             yield x
> ```
>
> ##### 实例
>
> ```python
> def check_item(x):
>     return x > 3
> for i in itertools.filterfalse(check_item, [-1,0,1,3,6,9]):
>     print(i)
> ```

#### 4.7 itertools.groupby(iterable, key=None)

> 返回一个按照key作用后的结果进行分组的迭代器.
>
> 按照keyfunc函数对序列每个元素执行后的结果分组(每个分组是一个迭代器), 返回这些分组的迭代器
>
> ##### 参考定义
>
> ```python
> class groupby:
>     # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
>     # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
>     def __init__(self, iterable, key=None):
>         if key is None:
>             key = lambda x: x
>         self.keyfunc = key
>         self.it = iter(iterable)
>         self.tgtkey = self.currkey = self.currvalue = object()
>     def __iter__(self):
>         return self
>     def __next__(self):
>         while self.currkey == self.tgtkey:
>             self.currvalue = next(self.it)    # Exit on StopIteration
>             self.currkey = self.keyfunc(self.currvalue)
>         self.tgtkey = self.currkey
>         return (self.currkey, self._grouper(self.tgtkey))
>     def _grouper(self, tgtkey):
>         while self.currkey == tgtkey:
>             yield self.currvalue
>             try:
>                 self.currvalue = next(self.it)
>             except StopIteration:
>                 return
>             self.currkey = self.keyfunc(self.currvalue)
> ```
>
> ##### 实例
>
> ```python
> for key, value in itertools.groupby('abbaabbccddcc'):
>     print(key, ':', list(value))
>
> # 按照key作用后的结果进行分组
> data = ['a', 'bb', 'cc', 'dd','ee']
> for key, value in itertools.groupby(data, len):
>     print(key, ':', list(value))
> ```

#### 4.8 itertools.islice(iterable, start, stop[, step])

> 切片操作,iterable 是可迭代对象，start 是开始索引，stop 是结束索引，step 是步长，start 和 step 可选
>
> ##### 参考定义
>
> ```python
> def islice(iterable, *args):
>     # islice('ABCDEFG', 2) --> A B
>     # islice('ABCDEFG', 2, 4) --> C D
>     # islice('ABCDEFG', 2, None) --> C D E F G
>     # islice('ABCDEFG', 0, None, 2) --> A C E G
>     s = slice(*args)
>     it = iter(range(s.start or 0, s.stop or sys.maxsize, s.step or 1))
>     try:
>         nexti = next(it)
>     except StopIteration:
>         return
>     for i, element in enumerate(iterable):
>         if i == nexti:
>             yield element
>             nexti = next(it)
> ```
>
> ##### 实例
>
> ```python
> list(islice([10, 6, 2, 8, 1, 3, 9], 5))
> [10, 6, 2, 8, 1]
>
> list(islice(count(), 6))
> [0, 1, 2, 3, 4, 5]
>
> list(islice(count(), 3, 10))
> [3, 4, 5, 6, 7, 8, 9]
>
> list(islice(count(), 3, 10 ,2))
> [3, 5, 7, 9]
> ```

#### 4.9 itertools.starmap(function, iterable)

> 返回一个迭代器, function (*c),将对iterable进行解包
>
> ##### 参考定义
>
> ```python
> def starmap(function, iterable):
>     # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
>     for args in iterable:
>         yield function(*args)
> ```
>
> ##### 实例
>
> ```python
> from itertools import starmap
>
> def foo(x, y):
>     return x + y
>
> list(starmap(foo, [('china', ' beijing'), ('USA', ' DC')]))
>
> # ['china beijing', 'USA DC']
> ```

#### 4.10 itertools.takewhile(predicate, iterable) 

> 和 dropwhile 相反
>
> predicate 是函数，iterable 是可迭代对象。对于 iterable 中的元素，如果 predicate(item) 为 true，则保留该元素，只要 predicate(item) 为 false，则立即停止迭代。
>
> #### 定义参考
>
> ```python
> def takewhile(predicate, iterable):
>     # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
>     for x in iterable:
>         if predicate(x):
>             yield x
>         else:
>             break
> ```

#### 4.11 itertools.tee(*iterable*, *n=2*) 

> 从单个可迭代中返回*n*独立迭代器
>
> ##### 定义参考
>
> ```python
> def tee(iterable, n=2):
>     it = iter(iterable)
>     deques = [collections.deque() for i in range(n)]
>     def gen(mydeque):
>         while True:
>             if not mydeque:             # when the local deque is empty
>                 try:
>                     newval = next(it)   # fetch a new value and
>                 except StopIteration:
>                     return
>                 for d in deques:        # load it to all the deques
>                     d.append(newval)
>             yield mydeque.popleft()
>     return tuple(gen(d) for d in deques)
> ```
>
> ##### 实例
>
> ```python
> from itertools import tee
>
> for i in tee('abcd'):
>     print(list(i))
> for i in tee('abcd', 4):
>     print("4", list(i))
>     
> """
> ['a', 'b', 'c', 'd']
> ['a', 'b', 'c', 'd']
> 4 ['a', 'b', 'c', 'd']
> 4 ['a', 'b', 'c', 'd']
> 4 ['a', 'b', 'c', 'd']
> 4 ['a', 'b', 'c', 'd']
>
> """
> ```

#### 4.12 itertools.zip_longest(*iterables, fillvalue=None) 

> 创建一个迭代器，聚合来自每个迭代器的元素。如果迭代的长度不均匀，则缺少的值将被填充*fillvalue*。迭代继续，直到最长可迭代被耗尽
>
> ##### 定义参考
>
> ```python
> class ZipExhausted(Exception):
>     pass
>
> def zip_longest(*args, **kwds):
>     # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
>     fillvalue = kwds.get('fillvalue')
>     counter = len(args) - 1
>     def sentinel():
>         nonlocal counter
>         if not counter:
>             raise ZipExhausted
>         counter -= 1
>         yield fillvalue
>     fillers = repeat(fillvalue)
>     iterators = [chain(it, sentinel(), fillers) for it in args]
>     try:
>         while iterators:
>             yield tuple(map(next, iterators))
>     except ZipExhausted:
>         pass
> ```
>
> ##### 实例
>
> ```python
> a = itertools.zip_longest('abcd', '123456789')
> print(list(a))
> b = zip('abcd', '123456789')
> list(b)
> ```
>
> ```python
> [('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), (None, '5'), (None, '6'), (None, '7'), (None, '8'), (None, '9')]
> ```

### 5.组合生成器

#### 5.1 itertools.product(**iterables*, *repeat=1*)

> 用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价
>
> ##### 定义参考
>
> ```python
> def product(*args, repeat=1):
>     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
>     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
>     pools = [tuple(pool) for pool in args] * repeat
>     result = [[]]
>     for pool in pools:
>         result = [x+[y] for x in result for y in pool]
>     for prod in result:
>         yield tuple(prod)
> ```
>
> ##### 实例
>
> ```python
> import itertools
> a = (1, 2, 3)
> b = ('A', 'B', 'C')
> c = itertools.product(a,b)
> for elem in c:
>     print elem
>
> (1, 'A')
> (1, 'B')
> (1, 'C')
> (2, 'A')
> (2, 'B')
> (2, 'C')
> (3, 'A')
> (3, 'B')
> (3, 'C')
> ```

####  5.2 itertools.permutations(iterable[, r])

> 创建一个迭代器，返回iterable中所有长度为r的项目序列，如果省略了r，那么序列的长度与iterable中的项目数量相同： 返回p中任意取r个元素做排列的元组的迭代器
>
> ##### 实例
>
> ```python
> list(permutations('ABC', 2))
> [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
>
> list(permutations('ABC'))
> [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
>
> ```

#### 5.3 itertools.combinations(iterable, r)

> 创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复)
>
> ##### 实例
>
> ```python
> list(combinations('ABC', 2))
> [('A', 'B'), ('A', 'C'), ('B', 'C')]
> ```

#### 5.4 itertools.combinations_with_replacement(iterable, r)

> 返回子序列,包含自身