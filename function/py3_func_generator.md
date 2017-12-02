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
> 使用迭代器的内置方法 `__next__  ` 和 ` next()` 方法,遍历元素
>
> ```python
> In [73]: e = iter(a)
>
> In [74]: next(e)
> Out[74]: 1
>
> In [75]: e.__next__
> Out[75]: <method-wrapper '__next__' of list_iterator object at 0x7f05571c8518>
>
> In [76]: e.__next__()
> Out[76]: 2
>
> In [77]: e.__next__()
> Out[77]: 3
>
> In [78]: e.__next__()
> ---------------------------------------------------------------------------
> StopIteration                             Traceback (most recent call last)
> <ipython-input-78-6024b5bd9bd2> in <module>()
> ----> 1 e.__next__()
>
> StopIteration: 
> ```
>
> 当遍历完毕时,会返回一个`StopIteration` 的错误.
>
> `for...in....` 遍历迭代 
>
> 当我们对一个`iterable` 使用`for ....in...` 进行遍历时,实际上是想调用`iter()` 方法得到一个`iterator` ,假设为`x ` ,然后循环的调用`x` 的`__next__()` (`next()`)方法,取得每一次的值,直到`iterator`为空,返回`StopIteration` 作为循环的结束的标准.`for....in...`会自动处理 `StopIteration` 异常,从而避免了抛出异常,从而使程序中断.流程图为:
>
> ```python
> x = [1, 2, 3]
> for i in x:
> 	print(x)
> ```
>
> ```mermaid
> graph LR
> id1["x = [1,2,3]"]
> id2>The iterable]
> id3["iterator"]
> id4>The iterator]
> id5((1))
> id6((2))
> id7((3))
> id8((fa:fa-times))
>
> id2 -.-> id1
>
> id1 -- "iter()" --> id3
>
> id3 -- "next()" --> id5
> id3 -- "next()" --> id6
> id3 -- "next()" --> id7
> id3 -- "next()" --> id8
> id4 -.-> id3
> ```
>
> 

#### `generator` 和 `yield`

> [官方](https://docs.python.org/3/glossary.html#term-generator)
>
> ```python
> generator
> A function which returns a generator iterator. It looks like a normal function except 
> that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.
>
> Usually refers to a generator function, but may refer to a generator iterator in some contexts.In cases where the intended meaning isn’t clear, using the full terms avoids ambiguity.
>
> generator iterator
> An object created by a generator function.
>
> Each yield temporarily suspends processing, remembering the location execution state (including local variables  and pending try-statements). When the generator iterator resumes, it picks-up where it left-off(in contrast to functions which start fresh on every invocation).
>
> generator expression
> An expression that returns an iterator. 
> It looks like a normal expression followed by a for expression defining a loop variable, range, 
> and an optional if expression. The combined expression generates values for an enclosing function:
> ```
>
> 可见,我们常说的生成器,就是带有`yield` 函数,而`generator iterator`则是`generator function`的返回值,即一个`generator`对象,而形如(`elem for elem in [1, 2, 3]`)的表达式,称为`generator expression`,实际使用与`generator`无异.
>
> 其实说白了,`generator`就是`iterator`的一种,以更优雅的方式实现的`iterator`.官方的说法是:
>
> ```python
> Python’s generators provide a convenient way to implement the iterator protocol.
> ```
>
> 你完全可以像使用`iterator`一样使用`generator`,当然除了定义.定义一个`iterator`,你需要分别实现`__iter__()`方法和`__next__()`方法,但`generator`只需要一个小小的`yield`	.
> `iterator`通过`__next__()`方法实现了每次调用,返回一个单一值的功能.而`yield`就是实现`generator`的__next__()方法的关键!先来看一个最简单的例子:

#### `yield` 直接跟值

> ```python
> In [83]: def g():
>    ....:     print '1 is' 
>    ....:     yield 1                          #1:first
>    ....:     print '2 is'
>    ....:     yield 2                          #2:second  
>    ....:     print '3 is'
>    ....:     yield 3                          #3:third
>    ....:     
>
> In [84]: z = g()
>
> In [85]: z 
> Out[85]: <generator object g at 0xb5e5c194>
>
> In [86]: next(z)
> 1 is
> Out[86]: 1
>
> In [87]: next(z)
> 2 is
> Out[87]: 2
>
> In [88]: next(z)
> 3 is
> Out[88]: 3
>
> In [89]: next(z)
> ---------------------------------------------------------------------------
> StopIteration                             Traceback (most recent call last)
> <ipython-input-89-7b32f85a2b4e> in <module>()
> ----> 1 next(z)
>
> StopIteration:
> ```
>
> 第一次调用`next()`方法时,函数似乎执行到`yield 1`,就暂停了.然后再次调用`next()`时,函数从`yield 1`之后开始执行的,并再次暂停.第三次调用`next(),`从第二次暂停的地方开始执行.第四次,抛出`StopIteration`异常.
>
> 事实上,`generator`确实在遇到`yield`之后暂停了,确切点说,是先返回了yield表达式的值,再暂停的.当再次调用next()时,从先前暂停的地方开始执行,直到遇到下一个`yield`.这与上文介绍的对`iterator`调用`next()`方法,执行原理一般无二.
>
> ```mermaid
> graph TB
>
> id3 -.-> id6
> subgraph one
> id1>"start"]
> id2["z=g()"]
> id3["first"]
> id4>"stop"]
>
> id1 --> id2 
> id2--> id3 
> id3 --> id4
> end
>
> id7 -.-> id10
> subgraph two
> id5>"start"]
> id6["first"]
> id7["second"]
> id8>"stop"]
>
>
> id5--> id6 
> id6 --> id7
> id7 --> id8
> end
> id11 -.-> id13
> subgraph there
> id9>"start"]
> id10["second"]
> id11["third"]
> id12>"stop"]
>
>
> id9 --> id10 
> id10 --> id11
> id11 --> id12
> end
>
> subgraph four
> id13["StopIteration"]
> end
> ```
>
> 每一次的结束点,是下一次的开始点,所以;`yield` 是有2个状态的(除了第一次之外),而使用`next()`这种形式调用的时候,开始点的`yield`的值都是`None`
>
> ```python
> In [110]: def foo():
>    .....:     yield None 
>    .....:     
>
> In [111]: a = foo()
>
> In [112]: next(a)
>
> In [113]: next(a)
> ---------------------------------------------------------------------------
> StopIteration                             Traceback (most recent call last)
> <ipython-input-113-3f6e2eea332d> in <module>()
> ----> 1 next(a)
>
> StopIteration: 
>
> In [114]: def foo():
>    .....:     yield
>    .....:     
>
> In [115]: a = foo()
>
> In [116]: next(a)
>
> In [118]: next(a)
> ---------------------------------------------------------------------------
> StopIteration                             Traceback (most recent call last)
> <ipython-input-118-3f6e2eea332d> in <module>()
> ----> 1 next(a)
>
> StopIteration:
>
> #这说明yield后默认就跟着None
> ```

#### `send(value) ` 传值给yield

> 除了可以在`yield` 之后直接加值外,`yield` 还支持第二种调用方式,`send(value)`,将`value` 作为`yield` **表达式**的当前值.你可以用该值再对其他变量进行赋值,这一段代码就很好理解了.当我们调用send(value)方法时,`generator`正由于`yield的`缘故被暂停了.
>
> 此时,`send(value)`方法传入的值作为`yield`表达式的值,函数中又将该值赋给了变量`s`,然后`print`函数打印`s`,循环再遇到`yield`,暂停返回.调用`send(value)`时要注意,要确保,`generator`是在`yield`处被暂停了,如此才能向`yield`表达式传值,也就是说第一次不能使用`send(value)`,因为`can't send non-None value to a just-started generator`
>
> ```python
> In [112]: def gen():
>      ...:     while True:
>      ...:         s = yield
>      ...:         print(s)
>      ...:         
>
> In [113]: g = gen()
>
> In [114]: g.send("hello")
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-114-76c03f080c2d> in <module>()
> ----> 1 g.send("hello")
>
> TypeError: can't send non-None value to a just-started generator
>
> In [115]: next(g)
>
> In [116]: g.send("hello")
> hello
> ```
>
> 

#### `send(value)`实例

> ```python
> In [124]: def echo(value=None):
>    .....:     while 1:
>    .....:         value = (yield value)
>    .....:         print 'The value is %s' %value
>    .....:         if vlaue:
>    .....:             value += 1
>    .....:             
>
> In [126]: g = echo(1)
>
> In [127]: next(g)
> Out[127]: 1
>
> In [128]: g.send(2)
> The value is 2
> Out[128]: 3
>
> In [129]: g.send(3)
> The value is 3
> Out[129]: 4
>
> In [130]: next(g)
> The value is None
> ```
>
> 上述代码既有`yield value`的形式,又有`value = yield`形式,看起来有点复杂.但以`yield`分离代码进行解读,就不太难了.
>
> * 第一次调用`next()`方法,执行到`yield value`表达式,保存上下文环境暂停返回1.
> * 第二次调用`send(value)`方法,从`value = yield`开始,打印,
> * 再次遇到`yield value`暂停返回.后续的调用`send(value)`或`next(`)都不外如是.
>
> 但是,这里就引出了另一个问题,`yield`作为一个暂停恢复的点,代码从`yield`处恢复,又在下一个`yield`处暂停.可见,在一次`next()`(非首次)或`send(value)`调用过程中,实际上存在2个`yield`,一个作为恢复点的`yield`与一个作为暂停点的`yield`.因此,也就有2个`yield`表达式.`send(value)`方法是将值传给恢复点`yield`;调用`next()`表达式的值时,其恢复点`yield`的值总是为`None`,而将暂停点的`yield`表达式的值返回.为方便记忆,你可以将此处的恢复点记作当前的(current),而将暂停点记作下一次的(next),这样就与next()方法匹配起来.

#### 使用场景

> 生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，,特别是结果集里还包含循环.这样做会消耗大量资源.
>
> 许多Python 2里的标准库函数都会返回列表，而Python 3都修改成了返回生成器，因为生成器占用更少的资源。
>
> 比如:通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
>
> 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的`list`，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，就是生成器：`generator`。
>
> 要创建一个`generator`，有很多种方法。第一种方法很简单，只要把一个列表生成式的`[]`改成`()`，就创建了一个`generator`：
>
> ```python
> >>> L = [x * x for x in range(10)]
> >>> L
> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> >>> g = (x * x for x in range(10))
> >>> g
> <generator object <genexpr> at 0x1022ef630>
> ```
>
> 如果要一个一个打印出来，可以通过`next()`函数获得`generator`的下一个返回值.
>
> ```python
> >>> next(g)
> 0
> >>> next(g)
> 1
> >>> next(g)
> 4
> >>> next(g)
> 9
> >>> next(g)
> 16
> >>> next(g)
> 25
> >>> next(g)
> 36
> >>> next(g)
> 49
> >>> next(g)
> 64
> >>> next(g)
> 81
> >>> next(g)
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> StopIteration
> ```
>
> 我们讲过，generator保存的是算法，每次调用`next(g)`，就计算出`g`的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出`StopIteration`的错误。
>
> 当然，上面这种不断调用`next(g)`实在是太变态了，正确的方法是使用`for`循环，因为generator也是可迭代对象：
>
> ```python
> >>> g = (x * x for x in range(10))
> >>> for n in g:
> ...     print(n)
> ... 
> 0
> 1
> 4
> 9
> 16
> 25
> 36
> 49
> 64
> 81
> ```
>
> 下面是一个计算斐波那契数列的生成器：
>
> ```python
> # generator version
> def fib(max):
>     n, a, b = 0, 0, 1
>     while n < max:
>        yield b
>         a, b = b, a + b
>         n = n + 1
>     return 'done'
> ```
>
> 函数使用方法如下：
>
> ```python
> for x in fib(1000000):
>     print(x)
>
> ```
>
> 用这种方式，我们可以不用担心它会使用大量资源。
>
> 但是用`for`循环调用generator时，发现拿不到generator的`return`语句的返回值。如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中：
>
> ```python
> >>> g = fib(6)
> >>> while True:
> ...     try:
> ...         x = next(g)
> ...         print('g:', x)
> ...     except StopIteration as e:
> ...         print('Generator return value:', e.value)
> ...         break
> ...
> g: 1
> g: 1
> g: 2
> g: 3
> g: 5
> g: 8
> Generator return value: done
> ```
>
> 然而，之前如果我们这样来实现的话：
>
> ```Python
> def fibon(n):
>     a = b = 1
>     result = []
>     for i in range(n):
>         result.append(a)
>         a, b = b, a + b
>     return result
> ```
> 这也许会在计算很大的输入参数时，用尽所有的资源
>
