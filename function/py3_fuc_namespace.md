###  函数命名空间和作用域

##### 简析

> 函数 `scope`
>
> python函数在运行的时候会创建自己的`scope ` 即作用域或者说是函数自己的`namespace`.执行函数时,如果在函数体中遇到了变量名,python会首先在该函数的`namespace`中寻找该变量.
>
> Python有一些内置函数,可以让我们来查看函数的`namespace`,下面例子,可以查看一个函数的`global`和`local`作用域.
>
> ```python
> globals()
>     Return the dictionary containing the current scope's global variables.
>     
>     NOTE: Updates to this dictionary *will* affect name lookups in the current
>     global scope and vice-versa.
>     
> locals()
>     Return a dictionary containing the current scope's local variables.
>     
>     NOTE: Whether or not updates to this dictionary will affect name lookups in
>     the local scope and vice-versa is *implementation dependent* and not
>     covered by any backwards compatibility guarantees.
>
> ```
>
> 实例
>
> ```python
> #!/usr/bin/env python
> #coding=utf-8
>
> a_string = "This is a global variable"
> def foo():
>     print("locals")
>     print(locals())
>
> print('globals')
> print(globals())
> foo()
>
> ```
>
> 运行结果
>
> ```python
> ningyanke@ningpython:~/python3_file$ python3 5.py 
> globals
> {'__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0xb706ee2c>, 'a_string': 'This is a global variable', '__package__': None, '__file__': '5.py', '__name__': '__main__', 'foo': <function foo at 0xb70fb6a4>, '__cached__': None, '__doc__': None}
> locals
> {}
>
> ```
>
> 函数的命名空间包括函数名和函数代码块,整个函数块都是他的命名空间.

##### Python LEGB规则

> 目标:
>
> - 命名空间和作用域-Python在哪里查找变量名?
> - 我们可以同时为多个对象定义/重用变量名吗?
> - Python在不同的命名空间中以哪种顺序搜索变量名
>
> 命名空间和作用域简介
>
> #####  `Namespace`
>
> `namespace`  只是将变量名映射到对象的容器.Python中的所有一切,都是对象(`literals,list,tuple.dict,functions,class`等).像这样的`name-to-object`的映射,允许我们通过分配给对象(object)的名字(name)来访问对象,比如,我们创建了一个简单的字符串`a string = "hello world"` 我们创建了一个对该`hello world`对象的引用(name),然后我们通过变量名`a_string`来访问它.
>
> 在Python中用字典来便是一个命名空间,命名空间中保存了变量(name)和对象(object)的映射关系,比如:
>
> ```python
> a_namespace = {'name_a':object1,'name_b':object2,.....}
> ```
>
> 现在,混绕的部分是 我们在Python中有多个独立命名空间,变量名可能重复出现在不同的命名空间(但是对应的对象都是唯一的).比如:
>
> ```python
> a_namespace = {'name_a':object1,'name_b':object2,.....}
> b_namespace = {'name_a':object3,'name_b':object4,.....}
> ```
>
> 比如,每次我们调用一个`for`循环,或者是定义一个函数,它都会创建自己的命名空间,命名空间会产生不同的层次机构(即`scope`),我们会在下面详细讨论.
>
> #####  `Scope`
>
> 以上,我们知道了命名空间可以彼此独立存在,并且有不同的层次结构,这就给我们带来了作用域(`scope`)的概念.
>
> 在Python中,`scope`作用域定义了在不同的层次结构中,我们应该怎么搜索 `name-to-object` 的映射.比如:
>
> ```python
> i = 1 
> def foo():
>     i = 5
>     print(i, 'in foo()')
> print(i,'global'
> foo()
> ```
>
> ```python
> 1 global
> 5 in foo()
> ```
>
> 我们定义了2次变量名`i`,其中 有一次定义在了`foo`函数内:
>
> * `foo_namespace = {'i':object_3, ...}`
> * `global_namespace = {'i':object_1, 'name_b':object_2, ...}`
>
> Python是如何寻找变量名的?,这就是我们要讨论的`LEGB`
>
> ##### 通过`LEBG` 规则解析变量名作用域(`scope`)
>
> 我们已经知道: 多个命名空间可以彼此独立的存在,并且他们可以在不同的层次上包含相同的变量名.
>
> 作用域`scope`定义了Python在层次搜索与变量名对应的对象.那么Python是以那种顺序来执行作用域的操作?
>
> 答案是`LGEB` 规则,它定义了寻找的优先级.
>
> `Local --> Enclosed --> Global  --> Built-in`
>
> ```python
> L-lcoal(function):函数内的命名空间
> E-Enclosing function locals: 外层嵌套函数的命名空间
> G-Global(module):函数定义所在模块(文件)的命名空间
> B-Buitin(Python):Python内置模块的命名空间
> ```
>
> 命名空间其实就是一个字典,在其内部保存了变量名称和对象之间的映射关系,因此,查找变量名就是在命名空间字典中查找 键-值对.
>
> **注意**
>
> 命名空间是可以进一步嵌套的,例如,如果我们导入模块,或者我们正在定义新的类,在这种情况下,我们必须使用前缀来访问这些嵌套的命名空间:
>
> ```python
> import  math
> import time
> print(math.pi,"from the math module")
> print(time.time, "from the time module")
> ```
>
> (这也是我们为什么必须小心,如果我们通过`from a_module import * ` 导入模块,它会将变量名加载到`global`命名空间中,有可能会覆盖已经存在的变量名称)
>
> ![LEGB](../picture/LEGB_1.png)
>
> ###### 1. LG-----`Local and Global scopes`
>
> eg.1
>
> ```python
> a_var = 'global varriable'
> def a_func():
>     print(a_var,'[a_var inside a_func()]')
>     
> a_func()
> print(a_var,'[a_var outside a_func()]')
> ```
>
> ```python
> global varriable', '[a_var inside a_func()]
> global varriable', '[a_var outside a_func()]
> ```
>
> 当我们调用`a_func()`,首先会看到他的本地作用域(L),变量名`a_var`并没有被定义,所以它会寻找它的上层作用域:(G)全局作用域.然后在输出结果
>
> eg.2
>
> ```python
> a_var = 'global varriable'
> def a_func():
>     a_var = 'local varriable'
>     print(a_var,'[a_var inside a_func()]')
>     
> a_func()
> print(a_var,'[a_var outside a_func()]')
> ```
>
> ```python
> local varriable', '[a_var inside a_func()]
> global varriable', '[a_var outside a_func()]
> ```
>
> 当我们调用`a_func` 函数时,它先寻找自己的本地作用域,找到了变量`a_var`,所以它的值被输出出来
>
> eg.3
>
> 如果我们使用了`global`关键字,则表明
>
> ```python
> a_var = 'global varriable'
> def a_func():
>     global a_var
>     a_var = 'local varriable'
>     print(a_var,'[a_var inside a_func()]')
>
> print(a_var,'[a_var outside a_func()]')
> a_func()
> print(a_var,'[a_var outside a_func()]')
> ```
>
> ```python
> global value [ a_var outside a_func() ]
> local value [ a_var inside a_func() ]
> local value [ a_var outside a_func() ]
> ```
>
> 当我们使用

 