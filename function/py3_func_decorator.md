### 装饰器

###  1.为什么需要装饰器
> Python中的装饰器是你进入Python大门的一道坎，不管你跨不跨过去它都在那里。
>
> 为什么需要装饰器
> 我们假设你的程序实现了say_hello()和say_goodbye()两个函数。
>
> ```python
> def say_hello():
>     print "hello!"
>
> def say_goodbye():
>     print "hello!"  # bug here
>
> if __name__ == '__main__':
>     say_hello()
>     say_goodbye()
> ```
>
> 但是在实际调用中，我们发现程序出错了，上面的代码打印了两个hello。经过调试你发现是say_goodbye()出错了。老板要求调用每个方法前都要记录进入函数的名称，比如这样：
>
>  ```python
> [DEBUG]: Enter say_hello()
> Hello!
> [DEBUG]: Enter say_goodbye()
> Goodbye!
>  ```
>
> 　好，小A是个毕业生，他是这样实现的。
> ```python
> def say_hello():
>     print "[DEBUG]: enter say_hello()"
>     print "hello!"
>
> def say_goodbye():
>     print "[DEBUG]: enter say_goodbye()"
>     print "hello!"
>
> if __name__ == '__main__':
>     say_hello()
>     say_goodbye()
>     
> ```
>
>  小B工作有一段时间了，他告诉小A可以这样写。
>
> 
>
> ```python
> def debug():
>
>     import inspect
>     caller_name = inspect.stack()[1][3]
>     print "[DEBUG]: enter {}()".format(caller_name)   
>
> def say_hello():
>     debug()
>     print "hello!"
>
> def say_goodbye():
>     debug()
>     print "goodbye!"
>
> if __name__ == '__main__':
>     say_hello()
>     say_goodbye()
>     
> ```
>
> 是不是好一点？那当然，但是每个业务函数里都要调用一下`debug(`)函数，是不是很难受？万一老板说`say`相关的函数不用`debug`，`do`相关的才需要呢？
>
> 那么装饰器这时候应该登场了。
>
> ```bash
> 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用.
> ```
>
> 概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。
### 2.装饰器基础，简单的装饰器
#### 2.1 函数作用域，命名空间
> python函数在运行的时候，会创建自己的`scope`,（即作用域，也称为命名空间，namespace），执行函数时，如果函数体中遇见了变量名，python首先会在该函数的`namespace`中寻找该变量。函数的命名空间包含函数名和函数代码块真个都是。python中也有一些内置的函数，可以让我们来查看函数的`namepsace`.
> ```python
> locals(...)
>    locals() -> dictionary
>    Update and return a dictionary containing the current scope's local variables.
>
> globals(...)
>     globals() -> dictionary
>     Return the dictionary containing the current scope's global variables.
> ```
>
> 举例：
>  ```python
> a_string = "This is a global variable"
>
> def foo():
> 	print "locals:"
> 	print locals()
> print  'globals:'
> print   globals()  #1,doctest
>
> foo() #2
> #----------------输出-------
> #globals:
> #{'foo': <function foo at 0x19c100c8>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': './2.py', 'a_string': 'This is a global variable', '__name__': '__main__', '__package__': None, '__doc__': None}
> locals:
> 　#{}
>  ```
>
####  2.2 变量的生存周期
> 变量是有生存周期(lifetime)的,变量的生存周期和变量声明的作用域息息相关，其作用域销毁时，变量也就销毁了。
> ```python
> def foo():
> 	x = 1 
>
> foo()
>
> print x  #1
> #---------------------------------------------------------------------------
> #NameError   Traceback (most recent call last)
> #<ipython-input-9-2d264e11d975> in <module>()
> #----> 1 print x
> #NameError: name 'x' is not defined
> #1.x是在 foo 函数中定义的，在 foo 的local中存在，因此，其作用域是 foo 函数的作用域
> #2. #1处打印x , #1,位于全局作用域，因此，其在globals中寻找x,没有找到，所以会报错
> ```
>
#### 2.3 嵌套函数
>
> ```python
> def outer():
> 	x = 1 
> 	def inner():
> 		print x  #1
> 	inner()   #2  变量名inner，函数名inner
>
> outer()
>
> #输出结果
> #1
>
> #这个例子比普通的函数定义看起来复杂了点，实际上都是合理的。
> #	1，#1 的地方pyhon寻找名为x的local变量，在inner作用域内的local中寻找不到，python就在外层作用域中寻#找，其外层是outer函数，x是定义在outer作用域内的local变量
> #	2，#2的地方，调用了inter函数，这里需要特别注意，inner也只是一个变量名，是遵循python的变量查询规则#的(python先在outer函数的作用域中寻找名为inter的local变量)
> ```
>
#### 2.4函数是python中的first-class对象
> 一切皆对象，函数也是一个对象
> ```python
> a = 1 
> print a.__class__
> print issubclass(a.__class__,object) #all objects in python inherit form a common baseclass
>
> def foo():
> 	pass 
>
> print foo.__class__  #1
> print issubclass(foo.__class__,object)
> #------------------------------------
> #<type 'int'>
> #True
> #<type 'function'>
> #True
> #可以看到foo和变量a一样，都是顶级父类object的子类，a是一个int变量,foo是一个函数。
> #所以，函数没有什么特殊的，它和python里的其他东西一样，都属于对象，其父类是object.
> #这意味着，
> #1，函数和其他变量是一样的，变量是可以传递和修改值得，函数也可以作为变量
> #2，函数也可以作为函数的参数或者函数的返回值。
> ```
>
####2.5装饰器
> 装饰器其实就是调用时，把一个函数作为参数，在此函数封装后，返回一个替代函数，即:装饰器其实就在不修改原函数的基础上，在执行原函数的前后执行别的代码。
> 下面手动实现一个装饰器
>
> ```python
>
> def outer(some_func):
>
> 	 def inner():
> 		 print "before some_func"
> 		 ret = some_func()  #1
> 		 return ret + 1 
> 	 return inner 
> def foo():
> 	 return 1 
>
> decorated = outer(foo)   #2  装饰器实现的本质
> print  decorated()
> print "decorated's  __name__"  + decorated.__name__
> #-----------------------------------------------输出---------
> #before some_func
> #2
> #decorated 's __name__ : inner
> #
> #1，outer函数有一个名叫 some_func 的参数，在outer函数里定义了一个嵌套函数inner,outer 将innner函数
> 作为一个返回值返回(函数的标签)，注意，并没有去调用inner，只是将inner作为变量返回
> #2，inner函数打印了一行字符串，然后调用了 some_func变量，并且在#1处获取了some_func的返回值
> #3，outer每次调用时，参数some_func的值可能会不同，但是我们都会在innner中调用这个函数
> #4，inner结束时，其返回值是some_func() +1 
> #5，在#2处，调用了outer函数(foo函数作为一个参数传入)，并将返回的inner函数作为赋值给decorated
> #6，最后调用decorated()函数，执行inner，打印一行，并在inner中调用foo函数，返回2
> ```
>
> 常用的`@语法糖`
>
> ```python
> def outer(some_func):
>
> 	def inner():
> 		print 'before some_func'
> 		ret = some_func()  #1 
> 		return ret + 1 
> 	return inner 
>
> @outer 
> def foo():
> 	return  1 
> #decorated = outer(foo)   #2 
> print  foo() 
> print  foo.__name__ 
> 　#
> 　#
> #执行结果同上，代码是等价的
> #
> 　#函数装饰器就是把一个函数作为参数，把此函数封装后，返回一个替代函数
> 　#对应上面的代码，就是
> #outer装饰器，把foo函数作为参数，把foo封装成inner后，返回innner
>
>
> ```
>
### 3.高级装饰器
#### 3.1 带参数的装饰器
> 假设我们要输出一个打印日志的装饰器，而且要设置打印日志的级别
> ```python
> def logging(level):
>
> 	def wrapper(func):
> 		def inner_wrapper(*arg,**kwargs):
> 			print '[{level}: enter function {func}()]'.format(
> 							 level=level,func = func.__name__)
> 			return func(*args,**kwargs)
> 		return inner_wrapper
> 	return wrapper
>
> @logging(level='INFO')
> def say(something):
> 	print 'say {}!'.format(something)
>
> #如果没有使用@语法糖
> #say= logging(level='INFo')(say)
>
> @logging(level='DEBUG')
> def do(something):
> 	print 'do {}....'.format(something)
>
> if __name__ == '__main__':
>  	say('Hello')
> 	do('My work')
>
>
> ```
>
####3.2 基于类实现的装饰器
>
> 装饰器函数其实就是一个约束接口，它需要传入一个`callable`对象作为参数，然后返回一个`callable`对象，在python中函数一般都是`callable`对象，但是，只要某个对象重载了`__call__()`方法，那么这个对象就是`callable`的。
> ```python
> class Test():
>
>	def __call__(self):
> 		print 'call me'
> ```
>
> `__call__`魔法函数
> `__call__`可以让类的实例的行为变现的想函数一样。可以调用他们，将一个函数作为参数传递给另外一个函数中。允许一个类的实例 像函数一样被调用，即`class A()`的实例`a`,能够像函数一样`a()`,调用的是`A.__call__()`,并且`class A()`能接受函数`b`做`A.__call__()`的参数，`__call__()`参数可变，这意味着可以定义更多自己想要的参数。
>
>
> 类是可以实现`callable`的，我们可以让类的构造函数`__init__()`接收一个函数，然后重载`__call__()`方法，也可以达到装饰器的效果。
>
> ```python
> @logging(level='DEBUG')
> def do(something):
> 
> 	print 'do {}....'.format(something)
>
> if __name__ == '__main__':
> 	say('Hello')
> 	do('My work')
>
>
> class logging(object):
> 	def __init__(self,func):
> 		self.func = func 
>
> 	def __call__(self,*args,**kwargs):
>		print '[{level}: enter function {func}()]'.format(
>						 level=level,func = func.__name__)
>		return self.func(*args,**kwargs)
>
> @logging
> def say(something):
> 	print 'say {}!'.format(something)
> #say = logging(say)
>
>
> ```
>
#### 3.3 带参数的类装饰器
> 如果需要通过类形式带参数的装饰器，那么在构造函数里接受的就不是一个函数，而是传入的参数。通过类把这些参数保存起来。然后在重载`__call__()`方法里就需要接受一个函数并返回一个函数。
> ```python
> class logging(object):
>
> 	def __init__(self,level='INFO'):
> 		self.level = level 
> 	def __call__(self,func):
> 		def wrapper(*args,**kwargs):
> 			print '[{level}: enter function {func}()]'.format(
> 							 level=level,func = func.__name__)			
> 			return func(*args,**kwargs)
> 		return wrapper
>
> @logging(level='DEBUG')
> def say(something):
> 	print 'say {}!'.format(something)
>
> ```
>
####3.4内置的装饰器
> 内置的装饰器和普通的装饰器原理是一样的，只不过返回的不是函数，而是类对象
>
##### 3.4.1  **`@property`**
>
> 上面的是`property(fget=None, fset=None, fdel=None, doc=None) ->property attribute`是用装饰器写一个属性的标准写法.(**实例只测试了一个**)
>  可以有这样的：
>
> ```python
> def getx(self):
>
>    return self._x
>
> def setx(self, value):
>    self._x = value
>
> def delx(self):
>    del self._x
>
> # create a property
> #用有了property的三种属性方法，下面调用可以分别 get,set,del
> x = property(getx, setx, delx, "I am doc for x property")
> ```
>
> 但是python也有黑魔法 `@语法糖`，这个能够达到一样的效果
> ```python
> @property
> def x(self): ....
>
> #等同于
> def x(self): ....
> x = property(x)   # 填入的setter 属性
> ```
>
> 属性有三个装饰器: `setter` ,`getter` ,`deleter`,都是`property()`的基础上做了一些封装。因为`setter`和`deleter`是`property()`的第二和第三个参数，不能直接套用@语法。
> + 1.只有`@property`表示只读
> + 2.同时有`@property`和@`x.setter`表示可读可写
> + 3.同时有`@property`和@`x.sette`r和`x.delter`便是可读可写可删除
>
>
> ```python
> # !/usr/bin/env python
> # coding=utf-8
> # 定义一个装饰器
> class Student(object):
>    def __init__(self,id):
>        self._id = id 
>        >>
>    @property #只读
>    def score(self):
>        return self._score
>        >>
>    @score.setter #可写
>    def score(self,value):
>        self._score = value
>        >>
>    @property #只读
>    def get_id(self):
>        return self._id
> if __name__ == '__main__':
>    #实例化
>    s = Student('111')
>    #写属性
>    s.score = 20
>    #只读属性
>    print s.score
>    #读属性
>    print s.get_id
>    #不能写入，保护了属性
>    s.get_id = 5
> #------------------------------
> #执行结果
> #20
> #111
> #Traceback (most recent call last):
> # File "2.py", line 28, in <module>
> #    s.get_id = 5
> #AttributeError: can't set attribute
>
> ```
>
##### 3.4.2 `property`和`@property`比较

> ```python
> class A(object):#新式类（继承自object类）  
>
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
>  a=A()  
>  print a.name #读  
>  a.name='python' #写  
>  print a.name #读  
>  del a.name #删除  
> #print a.name #a.name已经被删除 AttributeError: 'A' object has no attribute '_A__name'
> #------------------------------------------------------------------
> class A(object):#要求继承object  
>     def __init__(self):  
>         self.__name=None  
>
>    #下面开始定义属性，3个函数的名字要一样！  
>    @property #读  
>    def name(self):  
>        return self.__name  
>    @name.setter #写  
>    def name(self,value):  
>        self.__name=value  
>    @name.deleter #删除  
>    def name(self):  
>        del self.__name  
>
> a=A()  
> print a.name #读  
> a.name='python'  #写  
> print a.name #读  
> del a.name #删除  
> #print a.name # a.name已经被删除 AttributeError: 'A' object has no attribute '_A__name'   
>
>
> ```
>
##### 3.4.3 `classmethod`和`staticmethod`
> ```python
>
>
> #!/usr/bin/env Python
> # coding=utf-8
> __metaclass__ = type
>
> class StaticMethod:
> 	@staticmethod
> 	def foo():
> 		print "This is static method foo()."
>
> class ClassMethod:
> 	@classmethod
> 	def bar(cls):
> 		print "This is class method bar()."
> 		print "bar() is part of class:", cls.__name__
>
>
> if __name__ == '__main__':
> 	static_foo = StaticMethod  #实例化
> 	static_foo.foo()    # 实例调用静态方法
> 	StaticMethod.foo()  # 通过类来调用静态方法
> 	print '*****'
> 	class_bar = ClassMethod   #实例化
> 	class_bar.bar()          # 通过实例调用类方法
> 	ClassMethod.bar()    # 通过类来调用类方法
> #----------------------输出-------
> #This is static method foo().
> #This is static method foo().
> #********
> #This is class method bar().
> #bar() is part of class: ClassMethod
> #This is class method bar().
> #bar() is part of class: ClassMethod
> ```
>
> + 静态方法，后面的括号中不需要传入`self`,无法访问到实例变量，类和实例的属性
> + 类方法，类方法必须有`cls`这个参数，在类方法中，能够方法类属性，但是不能访问实例属性，`cls`后还可以接参数
##### 3.4.4 `functoos.wraps`
>使用上面的方法时，会产生一个弊端
>eg:
>
>```python
>def decorator(func):
>
>    def wrapper(*args, **kwargs):
>        return func(*args, **kwargs)
>    return wrapper
>
> @decorator
> def add(x, y):
>    return x + y
>
> add     # <function __main__.wrapper>
>```
>
>  可以看到被装饰的函数的名称，也就是函数的 __name__ 属性变成了 wrapper， 这就是装饰器带来的副作用，实际上add 函数整个变成了 decorator(add)，而 wraps 装饰器能消除这些副作用：
>
> ```python
> import functools
> def decorator(func):
>
>    @functools.wraps(func)
>    def wrapper(*args, **kwargs):
>        return func(*args, **kwargs)
>    return wrapper
>
> @decorator
> def add(x, y):
>    return x + y
>
> add     # <function __main__.add>
> ```
>
> 会更正的属性定义在 `WRAPPER_ASSIGNMENTS` 中
> ```python
> functools.WRAPPER_ASSIGNMENTS
> ('__module__', '__name__', '__doc__')
> functools.WRAPPER_UPDATES
> ('__dict__',)
> ```
>
###4.装饰器里的那些坑
> 装饰器可以让你代码更加优雅，减少重复，但也不全是优点，也会带来一些问题。
>
> 位置错误的代码
> 让我们直接看示例代码。
>
> ```python
> def html_tags(tag_name):
> 	print 'begin outer function.'
>     	def wrapper_(func):
>         	print "begin of inner wrapper function."
>         def wrapper(*args, **kwargs):
>             content = func(*args, **kwargs)
>             print "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)
>         print 'end of inner wrapper function.'
>         return wrapper
>     print 'end of outer function'
>     return wrapper_
>
>
> @html_tags('b')
> def hello(name='Toby'):
>     return 'Hello {}!'.format(name)
>
> hello()
> hello()
>
> ```
>
> 在装饰器中我在各个可能的位置都加上了print语句，用于记录被调用的情况。你知道他们最后打印出来的顺序吗？如果你心里没底，那么最好不要在装饰器函数之外添加逻辑功能，否则这个装饰器就不受你控制了。以下是输出结果：
>
> ```bash
> begin outer function.
> end of outer function
> begin of inner wrapper function.
> end of inner wrapper function.
> <b>Hello Toby!</b>
> <b>Hello Toby!</b>
> ```
>
> 错误的函数签名和文档
> 装饰器装饰过的函数看上去名字没变，其实已经变了。
>
> ```python
> def logging(func):
>
>    def wrapper(*args, **kwargs):
>        """print log before a function."""
>        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
>        return func(*args, **kwargs)
>    return wrapper
>
> @logging
>  def say(something):
>    """say something"""
>    print "say {}!".format(something)
>
> print say.__name__  # wrapper
>
> ```
>
> 为什么会这样呢？只要你想想装饰器的语法糖@代替的东西就明白了。@等同于这样的写法。
> `say = logging(say)`
> logging其实返回的函数名字刚好是wrapper，那么上面的这个语句刚好就是把这个结果赋值给say，say的__name__自然也就是wrapper了，不仅仅是name，其他属性也都是来自wrapper，比如doc，source等等。
>
>
> 使用标准库里的functools.wraps，可以基本解决这个问题。
>
> ```python
> from functools import wraps
>
> def logging(func):
>
>    @wraps(func)
>    def wrapper(*args, **kwargs):
>        """print log before a function."""
>        print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
>        return func(*args, **kwargs)
>    return wrapper
>
> @logging
> def say(something):
>     """say something"""
>     print "say {}!".format(something)
>
> print say.__name__  # say
> print say.__doc__ # say something
> ```
>
> 看上去不错！主要问题解决了，但其实还不太完美。因为函数的签名和源码还是拿不到的。
>
> ```python
> import inspect
> print inspect.getargspec(say)  # failed
> print inspect.getsource(say)  # failed
> ```
>
> 如果要彻底解决这个问题可以借用第三方包，比如wrapt。后文有介绍。
>
> 不能装饰@staticmethod 或者 @classmethod
> 当你想把装饰器用在一个静态方法或者类方法时，不好意思，报错了。
> ```python
> class Car(object):
> 	def __init__(self, model):
>     	self.model = model
>
> @logging  # 装饰实例方法，OK
> 	def run(self):
>     print "{} is running!".format(self.model)
>
> @logging  # 装饰静态方法，Failed
> @staticmethod
> 	def check_model_for(obj):
>     	if isinstance(obj, Car):
>          	print "The model of your car is {}".format(obj.model)
>       	else:
>             print "{} is not a car!".format(obj)
>
>    """
>    Traceback (most recent call last):
>
>    File "example_4.py", line 10, in logging
>    @wraps(func)
>    File "C:\Python27\lib\functools.py", line 33, in update_wrapper
>    setattr(wrapper, attr, getattr(wrapped, attr))
>    AttributeError: 'staticmethod' object has no attribute '__module__'
>    """
> ```
>
>    前面已经解释了@staticmethod这个装饰器，其实它返回的并不是一个callable对象，而是一个staticmethod对象，那么它是不符合装饰器要求的（比如传入一个callable对象），你自然不能在它之上再加别的装饰器。要解决这个问题很简单，只要把你的装饰器放在@staticmethod之前就好了，因为你的装饰器返回的还是一个正常的函数，然后再加上一个@staticmethod是不会出问题的。
>
> ```python
> class Car(object):
>
> def __init__(self, model):
>     self.model = model
>
> @staticmethod
> @logging  # 在@staticmethod之前装饰，OK
> def check_model_for(obj):
>     pass
> ```
###5.`decorator.py`.`wrapt`
>[详情见](https://segmentfault.com/a/1190000007321935#articleHeader2)
>
>
###6.参考
>[参考1](http://kissg.me/2016/07/16/translation-about-python-decorator/)
>
>[参考2](./py3_decorator/cankao_cn_decorator.md)
>
>[参考3](./py3_decorator/cankao_en_decorator.md)