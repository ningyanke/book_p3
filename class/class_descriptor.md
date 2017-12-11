## Python 描述器引导

### Python魔法方法-描述器(discriptor)　

####  1.官方文档
>
> [官方文档](https://docs.python.org/2/howto/descriptor.html)
> [参照文档](http://pyzh.readthedocs.io/en/latest/Descriptor-HOW-TO-Guide.html)

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

#### 3.描述器可以用来做上面

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
> 意对象具有其中**任一个方法**，就会成为描述器。从而被当做**对象属性**时重写默认的查找行为。
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
>
> 