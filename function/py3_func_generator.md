### 生成器 

> 要理解生成器(generator),要在理解一下`迭代(iteration)`, `迭代器(iterator)`, 和`可迭代对象(iterable)`,这个三个概念: 
>
> * 迭代(`iteration`):在python中迭代通常是通过`for...in...`来实现的.而且只要是可迭代对象`iterable`,都能进行迭代.
>
> * 可迭代对象(`iterable`):Python中的任意的对象，只要它定义了可以返回一个迭代器的 `__iter__`方法，或者定义了可以支持下标索引的`__getitem __`方法，那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象.返回的是一个`iterator` 对象.[官方解释](https://docs.python.org/3/glossary.html#term-iterable)
>
>   ```python
>   An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics.
>
>   Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), …). When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. This iterator is good for one pass over the set of values. When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. The for statement does that automatically for you, creating a temporary unnamed variable to hold the iterator for the duration of the loop. See also iterator, sequence, and generator.
>   ```
>
>
> * 迭代器(`iterator` ) : 简单的说,迭代器就是实现了`iterator.__iter__()` 和`iterator.__next__()` 的对象,`iterator.__iter__()`方法返回的是`iterator`对象本身.根据官方的说法,正是这个方法,实现了`for ... in ...`语句.而`iterator.__next__()`是`iterator`区别于`iterable`的关键了,它允许我们显式地获取一个元素.当调用next()方法时,实际上产生了2个操作:
>     - 1.更新iterator状态，令其指向后一项，以便下一次调用,每一个值过后,指针移动到下一位,对`iterator`遍历完后,其变成了一个空的容器,但不是`None` ,移动指针,可进行下一次遍历
>     - 2.返回当前结果
>
>     ```python
>     An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in function next()) return successive items in the stream. When no more data are available a StopIteration exception is raised instead. At this point, the iterator object is exhausted and any further calls to its __next__() method just raise StopIteration again. Iterators are required to have an __iter__() method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. One notable exception is code which attempts multiple iteration passes. A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.
>     ```
>
> 实例理解:
>
> ```python
> >>> from collections import Iterable, Iterator
> >>> a = [1,2,3]   # 众所周知,list是一个iterable
> >>> b = iter(a)   # 通过iter()方法,得到iterator,iter()实际上调用了__iter__(),
> >>> isinstance(a, Iterable)
> True
> >>> isinstance(a, Iterator)
> False
> >>> isinstance(b, Iterable)
> True
> >>> isinstance(b, Iterator)
> True
> ```
>
> **可见,`itertor` 一定是`iterable` ,但`iterable `不一定是`itertor `**
>
> ```python
> >>> dir(a)
> ['__add__','__class__','__contains__','__delattr__','__delitem__','__dir__','__doc__','__eq__','__format__','__ge__','__getattribute__','__getitem__','__gt__','__hash__','__iadd__','__imul__','__init__','__iter__','__le__','__len__','__lt__','__mul__','__ne__','__new__','__reduce__','__reduce_ex__','__repr__', '__reversed__','__rmul__', '__setattr__','__setitem__','__sizeof__','__str__', '__subclasshook__','append','clear' 'copy','count','extend','index','insert', 'pop','remove', 'reverse','sort']
>
> >>>dir(b)
>  ['__class__','__delattr__', '__dir__', '__doc__','__eq__', '__format__','__ge__' ,'__getattribute__', '__gt__','__hash__','__init__','__iter__','__le__','__length_hint__',
>  '__lt__','__ne__','__new__','__next__','__reduce__','__reduce_ex__','__repr__','__setattr__', '__setstate__','__sizeof__','__str__','__subclasshook__']
> ```
>
> 可以看到迭代器具有`__next__` 这个方法,可迭代对象具有`__getitem__`
>
> 迭代器是消耗型的,随着指针的移动,遍历完毕以后,就为空,但是不是`None`
>
> ```python
> >>> c = list(b)
> >>> c
> [1, 2, 3]
> >>> d = list(b)
> >>> d
> []
>
>
> # 空的iterator并不等于None.
> >>> if b:
> ...   print(1)
> ...
> 1
> >>> if b == None:
> ...   print(1)
> ...
>
> ```
>
> 
>
> d

