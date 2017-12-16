## 类属性和方法

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
> 类中的方法和函数定义一样,只不过传入的第一个参数是`self` ,这样在类实例化之后,实例作为第一个参数传入,也就是说,方法也是由`name-object` 这样的结构.函数是具有传递数据的功能.
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
> 函数具有保存数据的功能:
>
> * `1` 传入函数`foo` 实体对象中.
> * 最后.返回函数实体中对应的值
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