## 方法是对象

> 函数可以像常规对象一样处理,类的方法也是一种对象并且可以用与其他对象大部分相同的方式来广泛的使用-可以对他们赋值,存储在数据结构中,等等.
>
> 由于类方法可以从一个实例或一个类方法,他们实际上在Python中有两种形式:
>
> 类方法对象: 不调用`self` 或者是未定义`self`
>
> * Python3 中返回一个`function`函数对象,可以通过类名调用
> * Python2 中返回一个`unbound` 无绑定对象,必须传入实例对象
>
> 实例方法对象: self +函数对
>
> * 返回的是一个绑定对象(`bound`) ,由于是一个**实例** 方法,已经打包了实例对象,所以可以像一个普通的函数一样调用

### 演示实例的绑定对象和python不同版本的类对象

> ```python
> # python2.7
> In [2]: class A:
>    ...:     def __init__(self,x):
>    ...:         self.x = x
>    ...:     def get(self):
>    ...:         return self.x
>    ...:
>
>
> In [4]: foo = A(2)
>
> In [5]: foo.get
> Out[5]: <bound method A.get of <__main__.A instance at 0xb69c620c>>
>
> In [6]: A.get
> Out[6]: <unbound method A.get>
> ```
>
> ```python
> # python3.5
> In [3]: class A:
>    ...:     def __init__(self,x):
>    ...:         self.x = x
>    ...:     def get(self):
>    ...:         return self.x
>    ...:
>
> In [4]: foo = A(2)
>
> In [5]: foo.get
> Out[5]: <bound method A.get of <__main__.A object at 0x7f4db8264048>>
>
> In [6]: A.get
> Out[6]: <function __main__.A.get>
> ```

### Python 3中,无绑定方法是函数

> 在Python 3 中,无绑定方法已经变成了一个普通的函数,对于大多数用途来说,没有什么影响,
>
> 但是,Python3 已经对类中的单一的方法做出了改进
>
> ```python
> # python2.7
> In [2]: class Selfless:
>    ...:     def __init__(self, data):
>    ...:         self.data = data
>    ...:     def selfless(arg1,arg2):
>    ...:         return arg1 + arg2
>    ...:     def nomal(self, arg1, arg2):
>    ...:         return self.data + arg1 + arg2
>    ...:
>
> In [3]: foo = Selfless(2)
>
> In [4]: foo.nomal(3,4)
> Out[4]: 9
>
> # 实例来调用 类的方法,无绑定
> In [5]: foo.selfless(3,4)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-5-ab90f5d20494> in <module>()
> ----> 1 foo.selfless(3,4)
>
> TypeError: selfless() takes exactly 2 arguments (3 given)
>
> # 用类来调用类的方法, 无self ,无绑定
> In [6]: Selfless.selfless(3,4)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-6-78c80d148b5b> in <module>()
> ----> 1 Selfless.selfless(3,4)
>
> TypeError: unbound method selfless() must be called with Selfless instance as first argument (got int instance instead)
> ```
>
> 对比Python3
>
> ```python
> In [8]: class Selfless:
>    ...:     def __init__(self, data):
>    ...:         self.data = data
>    ...:     def selfless(arg1, arg2):
>    ...:         return arg1 + arg2
>    ...:
>
> In [9]: class Selfless:
>    ...:     def __init__(self, data):
>    ...:         self.data = data
>    ...:     def selfless(arg1, arg2):
>    ...:         return arg1 + arg2
>    ...:     def momal(self, arg1 , arg2):
>    ...:         return self.data + arg1 + arg2
>    ...:
>
> In [10]: foo = Selfless(2)
>
> In [11]: foo.momal(3,4)
> Out[11]: 9
>
> # 通过实例调用 无self ,提示错误,不能调用
> In [12]: foo.selfless(3,4)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-12-cab877fce8f9> in <module>()
> ----> 1 foo.selfless(3,4)
>
> TypeError: selfless() takes 2 positional arguments but 3 were given
>
>  # 通过类方法调用 无self,支持调用
> In [13]: Selfless.selfless(3,4)
> Out[13]: 7
> ```
>
> 通过对比,就可以发现 **在Python3中对 方法是函数,能够更灵活的使用** ,这这里,无`self` 参数的对象类似于函数的**静态方法** ,但是他是一个普通函数,在继承和函数实例是不能调用的.
>
> 这两个版本最大的区别是:
>
> * 在python2 中,从一个类获取一个方法会产生一个未绑定对象,没有手动传递一个实例就不会调用它
> * 在python3中,从一个类获取一个方法会产生一个简单函数,没有给输实例可以常规的调用
>
> ```python
> ## python2 ##
> In [10]: class A:
>     ...:     def foo(self,x):
>     ...:         return x
>     ...:
>
> In [11]: a = A.foo
>
> In [12]: a(1,2)
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-12-22416e0568fd> in <module>()
> ----> 1 a(1,2)
>
> TypeError: unbound method foo() must be called with A instance as first argument (got int instance instead)
>
> ## python3 ##
> In [16]: class A:
>     ...:     def foo(self,x):
>     ...:         return  x
>     ...:
>
> In [19]: a = A.foo
>
>
> In [22]: a(2,3)
> Out[22]: 3
> ```
>
> 在这里 self 已经变成一个普通的位置参数.
>
> **注意到这一点是非常重要的,因为绑定方法通常会更重要,因为,他们在一个单一对象中把实例和函数配对起来,所以绑定函数通常可以当做可调用对象调用(类似于一个函数)**

### 绑定方法和其他可调用对象

> 绑定方法(对实例而言)可以向一个通用对象一样处理,就像一个简单函数一样,他们可以任意在一个程序中传递.由于绑定方法在单个的包中,组合了函数和实例,因此他们可以像任何其他可调用对象一样对待,并且在调用的时候不需要特殊的语法: 
>
> 像常规对象一样操作 绑定方法对象
>
> ```python
> In [24]: class Number:
>     ...:     def __init__(self, base):
>     ...:         self.base = base
>     ...:     def double(self):
>     ...:         return self.base * 2
>     ...:     def triple(self):
>     ...:         return self.base * 3
>     ...:
>
> In [30]: x , y , z  = Number(2), Number(3),Number(4)
>
> In [31]: x.double
> Out[31]: <bound method Number.double of <__main__.Number object at 0x7f4db828fc18>>
>
> In [32]: x.double()
> Out[32]: 4
>
> In [33]: for i in [x.double,y.double,z.double]:
>     ...:     print(i(), end=" ")
>     ...:
> 4 6 8
> ```
>
> 和普通函数一样,绑定方法对象拥有自己的内省信息
>
> ```python
> In [34]: func_1 = x.double
>
> In [35]: type(func_1)
> Out[35]: method
>
> In [36]: dir(func_1)
> Out[36]:
> ['__call__',
>  '__class__',
>  '__delattr__',
>  '__dir__',
>  '__doc__',
>  '__eq__',
>  '__format__',
>  '__func__',
>  '__ge__',
>  '__get__',
>  '__getattribute__',
>  '__gt__',
>  '__hash__',
>  '__init__',
>  '__le__',
>  '__lt__',
>  '__ne__',
>  '__new__',
>  '__reduce__',
>  '__reduce_ex__',
>  '__repr__',
>  '__self__',
>  '__setattr__',
>  '__sizeof__',
>  '__str__',
>  '__subclasshook__']
> ```