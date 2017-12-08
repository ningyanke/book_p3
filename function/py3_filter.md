### `filter`

> ```python
> class filter(object)
>  |  filter(function or None, iterable) --> filter object
>  |  
>  |  Return an iterator yielding those items of iterable for which function(item)
>  |  is true. If function is None, return the items that are true.
> ```
>
> Python内建的`filter()` 函数用于过滤序列
>
> 和`map()` 类似.`filter()` 也接收一个函数和一个序列,和`map()` 不同的是,`filter()` 把传入的函数依次作用于每个元素,然后根据返回值是`True` 或者`False` 来决定保留还是丢弃该元素.
>
> 例如,在一个list中,删掉偶数,只保留奇数,
>
> ```python
> In [2]: def is_odd(x):
>    ...:     return  x % 2 != 0
>    ...: 
>
> In [3]: list(filter(is_odd,[1,2,3,4,5,6,7,8,9]))
> Out[3]: [1, 3, 5, 7, 9]
>
> ```
>
> 把一个序列中的空字符串删除:
>
> ```python
> In [12]: a 
> Out[12]: 'dfdf fdfds fsdf sdfa adf dsaf asdf sadf '
> In [13]: def foo(x):
>     ...:     return x != " "
>     ...: 
>     ...: 
>
> In [14]: list(filter(foo,a))
> In [15]: b.join(list(filter(foo,a)))
> Out[15]: 'dfdffdfdsfsdfsdfaadfdsafasdfsadf'
> ```
>
> ```python
> In [19]: def not_empty(s):
>     ...:     return s and s.strip()
>     ...: 
>
> In [20]: list(filter(not_empty,["a"," ",'B','None']))
> Out[20]: ['a', 'B', 'None']
> ```
>
> `filter()`这个高阶函数 关键在于正确的实现一个"筛选"函数
>
> 注意到 `filter()` 函数返回的是一个`iterator` ,也就是一个惰性序列,所以要完成`filter()` 的计算结果,需要使用`list()` 函数获取结果,并返回list
>
> ### 用filter求素数
>
> 计算[素数](http://baike.baidu.com/view/10626.htm)的一个方法是[埃氏筛法](http://baike.baidu.com/view/3784258.htm)，它的算法理解起来非常简单：
>
> 首先，列出从`2`开始的所有自然数，构造一个序列：
>
> 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
>
> 取序列的第一个数`2`，它一定是素数，然后用`2`把序列的`2`的倍数筛掉：
>
> 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, 9, ~~10~~, 11, ~~12~~, 13, ~~14~~, 15, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...
>
> 取新序列的第一个数`3`，它一定是素数，然后用`3`把序列的`3`的倍数筛掉：
>
> 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...
>
> 取新序列的第一个数`5`，然后用`5`把序列的`5`的倍数筛掉：
>
> 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...
>
> 不断筛下去，就可以得到所有的素数。
>
> 用Python来实现这个算法，可以先构造一个从`3`开始的奇数序列
>
> ```python
> def _odd_iter():
>     n = 1
>     while True:
>         n = n + 2
>         yield n
> ```
>
> 注意这是一个生成器，并且是一个无限序列。
>
> 然后定义一个筛选函数
>
> ```python
> def _not_divisible(n):
>     return lambda x: x % n > 0
> ```
>
> 最后，定义一个生成器，不断返回下一个素数：
>
> ```python
> def primes():
>     yield 2
>     it = _odd_iter() # 初始序列
>     while True:
>         n = next(it) # 返回序列的第一个数
>         yield n
>         it = filter(_not_divisible(n), it) # 构造新序列
> ```
>
> 这个生成器先返回第一个素数`2`，然后，利用`filter()`不断产生筛选后的新的序列。
>
> 由于`primes()`也是一个无限序列，所以调用时需要设置一个退出循环的条件：
>
> ```python
> # 打印1000以内的素数:
> for n in primes():
>     if n < 1000:
>         print(n)
>     else:
>         break       
> ```
> 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。
