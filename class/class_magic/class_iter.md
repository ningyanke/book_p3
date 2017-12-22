## 迭代器器对象

> 大多数的容器对象都可以使用`for` 语句循环遍历.比如
>
> ```python
> In [1]: for element in [1,2,3]:
>    ...:     print(element)
>    ...:
> 1
> 2
> 3
>
> In [2]: for element in (1,2,3):
>    ...:     print(element,end=" ")
>    ...:
> 1 2 3
> In [3]: for key in {'one':1,"two":2}:
>    ...:     print(key)
>    ...:
> one
> two
>
> In [4]: for char in "1234":
>    ...:     print(char,end=" ")
>    ...:
> 1 2 3 4
>
> In [5]: for line in open("myfile.txt"): # 文件对象,类文件对象都可以
>    ...:     print(line,end=" ")
>    ...:
> ```
>
> 这种访问方式清晰，简洁，方便。Python中 `for` 是通过在容器对象上调用`iter() ` 完成遍历的,`iter()` 函数返回一个迭代器对象,并调用`__next__` 方法输出其中的内容.当没有更多的元素时,`__next__()` 引发一个`StopIteration` 的异常来告诉`for` 循环终止.可以使用內建的`next() ` 方法来调用`__next__` 方法.比如:
>
> ```python
> In [6]: s = 'abc'
>
> In [7]: it = iter(s)
>
> In [8]: it
> Out[8]: <str_iterator at 0xb5eea5ec>
>
> In [9]: next(it)
> Out[9]: 'a'
>
> In [10]: next(it)
> Out[10]: 'b'
>
> In [11]: next(it)
> Out[11]: 'c'
>
> In [12]: next(it)
> ---------------------------------------------------------------------------
> StopIteration                             Traceback (most recent call last)
> <ipython-input-12-2cdb14c0d4d6> in <module>()
> ----> 1 next(it)
>
> StopIteration:
> ```
>
> 对于自定义的类而言,添加迭代行为是非常容易的.只要实现了迭代器协议即可

### 自定义迭代器(单个)

> 在类内部定义迭代器协议,`__iter__` 和`__next__` .
>
> ```python
> An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its __next__() method just raise StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.
> ```
>
> * 使`__iter__`  just return self ,因为 我们定义的对象本身就是可迭代的
> * 使用`__next__` 循环遍历,当遍历完时,返回一个`StopIteration` 的异常
>
> ```python
> class Rerverse:
>     """
>     Iterator for looping over a sequnce backwards
>     """
>     def __init__(self, data):
>         self.data = data 
>         self.index = len(data)
>     
>     def __iter__(self):   # 返回一个迭代器对象本身 iterator object itself 
>         return self       #  或者是一个可迭代对象也是可以接受的
>     					  # 在这里 类本身就是一个迭代器对象 返回self 
>     
>     def __next__(self):
>         if self.index == 0:
>             raise(StopIteration)
>         self.index = self.index - 1 
>         return self.data[self.index]
>     
> rev = Rerverse('spam')
>
> for char in rev:
>     print(char, end=" ")
>     
> for i in rev:
>     for j in rev:
>         print(i+j)        
> ```
>
> ```python
> m a p s 
> ```
>
> 更简单的采用 `yield`生成一个 生成器来创建.
>
> ```python
> def counter(low, high):
>     current = low
>     while current <= high:
>         yield current
>         current += 1
>
> for c in counter(3, 8):
>     print(c)
> ```
>
> 

### 有多个迭代器的对象	

> ```python
> Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted.
> ```
>
> 对于大多数的内置类型(`list,tuple,dict`) 他们都支持多次迭代.
>
> ```python
> S = "abc"
>
> for x in S:
>     for y in S:
>         print(x + y)
>
> def foo1(value):
>     while True:
>         value = yield value
>         value = value + 1
>     
> foo1 = foo1(2)
> print(next(foo1))
> foo1.send(3)
> foo1.send(4)
> ```
>
>  而`map,zip` 这样的内置函数都是单迭代对象
>
> ```python
> def foo2(x):
>     return x**2
> a = map(foo2,[1,2,3,4])
> print(list(a))
> ```
>
> 当自己用类别写用户定义的迭代器时,是由我们自己来决定是支持一个单个的或者多个活跃的迭代器,
>
> 要达到多个迭代器的效果,`__iter__` 只需要替迭代器定义新的状态对象,而不是返回`self` 
>
> 这有点类似于循环遍历元素,
>
> ```python
> next(...)
>     next(iterator[, default])
>     
>     Return the next item from the iterator. If default is given and the iterator
>     is exhausted, it is returned instead of raising StopIteration.
>
> Help on built-in function iter in module builtins:
>
> iter(...)
>     iter(iterable) -> iterator
>     iter(callable, sentinel) -> iterator
>     
>     Get an iterator from an object.  In the first form, the argument must
>     supply its own iterator, or be a sequence.
>     In the second form, the callable is called until it returns the sentinel.
>     
> Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the iteration methods.
>
> One method needs to be defined for container objects to provide iteration support:
>
> container.__iter__()
> Return an iterator object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.
>
> The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:
>
> iterator.__iter__()
> Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.
>
> iterator.__next__()
> Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.
> ```
>
> ```python
> from collections import Iterable,Iterator
> class SkipIterator:
>     def __init__(self, wrapper):
>         self.wrapper = wrapper
>         self.offset = 0
>     def __iter__(self):
>         return self
>     
>     def __next__(self):
>         if self.offset >= len(self.wrapper):
>             raise(StopIteration)
>         else:
>             item = self.wrapper[self.offset]
>             self.offset += 2 
>             return item 
> class SkipObject:
>     def __init__(self, wrapper):
>         self.wrapper = wrapper
>     def __iter__(self):
>        # print(isinstance(SkipIterator(self.wrapper), Iterator))
>         return SkipIterator(self.wrapper)
>     
> if __name__ == "__main__":
>     alpha = "abcde"
>     skipper = SkipObject(alpha)
>     I = iter(skipper)
>     print(next(I),next(I),next(I))
>     print(isinstance(skipper,Iterable))
>     print(callable(skipper))
>     print(isinstance(I, Iterator))
>
>     for x in skipper:
>         for y in skipper:
>             print(x + y ,end =" ")
> ```
>
> 正如上面提到的`class` 这个`container` 的`__iter__`只需要保证返回一个`iterator` 即可,而返回的对象是需要遵守迭代器协议的.
>
> `__iter__` 必须保证返回一个迭代器对象
>
> ```python
> class foo:
>     def __init__(self,value):
>        self.value = value 
>     def __iter__(self):
>         return (i for i in [1,2,3])    
> foo = foo('abc')
> from collections import Iterable
> print(isinstance(foo,Iterable))
> print(isinstance([1,2,3],Iterable))
>
> i = iter(foo)
> print(next(i))
> ```
>
> 在比如:
>
> ```python
> class C:
>     def __init__(self):
>         self.stuff = ["a","b","c","d"]
>     def __iter__(self):
>         return iter(self.stuff)
> thing = C()
> for x in thing:
>     for y in thing:
>         print (x,y,x ==y,end = " ")
> ```
>
> 如果要实现一个自定义的多迭代器的类,则需要定义两个类
>
> ```python
> class C:
>     def __init__(self):
>         self.stuff = ["a","b","c","d"]
>     def __iter__(self):
>         return C_iterator(self)
>  
> class C_iterator:
>     def __init__(self, parent):
>         self.idx = 0
>         self.parent =parent 
>         
>     def __iter__(self):
>         return self
>     def __next__(self):
>         self.idx += 1
>         if self.idx > len(self.parent.stuff):
>             raise(StopIteration)
>         else:
>             return self.parent.stuff[self.idx - 1]
>         
> thing = C()
> for x in thing:
>     for y in thing:
>         print (x,y,x ==y,end = " ")
> ```
>
> 
