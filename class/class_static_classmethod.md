## 类方法,静态方法

> ```python
> class C:
>     @staticmethod
>     def f(arg1, arg2, ...): ...
>
>         
> class C:
>     @classmethod
>     def f(cls, arg1, arg2, ...): ...
> ```
>
> 类方法传入的第一个参数是类本身,如果被子类继承,则传入的是子类本身, 
>
> 静态方法默认是没有传入参数的,
>
> 类方法和静态方法都是绑定到类本体上的.

### 为什么使用特殊方法

> 有时候,程序需要处理与类而不是实例相关的数据,比如要纪录由一个类创建的实例的数目,或者维护当前内存中的一个类的 所有实例的列表,这种类型的信息及其处理与类相关,而非与其实例有关,也就是说,这种信息存储在类自身上,不需要任何实例也可以处理.
>
> 对于这样的任务,一个类之外的简单函数编码往往能够做好,因为他们可以通过类名访问类属性,他们能够访问类数据不需要通过一个实例,然而,要更好的把这样的代码和类联系起来,并且允许这样的过程像通常一样用继承来定制,在类吱声上编写这类函数会更好,为了做好这点,我们需要一个类中的方法不仅不传递而且也不期待传递一个 self 实参参宿.
>
> Python可以通过静态方法来支持这样的目标,用来操作类属性,而不是实例属性.
>
> Python的类方法,通常用在构造函数上,传递给他的第一个参数是类对象本身,不管是通过一个类还是通过实例,都可以调用他们.

### 示例

> 参看示例:
>
> ```python
> class A:
>     def foo(self,x):
>         print("executing foo(%s,%s)"%(self,x))
>
>     @classmethod
>     def class_foo(cls,x):
>         print("executing class_foo(%s,%s)"%(cls,x))
>
>     @staticmethod
>     def static_foo(x):
>         print("executing static_foo(%s)"%x)
>
> a=A()
> ```
>
> 对象实例调用方法的常用方法, a 隐式的作为第一个参数传入
>
> ```python
> a.foo(1)
> # executing foo(<__main__.A object at 0x0000000004B1D5F8>,1)
> ```
>
> 在 `classmethod` 中 ,类对象作为第一个参数传入,而不是self.
>
> 可以从类直接调用类方法,也可以使用实例直接调用类方法,得到的结果是等价的,但是,从类直接调用会更好,因为定义了类方法,这意味着要从类中调用方法,而不是实例
>
> ```python
> a.class_foo(1)
>
> A.class_foo(1)
>
> # executing class_foo(<class '__main__.A'>,1)
> # executing class_foo(<class '__main__.A'>,1)
> ```
>
> 在`staticmethod` 中,self（对象实例）和cls（类）都不会 作为第一个参数隐式传递。除了可以从实例或类调用它们之外，它们的行为与普通函数类似,
>
> `staticmethod` 也支持从实例或类中直接调用,
>
> ```python
> A.static_foo(1)
> a.static_foo(1)
>
> # executing static_foo(1)
> # executing static_foo(1)
> ```
>
> **静态方法用与对类具有某种逻辑连接的函数进行分组**
>
> 在`a.class_foo `中，绑定被到`class_foo` 的不是a，而是A这个类。\
>
> ```python
> print(a.class_foo)
>
> # <bound method type.class_foo of <class '__main__.A'>>
> ```
>
> 尽管这里的`staticmethod`是一个方法`，a.static_foo也`只是返回函数，并且这个函数没有绑定的参数.`static_foo`有1个参数`，a.static_foo`也有1个参数。
>
> ```python
> print(a.static_foo)
>
> # <function static_foo at 0xb7d479cc>
> ```
>
> 当然，当你用甲这个类来调用`static_foo` 的时候，会出现同样的情况。
>
> ```python
> print(A.static_foo)
>
> # <function static_foo at 0xb7d479cc>
> ```
>
> 参看[绑定方法](./class_bound_function.md)

### `classmethod`和`staticmethod` 区别

> 虽然`classmethod`和`staticmethod` 非常相似，但两个实体的使用情况略有不同：`classmethod` 必须具有对类对象的引用作为第一个参数，而`staticmethod` 根本没有参数。
>
> 比如:
>
> ```python
> # classmethod , staticmethod 使用的情况是不同的
> class Date:
>     def __init__(self, day=0, month=0, year=0):
>         self.day = day
>         self.month = month
>         self.year = year
>
>     @classmethod
>     def from_string(cls, date_as_sting):
>         day, month, year = map(int, date_as_sting.split("-"))
>         date1 = cls(day, month, year)
>         return date1
>
>     @staticmethod
>     def is_date_valid(date_as_sting):
>         day, month, year = map(int, date_as_sting.split("-"))
>         return day <= 31 and month <= 12 and year <= 3999
>
>
> date2 = Date.from_string("11-03-2012")
> is_date = Date.is_date_valid("11-03-2012")
> print(date2, is_date)
> ```
>
> #### 他们的使用场景不同
>
> 假设一个类的例子,处理日期信息:
>
> ```python
> class Date:
>     def __init__(self, day=0, month=0, year=0):
>         self.day = day
>         self.month = month
>         self.year = year
> ```
>
> 在这里`__init__` 是一个典型的Python类处理是的初始化方法,它接受一个典型的参数`Instancemethod` .
>
> #### Class Method:
>
> 我们有一些使用`classmethdo`可以很好的完成的任务
>
> 比如:接受一个外部源数据,他们的格式是`dd-mm-yyyy` ,要对这些数据进行处理,我要创建大量的`class Date`的实例,并且还要在 `class Date` 的外部生成一个处理数据格式的函数:
>
> 它的工作流程像这样:
>
> * 定义一个函数,将字符串解析为 day,mount,year 3个变量,或者是一个三元组
> * `Date` 通过将这些值传递给初始化函数,来实例化
>
> 这看起来像:
>
> ```python
> day, month, year = map(int, string_date.split('-'))
> date1 = Date(day, month, year)
> ```
>
> 注意,要有大量的数据要进行相同的处理,也就是要生成大量的处理对象和实例对象,
>
> 在这里,可以利用`classmethod` 对函数进行重构,减少生成的对象,优化内存
>
> ```python
>     @classmethod
>     def from_string(cls, date_as_sting):
>         day, month, year = map(int, date_as_sting.split("-"))
>         date1 = cls(day, month, year)
>         return date1
> ```
>
> 类方法,每次传递参数的时候实例化,是类的方法,而不是实例的方法.
>
> 这样做的优势:
>
> * 我们已经在一个地方实现了日期字符串解析，现在它是可重用的。
> * 封装在这里工作得很好（如果你认为你可以在别处实现字符串解析作为一个单独的函数，这个解决方案更适合OOP范例）
> * cls是持有类本身的对象，而不是类的一个实例。因为如果我们继承我们的Date class，所有的子类也将继承 `from_string`
>
> #### static method
>
> `staticmethod`类似`classmethod` 但不采取任何强制性的参数(如`self , cls`) ,就是一个普通的方法函数,但是它对类具有着某种联系,但是既不对类操作,也不对实例操作.
>
> 比如:
>
> 我们想要以某种方式验证日期字符串。这个任务也被逻辑地绑定到Date我们到目前为止使用的类，但是仍然不需要实例化它。
>
> ```python
>     @staticmethod
>     def is_date_valid(date_as_sting):
>         day, month, year = map(int, date_as_sting.split("-"))
>         return day <= 31 and month <= 12 and year <= 3999
> ```
>
> 所以，从使用中我们可以看到`staticmethod` ，我们没有任何访问类的东西 - 它基本上只是一个函数，在语法上就像一个方法.

 