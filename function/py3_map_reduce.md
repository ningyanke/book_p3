### map/reduce

> Python內建了`map()`和`reduce()` 函数

#### map

> ```python
> map
> class map(object)
>  |  map(func, *iterables) --> map object
>  |  
>  |  Make an iterator that computes the function using arguments from
>  |  each of the iterables.  Stops when the shortest iterable is exhausted.
>  |  
>  |  Methods defined here:
>  |  
>  |  __getattribute__(self, name, /)
>  |      Return getattr(self, name).
>  |  
>  |  __iter__(self, /)
>  |      Implement iter(self).
>  |  
>  |  __new__(*args, **kwargs) from builtins.type
>  |      Create and return a new object.  See help(type) for accurate signature.
>  |  
>  |  __next__(self, /)
>  |      Implement next(self).
>  |  
>  |  __reduce__(...)
>  |      Return state information for pickling.
> ```
>
> `map` 函数,接受2个参数,一个是函数,另外接收一个`iterables`可迭代对象,`map`将传入的函数依次作用到序列的每个元素,并把结果作为一个新的`iterator`返回.
>
> 举例说明,比如我们有一个函数`f(x)=x**2`,要把这个函数作用于在一个`list`[1,2,3,4,5,6,7,8,9]上,可以用`map`实现如下.
>
> ```mermaid
> graph TD
> id1["f(x)=x**2" ]
> id2("[1,2,3,4,5,6,7,8,9]")
> id3((1))
> id4((2))
> id5((3))
> id6((4))
> id7((5))
> id8((6))
> id9((7))
> id10((8))
> id11((9))
> id12((1))
> id13((4))
> id14((9))
> id15((16))
> id16((25))
> id17((36))
> id18((49))
> id19((64))
> id20((81))
> id21("[1, 4, 9, 16, 25, 36, 49, 64, 81]")
> id1 --> id2
> id2 --> id3
> id2 --> id4
> id2 --> id5
> id2 --> id6
> id2 --> id7
> id2 --> id8
> id2 --> id9
> id2 --> id10
> id2 --> id11
> id3 --> id12
> id4 --> id13
> id5 --> id14
> id6 --> id15
> id7 --> id16
> id8 --> id17
> id9 --> id18
> id10 --> id19
> id11 --> id20
> id12 --> id21
> id13 --> id21
> id14 --> id21
> id15 --> id21
> id16 --> id21
> id17 --> id21
> id18 --> id21
> id19 --> id21
> id20 --> id21
>
> ```
>
> Python代码的实现
>
> ```python
> In [45]: list1
> Out[45]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
>
> In [46]: def f_L(x):
>    ....:     return  x**2
>    ....: 
>
> In [47]: a = map(f,list1)
>
> In [48]: list(a)
> Out[48]: [1, 4, 9, 16, 25, 36, 49, 64, 81]
> ```
>
> **`map()` 传入的第一个参数`f` 是函数对象本身,而不是函数的调用**,结果生成的是一个`iterator` ,`iterator`是一个**惰性序列** ,因此`list()` 函数可以让整个序列转换返回一个`list`
>
> 当然这个例子也可以通过使用循环来实现:
>
> ```python
> L = []
> for i in [1,2,3,4,5,6,7,8,9]:
>     L.append(i**2)
> print(L)
> ```
>
> 的确是可以,但是,从上面的循环结构,我们不能马上理解出"把f(x)作用在list的每一个元素并把结果生成一个新的list".这个是平铺直叙,但是`map`作为高阶函数,事实上,它把整个规则抽象化了.
>
> 假如,我们想要把整个`list`中的所有数字转换为字符串,当然 循环结构是可以实现的,但是等于,我们每次对`list1`提出一次操作,就需要去思考循环一次,当然可以把整个思考的过程抽象成函数.

#####  reduce

> ```python
> In [50]: from functools import reduce
>
> In [51]: help(reduce)
>
> Help on built-in function reduce in module _functools:
>
> reduce(...)
>     reduce(function, sequence[, initial]) -> value
>     
>     Apply a function of two arguments cumulatively to the items of a sequence,
>     from left to right, so as to reduce the sequence to a single value.
>     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
>     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
>     of the sequence in the calculation, and serves as a default when the
>     sequence is empty.
>
> ```
>
> `reduce` 是把函数作用在一个序列上(eg:`[1,2,3,4,..]`) ,这个函数必须接受2个参数,`reduce` 把结果继续和序列的下一个元素做累积计算,其效果是:
>
> ```python
> reduce(function,sequence[,starting_varlue])
> reduce(f,[x1,x2,x3,x4]) == f(f(f(x1,x2),x3),x4)
> #对序列中的item顺序迭代调用function,如果有starting_value,还可以作为初始值调用
> ```
>
> 比如说一个序列求和:
>
> ```python
> from functools import reduce
> def add(x,y)
> 	return x+y
> reduce(add,[1,2,3,4])
> ```
>
> 比如,将序列`[1,3,5,7,9]` 转换为整数`13579` ,用`reduce`实现
>
> ```python
> In [53]: list2 = [1,3,5,7,9]
>
> In [54]: def foo(x,y):
>    ....:     return int(str(x) + str(y))
>    ....: 
>
> In [55]: a = reduce(foo,list2)
>
> In [56]: a 
> Out[56]: 13579
> #-----------------------------------------
> In [60]: def foo1(x,y):
>    ....:     return x*10 + y
>    ....: 
>
> In [61]: c = reduce(foo1,list2)
>
> In [62]: c 
> Out[62]: 13579
>
> ```
>
> 这个例子本身没多大用处，但是，如果考虑到字符串`str`也是一个序列，对上面的例子稍加改动，配合`map()`，我们就可以写出把`str`转换为`int`的函数：
>
> ```python
> >>> from functools import reduce
> >>> def fn(x, y):
> ...     return x * 10 + y
> ...
> >>> def char2num(s):
> ...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
> ...
> >>> reduce(fn, map(char2num, '13579'))
> 13579
> ```
>
> 整理成一个
>
> ```python
> from functools import reduce
>
> def str2int(s):
>     def fn(x, y):
>         return x * 10 + y
>     def char2num(s):
>         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
>     return reduce(fn, map(char2num, s))
> ```
>
> 还可以用`lambda`继续简化
>
> ```python
> from functools import reduce
>
> def char2num(s):
>     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
>
> def str2int(s):
>     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
> ```

##### 练习

> eg. 1
>
> 利用map函数,把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
>
> ```python
> i = 0
> name_list = []
> while i < 3:
>     name = input("请输入用户名:")
>     i += 1
>     name_list.append(name)
>
> def foo(x):
>
>     return x.lower().capitalize()
>
> a = map(foo,name_list)
>
> print(list(a))
> ```
>
> eg. 2
>
> Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
>
> ```python
>
> from  functools import reduce
>
> def foo(x,y):
>     return x * y
>
> b = reduce(foo,[1,2,3,4])
> print(b)
> ```
>
> eg. 3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
>
> ```python
> from functools import reduce
>
> a = '123.456'
>
> def foo(x,y):
>     return x*10 + y
>
> def main(ch_nu):
>     def foo1(x):
>         return int(x)
>
>     def foo3(x):
>         return int(x)/1000
>
>     def foo2(x1,x2):
>         x1 = reduce(foo,map(foo1,x1))
>         x2 = reduce(foo,map(foo3,x2))
>         print(x1 + x2)
>
>     return foo2(*ch_nu)
>
> main(a.split("."))
> ```
>
> 
