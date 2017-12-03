### 函数的定义

#### 标准定义

> 在[计算机科学](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)中，**子程序**（英语：Subroutine, procedure, function, routine, method, subprogram, callable unit），是一个大型程序中的某部分代码，由一个或多个语句块组成。它负责完成某项特定任务，而且相较于其他代码，具备相对的独立性。
>
> 一般会有输入参数并有返回值，提供对过程的封装和细节的隐藏。这些代码通常被集成为[软件库](https://zh.wikipedia.org/wiki/%E8%BD%AF%E4%BB%B6%E5%BA%93)。
>
> 函数在[面向过程](https://zh.wikipedia.org/wiki/%E7%A8%8B%E5%BA%8F%E7%B7%A8%E7%A8%8B)的语言中已经出现。是结构（Struct）和[类](https://zh.wikipedia.org/wiki/%E7%B1%BB)（Class）的前身。本身就是对具有相关性语句的归类和对某过程的抽象                                                                                    ----摘自维基百科

####  Python中的定义

> 函数是Python为了代码最大程度的复用和最小代码的冗余而提供的基本程序结构.
>
> 函数是一种设计工具,它能够让程序员将复杂的系统分解为可管理的多个部分.函数可以将相关功能打包,并参数化

#### 在Python中可以创建4种函数:

> 全局函数:定义在模块中
>
> 局部函数: 嵌套在其他函数中
>
> `lambda`函数: 表达式,匿名函数
>
> 方法: 与特定的数据类型关联的函数,并且只能与数据类型关联在一起使用,比如内置类型`len()`

#### 语法

```python
def function(paraeters):
    suite
    
# def 函数名(函数参数):
#	函数体
#	函数返回值
```

> 1.`def`是一个可执行语句,因此可以出现在任何使用语句的地方,甚至可以嵌套在其他语句中,如`if`,`while` ,`del`中.`def`创建了一个对象,并将其赋值给一个变量名(即函数名).
>
> 2.`return`用于返回结果对象,其为可选.`return`可以返回0到多个对象,也可以不写 `return`
>
> > 返回0个值,不写`return`语句,函数的返回值均为`None`
> >
> > 返回多个值,彼此之间使用`,`号隔开,返回是一个元组对象
>
> ```python
> In [3]: def foo():   #不使用return语句
>    ...:    a =  "No return"     
> #直接调用函数,不会有任何输出
> In [4]: foo()
> #打印函数,直接返回None
> In [5]: print(foo())
> None
> # return语句不返回值
> In [6]: def foo():
>    ...:     a = "return"
>    ...:     return
>    ...: 
> #直接调用函数,没有输出
> In [7]: foo()
> #打印函数,打印出None    
> In [8]: print(foo())
> None
> #多个变量return之后,会以元组的形式返回
> In [10]: def foo():
>     ...:     return 1,2,3
>     ...: 
>
> In [11]: foo()
> Out[11]: (1, 2, 3)
>
> In [12]: print(foo())
> (1, 2, 3)
>
> ```
>
> 3.`def`语句运行之后,可以通过函数名加括号的形式调用函数.
>

#### `None`

> `None`是Python的一个内建的常量,表示什么都没有,但是它不能和空字符串,空元组,空列表划等号.它只是一个空值的对象,也就是一个空的对象,只是没有赋值.
>
> ```python
> The Python None object, denoting lack of value. This object has no methods. It needs to be treated just like any other object with respect to reference counts.
> ```
>
> `None`不是0,也不是空字符串,它有自己的数据类型,这表示无法和其他数据类型使用`is`判断.在布尔值中,`None`即为`false`
>
> ```python
> In [26]: None == 0 
> Out[26]: False
>
> In [28]: None == ""
> Out[28]: False
>
> In [29]: None == []
> Out[29]: False
>
> In [30]: None == ()
> Out[30]: False
>
> In [31]: None == False 
> Out[31]: False
>
> ```
>
> `None`可以用来初始化列表,比如,新建一个包含10个元素空间,却暂时没有放入实质内容的列表.
>
> `lit1 = [None]*10`
>
> 

