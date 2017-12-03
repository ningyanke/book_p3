### 1.Python的函数是对象

> 为了理解装饰器，你必须先理解：在Python的世界，函数是对象。这一点很重要。让我们通过一个简单的例子来看看为什么：
>
> ```python
> def shout(word="yes"):
>     return word.capitalize()+"!"
>
> print(shout())
> # outputs : 'Yes!'
>
> # 做为一个对象,函数可以像其他对象一样赋值给其他变量
> scream = shout
>
> # 注意, 我们并没有使用括号:
> # 我们没有调用函数, 我们是将"shout"函数装入到"scream"变量中,函数本身
> # 这意味着你可以像从"scream"调用"shout"
>
> print(scream())
> # outputs : 'Yes!'
>
> # 不仅如此, 它还意味着你可以删除旧的名字"shout",
> # 而仍然可以通过"scream"访问函数
>
>
> del shout
> try:
>     print(shout())
> except NameError, e:
>     print(e)
>     #outputs: "name 'shout' is not defined"
>
> print(scream())
> # outputs: 'Yes!'
> ```
>
> 好的！在脑海中保留这个概念。我们之后会用它。
>
> Python函数的另一个有趣的属性是：它们可以在另一个函数的内部被定义
>
> ```python
> def talk():
>
>     # 你可以在运行时, 在"talk"函数内部定义一个函数
>     def whisper(word="yes"):
>         return word.lower()+"..."
>
>     # 然后立马使用它
>     print(whisper())
>
> # 当调用"talk"时, 你的每一次调用都会定义"whisper"一次,
> # 然后,"whisper"在'talk'内部被调用
> talk()
> # outputs: 
> # "yes..."
>
> # 但是"whisper"不存在"talk"作用域之外:
>
> try:
>     print(whisper())
> except NameError, e:
>     print(e)
>     #outputs : "name 'whisper' is not defined"*
>     #Python's functions are objects
> ```

### 2.函数引用

> 现在我们已经知道了函数是一种对象。因此，
>
> * **函数可以赋值给一个变量**
> * **函数可以在另一个函数中被定义**
>
> 这意味着:
>
> * **函数能作为其他函数的返回值**
>
> ```python
> def getTalk(kind="shout"):
>
>     # 我们在运行时定义函数
>     def shout(word="yes"):
>         return word.capitalize()+"!"
>
>     def whisper(word="yes") :
>         return word.lower()+"...";
>
>     # 然后我们返回其中的一个
>     if kind == "shout":
>         # 不使用"()",不是调用函数,而是使用函数本生
>         # 我们在返回一个函数对象本身
>         return shout  
>     else:
>         return whisper
>
> # 如何使用函数 getTalk
>
> # 首先调用函数并命名给一个变量
> talk = getTalk()      
>
> # 可以看到变量"talk"是一个函数对象
> print(talk)
> #outputs : <function shout at 0xb7ea817c>
>
> # 调用"talk()" 函数返回结果
> print(talk())
> #outputs : Yes!
>
> # 你也可以直接这样使用"getTalk()"函数
> print(getTalk("whisper")())
> #outputs : yes...
> ```
>
> 当然:
>
> 也可以把函数当做参数返回,或者是当做另外一个函数的参数传入:
>
> ```python
> def doSomethingBefore(func): 
>     print("I do something before then I call the function you gave me")
>     print(func())
>
> doSomethingBefore(scream)
> #outputs: 
> #I do something before then I call the function you gave me
> #Yes!
> ```
>
> 现在，你已经具备了理解装饰器所需的一切知识。如你所见，装饰器就是`wrappers`，也就是说，**装饰器允许你在被装饰的函数前后执行代码，而不对函数本身做任何修改。**

### 3.自己动手写一个装饰器

> **纯净版**
>
> ```python
> def my_shiny_new_decorator(a_function_to_decorate):
>     
>     def the_wrapper_around_the_original_function():
> 		print("Before the function runs")
> 		a_function_to_decorate()
>         print("After the function runs")
>         
>     return the_wrapper_around_the_original_function
>
> def a_stand_alone_function():
>     print("I am a stand alone function, don't you dare modify me")
>
> a_stand_alone_function() 
>
> a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
> a_stand_alone_function_decorated()
> #outputs:
> #Before the function runs
> #I am a stand alone function, don't you dare modify me
> #After the function runs
> ```
>
> **注释版**
>
> ```python
> # 装饰器是函数, 它以另一个函数作为参数
> def my_shiny_new_decorator(a_function_to_decorate):
>     
>     
>  	# 在装饰器的内部, 定义一个"wrapper"函数
>     # wrapper函数用于包装原函数, 以在原函数前后执行代码
>     def the_wrapper_around_the_original_function():
>
>         #在此处输入你想在调用原函数之前执行的代码
>         print("Before the function runs")
>
>         # 调用被装饰的函数(是函数调用, 需要括号)
>         a_function_to_decorate()
>
>         # 在此处输入你想在调用原函数之后执行的代码
>         print("After the function runs")
>
>     # 此处, 被装饰的函数并没有被执行
>     # 返回刚刚创建的包装函数
>     # 包装函数包括被装饰的函数, 在函数前后执行的代码
>     return the_wrapper_around_the_original_function
>
> # 现在, 假设你创建了一个可能用不到的函数
> def a_stand_alone_function():
>     print("I am a stand alone function, don't you dare modify me")
>
> a_stand_alone_function() 
> #outputs: I am a stand alone function, don't you dare modify me
>
> # 然而, 你可以装饰它, 扩展它
> # 只需要将它传递给一个装饰器, 装饰器将动态地将函数包装进任何你想要的代码中
> # 并返回一个可用的新函数
>
> a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
> a_stand_alone_function_decorated()
> #outputs:
> #Before the function runs
> #I am a stand alone function, don't you dare modify me
> #After the function runs
> ```
>
> 现在，可能你想要在每次调用`a_stand_alone_function`时，替代地调用`a_stand_alone_function_decorated`。很简单，装饰用器`my_shiny_new_decorator`覆盖原函数`a_stand_alone_function`即可。
>
> ```python
> a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
> a_stand_alone_function()
> #outputs:
> #Before the function runs
> #I am a stand alone function, don't you dare modify me
> #After the function runs
>
> # 这就是装饰器的本质
> ```
>
> 

### 4.装饰器解密

> 用装饰器语法重现先前的例子，是这样的：
>
> ```python
> @my_shiny_new_decorator
> def another_stand_alone_function():
>     print("Leave me alone")
>
> another_stand_alone_function()  
> #outputs:  
> #Before the function runs
> #Leave me alone
> #After the function runs
> ```
>
> 是的，就是这样，这么简单。@decorator是以下形式的缩写：
>
> ```python
> another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
> ```
>
> 装饰器只是装饰器设计模式在Python中的变体。Python自带了许多经典设计模式来方便开发，比如迭代器。
>
> 当然，你可以**叠加装饰器：**
>
> ```python
> def bread(func):
>     def wrapper():
>         print("</''''''\>")
>         func()
>         print("<\______/>")
>     return wrapper
>
> def ingredients(func):
>     def wrapper():
>         print("#tomatoes#")
>         func()
>         print("~salad~")
>     return wrapper
>
> def sandwich(food="--ham--"):
>     print(food)
>
> sandwich()
> #outputs: --ham--
> sandwich = bread(ingredients(sandwich))
> sandwich()
> #outputs:
> #</''''''\>
> # #tomatoes#
> # --ham--
> # ~salad~
> #<\______/>
> ```
>
> 使用python装饰器语法:
>
> ```python
> @bread
> @ingredients
> def sandwich(food="--ham--"):
>     print(food)
>
> sandwich()
> #outputs:
> #</''''''\>
> # #tomatoes#
> # --ham--
> # ~salad~
> #<\______/>
> ```
>
> 设置装饰器语法糖的顺序也是重要的:
>
> ```python
> @ingredients
> @bread
> def strange_sandwich(food="--ham--"):
>     print(food)
>
> strange_sandwich()
> #outputs:
> ##tomatoes#
> #</''''''\>
> # --ham--
> #<\______/>
> # ~salad~
> ```

### 5.实现串在一起的装饰器

> ```python
> def makebold(fn):
>     def wrapper():      
>         return "<b>" + fn() + "</b>"
>     return wrapper
>
>
> def makeitalic(fn):
> 	def wrapper():
>         return "<i>" + fn() + "</i>"
>     return wrapper
>
> @makebold
> @makeitalic
> def say():
>     return "hello"
>
> print(say())
>
> def say():
>     return "hello"
>
> print(say())
> ```
>
> ```python
> # The decorator to make it bold
> def makebold(fn):
>     # The new function the decorator returns
>     def wrapper():
>         # Insertion of some code before and after
>         return "<b>" + fn() + "</b>"
>     return wrapper
>
> # The decorator to make it italic
> def makeitalic(fn):
>     # The new function the decorator returns
>     def wrapper():
>         # Insertion of some code before and after
>         return "<i>" + fn() + "</i>"
>     return wrapper
>
> @makebold
> @makeitalic
> def say():
>     return "hello"
>
> print(say())
> #outputs: <b><i>hello</i></b>
>
> # This is the exact equivalent to 
> def say():
>     return "hello"
> say = makebold(makeitalic(say))
>
> print(say())
> #outputs: <b><i>hello</i></b>
> ```

### 6.装饰器进阶-向被装饰函数传递参数

> ```python
> #这并不是黑魔法,you just have to let the wrapper pass the argument:
>
> def a_decorator_passing_arguments(function_to_decorate):
>     def a_wrapper_accepting_arguments(arg1, arg2):
>         print("I got args! Look: {0}, {1}".format(arg1, arg2))
>         function_to_decorate(arg1, arg2)
>     return a_wrapper_accepting_arguments
>
> # 当你调用装饰器返回的函数时, 你调用了wrapper
> # 向wrapper中传递的参数将可继续传递给被装饰函数
>
>
> @a_decorator_passing_arguments
> def print_full_name(first_name, last_name):
>     print("My name is {0} {1}".format(first_name, last_name))
>
> print_full_name("Peter", "Venkman")
> # outputs:
> #I got args! Look: Peter Venkman
> #My name is Peter Venkman
> ```
>
> 这个也很好理解,我们只需要,在运行程序中,在最后运行:
>
> ```python
> print("print_full_name.__name__ is ", print_full_name.__name__)
> ```
>
> 得到的结果是
>
> ```python
> print_full_name.__name__ is a_wrapper_accepting_arguments
> ```
>
> 所以,我们调用`print_full_name()` 函数,其实调用的就是`a_wrapper_accepting_arguments` 函数,这样,相当于直接在函数内部传递参数 .    [^note]
>
> [^note]注释
>
> 

### 7.装饰方法

> python好的一点是，方法（method）和函数（function）实际是一样的。唯一的区别在于，方法的第一个参数需要是当前对象（self）的引用。
>
> 这意味着，你可以使用同样的方式创建方法的装饰器！不过，别忘了 `self`。
>
> ```python
> def method_friendly_decorator(method_to_decorate):
>     def wrapper(self, lie):
>         lie = lie - 3 # very friendly, decrease age even more :-)
>         return method_to_decorate(self, lie)
>     return wrapper
>
>
> class Lucy(object):
>
>     def __init__(self):
>         self.age = 32
>
>     @method_friendly_decorator
>     def sayYourAge(self, lie):
>         print("I am {0}, what did you think?".format(self.age + lie))
>
> l = Lucy()
> l.sayYourAge(-3)
> #outputs: I am 26, what did you think?
> ```
>
> 如果要写一个通用的装饰器-可用于任何函数或方法，而不必考虑其参数-那么，用`*args`,` **kwargs`就好了：
>
> ```python
> def a_decorator_passing_arbitrary_arguments(function_to_decorate):
>     # wrapper 接收任意参数
>     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
>         print("Do I have args?:")
>         print(args)
>         print(kwargs)
>         # 将得到的参数解压(unpack), 此处为*args, **kwargs
>         # 如果对解压不熟悉, 可参考
>         # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
>         function_to_decorate(*args, **kwargs)
>     return a_wrapper_accepting_arbitrary_arguments
>
> @a_decorator_passing_arbitrary_arguments
> def function_with_no_argument():
>     print("Python is cool, no argument here.")
>
> function_with_no_argument()
> #outputs
> #Do I have args?:
> #()
> #{}
> #Python is cool, no argument here.
>
> @a_decorator_passing_arbitrary_arguments
> def function_with_arguments(a, b, c):
>     print(a, b, c)
>
> function_with_arguments(1,2,3)
> #outputs
> #Do I have args?:
> #(1, 2, 3)
> #{}
> #1 2 3 
>
> @a_decorator_passing_arbitrary_arguments
> def function_with_named_arguments(a, b, c, platypus="Why not ?"):
>     print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))
>
> function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
> #outputs
> #Do I have args ? :
> #('Bill', 'Linus', 'Steve')
> #{'platypus': 'Indeed!'}
> #Do Bill, Linus and Steve like platypus? Indeed!
>
> class Mary(object):
>
>     def __init__(self):
>         self.age = 31
>
>     @a_decorator_passing_arbitrary_arguments
>     def sayYourAge(self, lie=-3): # You can now add a default value
>         print("I am {0}, what did you think?".format(self.age + lie))
>
> m = Mary()
> m.sayYourAge()
> #outputs
> # Do I have args?:
> #(<__main__.Mary object at 0xb7d303ac>,)
> #{}
> #I am 28, what did you think?
> ```

### 8.向装饰器传递参数

> 好吧，现在你觉得如何向装饰器本身传递参数呢？
>
> 这有点绕，因为装饰器必须接收一个函数作为参数。因此，你不能向装饰器直接传递被装饰的函数的参数。
>
> 在讲解解决方法之前，让我们先做一个小小的回顾：
>
> ```python
> # Decorators are ORDINARY functions
> def my_decorator(func):
>     print("I am an ordinary function")
>     def wrapper():
>         print("I am function returned by the decorator")
>         func()
>     return wrapper
>
> # Therefore, you can call it without any "@"
>
> def lazy_function():
>     print("zzzzzzzz")
>
> decorated_function = my_decorator(lazy_function)
> #outputs: I am an ordinary function
>
> # It outputs "I am an ordinary function", because that’s just what you do:
> # calling a function. Nothing magic.
>
> @my_decorator
> def lazy_function():
>     print("zzzzzzzz")
>
> #outputs: I am an ordinary function
> ```
>
> 上述两者完全相同，都是调用了`my_decorator`。所以当你`@my_decorator`，你是在告诉Python的调用被变量`my_decorator` 标记的函数。
>
> 这一点很重要！你可以用标签直接指明装饰器，或者不这样。
>
> 让我们再深入一点。
>
> ```python
> def decorator_maker():
>
>     print("I make decorators! I am executed only once: "
>           "when you make me create a decorator.")
>
>     def my_decorator(func):
>
>         print("I am a decorator! I am executed only when you decorate a function.")
>
>         def wrapped():
>             print("I am the wrapper around the decorated function. "
>                   "I am called when you call the decorated function. "
>                   "As the wrapper, I return the RESULT of the decorated function.")
>             return func()
>
>         print("As the decorator, I return the wrapped function.")
>
>         return wrapped
>
>     print("As a decorator maker, I return a decorator")
>     return my_decorator
>
> # 让我们创建一个装饰器
> new_decorator = decorator_maker()       
> #outputs:
> #I make decorators! I am executed only once: when you make me create a decorator.
> #As a decorator maker, I return a decorator
>
> # 接下来, 我们来装饰函数
> def decorated_function():
>     print("I am the decorated function.")
>
> decorated_function = new_decorator(decorated_function)
> #outputs:
> #I am a decorator! I am executed only when you decorate a function.
> #As the decorator, I return the wrapped function
>
> # 调用函数
> decorated_function()
> #outputs:
> #I am the wrapper around the decorated function. I am called when you call the decorated function.
> #As the wrapper, I return the RESULT of the decorated function.
> #I am the decorated function.
> ```
>
> 这里没有什么可惊奇的。
>
> 跳过所有繁琐的中间变量，以下与上述方法完全一样。
>
> ```python
> def decorated_function():
>     print("I am the decorated function.")
> decorated_function = decorator_maker()(decorated_function)
> #outputs:
> #I make decorators! I am executed only once: when you make me create a decorator.
> #As a decorator maker, I return a decorator
> #I am a decorator! I am executed only when you decorate a function.
> #As the decorator, I return the wrapped function.
>
> # Finally:
> decorated_function()    
> #outputs:
> #I am the wrapper around the decorated function. I am called when you call the decorated function.
> #As the wrapper, I return the RESULT of the decorated function.
> #I am the decorated function.
> ```
>
> 可以更精简一些
>
> ```python
> @decorator_maker()
> def decorated_function():
>     print("I am the decorated function.")
> #outputs:
> #I make decorators! I am executed only once: when you make me create a decorator.
> #As a decorator maker, I return a decorator
> #I am a decorator! I am executed only when you decorate a function.
> #As the decorator, I return the wrapped function.
>
> #Eventually: 
> decorated_function()    
> #outputs:
> #I am the wrapper around the decorated function. I am called when you call the decorated function.
> #As the wrapper, I return the RESULT of the decorated function.
> #I am the decorated function.
> ```
>
> 嘿，你看到了吗？我们通过`“ @”` 语法使用了函数。
>
> 所以，回到带参的装饰器。如果我们可以用函数在运行时生成装饰器，我们就能够向那个函数传递参数了，对吧？
>
> ```python
> def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
>
>     print("I make decorators! And I accept arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))
>
>     def my_decorator(func):
>         # 此处传递参数的能力, 得益于闭包的性质
>         # 如果你不习惯闭包, 你可以假设它是ok的, 或者看一下这篇文章:
>         # or read: https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
>         print("I am the decorator. Somehow you passed me arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))
>
>          # 不要混淆了装饰器参数和函数参数!
>         def wrapped(function_arg1, function_arg2) :
>             print("I am the wrapper around the decorated function.\n"
>                   "I can access all the variables\n"
>                   "\t- from the decorator: {0} {1}\n"
>                   "\t- from the function call: {2} {3}\n"
>                   "Then I can pass them to the decorated function"
>                   .format(decorator_arg1, decorator_arg2,
>                           function_arg1, function_arg2))
>             return func(function_arg1, function_arg2)
>
>         return wrapped
>
>     return my_decorator
>
> @decorator_maker_with_arguments("Leonard", "Sheldon")
> def decorated_function_with_arguments(function_arg1, function_arg2):
>     print("I am the decorated function and only knows about my arguments: {0}"
>            " {1}".format(function_arg1, function_arg2))
>
> decorated_function_with_arguments("Rajesh", "Howard")
> #outputs:
> #I make decorators! And I accept arguments: Leonard Sheldon
> #I am the decorator. Somehow you passed me arguments: Leonard Sheldon
> #I am the wrapper around the decorated function. 
> #I can access all the variables 
> #   - from the decorator: Leonard Sheldon 
> #   - from the function call: Rajesh Howard 
> #Then I can pass them to the decorated function
> #I am the decorated function and only knows about my arguments: Rajesh Howard
>
> ```
>
> 这就是带参的装饰器了。参数也可以设置成变量：
>
> ```python
> c1 = "Penny"
> c2 = "Leslie"
>
> @decorator_maker_with_arguments("Leonard", c1)
> def decorated_function_with_arguments(function_arg1, function_arg2):
>     print("I am the decorated function and only knows about my arguments:"
>            " {0} {1}".format(function_arg1, function_arg2))
>
> decorated_function_with_arguments(c2, "Howard")
> #outputs:
> #I make decorators! And I accept arguments: Leonard Penny
> #I am the decorator. Somehow you passed me arguments: Leonard Penny
> #I am the wrapper around the decorated function. 
> #I can access all the variables 
> #   - from the decorator: Leonard Penny 
> #   - from the function call: Leslie Howard 
> #Then I can pass them to the decorated function
> #I am the decorated function and only knows about my arguments: Leslie Howard
> ```
>
> 如你所见，使用该技巧，你可以像任何（普通）函数一样向装饰器传递参数。如果你愿意，你甚至可以使用`*args`, `**kwargs`。但是，请记住装饰器只能被调用1次，即在导入脚本的时候。之后你就不能动态地设置参数了。当你“进口X”时，函数已经被装饰了，你不能再做任何修改。

### 9. 让我们实践一下：写一个装饰器来装饰另一个装饰器

>  作为奖励，我会给你一段代码来让任意装饰器接受任意参数。然后，为了接受参数，我们使用另一个函数来创建我们的装饰器。我们包装这个装饰器。
>
>  ```python
>  def decorator_with_args(decorator_to_enhance):
>     """ 
>     This function is supposed to be used as a decorator.
>     It must decorate an other function, that is intended to be used as a decorator.
>     Take a cup of coffee.
>     It will allow any decorator to accept an arbitrary number of arguments,
>     saving you the headache to remember how to do that every time.
>     """
>
>     # We use the same trick we did to pass arguments
>     def decorator_maker(*args, **kwargs):
>
>         # We create on the fly a decorator that accepts only a function
>         # but keeps the passed arguments from the maker.
>         def decorator_wrapper(func):
>
>             # We return the result of the original decorator, which, after all, 
>             # IS JUST AN ORDINARY FUNCTION (which returns a function).
>             # Only pitfall: the decorator must have this specific signature or it won't work:
>             return decorator_to_enhance(func, *args, **kwargs)
>
>         return decorator_wrapper
>
>     return decorator_maker
>  ```
>
>  你可以这样使用：
>
>  ```python
>  # You create the function you will use as a decorator. And stick a decorator on it :-)
>  # Don't forget, the signature is "decorator(func, *args, **kwargs)"
>  @decorator_with_args 
>  def decorated_decorator(func, *args, **kwargs): 
>     def wrapper(function_arg1, function_arg2):
>         print "Decorated with", args, kwargs
>         return func(function_arg1, function_arg2)
>     return wrapper
>
>  # Then you decorate the functions you wish with your brand new decorated decorator.
>
>  @decorated_decorator(42, 404, 1024)
>  def decorated_function(function_arg1, function_arg2):
>     print "Hello", function_arg1, function_arg2
>
>  decorated_function("Universe and", "everything")
>  #outputs:
>  #Decorated with (42, 404, 1024) {}
>  #Hello Universe and everything
>
>  # Whoooot!
>  ```
>
>  我知道，你会有这种感觉，就像一个家伙对你说：“在理解递归之前，你先要理解递归”。现在，你还会感觉你掌握这写了吗？

### 10.最佳实践

> *  需要Python 2.4及以上的版本
> *  装饰器会让函数调用变慢。谨记。
> *  你不能取消装饰器。尽管有一些方法可以创建可以移除的装饰器，但没人这么干。
> *  被装饰器包装的函数，这会让你很难调试。
>
> Python 2.5解决了这个调试问题，通过`functools`模块里的`functools.wraps`，你可以复制被装饰的函数名称，模块和文档。有趣的是，`functools.wraps`也是一个装饰器。
>
> ```markdown
> 这个问题指的是;
>
>
> 错误的函数签名和文档
> 装饰器装饰过的函数看上去名字没变，其实已经变了。
> #--------------
> #装饰器
> def logging(func):
>     def wrapper(*args, **kwargs):
>         """print log before a function."""
>         print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
>         return func(*args, **kwargs)
>     return wrapper
>
> @logging
> def say(something):
>     """say something"""
>     print "say {}!".format(something)
>
> print say.__name__  # wrapper
> #-------------
> 为什么会这样呢？只要你想想装饰器的语法糖@代替的东西就明白了。@等同于这样的写法。
> `say = logging(say)`
> logging其实返回的函数名字刚好是wrapper，那么上面的这个语句刚好就是把这个结果赋值给say，say的__name__自然也就是wrapper了，不仅仅是name，其他属性也都是来自wrapper，比如doc，source等等。
>
>
> 使用标准库里的functools.wraps，可以基本解决这个问题。
> ​```python
> from functools import wraps
>
> def logging(func):
>     @wraps(func)
>     def wrapper(*args, **kwargs):
>         """print log before a function."""
>         print "[DEBUG] {}: enter {}()".format(datetime.now(), func.__name__)
>         return func(*args, **kwargs)
>     return wrapper
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
> ```python
> # For debugging, the stacktrace prints you the function __name__
> def foo():
>     print "foo"
>
> print foo.__name__
> #outputs: foo
>
> # With a decorator, it gets messy    
> def bar(func):
>     def wrapper():
>         print "bar"
>         return func()
>     return wrapper
>
> @bar
> def foo():
>     print "foo"
>
> print foo.__name__
> #outputs: wrapper
>
> # "functools" can help for that
>
> import functools
>
> def bar(func):
>     # We say that "wrapper", is wrapping "func"
>     # and the magic begins
>     @functools.wraps(func)
>     def wrapper():
>         print "bar"
>         return func()
>     return wrapper
>
> @bar
> def foo():
>     print "foo"
>
> print foo.__name__
> #outputs: foo
> ```

### 11.装饰器有什么用？

> 现在的问题是：我能用装饰器做什么？看起来很酷很强大，但是实践的例子更有用。这有1000种可能性。经典的用法是继承一个外部函数的行为（你不能修改它）或者用于调试（你不能修改因为它是临时的）。你可以使用它来扩展N多函数，又不用每次重写，遵循DRY原则，例如：
>
> ```python
> def benchmark(func):
>     """
>     A decorator that prints the time a function takes
>     to execute.
>     """
>     import time
>     def wrapper(*args, **kwargs):
>         t = time.clock()
>         res = func(*args, **kwargs)
>         print func.__name__, time.clock()-t
>         return res
>     return wrapper
>
>
> def logging(func):
>     """
>     A decorator that logs the activity of the script.
>     (it actually just prints it, but it could be logging!)
>     """
>     def wrapper(*args, **kwargs):
>         res = func(*args, **kwargs)
>         print func.__name__, args, kwargs
>         return res
>     return wrapper
>
>
> def counter(func):
>     """
>     A decorator that counts and prints the number of times a function has been executed
>     """
>     def wrapper(*args, **kwargs):
>         wrapper.count = wrapper.count + 1
>         res = func(*args, **kwargs)
>         print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
>         return res
>     wrapper.count = 0
>     return wrapper
>
> @counter
> @benchmark
> @logging
> def reverse_string(string):
>     return str(reversed(string))
>
> print reverse_string("Able was I ere I saw Elba")
> print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")
>
> #outputs:
> #reverse_string ('Able was I ere I saw Elba',) {}
> #wrapper 0.0
> #wrapper has been used: 1x 
> #ablE was I ere I saw elbA
> #reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
> #wrapper 0.0
> #wrapper has been used: 2x
> #!amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A
> ```
>
> 当然装饰器最好的用途就是避免重复，DRY.
>
> ```python
> @counter
> @benchmark
> @logging
> def get_random_futurama_quote():
>     import httplib
>     conn = httplib.HTTPConnection("slashdot.org:80")
>     conn.request("HEAD", "/index.html")
>     for key, value in conn.getresponse().getheaders():
>         if key.startswith("x-b") or key.startswith("x-f"):
>             return value
>     return "No, I'm ... doesn't!"
>
> print get_random_futurama_quote()
> print get_random_futurama_quote()
>
> #outputs:
> #get_random_futurama_quote () {}
> #wrapper 0.02
> #wrapper has been used: 1x
> #The laws of science be a harsh mistress.
> #get_random_futurama_quote () {}
> #wrapper 0.01
> #wrapper has been used: 2x
> #Curse you, merciful Poseidon!
> ```
>
> Python提供了很多装饰器：`property`,`staticmethod`,等等。Django使用装饰器来管理缓存和视图权限。Twisted来做异步函数调用。这有很大的应用场景。