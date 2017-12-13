## Python 描述器引导

### Python魔法方法-描述器(discriptor)　

####  1.官方文档
>
> [官方文档](https://docs.python.org/3/howto/descriptor.html#functions-and-methods)
>

#### 2. 描述器定义

> 一般来说，一个描述器是一个有 “绑定行为”(binding behavior) 的对象属性(object attribute),它的访问控制被**描述器协议**方法重写，这些方法是 `__get__()`, `__set__()`, `__del__()`。有这些方法的对象就叫做描述器.
>
> ```markdown
> In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol: __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.
> ```
>
> 描述器是强大的，应用广泛的。描述器正是**属性, 实例方法, 静态方法, 类方法和 `super `**的背后的实现机制。描述器在Python自身中广泛使用，以实现Python 2.2中引入的新式类。描述器简化了底层的C代码，并为Python的日常编程提供了一套灵活的新工具。
>
> **描述器协议**
>
> ```python
> The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ __dict__.
>
> object.__get__(self, instance, owner)
> Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). owner is always the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner. This method should return the (computed) attribute value or raise an AttributeError exception.
>
> object.__set__(self, instance, value)
> Called to set the attribute on an instance instance of the owner class to a new value, value.
>
> object.__delete__(self, instance)
> Called to delete the attribute on an instance instance of the owner class.
>
> object.__set_name__(self, owner, name)
> Called at the time the owning class owner is created. The descriptor has been assigned to name.
> New in version 3.6.
> ```
>
> 可以看出,这个方法仅仅适用于**包含描述器方法的类**的 **实例**,描述器出现在`owner class`(the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents)中,出现在`owner class` 的`__dict__` 中,或者是实例所属类的父类之一的`__dict__` 中.
>
> `the  attribute` 指的是`owner class` 中的`__dict__` 中的`key` ,所以协议只有4条:实现任意一条,都是描述器(discriptor),最后一条是新出现在python3.6 中.
>
> ```python
> object.__get__(self, instance, owner)
> object.__set__(self, instance, value)
> object.__delete__(self, instance)
> ```
>
> ```python
> self --->self refers to descriptor itself.(self 指向了描述器自身)
> instence --> 实例有2种情况, 当通过实例调用时,指向了实例本身,如果用类来调用,指向了 None
> owner ----> 即包含 描述器的类
> # 结合下面实例理解
> ```
>
> ```python
> # 描述器
> class Description1:
>     def __get__(self, instance, owner):
>         print("get self: %s ,get instance:%s ,get owner: %s" % (self,instance,owner))
>     def __set__(self, instance, value):
>
>         print("set self: %s ,set instance:%s ,set value: %s" % (self,instance,value))
>
>     def __del__(self):
>         print("delete self %s" % self)
> # 包含描述器的类 
> class Foo1:
>     x = Description1()
>     def __init__(self,x):
>         self.x = x
>         
> if __name__ == '__main__':
>     # 实例化
>     foo1 = Foo1(10)
>     # instance
>     # 打印实例访问描述器
>     print(foo1.x)
>     # instance
>     # 打印类访问描述器
>     print(Foo1.x)
>     # self
>     # 描述器中的self
>     print(Foo1.__dict__)
> ```
>
> 打印结果
>
> ```python
> # 注意观察 instance--> 来自实例
> set self: <__main__.Description1 object at 0x7f0b221e56d8> ,set instance:<__main__.Foo1 object at 0x7f0b221e5780> ,set value: 10
> # 注意观察 instance--> 来自实例         
> get self: <__main__.Description1 object at 0x7f0b221e56d8> ,get instance:<__main__.Foo1 object at 0x7f0b221e5780> ,get owner: <class '__main__.Foo1'>
> # 注意观察 instence--> 来自类 class
> get self: <__main__.Description1 object at 0x7f0b221e56d8> ,get instance:None ,get owner: <class '__main__.Foo1'>
> # 注意观察 'x' 对应的值,就是上面的 self的对应值
> {'__doc__': None, '__weakref__': <attribute '__weakref__' of 'Foo1' objects>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo1' objects>, '__init__': <function Foo1.__init__ at 0x7f0b221d2d08>, 'x': <__main__.Description1 object at 0x7f0b221e56d8>}
> # 程序运行结束后自行销毁 descriptor 
> delete self <__main__.Description1 object at 0x7f0b221e56d8>
> ```

#### 3.描述器可以用来做什么

> [stackoverflow](https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors)这里做了很多详细的说明,简单的来说,基于描述符的`@classmethod` `@staticmethod` ,`property` 等等,它还可以用来节约内存`__slots` ,或者做数据库的`orm` 等等.

#### 4.默认访问顺序

> 默认对属性的访问控制是从对象的字典属性中(`__dict__`)中获取(`get`)，设置(`set`)，删除(`delete`)它.
>
> ```python
> In [248]: class A(object):
>      ...:     name = 'Jerry'
>      ...:     
> #查看`__dict__`中保存的内容
> In [249]: A.__dict__
> Out[249]: 
> dict_proxy({'__dict__': <attribute '__dict__' of 'A' objects>,
>             '__doc__': None,
>             '__module__': '__main__',
>             '__weakref__': <attribute '__weakref__' of 'A' objects>,
>             'name': 'Jerry'})
> #`get`
> In [250]: A.name
> Out[250]: 'Jerry'
> #`set`
> In [251]: A.age = 40
> #查看`__dict__`中保存的内容
> In [253]: A.__dict__
> Out[253]: 
> dict_proxy({'__dict__': <attribute '__dict__' of 'A' objects>,
>             '__doc__': None,
>             '__module__': '__main__',
>             '__weakref__': <attribute '__weakref__' of 'A' objects>,
>             'age': 40,
>             'name': 'Jerry'})
> #`delete`
> In [254]: del A.name
> #查看`__dict__`中保存的内容
> In [255]: A.__dict__
> Out[255]: 
> dict_proxy({'__dict__': <attribute '__dict__' of 'A' objects>,
>             '__doc__': None,
>             '__module__': '__main__',
>             '__weakref__': <attribute '__weakref__' of 'A' objects>,
>             'age': 40})
> ```
>
> 而实例，`a.x`的查找顺序是，`a.__dict__['x']`,然后`type(a).__dict__['x']`,最后找`type(a)`的父类(不包含`metaclass`元类)。**如果查找到的值是一个描述器，Python就会调用描述器的方法来重写默认的控制行为。这个重写发生在这个查找环节的哪里取决于那个描述器方法。注意, 只有在新式类中时描述器才会起作用。(新式类是继承自 type 或者 object 的类)**
>
> ```python
> In [256]: a = A()
> >>
> In [257]: a.__dict__
> Out[257]: {}
> >>
> In [258]: type(a).__dict__
> Out[258]: 
> dict_proxy({'__dict__': <attribute '__dict__' of 'A' objects>,
>             '__doc__': None,
>             '__module__': '__main__',
>             '__weakref__': <attribute '__weakref__' of 'A' objects>,
>             'age': 40})
> ```

#### 5.描述器访问顺序

> 描述器协议
>
> ```python
> object.__get__(self, instance, owner)
> object.__set__(self, instance, value)
> object.__delete__(self, instance)
> ```
>
> 任意对象具有其中**任一个方法**，就会成为描述器。从而被当做**对象属性**时重写默认的查找行为。
>
> * 如果一个对象同时定义了`__get__()`,`__set__()`，它就叫做`data descriptor`
> * 仅仅定义了`__get__()`的描述器就叫做`non-data descriptor`.
>
> `data descriptor`和`non-data descriptor`的区别在于:相对于实例字典的优先级。如果实例有和描述器同名的属性。
>
> * 如果描述器是`data descriptor`。优先使用`data descriptor`的定义.
> * 如果描述器是`non-data descriptor`.优先使用`__dict__`中的属性.
>
> ```python
> class Description1:
>     def __get__(self, instance, owner):
>         print("get self: %s ,get instance:%s ,get owner: %s" % (self,instance,owner))
>     def __set__(self, instance, value):
>
>         print("set self: %s ,set instance:%s ,set value: %s" % (self,instance,value))
>
>     def __del__(self):
>         print("delete self %s" % self)
>
> class Description2:
>     def __get__(self, instance, owner):
>         print("get self: %s ,get instance:%s ,get owner: %s" % (self,instance,owner))
>
>
>
>
> class Foo1:
>     x = Description1()
>     def __init__(self,x):
>         self.x = x
>
> class Foo2:
>     x = Description2
>     def __int__(self,x):
>         self.x = x
>
> if __name__ == '__main__':
>     foo1 = Foo1(10)
>     print(foo1.x )
>     print(Foo1.x)
>     print(Foo1.__dict__)
>     foo2 = Foo2()
>     print(foo2.x)
>     print(Foo2.x)
>     print(Foo2.__dict__)
> ```
>
> ```python
> set self: <__main__.Description1 object at 0x7f11465c27f0> ,set instance:<__main__.Foo1 object at 0x7f11465c28d0> ,set value: 10
> get self: <__main__.Description1 object at 0x7f11465c27f0> ,get instance:<__main__.Foo1 object at 0x7f11465c28d0> ,get owner: <class '__main__.Foo1'>
> None
> get self: <__main__.Description1 object at 0x7f11465c27f0> ,get instance:None ,get owner: <class '__main__.Foo1'>
> None
> {'__weakref__': <attribute '__weakref__' of 'Foo1' objects>, 'x': <__main__.Description1 object at 0x7f11465c27f0>, '__dict__': <attribute '__dict__' of 'Foo1' objects>, '__doc__': None, '__module__': '__main__', '__init__': <function Foo1.__init__ at 0x7f11465afe18>}
> <class '__main__.Description2'>
> <class '__main__.Description2'>
> {'__weakref__': <attribute '__weakref__' of 'Foo2' objects>, 'x': <class '__main__.Description2'>, '__dict__': <attribute '__dict__' of 'Foo2' objects>, '__doc__': None, '__int__': <function Foo2.__int__ at 0x7f11465afea0>, '__module__': '__main__'}
> delete self <__main__.Description1 object at 0x7f11465c27f0>
> ```

#### 6.描述器的调用

> 描述器可以直接调用： `d.__get__(obj)`,**更常见的是描述器在属性访问时会被自动调用**.
>
> 以下: `d` 为`obj`属性 ,`d` 同时也是`descriptor` 的实例.
>
> 举例来说， `obj.d `会在 obj 的`__dict__`中找 d ,如果 d 定义了 `__get__ `方法，那么 `d.__get__(obj) `会依据下面的优先规则被调用。调用的细节取决于 obj 是一个类还是一个实例.
>
> + 对于实例对象，方法`object.__getattribute__()`把`b.x`变成`type(b).__dict__['x'].__get__(b,type(b))`.具体实现是依据这样的优先顺序:`data descriptor` > `b.__dict__` > `non-data discription` > `__getattr__()`.
> + 对于类来讲。方法 `type.__getattribute__()`把`B.x`变成`B.__dict__['x'].__get__(None,B)`.
>
> 用Python来描述就是:
>
> ```python
> def __getattribute__(self,key):
> 	v = object.__getattribute__(self,key)
>     if hasattr(v,'__get__'):
>     	return v.__get__(None,self)
>     return v
> ```
>
> 注释:`object.__getattribute__` 相当于`__dict__` 见[这里](./class_intercept.md)
>
> ]其中有重要的几点
>
> - **描述器的调用是因为`__getattribute__()`**
>
> - **重写`__getattribute__()`方法会阻止正常的描述器调用**
>
> - **`__getattribute__()`只对新式类的实例可以用**
>
> - **`object.__getattribute__() `和 `type.__getattribute__()` 对` __get__() `的调用不一样**
>
> - **`data descriptor`总是比实例字典优先。**
>
> - **`non-data descriptor`不如实例字典优先)**
>

#### 7.不改写 `__getattribute__`查找顺序
>
> ```python
> #-------------如果重载了__getattribute__() ,则调用 __getattribute__()----------------
> #
> #
> #1. 定义 descriptor
> >>> class Descriptor(object):
> ...     name = 'Jerry'
> ...     def __get__(self,instence,owner):
> ...         return 'self:%s,instence:%s,owner:%s' % (self,instence,owner)
> ...     def __set__(self,instence,value):
> ...         return 'value:%s' % value
> ...
> #
> #
> #2. 引用 descriptor
> >>> class Foo(object):
> ...     x = Descriptor()
> ...     def __init__(self,x):
> ...         self.x = x 
> ... 
> >>> d = Descriptor()descriptor
> #
> #
> #3. 描述器可以直接调用 __get__ 
> # instence: 实例对象本身
> # owner： typer(instence)
> #
> #
> >>> d.__get__(d,Descriptor)
> "self:<__main__.Descriptor object at 0xb705442c>,instence:<__main__.Descriptor object at 0xb705442c>,owner:<class '__main__.Descriptor'>"
> >>> foo = Foo(10)
> #
> #
> #4. 更常用的当做属性来调用
> >>> foo.x
> "self:<__main__.Descriptor object at 0xb705430c>,instence:<__main__.Foo object at 0xb705448c>,owner:<class '__main__.Foo'>"
> #
> #
> #5. 当做属性调用时
> #
> #5.1 如果是实例对象
> # object.__getattribute__()   这个属性会把 foo.x 转化为 type(foo).__dict__['x'].__get__(foo,type(foo))
> # 查找顺序是： type.x 引起了一个 data descriptor，优先级最高，直接返回 data descriptor 的 __get__ 定义
> >>> type(foo)
> <class '__main__.Foo'>
> >>> type(foo).__dict__
> dict_proxy({'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Foo' objects>, 'x': <__main__.
> tor object at 0xb705430c>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None, '__init__': <function __init__ at 0xb7473bc4>})
> >>> type(foo).__dict__['x'].__get__(foo,type(foo))
> "self:<__main__.Descriptor object at 0xb705430c>,instence:<__main__.Foo object at 0xb705448c>,owner:<class '__main__.Foo'>"
> #
> #
> #5.2 如果是类对象
> # type 的 type.__getattribute__() 会把 Foo.x  直接转换  Foo.__dict__['x'].__get__(None,Foo)
> # __get__()  中的 instence 为None，没有。owner 为类本身
> >>> Foo.__dict__['x'].__get__(None,Foo)
> "self:<__main__.Descriptor object at 0xb705430c>,instence:None,owner:<class '__main__.Foo'>"
> ```
>

#### 8.深度理解调用顺序-举例说明(讨论描述器存在的情况)
>##### 1. 重写`__getattribute__()`,返回重写的值
>
>##### 2. 类属性 > 数据描述器
>
>修改类属性,会覆盖数据描述器属性
>
>```python
>class Descriptor:
>
>    def __get__(self, instance, owner):
>        print("get self,", self, "instance:", instance, 'owner:', owner)
>
>    def __set__(self, instance, value):
>        print("set self:", self, "instance:", instance, "value:", value)
>
>    def __del__(self):
>        print("del self:", self)
>
>class Foo:
>    x = Descriptor()
>
>if __name__ == '__main__':
>    foo = Foo()
>    print("Foo的__dict__:",Foo.__dict__)
>    print("foo.__dict__",foo.__dict__)
>    print("实例修改x对应的属性值")
>    foo.x = 4
>    print("Foo.__dict__:",Foo.__dict__)
>    print("foo.__dict__:",foo.__dict__)
>    print("修改类属性的值")
>    Foo.x = 3
>    print("Foo.__dict__:",Foo.__dict__)
>    print("foo.__dict__:",foo.__dict__)
>    print("实例 __dict__ 中没有值,它会优先查找到 descriptor ,修改了类属性值后,类 __dict__ 覆盖了描述器")
>```
>
>输出结果:
>
>```python
>Foo的__dict__: {'__doc__': None, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__dict__': <attribute '__dict__' of 'Foo' objects>, 'x': <__main__.Descriptor object at 0x7f69e86951d0>, '__module__': '__main__'}
>foo.__dict__ {}
>实例修改x对应的属性值
>set self: <__main__.Descriptor object at 0x7f69e86951d0> instance: <__main__.Foo object at 0x7f69e8695710> value: 4
>Foo.__dict__: {'__doc__': None, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__dict__': <attribute '__dict__' of 'Foo' objects>, 'x': <__main__.Descriptor object at 0x7f69e86951d0>, '__module__': '__main__'}
>foo.__dict__: {}
>修改类属性的值
>del self: <__main__.Descriptor object at 0x7f69e86951d0>
>Foo.__dict__: {'__doc__': None, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__dict__': <attribute '__dict__' of 'Foo' objects>, 'x': 3, '__module__': '__main__'}
>foo.__dict__: {}
>实例 __dict__ 中没有值,它会优先查找到 descriptor ,修改了类属性值后,类 __dict__ 覆盖了描述器
>```
>
>可以看到修改类属性对应的`descriptor` 时,会先调用`__del__(self) ` ,描述器的属性值被覆盖
>
>##### 3.数据描述器 >  实例属性
>
>有数据描述器时,实例的`__dict__` 为空,值被传入到了数据描述器.
>
>```python
># 描述器,描述符str
>class Str:
>    def __get__(self, instance, owner):
>        print("Str get")
>
>    def __set__(self, instance, value):
>        print("str set")
>
>    def __del__(self):
>        print("str del")
>
>    def __delete__(self, instance):
>        print("str delete")
>
>
>class People:
>    name = Str()
>
>    def __init__(self, name, age):
>        self.name = name
>        self.age = age
># 如果描述符是一个数据描述符(即有__get__又有__set__),那么p1.name的调用与赋值都是触发描述符的操作,于p1本身无关了,相当于覆盖了实例的属性
>
>if __name__ == '__main__':
>    print("实例化 p1")
>    p1 = People('Egon', 19)
>    print("更改实例 p1 的 descriptor 属性值")
>    p1.name = 'Jack'
>    print("查看 实例的 __dict__ 中对应的 descriptor")
>    print("p1.name:",p1.name)
>
>    print("P1.__dict__:", p1.__dict__)
>	# 实例的属性字典中没有name,因为name是一个数据描述符,优先级高于实例属性,查看/赋值/删除都与描述符有关,与实例无关了
>    del p1.name
>```
>
>输出结果
>
>```python
>实例化 p1
>str set
>更改实例 p1 的 descriptor 属性值
>str set
>查看 实例的 __dict__ 中对应的 descriptor
>Str get
>p1.name: None
>P1.__dict__: {'age': 19}
>str delete
>str del
>```
>
>##### 4.实例属性 > 非数据描述器
>
>当描述器是一个`non data discriptor` 会优先查看实例 `__dict__ ` 中的值
>
>```python
># 函数是一个非数据描述器对象
># 字符串,也是如此
>class Foo(object):
>    def func(self):
>        print("我是一个非数据描述器对象")
>foo = Foo()
>print(foo.__dict__)
>print(hasattr(Foo.func,"__get__"))
>print(hasattr(Foo.func,"__del__"))
>print(hasattr(Foo.func,"__set__"))
>foo.func = 3
>print(foo.__dict__)
># 输出
># D:\Python\python.exe E:/工程/Python/jatrix.py
># {}
># True
># False
># False
># {'func': 3}
>```

#### 9.属性(properties)

> [官网](https://docs.python.org/3/library/functions.html#property)
>
> 调用 `property()` 是建立`data discriptor`的一种简洁方式，从而可以在**访问属性**时接触相应的方法调用。即返回`Return a property attribute.` 它可以让你把`class method` 像`class attribute` 一样调用.` If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.` 
>
> 函数原型:
>
> ```python
> property(fget=None, fset=None, fdel=None, doc=None) ->property attribute
> ```
>
> 下面展示了一个典型应用；定义一个托管属性(Managed Attribute) `x `:
>
> ```python
> class C:
>     def getx(self):
>         return self._x
>
>     def setx(self, value):
>         self._x = value
>
>     def delx(self):
>         del self._x
>
>     x = property(getx, setx, delx, 'I am the "x" property.')
> # If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
> c = C()
> # 如果给定 doc ,它是 property 属性的文档字符串
> C.x.__doc__
> c.x = 7  # 调用 setx
> print(c.x )  # 调用 getx
> print(c.__dict__) 
> print(C.__dict__)
> del c.x  # 调用 delx
> ```
>
> 它可以让你把`class method` 像`class attribute` 一样调用.
>
> 以下是一个纯python的`property`的等价实现:
>
> ```python
> """
> property 使用纯python代码实现
> property 是描述器的简洁实现方式
> property 实现把函数方法当做属性调用
> """
>
>
> class Property:
> 	"Emulate PyProperty_Type() in Object/decrobject.c"
>
> 	def __init__(self, fget=None, fset=None, fdel=None, doc=None):
> 		self.fget = fget
> 		self.fset = fset
> 		self.fdel = fdel 
> 		self.__doc__ = doc 
>
> 	#obj-->instence , objtype-->owner
> 	def __get__(self,obj,objtype=None):
> 		if obj is None:
> 			return self
> 		if self.fget is None:
> 			raise AttributeError,'unreadable attribute'
> 		return self.fget(obj)
>
> 	def __set__(self,obj,value):
> 		if self.fset is None:
> 			raise AttributeError,'can not set attribute'
> 		self.fset(obj,value)
>
> 	def __delete__(self,obj):
> 		if self.fdel is None:
> 			raise AttributeError,'can not delete attribute'
> 		self.fdel(obj)
>
> 	def getter(self,fget):
> 		return type(self)(fget,self.fset,self.fdel,self.__doc__)
>
> 	def setter(self,fset):
> 		return type(self)(self.fget,fset,self.fdel,self.__doc__)
>
> 	def delete(self,fdel):
> 		return type(self)(self.fget,self.fset,fdel,self.__doc__)
> ```
>
> 通过下面实例理解
>
> ```python
> # 定义使用property描述器
> In [1]: class B:
>    ...:     def __init__(self,name):
>    ...:         self.name = name
>    ...:     def add(self):
>    ...:         return 'hello %s' % self.name
>    ...:     addtest = property(add)
>    ...:     
>
> # 实例化
> In [3]: b = B('Jack')
> # addtest 对应的就是 描述器 property 对象
> In [4]: B.__dict__
> Out[4]: 
> mappingproxy({'__dict__': <attribute '__dict__' of 'B' objects>,
>               '__doc__': None,
>               '__init__': <function __main__.B.__init__>,
>               '__module__': '__main__',
>               '__weakref__': <attribute '__weakref__' of 'B' objects>,
>               'add': <function __main__.B.add>,
>               'addtest': <property at 0x7f66008d9d68>})
> # 像属性一样调用方法
>
> In [5]: b.addtest
> Out[5]: 'hello Jack'
> # 理解:
> # If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
> # b 是实例, property 是一个 data descriptor, 所以被 obj.__attribute__() 方法转变为
> In [6]: type(b).__dict__['addtest'].__get__(b,type(b))
> Out[6]: 'hello Jack
> ```

#### 10.`@property`

> 上面的写法是`property` 写一个属性的标准写法.
>
> ```python
> property(fget=None, fset=None, fdel=None, doc=None) ->property attribute
> ```
>
> 但是Python也能使用`decorator`  装饰器来简化,这就是 `@` 语法糖
>
> `property` 的实现是基于`getter` ,`setter`, `delete`   ,返回的结果(参照上面等价实现)
>
> ```python
> @property
> def x(self)
> # 等价于
> x = property(x) # 填入setter等的值
> ```
>
> 属性有三个装饰器: `setter` ,`getter` ,`deleter`,都是`property()`的基础上做了一些封装。因为`setter`和`deleter`是`property()`的第二和第三个参数，不能直接套用@语法。
>
> + 1.只有`@property`表示**只读**
> + 2.同时有`@property`和@`x.setter`表示**可读可写**
> + 3.同时有`@property`和@`x.sette`r和`x.delter`便是**可读可写可删除**
>
>
> ```python
> #!/usr/bin/env python
> #coding=utf-8
> #定义一个装饰器
> class Student(object):
>     def __init__(self,id):
>         self._id = id 
>         
>     @property #只读
>     def score(self):
>         return self._score
>         
>     @score.setter #可写
>     def score(self,value):
>         self._score = value
>         
>     @property #只读
>     def get_id(self):
>         return self._id
> if __name__ == '__main__':
>     #实例化
>     s = Student('111')
>     #写属性
>     s.score = 20
>     #只读属性
>     print(s.score)
>     #读属性
>     print(s.get_id)
>     #不能写入，保护了属性
>     s.get_id = 5
> #------------------------------
> #执行结果
> #20
> #111
> #Traceback (most recent call last):
> # File "2.py", line 28, in <module>
> #    s.get_id = 5
> #AttributeError: can't set attribute
> ```

#### 11.`property` 和`@property` 比较

> ```python
> class A(object):#新式类（继承自object类）  
>     def __init__(self):  
>         self.__name=None  
>     def getName(self):  
>         return self.__name  
>     def setName(self,value):  
>         self.__name=value  
>     def delName(self):  
>         del self.__name  
>     name=property(getName,setName,delName)  
>   
> a=A()  
> print a.name #读  
> a.name='python' #写  
> print a.name #读  
> del a.name #删除  
> #print a.name #a.name已经被删除 AttributeError: 'A' object has no attribute '_A__name'
> #------------------------------------------------------------------
> class A(object):#要求继承object  
>     def __init__(self):  
>         self.__name=None  
>
>     #下面开始定义属性，3个函数的名字要一样！  
>     @property #读  
>     def name(self):  
>         return self.__name  
>     @name.setter #写  
>     def name(self,value):  
>         self.__name=value  
>     @name.deleter #删除  
>     def name(self):  
>         del self.__name  
>
> a=A()  
> print a.name #读  
> a.name='python'  #写  
> print a.name #读  
> del a.name #删除  
> #print a.name # a.name已经被删除 AttributeError: 'A' object has no attribute '_A__name
> ```

#### 12. 函数和方法

> Python的面向对象特征是建立在基于函数的环境之中。`non-data discriptor`把两者连接起来。
>
> 类的字典把方法当做函数存储。在定义类的时候，方法通过使用关键字`def`和`lambda`来声明。这和创建函数是一样的。唯一的不同之处是类方法的第一个参数是来表示对象实例。python约定，参数通常为`self`
>
> 为了支持函数作为方法在类中调用，函数提供一个`__get__()` 方法以便在属性访问时绑定方法，也就是说**所有函数都是`non data discriptor`**.当他们从一个对象中被调用时他们返回绑定(bound)的方法.
>
> 所有函数都是`non data discriptor` 的原理:
>
> ```python
> class Function(object):
>     . . .
>     def __get__(self, obj, objtype=None):
>         "Simulate func_descr_get() in Objects/funcobject.c"
>         if obj is None:
>             return self
>         return types.MethodType(self, obj)
> ```
>
> 验证:
>
> ```python
> In [7]: def A():
>    ...:     pass
>    ...: 
>
> In [8]: A.__dict__
> Out[8]: {}
>
> In [10]: hasattr(A,'__get__')
> Out[10]: True
>
> In [21]: A.__get__
> Out[21]: <method-wrapper '__get__' of function object at 0x7f6600838bf8>
> # object的一个装饰器方法
>
> In [22]: A.__qualname__  # 自我检查
> Out[22]: 'A'
> ```
>
> 函数descriptor工作流程
>
> ```python
> class D(object):
>     def f(self, x):
>         return x
>
> d = D()
>
> # 通过类字典访问,不会调用 __get__,
> # 只是返回底层的函数对象
> # 类字典的优先级别高
> >>> D.__dict__['f']
> >>> <function __main__.D.f>
>
> # 来自类的点 .  的调用时,会调用 __get__, 但是返回的是底层函数对象
> # 来自 D.__getattribute__ 的转变,等价于
> # D.__dict__['f'].__get__(None,D)
> >>> D.f
> >>> <function __main__.D.f>
>
> # 函数的 __qualname__ 支持自我检查
> # 参看上面的 A.__qualname__
> >>> D.f.__qualname__
> >>> 'D.f'
>
> # 来自实例的访问方法时,调用 __get__()，在绑定方法对象中返回 function wrapper
> # 来自 __getattribute__ 的转变,它等价于
> # type(b).__dict__['f'].__get__(b,type(b))
> >>> d.f
> >>> <bound method D.f of <__main__.D object at 0x7f66007777f0>>
>
> # 在内部，绑定方法存储底层函数
> >>> d.f.__func__
> >>> <function __main__.D.f>
> # 绑定实例
> >>> d.f.__self__
> >>> <__main__.D at 0x7f66007777f0>
> # 绑定实例的类
> >>> d.f.__class__
> >>> method
>
> # 等价实现
> >>> type(d).__dict__['f'].__get__(d,type(d)).__func__
> >>> <function __main__.D.f>
>
> >>> type(d).__dict__['f'].__get__(d,type(d)).__self__
> >>> <__main__.D at 0x7f6600730128>
>
> >>>  type(d).__dict__['f'].__get__(d,type(d)).__class__
> >>> method
> ```
>
> 参考
>
> ```python
> >>> class D(object):
> ...     def f(self, x):
> ...         return x
> ...
> >>> d = D()
>
> # Access through the class dictionary does not invoke __get__.
> # It just returns the underlying function object.
> >>> D.__dict__['f']
> <function D.f at 0x00C45070>
>
> # Dotted access from a class calls __get__() which just returns
> # the underlying function unchanged.
> >>> D.f
> <function D.f at 0x00C45070>
>
> # The function has a __qualname__ attribute to support introspection
> >>> D.f.__qualname__
> 'D.f'
>
> # Dotted access from an instance calls __get__() which returns the
> # function wrapped in a bound method object
> >>> d.f
> <bound method D.f of <__main__.D object at 0x00B18C90>>
>
> # Internally, the bound method stores the underlying function,
> # the bound instance, and the class of the bound instance.
> >>> d.f.__func__
> <function D.f at 0x1012e5ae8>
> >>> d.f.__self__
> <__main__.D object at 0x1012e1f98>
> >>> d.f.__class__
> <class 'method'>
> ```
>
> 这样看来,函数确实是一个非数据描述器,在来看一下`class attribute` 的实现
>
> ```python
> # 一个普通的函数
> >>> def foo():
> ...     print("foo")
> ... 
> # 类A
> >>> class A:
> ...     def bar(self):
> ...             print("bar")
> ... 
> # 实例化
> >>> a = A()
> # 普通的函数和 被绑定的函数
> >>> foo
> <function foo at 0x7f8a3d287f28>
> >>> a.bar
> <bound method A.bar of <__main__.A object at 0x7f8a3d29f208>>
> # 新定义一个含有 self 的函数
> >>> def fooFighters(self):
> ...     print("fooFighters")
> ... 
> # 函数都是 non-data descriptor
> # A.fooFighters 是类的属性
> # A.fooFighters = fooFighters.__get__(A)
> # 参看上面的函数描述器原理
> # 返回 
> #  >>> types.MethodType(test,A)
> #  <bound method test of <class '__main__.A'>>
> >>> A.fooFighters = fooFighters
> >>> a2  = A()
> >>> a2.fooFighters
> <bound method fooFighters of <__main__.A object at 0x7f8a3d29f4a8>>
> >>> a2.fooFighters()
> fooFighters
> ```
>
> 把一个函数传递给了类,而且函数自身是通过`self` 传递,
>
> [参考阅读](https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance/2982#2982) 

#### 13.静态方法和类方法

> 通过上面我们可以知道,我们可以把一个 函数 绑定到 类中,作为 类的 方法存在,但是他们的最主要的区别在于,你必须手动传入一个 `self` 参数.
>
> `non-date descriptor` 将函数绑定成方法这种常见模式提供了一个简单的实现机制。
>
> 所有的函数都有方法`__get__()`,当函数被当做属性访问时，它就会把函数变成一个方法.`non-data descriptor` 将`obj.f(*args)` 转化为`f(obj,*args)`(实例),将`klass.f(*args)` 转化为`f(*args)`(类)
>
> 这是一个转变的表格:
>
> | Transformation | Called from an Object | Called from a Class |
> | -------------- | --------------------- | ------------------- |
> | function       | f(obj,*args)          | f(*args)            |
> | staticmethod   | f(*args)              | f(*args)            |
> | classmethod    | f(type(obj),*args)    | f(klass,*args)      |
>
> `classmethod` 原样返回函数，不管是从一个对象还是一个类，这个函数都会同样访问到。那些不需要` self` 变量的方法适合用做静态方法
>
> `staticmethod`的纯pyton看起来像这样
> ```python
> class StaticMethod(object):
> 	"Emulate PyStaticMethod_Type() in Objects/funcobject.c"
> 	def __init__(self, f):
> 		self.f = f
> 	def __get__(self, obj, objtype=None):
>         return self.f
> ```
> 而`classmethod`看起来像这样的
> ```python
> class ClassMethod(object):
> 	"Emulate PyClassMethod_Type() in Objects/funcobject.c"
>      def __init__(self, f):
>           self.f = f
>
>      def __get__(self, obj, klass=None):
>           if klass is None:
>                klass = type(obj)
>           def newfunc(*args):
>                return self.f(klass, *args)
>           return newfunc
> ```
> 有了`@property`装饰器的了解，这两个装饰器的原理是差不多的。`@staticmethod`返回的是一个`staticmethod`类对象，而`@classmethod`返回的是一个`classmethod`类对象。他们都是调用的是各自的`__init__()`构造函数。

#### 14.`@classmethod` `@staticmethod`

> [这是一个非常好的解释](https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner?rq=1)
>
> Though `classmethod` and `staticmethod` are quite similar, there's a slight difference in usage for both entities: `classmethod` must have a reference to a class object as the first parameter, whereas `staticmethod` can have no parameters at all.
>
> ## Example
>
> ```python
> class Date(object):
>
>     def __init__(self, day=0, month=0, year=0):
>         self.day = day
>         self.month = month
>         self.year = year
>
>     @classmethod
>     def from_string(cls, date_as_string):
>         day, month, year = map(int, date_as_string.split('-'))
>         date1 = cls(day, month, year)
>         return date1
>
>     @staticmethod
>     def is_date_valid(date_as_string):
>         day, month, year = map(int, date_as_string.split('-'))
>         return day <= 31 and month <= 12 and year <= 3999
>
> date2 = Date.from_string('11-09-2012')
> is_date = Date.is_date_valid('11-09-2012')
> ```
>
> ## Explanation
>
> Let's assume an example of a class, dealing with date information (this is what will be our boilerplate to cook on):
>
> ```python
> class Date(object):
>
>     def __init__(self, day=0, month=0, year=0):
>         self.day = day
>         self.month = month
>         self.year = year
> ```
>
> This class obviously could be used to store information about certain dates (without timezone information; let's assume all dates are presented in UTC).
>
> Here we have `__init__`, a typical initializer of Python class instances, which receives arguments as a typical `instancemethod`, having the first non-optional argument (`self`) that holds reference to a newly created instance.
>
> **Class Method**
>
> We have some tasks that can be nicely done using `classmethod`s.
>
> *Let's assume that we want to create a lot of Date class instances having date information coming from outer source encoded as a string of next format ('dd-mm-yyyy'). We have to do that in different places of our source code in project.*
>
> So what we must do here is:
>
> 1. Parse a string to receive day, month and year as three integer variables or a 3-item tuple consisting of that variable.
> 2. Instantiate `Date` by passing those values to initialization call.
>
> This will look like:
>
> ```python
> day, month, year = map(int, string_date.split('-'))
> date1 = Date(day, month, year)
> ```
>
> For this purpose, C++ has such feature as overloading, but Python lacks that feature- so here's when `classmethod` applies. Lets create another "*constructor*".
>
> ```python
>     @classmethod
>     def from_string(cls, date_as_string):
>         day, month, year = map(int, date_as_string.split('-'))
>         date1 = cls(day, month, year)
>         return date1
>
> date2 = Date.from_string('11-09-2012')
> ```
>
> Let's look more carefully at the above implementation, and review what advantages we have here:
>
> 1. We've implemented date string parsing in one place and it's reusable now.
> 2. Encapsulation works fine here (if you think that you could implement string parsing as a single function elsewhere, this solution fits OOP paradigm far better).
> 3. `cls` is an object that holds **class itself**, not an instance of the class. It's pretty cool because if we inherit our `Date` class, all children will have `from_string` defined also.
>
> **Static method**
>
> What about `staticmethod`? It's pretty similar to `classmethod` but doesn't take any obligatory parameters (like a class method or instance method does).
>
> Let's look at the next use case.
>
> *We have a date string that we want to validate somehow. This task is also logically bound to Dateclass we've used so far, but still doesn't require instantiation of it.*
>
> Here is where `staticmethod` can be useful. Let's look at the next piece of code:
>
> ```python
>     @staticmethod
>     def is_date_valid(date_as_string):
>         day, month, year = map(int, date_as_string.split('-'))
>         return day <= 31 and month <= 12 and year <= 3999
>
>     # usage:
>     is_date = Date.is_date_valid('11-09-2012')
> ```
>
> So, as we can see from usage of `staticmethod`, we don't have any access to what the class is- it's basically just a function, called syntactically like a method, but without access to the object and it's internals (fields and another methods), while classmethod does.

####15.`@property`,`@classmethod`,`@staticmethod`区别
>`@property` 是由`data descriptor`而来的把方法转变成属性，主要针对的还是实例，包含有`self`参数
>`@classmethod`,`@staticmethod`是由`non-data descriptor`而来的把方法转变成属性,主要针对类，类直接调用方法。