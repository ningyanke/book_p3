###  变量的生存周期

#### 生存周期

> ```python
> def foo():
>     x = 1
> foo()
> print (x)
> ```
>
> ```python
> ---------------------------------------------------------------------------
> NameError                                 Traceback (most recent call last)
> <ipython-input-23-81745ac23551> in <module>()
> ----> 1 print(x)
>
> NameError: name 'x' is not defined
> ```
>
> 函数的变量是有生存周期的,变量的生存周期和作用域息息相关,其作用域销毁时,变量也就销毁了.
>
> 以上例子:
>
> - 1. `x`  是在 `foo()`内部定义的.在`foo()` 函数的local作用域,
> - 2. 全局打印`x` ,位于全局作用域,因此,在全局作用域中寻找变量`x` 的值,没有找到,报错
>
> ```python
> def outer():
>     x = 1
>     def inner():
>         print(x) #1
>     inner()  #2
>
> outer()
> ```
>
> ```python
> 1
> ```
>
>  这个例子比普通的函数定义看起来复杂了点，实际上都是合理的。
>
> - 1，  # 1 的地方python寻找名为x的local变量，在inner作用域内的local中寻找不到，python就在外层作用域中寻找，其外层是outer函数，x是定义在outer作用域内的local变量
> - 2，  # 2的地方，调用了inter函数，这里需要特别注意，inner也只是一个变量名，是遵循python的变量查询规则的(python先在outer函数的作用域中寻找名为inter的local变量)