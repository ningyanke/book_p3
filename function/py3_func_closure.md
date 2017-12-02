### 函数闭包

#### 函数作为返回值

> 高阶函数除了可以接受函数作为参数外,还可以把函数作为返回值,返回,
>
> 我们来实现一个可变参数的求和,通常情况下,可以如此定义
>
> ```python
> def calc_sam(*args):
>     ax = 0  
>     for n in args:
>         ax = ax + n
>     return ax 
> ```
>
> 但是，如果不需要立刻返回求和的结果，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
>
> ```python
> def lazy_sum(*args):
>     def sum():
>         ax = 0
>         for n in args:
>             ax = ax + n
>         return ax 
>     return sum 
> ```
>
> 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
>
> ```python
> >>> f = lazy_sum(1, 3, 5, 7, 9)
> >>> f
> <function lazy_sum.<locals>.sum at 0x101c6ed90>
> ```
>
> '调用`f()` 时,才真正计算求和的结果:
>
> ```python
> >>> f()
> 25
> ```
>
> 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
>
> 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
>
> ```python
> >>> f1 = lazy_sum(1, 3, 5, 7, 9)
> >>> f2 = lazy_sum(1, 3, 5, 7, 9)
> >>> f1==f2
> False
> ```
>
> 

#### 闭包

> 先看一个例子:
>
> ```python
> def outer():
>     print("outer local namespaces", locals())
>     x = 1
>
>     def inner():
>         print("inner local namespaces", locals())
>         print(x) #1
>
>     return inner
>
>
> foo = outer()
> print(foo.__closure__)#2
>
> foo()
> ```
>
> ```Python
> outer local namespaces {}
> (<cell at 0x0000000000677C48: int object at 0x000000005AA222B0>,)
> inner local namespaces {'x': 1}
> 1
> ```
>
> 从这个例子我们看到,内层函数`inner` (**注意不是调用内层函数**) 作为了外层函数的返回值.然后存储在了变量`foo`中,我们可以调用`foo()`直接调用内层函数`innner()` ,但是从作用域的规则来看.
>
> * x是outer函数里的local变量 
>
> * 在#1处，inner打印x时，python在inner的local中寻找x，找不到再到外层作用域(outer函数)中寻找，找到后打印
>
> 看起来一切都ok,那么从变量的生命周期(lifetime)的角度看:
>
> * x是outer的local变量，这意味着只有outer运行时，x才存在，那么按照python的运行的模式，我们不能
>   在outer结束后再去调用inner
>
> * 在我们调用inner的时候，x应该不存在了(print的时候应该不存在的)，应该会发生一个运行时错误或者其他错误.
>
>   ​
>
> 但是这一切都没有发生，`innner `函数依旧正常执行，打印了x . 
>
> python支持一种特性叫做函数闭包(`functino closures` ):在非全局`global` 作用域中定义`inner`函数(嵌套函数)时，会记录下他的嵌套函数`namespace`(嵌套函数作用域的`local` )，可以通过`__closure__`这个属性来获得inner函数的外层嵌套函数的`namespaces`
>
> 注意，每次调用outer函数，inner函数都是新定义的，上面例子中，x是固定的，所以每次调用inner函数的结果都一样.
>
> 下面看一个不同的例子:
>
> ```python
> def outer(x):
>     def inner():
>         print(x)
>
>     return inner
>
>
> p1 = outer(1)
> p2 = outer(2)
>
> print(p1.__closure__)
> p1()
> print(p2.__closure__)
> p2()
>
> ```
>
> ```python
> (<cell at 0x0000000000677C78: int object at 0x000000005AA222B0>,)
> 1
> (<cell at 0x0000000000677CA8: int object at 0x000000005AA222D0>,)
> 2
>
> ```
>
> 通过上面例子，我们能看到**闭包实际上就是记录了外层嵌套函数作用域中的local变量**
>
> **另外需要特别注意的是,返回的函数并没有立刻执行,而是在调用`f()` 时才执行**
>
> ```python
> def count():
>     fs = []
>     for i in range(1, 4):
>         def f():
>              return i*i
>         fs.append(f)
>     return fs
>
> f1, f2, f3 = count()
> ```
>
> 每次循环,都创建了一个新的函数,然后,把创建的3个函数都返回了,那么`f1(),f2(),f3()`的函数的返回值是
>
> ```python
> >>> f1()
> 9
> >>> f2()
> 9
> >>> f3()
> 9
> ```
>
> 这是因为函数引用了变量`i` ,但它并没有立即执行,而是等到三个函数都返回时,他们所引用的变量`i` 已经变成了`3`,最后变成了`9`,如下
>
> ```python
> def count():
>     fs = []
>     for i in range(1, 4):
>         print("local_1", locals())
>
>         def f():
>             print("local_2", locals())
>             return i * i
>
>         fs.append(f)
>         print("local_3", locals())
>     return fs
>
>
> f1, f2, f3 = count()
>
> print(f1.__closure__, f2.__closure__, f3.__closure__)
> print(f1(), f2(), f3())
>
> ```
>
> ```python
> local_1 {'i': 1, 'fs': []}
> local_3 {'i': 1, 'fs': [<function count.<locals>.f at 0x000000000070D9D8>], 'f': <function count.<locals>.f at 0x000000000070D9D8>}
> local_1 {'i': 2, 'fs': [<function count.<locals>.f at 0x000000000070D9D8>], 'f': <function count.<locals>.f at 0x000000000070D9D8>}
> local_3 {'i': 2, 'fs': [<function count.<locals>.f at 0x000000000070D9D8>, <function count.<locals>.f at 0x000000000070DA60>], 'f': <function count.<locals>.f at 0x000000000070DA60>}
> local_1 {'i': 3, 'fs': [<function count.<locals>.f at 0x000000000070D9D8>, <function count.<locals>.f at 0x000000000070DA60>], 'f': <function count.<locals>.f at 0x000000000070DA60>}
> local_3 {'i': 3, 'fs': [<function count.<locals>.f at 0x000000000070D9D8>, <function count.<locals>.f at 0x000000000070DA60>, <function count.<locals>.f at 0x000000000070DAE8>], 'f': <function count.<locals>.f at 0x000000000070DAE8>}
> (<cell at 0x0000000000687D08: int object at 0x000000005AA222F0>,) (<cell at 0x0000000000687D08: int object at 0x000000005AA222F0>,) (<cell at 0x0000000000687D08: int object at 0x000000005AA222F0>,)
> local_2 {'i': 3}
> local_2 {'i': 3}
> local_2 {'i': 3}
> 9 9 9
> ```
>
> 可以看到每次返回的列表中都是`fs` 列表只是生成了内存中的函数`f` 本身的对应位置,但是`f` 并没有被调用,当执行完毕,调用`f()` 时,此时调用的是变量 `i=3` 的值.
>
> ### **返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量** 
>
> 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
>
> ```python
> def count():
>     def f(j):
>         def g():
>             return j*j
>         return g
>     fs = []
>     for i in range(1, 4):
>         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
>     return fs
> ```
>
> ```python
> >>> f1, f2, f3 = count()
> >>> f1()
> 1
> >>> f2()
> 4
> >>> f3()
> 9
> ```
>
> 