## 类属性和方法

> ```python
> Methods are functions that are called using the attribute notation. There are two flavors: built-in methods (such as append() on lists) and class instance methods. Built-in methods are described with the types that support them.
>
> If you access a method (a function defined in a class namespace) through an instance, you get a special object: a bound method (also called instance method) object. When called, it will add the self argument to the argument list. Bound methods have two special read-only attributes: m.__self__ is the object on which the method operates, and m.__func__ is the function implementing the method. Calling m(arg-1, arg-2, ..., arg-n) is completely equivalent to calling m.__func__(m.__self__, arg-1, arg-2, ..., arg-n).
>
> Like function objects, bound method objects support getting arbitrary attributes. However, since method attributes are actually stored on the underlying function object (meth.__func__), setting method attributes on bound methods is disallowed. Attempting to set an attribute on a method results in an AttributeError being raised. In order to set a method attribute, you need to explicitly set it on the underlying function object:
> ```
>
> 以上来自官网对函数方法的定义:
>
> 方法是使用属性符号(object.attribute)来调用的函数,有两种方法,內建方法和类实例方法,內建方法用支持他们的类型来描述.如果通过实例访问方法,就会得到一个特殊的对象: 一个帮顶方法对象,它将添加self参数在参数列表中,绑定方法有2中特殊的只读属性`m.__self__` ,`m.__func__` 实现方法的函数,调用`m(*args)` 等同于调用`m.__fun__(*args)` 
>
> 绑定方法对象支持获取任意属性,然而由于方法属性实际上存储在底层函数对象`meth.__func__` 上,设置方法属性在绑定方法上是不被允许的,强行设置会返回一个`AttributeError` ,如果想要设置属性,必须设置在底层函数上.
>
> ```python
> >>> class C:
> ...     def method(self):
> ...         pass
> ...
> >>> c = C()
> >>> c.method.whoami = 'my name is method'  # can't set on the method
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> AttributeError: 'method' object has no attribute 'whoami'
> >>> c.method.__func__.whoami = 'my name is method'
> >>> c.method.whoami
> 'my name is method'
> ```
>
> [Method](https://docs.python.org/3.6/library/stdtypes.html#object.__dict__)
>
> 类的方法也是属性.但方法是可调用(callable)的属性.
>
> 我们可以通过使用`callable()` 来判断一个函数的属性是不是一种方法
>
> ```python
> In [1]: def foo(x):
>    ...:     return x
>    ...:
>
> In [2]: callable(foo)
> Out[2]: True
>
> In [3]: callable(1)
> Out[3]: False
>     
> In [4]: class A:
>    ...:     name = 'Jack'
>    ...:     def foo(self,x):
>    ...:         return x
>    ...:
>
> In [5]: callable(A.name)
> Out[5]: False
>
> In [6]: callable(A.foo)
> Out[6]: True
> ```
>
> 类中的方法和函数定义一样,只不过传入的第一个参数是`self` ,这样在类实例化之后,实例作为第一个参数传入`m.__self__`,也就是说,方法也是由`name-object` 这样的结构.函数是具有传递数据的功能.
>
> 当实例调用一个`method` 时,它会先寻找`attribute ` (一个 `getattr()`操作),然后再调用结果返回.
>
> ```python
> In [20]: a = A()
>     
> In [21]: a.foo(1)
> ```
>
> is two steps; finding the attribute (which in this case looks up the attribute on the class, and treats it as a descriptor), then calls the resulting object, a method.
>
> 所有的函数都是`non-data descriptor` ,优先级小于实例属性的.实例没有属性时,会被`__getattribute__` 转换为`type(a).__dict__['foo'].__get__(a,type(a))` 这个非数据描述器中的值.
>
> 从命名空间上来说,类方法是属于类的本地作用域,而不是实例的,实例调用类方法,只是发生了继承.就像访问类属性一样,但是访问类方法会返回一个绑定对象,只有发成调用,才能返回方法中保存的值.
>
> * `1` 传入方法`foo` 的实体对象中
> * 最后.发生调用,返回方法实体中对应的值
>
> ```python
> In [22]: a.__dict__
> Out[22]: {}
>   
> In [23]: type(a).__dict__['foo'].__get__(a,type(a))
> Out[23]: <bound method A.foo of <__main__.A object at 0xb5dd73ac>>
> ```

> 当你输入`a.foo(1)` 时,值已经被传入,最后返回时才能返回需要的值.也就是`foo` 是变量名,对应的实体对象已经接受值.
>
> 当你直接赋值时:实例属性优先级高于`非数据描述器` ,变量名,变量标签就贴在你新加的值上,所以再次访问,得到的是`__dict__` 中的值.