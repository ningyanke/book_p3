###  函数的调用

####  调用规则

> 函数既可以返回调用函数本身(递归),可以返回函数标签,在Python中一切皆对象,函数也是python的对象.
>
> ```python
> In [34]: def foo1():
>     ...:     x = 3    #foo1的local变量
>     ...:     def foo2():   #嵌套函数foo2
>     ...:         y = 'hello' #foo2的local变量
>     ...:         z = 2   #foo2的local变
>     ...:         print(x)  
>     ...:         print(x + z )
>     ...:     return foo2  #返回函数foo2,
>     ...: 
> #直接调用函数foo1,返回的是foo1的本地变量foo2
> #想到与foo1() 是一个函数名,只想了foo2函数名
> In [35]: foo1()
> Out[35]: <function __main__.foo1.<locals>.foo2>
> # a1这个变量名标签指向了foo2这个函数名
> In [36]: a1 = foo1()
>
> In [37]: a1
> Out[37]: <function __main__.foo1.<locals>.foo2>
> #想到于直接调用foo2函数,foo2()
> In [38]: a1()
> 3
> 5
> #利用__name__函数,可以直观的看到a1 这个变量名指向了foo2这个函数名
> In [39]: a1.__name__
> Out[39]: 'foo2'
> ```
>
> 