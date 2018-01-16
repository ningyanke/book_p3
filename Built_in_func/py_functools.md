## functools

[TOC]

### 1.简介

> functools 是 Python 中很简单但也很重要的模块，主要是一些 Python 高阶函数相关的函数.
> 高阶函数，这是函数式编程范式中很重要的一个概念，简单地说， 就是一个可以接受函数作为参数或者以函数作为返回值的函数，因为 Python 中函数是一类对象， 因此很容易支持这样的函数式特性。
> functools 模块中函数只有` cmp_to_key、partial、reduce、total_ordering、update_wrapper、wraps` 这几个:
>
> ```python
> cmp_to_key: Convert a cmp= function into a key= function.
> get_cache_token: Returns the current ABC cache token.
> lru_cache: Least-recently-used cache decorator.
> namedtuple: Returns a new subclass of tuple with named fields.
> reduce: reduce(function, sequence[, initial]) -> value
> singledispatch: Single-dispatch generic function decorator.
> total_ordering: Class decorator that fills in missing ordering methods
> update_wrapper: Update a wrapper function to look like the wrapped function
> wraps: Decorator factory to apply update_wrapper() to a wrapper function
>
> ```

### 2.官方

> [官方文档](http://python.usyiyi.cn/translate/python_352/library/functools.html)

### 3.常用方法

#### 3.1 `reduce`

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

#### 3.2 偏函数partial和partialmethod

> 作用:
>
> functools.partial 通过包装手法，允许我们 "重新定义" 函数签名
>
> 用一些默认参数包装一个可调用对象,返回结果是可调用对象，并且可以像原始对象一样对待
>
> 冻结部分函数位置函数或关键字参数，简化函数,更少更灵活的函数参数调用
>
> ```python
> #args/keywords 调用partial时参数
> def partial(func, *args, **keywords):
>     def newfunc(*fargs, **fkeywords):
>         newkeywords = keywords.copy()
>         newkeywords.update(fkeywords)
>         return func(*(args + fargs), **newkeywords) #合并，调用原始函数，此时用了partial的参数
>     newfunc.func = func
>     newfunc.args = args
>     newfunc.keywords = keywords
>     return newfunc
>
> ```
>
> 声明：
>
> ```python
> urlunquote = functools.partial(urlunquote, encoding='latin1')
> ```
>
> 当调用 urlunquote(*args, **kargs)
>
> 相当于 urlunquote(*args, **kargs, encoding='latin1')
>
> E.g:
>
> ```python
> import functools
>
> def add(a, b):
>     return a + b
>
> add(4, 2)
> 6
>
> plus3 = functools.partial(add, 3)
> plus5 = functools.partial(add, 5)
>
> plus3(4)
> 7
> plus3(7)
> 10
>
> plus5(10)
> 15
>
> ```
>
> 应用:
>
> 典型的，函数在执行时，要带上所有必要的参数进行调用。
>
> 然后，有时参数可以在函数被调用之前提前获知。
>
> 这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。
>
> partialmethod 是 Python 3.4 中新引入的装饰器，作用基本类似于 partial， 不过仅作用于方法。举个例子就很容易明白：
>
> ```python
> class Cell(object):
>     def __init__(self):
>         self._alive = False
>     @property
>     def alive(self):
>         return self._alive
>     def set_state(self, state):
>         self._alive = bool(state)
>     set_alive = partialmethod(set_state, True)
>     set_dead = partialmethod(set_state, False)
> ```

#### 3.3 装饰器相关

##### wrapper

> 说到“接受函数为参数，以函数为返回值”，在 Python 中最常用的当属装饰器了。 functools 库中装饰器相关的函数是 update_wrapper、wraps，还搭配 WRAPPER_ASSIGNMENTS 和 WRAPPER_UPDATES 两个常量使用，作用就是消除 Python 装饰器的一些负面作用
>
> ```python
> def decorator(func):
>     def wrapper(*args, **kwargs):
>         return func(*args, **kwargs)
>     return wrapper
>
> @decorator
> def add(x, y):
>     return x + y
> add # <function __main__.decorator.<locals>.wrapper>
> ```
>
> 可以看到被装饰的函数的名称，也就是函数的 __name__ 属性变成了 wrapper， 这就是装饰器带来的副作用，实际上add 函数整个变成了 decorator(add)，而 wraps 装饰器能消除这些副作用,
>
> ```python
> from functools import wraps
> def decorator(func):
>     @wraps(func)
>     def wrapper(*args, **kwargs):
>         print('hello world')
>         return func(*args, **kwargs)
>     return wrapper
> @decorator
> def add(x,y):
>     return x + y
> add
>
> # Out[32]:
> # <function __main__.add>
> ```
>
> 会更正的属性定义在 `WRAPPER_ASSIGNMENTS` 中
>
> ```python
> In [8]: functools.WRAPPER_ASSIGNMENTS
> Out[8]: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
>
> In [9]: functools.WRAPPER_UPDATES
> Out[9]: ('__dict__',)
> ```

##### update_wrapper

> `update_wrapper `的作用与 `wraps` 类似，不过功能更加强大，换句话说，`wraps `其实是 `update_wrapper `的特殊化，实际上 `wraps(wrapped)` 相当于` partial(update_wrapper, wrapped=wrapped, **kwargs)`。
>
> 因此，上面的代码可以用 update_wrapper 重写如下:
>
> ```python
> def decorator(func):
>     def wrapper(*args, **kwargs):
>         return func(*args, **kwargs)
>     return update_wrapper(wrapper, func)
> ```

#### 3.4 用于比较的 cmp_to_key 和total_ordering

##### cmp_to_key

> cmp_to_key 是 Python 2.7 中新增的函数，用于将比较函数转换为 key 函数， 这样就可以应用在接受 key 函数为参数的函数中，比如 sorted、max 等等。 例如：
>
> ```python
> sorted(range(5), key=cmp_to_key(lambda x, y: y-x))      # [4, 3, 2, 1, 0]
> ```

##### total_ordering

> total_ordering 同样是 Python 2.7 中新增函数，用于简化比较函数的写法。如果你已经定义了 __eq__ 方法，以及 __lt__、__le__、__gt__ 或者 __ge__() 其中之一， 即可自动生成其它比较方法。官方示例
>
> ```python
> @total_ordering
> class Student:
>     def __eq__(self, other):
>         return ((self.lastname.lower(), self.firstname.lower()) ==
>                 (other.lastname.lower(), other.firstname.lower()))
>     def __lt__(self, other):
>         return ((self.lastname.lower(), self.firstname.lower()) <
>                 (other.lastname.lower(), other.firstname.lower()))
>   
> dir(Student)   
> # ['__doc__', '__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__module__']
> ```



