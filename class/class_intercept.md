### 属性拦截

> 拦截(intercept)对象的所有特性是可能的,当访问某个类或者是实例,如果不存在,就会异常,对于异常也总是要处理的,当然,这个也可以理解为定义某些私有的属性.
>
> * `__getattr__(self, name)`: 
>
>   ``` markdown
>    当用户访问一个根本不存在(或者暂时不存在) 的属性时，你可以通过这个魔法方法来定义类的行为。这个可以用于捕捉错误的拼写并且给出指引，使用废弃属性时给出警告（如果你愿意，仍然可以计算并且返回该属性），以及灵活地处理AttributeError`。只有当试图访问不存在的属性时它才会被调用，所以这不能算是一个真正的封装的办法。
>   ```
>
> * `__setattr__(self, name, value)` 
>   ```markdown
>     和 __getattr__ 不同， __setattr__ 可以用于真正意义上的封装。它允许你自定义某个属性的赋值行为，不管这个属性存在与否，也就是说你可以对任意属性的任何变化都定义自己的规则。然后，一定要小心使用 __setattr__ ，这个列表最后的例子中会有所展示。
>   ```
>
>  * `__delattr__(self, name)`
>
>    ```markdown
>     和 __getattr__ 不同， __setattr__ 可以用于真正意义上的封装。它允许你自定义某个属性的赋值行为，不管这个属性存在与否，也就是说你可以对任意属性的任何变化都定义自己的规则。然后，一定要小心使用 __setattr__ ，这个列表最后的例子中会有所展示。
>    ```
>
>  * `__getattribute__(self, name)`
>
>  * ​
>
>    ```markdown
>     __getattribute__ 允许你自定义属性被访问时的行为，__getattribute__ 基本上可以替代 __getattr__ 。如果类也定义__getattr__()，后者将不会被调用，除非__getattribute__()明确地调用它或提出一个 AttributeError。为了避免无线循环,通常使用 
>     return object.__getattribute__(self, name) 作为返回值.
>    ```
>
>
> 简单的说他们有如下的调用:
>
> | 魔法方法                           | 什么时候调用              | 解释                                     |
> | ------------------------------ | ------------------- | -------------------------------------- |
> | `__getattr__(self, name)`      | `self.name`         | 当属性`name` 被访问,同时`name` 不<br>存在,被自动调用   |
> | `__setattr__(self,name,value)` | `self.name = value` | 当给属性`name` 赋值时,调用此方法                   |
> | `__delattr__(self,name)`       | `del self.name`     | 删除属性`name` 被调用                         |
> | `__getattribute__`             | `self.name`         | 当属性`name` 被访问时自动调用,无论<br>属性`name` 是否存在 |
>
> ** **

#### 1.`object.__getattr__(self, name)` 

> 如果某个类定义了` __getattr__() `方法，Python 将只在正常的位置查询属性时才会调用它。如果实例 x 定义了属性 color， x.color 将 不会 调用``x.__getattr__('color')；`而只会返回 x.color 已定义好的值.
>
> ```python
> class Dynamo(object):
>     def __getattr__(self, key):
>         if key == 'color':         
>             return 'PapayaWhip'
>         else:
>             raise AttributeError   
>
> >>> dyn = Dynamo()
> >>> dyn.color                      
> 'PapayaWhip'
> >>> dyn.color = 'LemonChiffon'
> >>> dyn.color                 
> ```
>
> 显式的定义了color之后,调用的就是`__dict__` 中的值,

#### 2.`object.__getattribute__(self, name)`  

> 自定义`object.__getattribute__` 很容易产生无限递归,
>
> ```python
> class B:
>     def __getattribute__(self, name):
>         print(" you are useing getattribute")
>         return object.__getattribute__(self, name)
>     	# return self.__dict__[name]
> ```
>
> 假如我们使用`self.__dict__[name]` 这样的方式,就是访问`self.__dict__` ,而`__getattribute__` 是拦截所有特性的访问,也拦截对`__dict__` 的访问,这样就会递归的调用`__getattribute__` 直到程序崩溃,
>
> 所以,访问`__getattibute__`中与`self` 相关的属性时,使用超类的`__getattribute__` 方法(super),对于python3 来说,所有类都是新式类,`object.__getattribute__(self, name)` ,实现的是同样的效果.

####  3.不重写`object.__getattribute__(self, name)`

> 对于一个普通定义的类,我们没有重写`__getattribute__` ,默认全部继承自`object ` 类,它的`__getattribute` 中默认返回的是`__dict__` 中的值,也就是实例`A.x`,会先去寻找`__getattribute__` ,但是返回项目是 `object.__getattribute__(self,name)` ,转向了`object.__dict__[name]`
>
> ```python
> In [1]: class Test:
>    ...:     name = 'Jack'
>    ...:     def __init__(self,k):
>    ...:         self.age = k
>    ...:
>
> In [2]: Test.name == Test.__getattribute__(Test,'name')
> Out[2]: True
>
> In [3]: Test.name == Test.__dict__['name']
> Out[3]: True
>
> In [4]: Test.__dict__['name'] == Test.__getattribute__(Test,'name')
> Out[4]: True
>
>     
> In [6]: Test.__dict__["name"] == object.__getattribute__(Test,'name')
> Out[6]: True
> ```

#### 4.`__getattr__` 和`__getattribute__`比较

> 让我们看看两个`__getattr__`和`__getattribute__`魔术方法的一些简单的例子。
>
>  ###### `__getattr__`
>
> `__getattr__`只要您请求尚未定义的属性，Python就会调用该 方法。
>
> 在下面的例子中，我的类Count没有`__getattr__`方法。现在,当我试图同时访问`obj1.mymin`和`obj1.mymax`属性，一切工作正常。但是，当我尝试访问`obj1.mycurrent` 属性 - Python给我`AttributeError: 'Count' object has no attribute 'mycurrent'`
>
> ```python
> class Count():
>     def __init__(self,mymin,mymax):
>         self.mymin=mymin
>         self.mymax=mymax
>
> obj1 = Count(1,10)
> print(obj1.mymin)
> print(obj1.mymax)
> print(obj1.mycurrent)  --> AttributeError: 'Count' object has no attribute 'mycurrent'
> ```
>
> 
>
> 现在我的类Count有 `__getattr__`方法。现在，当我尝试访问 ` obj1.mycurrent` 属性,会创建一个新的值.在我的示例中，每当我尝试调用一个不存在的属性时，python都会创建该属性并将其设置为整数值0。
>
> ```python
> class Count:
>     def __init__(self,mymin,mymax):
>         self.mymin=mymin
>         self.mymax=mymax    
>     
>     def __getattr__(self, item):
>         self.__dict__[item]=0
>         return 0
>
> obj1 = Count(1,10)
> print(obj1.mymin)
> print(obj1.mymax)
> print(obj1.mycurrent1)
> ```
>
> ##### `__getattribute__`
>
> 现在让我们看看这个`__getattribute__` 方法。如果你`__getattribute__`的类中有 方法，python会为每个属性调用这个方法，不管它是否存在。那么为什么我们需要`__getattribute__`方法？一个很好的理由是，您可以防止访问属性并使其更安全，如以下示例所示。
>
> 每当有人试图访问我的属性，以子字符串开始“cur” python引发AttributeError异常。否则，它返回该属性。
>
>  ```python
> class Count:
>
>     def __init__(self,mymin,mymax):
>         self.mymin=mymin
>         self.mymax=mymax
>         self.current=None
>     
>     def __getattribute__(self, item):
>         if item.startswith('cur'):
>             raise AttributeError
>         return object.__getattribute__(self,item) 
>         # or you can use ---return super().__getattribute__(item)
>
> obj1 = Count(1,10)
> print(obj1.mymin)
> print(obj1.mymax)
> print(obj1.current)
>
>  ```
>
>
> 重要：为了避免__getattribute__方法中的无限递归，它的实现应该总是调用具有相同名字的基类方法来访问它所需要的任何属性。例如：`object.__getattribute__(self, name)`或` super().__getattribute__(item)`而不是`self.__dict__[item]`
>
> 重要
>
> 如果你的类同时包含`getattr`和`getattribute`魔术方法，那么 ` __getattribute__`首先调用它。但是，如果`  __getattribute__`引发  AttributeError异常，则该异常将被忽略，`__getattr__`方法将被调用。看下面的例子：
>
>  ```python
> class Count(object):
>
>     def __init__(self,mymin,mymax):
>         self.mymin=mymin
>         self.mymax=mymax
>         self.current=None
>     
>     def __getattr__(self, item):
>             self.__dict__[item]=0
>             return 0
>     
>     def __getattribute__(self, item):
>         if item.startswith('cur'):
>             raise AttributeError
>         return object.__getattribute__(self,item)
>         # or you can use ---return super().__getattribute__(item)
>         # note this class subclass object
>
> obj1 = Count(1,10)
> print(obj1.mymin)
> print(obj1.mymax)
> print(obj1.current)
>  ```