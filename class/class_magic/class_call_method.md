## Python 内置方法 `__call__` 和函数装饰器

> ```python
> object.__call__(self[, args...])¶
> 	Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
> ```
>
> Python内置魔方方法`__call__` ,允许类的实例像函数一样调用.
>
> ```python
> In [51]: class A:
>     ...:     def __init__(self, name):
>     ...:         self.name = name
>     ...:     def __call__(self,*args,**kwargs):
>     ...:         return "hello {}".format(self.name)
>     ...:     
>
> In [52]: foo = A("Jack")
>
> In [53]: foo()
> Out[53]: 'hello Jack'
> ```
>
> `__call__()` 可以传递多个参数,一个类定义了这个方法,那么它就是可调用的(`callable` ) 
>
> `__call__`可以让类的实例的行为变现的想函数一样。可以调用他们，将一个函数作为参数传递给另外一个函数中。允许一个类的实例 像函数一样被调用，即`class A()`的实例`a`,能够像函数一样`a()`,调用的是`A.__call__()`,并且`class A()`能接受函数`b`做`A.__call__()`的参数，`__call__()`参数可变，这意味着可以定义更多自己想要的参数
>
> 基于类的内置`__call__()` 方法,可以实现,类的装饰器

### 类装饰器

> 装饰器函数其实就是一个约束接口，它需要传入一个`callable`对象作为参数，然后返回一个`callable`对象，在python中函数一般都是`callable`对象，但是，只要某个对象重载了`__call__()`方法，那么这个对象就是`callable`的。
>
> 我们可以让类的构造函数`__init__()`接收一个函数，然后重载`__call__()`方法，也可以达到装饰器的效果。
>
> ```python
> class Logging:
>
>     def __init__(self, func):
>         self.func = func
>
>     def __call__(self, *args, **kwargs):
>         print('[{level}: enter function {func}()]'.format(
>             level="level", func=self.func.__name__))
>         return self.func(*args, **kwargs)
>
> @Logging
> def do(something):
>     print("do {}...".format(something))
>
> @Logging
> def say(something):
>     print("say {}".format(something))
>
> def foo(whatis):
>     print("This is foo")
>
> whois = Logging(foo)
>
> if __name__ == '__main__':
>     do("Jack")
>     say("Ning")
>     whois("foo")
> ```
>
> 类装饰器和函数相似,只不过类装饰器返回的是一个类对象,函数返回的是一个函数对象.
>
> `whois = logging(foo)` 是`@` 语法糖实现的等效方法

### 带参数的类装饰器

> 如果需要通过类形式带参数的装饰器，那么在构造函数里接受的就不是一个函数，而是传入的参数。通过类把这些参数保存起来。然后在重载`__call__()`方法里就需要接受一个函数并返回一个函数。
>
> ```python
> class Logging_1:
>
>     def __init__(self, level='INFO'):
>         self.level = level
>
>     def __call__(self, func):
>         def wrapper(*args, **kwargs):
>             print('[{level}: enter function {func}()]'.format(
>                 level=self.level, func=func.__name__))
>             return func(*args, **kwargs)
>         return wrapper
>
> @Logging_1(level='DEBUG')
> def say_1(something):
>     print('say {}!'.format(something))
>
> def do_1(something):
>     print("do:{}...".format(something))
> if __name__ == "__main__":
> 	ins_do = Logging_1(level="Debug")(do_1)
> 	ins_do("play with dog")
> 	say_1("cat is cute")
> ```
>
> `in_do("play with dog") ` 是装饰器的等价形式.
>
> 可以看到装饰器的数据传输是按照顺序传输的

### 类接受一个装饰器

> python好的一点是，方法（method）和函数（function）实际是一样的。唯一的区别在于，方法的第一个参数需要是当前对象（self）的引用。
>
> 这意味着，你可以使用同样的方式创建方法的装饰器！不过，别忘了 `self`。
>
> ```python
> def method_friendly_decorator(method_to_decorate):
> 	def wrapper(self, lie):
> 		lie = lie - 3 # very friendly, decrease age even more :-)
> 		return method_to_decorate(self, lie)
> 	return wrapper
>
>
> class Lucy(object):
>
> def __init__(self):
> 	self.age = 32
>
> @method_friendly_decorator
> def sayYourAge(self, lie):
> 	print("I am {0}, what did you think?".format(self.age + lie))
>
> l = Lucy()
> l.sayYourAge(-3)
> #outputs: I am 26, what did you think?
> ```
>
> 如果要写一个通用的装饰器-可用于任何函数或方法，而不必考虑其参数-那么，用`*args`,` **kwargs`就好了：
