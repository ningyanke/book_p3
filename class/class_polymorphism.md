## 多态

> 是指计算机程序运行时，相同的消息可能会送给多个不同的类别之对象，而系统可依据对象所属类别，引发对应类别的方法，而有不同的行为。简单来说，所谓多态意指相同的消息给予不同的对象会引发不同的动作称之。
>
> 多态可分为变量多态与函数多态。变量多态是指：基类型的变量（对于C++是引用或指针）可以被赋值基类型对象，也可以被赋值派生类型的对象。函数多态是指，相同的函数调用界面（函数名与实参表），传送给一个对象变量，可以有不同的行为，这视该对象变量所指向的对象类型而定。因此，变量多态是函数多态的基础。
>
> 
>
> 动态多态（dynamic polymorphism）:通过类继承机制和虚函数机制生效于运行期。可以优雅地处理异质对象集合，只要其共同的基类定义了虚函数的接口。也被称为子类型多态（Subtype polymorphism）或包含多态（inclusion polymorphism）。在面向对象程序设计中，这被直接称为多态。
> 静态多态（static polymorphism）：模板也允许将不同的特殊行为和单个泛化记号相关联，由于这种关联处理于编译期而非运行期，因此被称为“静态”。可以用来实现类型安全、运行高效的同质对象集合操作。C++ STL不采用动态多态来实现就是个例子。
> 非参数化多态或译作特设多态（Ad-hoc polymorphism）：
> 函数重载（Function Overloading）
> 运算符重载（Operator Overloading）
> 带变量的宏多态（macro polymorphism）
> 参数化多态（Parametric polymorphism）：把类型作为参数的多态。在面向对象程序设计中，这被称作泛型编程。

### Python多态

> 在Python中多态指的是"鸭子类型".
>
> 在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定.“鸭子测试”可以这样表述：
>
> “当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。
>
> 在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。例如，在不使用鸭子类型的语言中，我们可以编写一个函数，它接受一个类型为"鸭子"的对象，并调用它的"走"和"叫"方法。在使用鸭子类型的语言中，这样的一个函数可以接受一个任意类型的对象，并调用它的"走"和"叫"方法。如果这些需要被调用的方法不存在，那么将引发一个运行时错误。任何拥有这样的正确的"走"和"叫"方法的对象都可被函数接受的这种行为引出了以上表述，这种决定类型的方式因此得名。
>
> 鸭子类型通常得益于"不"测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。
>
> python中的定义
>
> ```python
> A programming style which does not look at an object’s type to determine if it has the right interface; instead, the method or attribute is simply called or used (“If it looks like a duck and quacks like a duck, it must be a duck.”) By emphasizing interfaces rather than specific types, well-designed code improves its flexibility by allowing polymorphic substitution. Duck-typing avoids tests using type() or isinstance(). (Note, however, that duck-typing can be complemented with abstract base classes.) Instead, it typically employs hasattr() tests or EAFP programming.
> ```

### Python多态的表现

> 类是一个对象,对象拥有自己的数据类型,我们定义的类的数据类型和Python自带的数据类型没有什么两样
>
> ```python
> In [5]: a = [1,2,3]
>
> In [6]: b = (1,2,3)
>
> In [7]: class Animal:
>    ...:     def run(self):
>    ...:         print("Animal running")
>    ...:         
>
> In [8]: isinstance(a,list)
> Out[8]: True
>
> In [9]: isinstance(b,tuple)
> Out[9]: True
>
> In [12]: foo = Animal()
>
> In [13]: isinstance(foo,Animal)
> Out[13]: True
> ```
>
> 不同的数据类型他们拥有的属性和方法也是不同的
>
> ```python
> In [19]: class People:
>     ...:     def sing(self):
>     ...:         print("People sing")
>     ...:         
>
> In [20]: class Dog(Animal):
>     ...:     def speek(self):
>     ...:         print("wo wo")
>     ...:         
>
> In [21]: puppy = Dog()
>
> In [22]: chinise = People()
>
> In [23]: puppy.speek()
> wo wo
>
> In [24]: puppy.run()
> Animal running
>
> In [25]: isinstance(puppy,Animal)
> Out[25]: True
>
> In [26]: isinstance(puppy,Dog)
> Out[26]: True
>
> In [27]: isinstance(chinise,People)
> Out[27]: True
>
> In [28]: pupyy.sing
> ---------------------------------------------------------------------------
> NameError                                 Traceback (most recent call last)
> <ipython-input-28-aa5bad9c8929> in <module>()
> ----> 1 pupyy.sing
>
> NameError: name 'pupyy' is not defined
>
> ```
>
> `puppy.sing` 没有定义,属性既没有自己定义,也不是来自继承,他们拥有不同的属性和方法
>
> 而对于多态
>
> ```python
> In [29]: class Cat:
>     ...:     def speak(self):
>     ...:         print("meow")
>     ...:         
>
> In [30]: class Dog:
>     ...:     def speak(slef):
>     ...:         print("woof")
>     ...:         
>
> In [31]: class Bob:
>     ...:     def bow(self):
>     ...:         print("thank you ,thank you ")
>     ...:     def speek(self):
>     ...:         print("hello, welcome to the neighborhood")
>     ...:     def drive(self):
>     ...:         print("beep,beep")
>     ...:         
>
> In [32]: def command(pet):
>     ...:     pet.speak()
>     ...:     
>
> In [33]: pets = [Cat(),Dog(),Bob()] 
>
> In [34]: for pet in pets:
>     ...:     command(pet)
>
> ```
>
> 他们各自的数据类型不同,却可以在同一个函数中调用,只是因为他们都有一个`speak` 方法.
>
> Python不会检查传入的数据类型,而只是在意时候拥有这个方法或属性,

### 接口

> 在Python中接口的概念不是那么的重要,因为Python是一种动态语言,不需要显式的声明接口,
>
> [Java接口](https://www.zhihu.com/question/20111251)
>
> 由于后期绑定，他们不需要它。在Java / C＃中，接口用于声明某些类具有某些方法，并在编译期间进行检查; 在Python中，在运行中就可以检查时候是方法
>
> ```python
> >>> class A:
> ...  def foo(self):
> ...    return "A"
> ...
> >>> class B(A):
> ...  def foo(self):
> ...    return "B"
> ...
> >>> B().foo()
> 'B'
> ```
>
> 当然,可以简单的认为 Python 中的 `class interface` 指的是类的属性和集合

#### 类的接口技术(来自于Python学习手册)

> Python学习手册中用到了这个概念,理解为类的属性和方法的集合.
>
> ```python
> #!/usr/bin/env python
> # coding=utf-8
>
> class Super:
>     def method(self):
>         print("in super.method")
>
>     def delegate(self):
>         self.action()
>         
> class Inheritor(Super):
>     pass
>
> class Repalcer(Super):
>
>     def method(self):
>         print("in repalcer.method")
>
> class Extender(Super):
>     def method(self):
>         print("starting Extender.method")
>         Super.method(self)
>         print("ending extender.method")
>
> class Provider(Super):
>     def action(self):
>         print("in Provider.action")
>
> if __name__ == "__main__":
>     for klass in (Inheritor, Repalcer, Extender):
>         print("\n" + klass.__name__ + '...')
>         klass().method()
>     print("\nProvider....")
>     x = Provider()
>     x.delegate()
>
> """
> Inheritor...
> in super.method
>
> Repalcer...
> in repalcer.method
>
> Extender...
> starting Extender.method
> in super.method
> ending extender.method
>
> Provider....
> in Provider.action
> """
> ```
>
> 类扩展,覆盖等等方法,都是对超类接口(属性和方法)的一种方式

### 抽象基类

> ```python
> class Super:
>     def method(self):
>         print("in super.method")
>
>     def delegate(self):
>         self.action()
>         
> class Provider(Super):
>     def action(self):
>         print("in Provider.action")     
> ```
>
> 像这样的: 类的部分行为由其子类来提供,我们称呼 类 为抽象基类,如果预期的方法没有在之类中定义,Python会引发一个异常.

### Python3 抽象基类(ABC)

> An interface, for an object, is a set of methods and attributes on that object.
>
> In Python, we can use an abstract base class to define and enforce an interface.
>
> [python3 抽象基类](https://docs.python.org/3/library/abc.html?highlight=abstract%20super%20class)
>
> 抽象基类一般用于规定子类必须重新定义某些方法。比如 web 框架中的 cache 部分的基类一般类似下面这样:
>
> ```
> class BaseCache(object):
>     def get(self, key):
>         raise NotImplementedError('subclasses of BaseCache must provide a get() method')
>
>     def set(self, key, value, timeout=60):
>         raise NotImplementedError('subclasses of BaseCache must provide a set() method')
>
>
> class MemcachedCache(BaseCache):
>     def get(self, key):
>         value = self._cache.get(key)
>         return value
>
>     def set(self, key, value, timeout=60):
>         self._cache.set(key, value, timeout)
>
> ```
>
> 在插件、cache、session 等支持功能扩展的系统中，常用抽象基类来统一接口。
>
> > Why use Abstract Base Classes?
> >
> > Abstract base classes are a form of interface checking more strict than individual hasattr() checks for particular methods. By defining an abstract base class, you can define a common API for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins to an application, but can also aid you when working on a large team or with a large code-base where keeping all classes in your head at the same time is difficult or not possible.
>
> 下面介绍三种定义抽象基类的方法。
>
> ## 使用 assert 语句
>
> ```
> class BaseClass(object):
>     def action(self, foobar):
>         assert False, 'subclasses of BaseClass must provide an action() method'
>
> In [6]: BaseClass().action('a')
> ---------------------------------------------------------------------------
> AssertionError                            Traceback (most recent call last)
> <ipython-input-6-69f195c0ee1f> in <module>()
> ----> 1 BaseClass().action('a')
>
> <ipython-input-3-25c84a2cb72e> in action(self, foobar)
>       1 class BaseClass(object):
>       2     def action(self, foobar):
> ----> 3         assert False, 'subclasses of BaseClass must provide an action() method'
>
> AssertionError: subclasses of BaseClass must provide an action() method
>
> ```
>
> ## 使用 NotImplementedError 异常
>
> ```
> class BaseClass(object):
>     def action(self, foobar):
>         raise NotImplementedError('subclasses of BaseClass must provide an action() method')
>
> In [8]: BaseClass().action('a')
> ---------------------------------------------------------------------------
> NotImplementedError                       Traceback (most recent call last)
> <ipython-input-8-69f195c0ee1f> in <module>()
> ----> 1 BaseClass().action('a')
>
> <ipython-input-7-81782a1e8377> in action(self, foobar)
>       1 class BaseClass(object):
>       2     def action(self, foobar):
> ----> 3         raise NotImplementedError('subclasses of BaseClass must provide an action() method')
>
> NotImplementedError: subclasses of BaseClass must provide an action() method
>
> ```
>
> ## 使用 abc 模块
>
> python 2.6, 2.7:
>
> ```
> from abc import ABCMeta, abstractmethod
>
> class BaseClass(object):
>     __metaclass__ = ABCMeta
>
>     @abstractmethod
>     def action(self, foobar):
>         pass
>
> In [11]: BaseClass().action('a')
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-11-69f195c0ee1f> in <module>()
> ----> 1 BaseClass().action('a')
>
> TypeError: Can't instantiate abstract class BaseClass with abstract methods action
>
> ```
>
> python 3.x:
>
> ```
> from abc import ABCMeta, abstractmethod
>
> class BaseClass(metaclass=ABCMeta):
>     @abstractmethod
>     def action(self, foobar):
>         pass
>
> ```
>
> 推荐使用 `abc` 模块，`NotImplementedError` 也比较常用。

