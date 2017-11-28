###  函数是python的`first-class` 对象

> 在Python中一切皆对象,函数也是一种对象类型
>
> ```python
> issubclass 
> issubclass(...)
>     issubclass(C, B) -> bool
>     
>     Return whether class C is a subclass (i.e., a derived class) of class B.
>     When using a tuple as the second argument issubclass(X, (A, B, ...)),
>     is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).
>
> ```
>
> `issubclass` 用于判断一个是不是另一个的子类
>
> ```python
> a = 1
>
> print(a.__class__)
> print(issubclass(a.__class__, object))
>
> def foo():
>     pass
>
> print(foo.__class__)
> print(issubclass(foo.__class__, object))
> """
> 函数和普通变量a一样,都是顶级父类object的子类,a 是一个int 类型变量,foo 是一个函数类型变量,函数和python其他数据类型相同,都属于对象,其父类为object
> 这意味着
> 	函数和其他变量是一样的,变量是可以用来传递和修改值,函数也可以作为一种变量
> 	函数也可以作为函数的参数或者函数的返回值
> """
> class Line:
>     pass
>
> class Redline(Line):
>     pass
>
> class Rect:
>     pass
>
> print(issubclass(Redline, Line))
>
> print(issubclass(Rect, Line))
>
>
> ```
>
> 运行结果
>
> ```python
> <class 'int'>
> True
> <class 'function'>
> True
> True
> False
> ```
>
> 以上说明,
>
> ```python
> Elements with the fewest restrictions are said to have first-class status. Some of the ''rights and privileges'' of first-class elements are:
> 1. They may be named by variables.
> 2. They may be passed as arguments to procedures.
> 3. They may be returned as the results of procedures.
> 4. They may be included in data structure
> #一言以蔽之就是，你能把函数像普通变量一样任意地使用,。包括赋值，以及作为其它函数的参数和返回值。这样就能很容易地写出高阶函数与闭包的代码。
> ```
>
> 如下例子:
>
> ```python
> def add(x, y):
>     return x + y
>
> def sub(x, y):
>     return x - y
>
> def apply(func, x, y): #1
>     return func(x, y)  #2
>
> print(apply(add, 2, 1))  #3
> print(apply(sub, 2, 1))
>
> ```
>
> ```python
> 3
> 1
> ```
>
> 在这个例子中,函数`add` `sub` `apply` ,都是普通的函数对象:
>
> * 注释1处,`func` 变量用来接收传递来的函数变量(函数像变量一样传递)
> * 注释2处,`func` 用来执行传递来的函数变量(函数作为其他函数的返回值)
> * 注释3处,将其他函数传递到一个函数中,并执行,返回结果
>
> ```python
> def outer():
>     def inner():
>         print("Inside inner")
>     return inner #1
>
>
> foo1 = outer() #2
>
>
> print(foo1)
> foo1()
> ```
>
> ```python
> <function outer.<locals>.inner at 0x0000000000D9D8C8> #3
> Inside inner
> ```
>
> * 注释1 处,我们返回了内层函数本身(这个变量是函数标签),而并没有调用函数,(调用会带 `()` )
> * 注释2 处,因为调用内层函数,返回一个函数对象,我们要想使用它,必须用赋值语句, 用变量来代替这个对象         `name-object`
> * 注重理解,函数可以当做变量,可以用来传递和修改值,可以当做其他函数的参数,或者返回值.

