## 类基础

### `class object `, `instance object`

> - 类对象是实例对象工厂,类用于创建多个实例对象,
> - 类对象定义了默认行为,实例对象是程序处理的实际对象,
> - 类对象和实例对象各自拥有命名空间,
> - 类对象来自与语句(class) ,实例对象来自于[调用called](./class_callable.md)
> - 实例对象继承类对象的属性

### 创建一个简单类

> ```python
> # class 语句用于定义类
> class FirstClass:
>     def setdata(self, value):
>         self.value = value
>     def display(self):
>         return self.value
>
> # called 产生实例对象
> instance_1 = FirstClass()
> instance_2 = FirstClass()
> # 位于类中的函数通常称为方法
> ```
>
> 位于类中的函数通常称为方法(`method`),但是对于类来说,统一都可以称为属性(`Attribute`) ,他们都可以使用
>
> `object.attribute` 的方法访问.
>
> 事实上,类只是一个[**完整的命名空间** ](./class_namespace_tree.md) ,可以根据自己的需要,修改不同的属性

### 类定制

> 类是生成实例的工厂,类可以通过继承来进行深度的类定制,从而编写出类层次.总的来说,有以下核心点:
>
> * 超类列在了类开头的括号中
> * 类从超类中继承属性
> * 实例会继承说有可读取类的属性
> * 每个`object.attrbute` 会开启新的独立搜索
>   * Python会对每个属性去除表达式进行类树的独立搜索,不仅仅包括实例对象,包括类的属性和方法(类的引用),
> * 逻辑的修改是通过创建子类,而不是修改超类
>   * 搜索树层次越低,优先级越高,可以在子类中重新定义超类的属性.
>
> 属性重载
>
> ```python
> class FirstClass:
>     def setdata(self, value):
>         self.value = value
>     def display(self):
>         return self.value
> class SecondClass(FirstClass):
>     def display(self):
>         return  "hello world"
>     
> foo = SecondClass()
> foo.display()
> ```
>

### 构造一个完整的类

#### 目的

> 编写两个类
>
> * `Person`创建并处理关于人员 信息的一个类
> * `Manager` 一个定制的`Person` ,修改了继承的行为
>
> 最后把实例存储在面向对象的数据库 `shelve` 中,并持久化

#### 1.创建实例

##### 编写主类,并测试

> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay
>         
> if __name__ == "__main__":
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,bob.pay)
>     print(sue.name,sue.pay)
> ```

#### 2.添加行为方法

> 实现获取 lastname 并实现人员的涨薪 
>
> 一个硬编码的实现
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay
>         
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     
>     print(bob.name.split(" ")[-1],bob.pay*(1+ 0.1))
>     print(sue.name.split(" ")[-1],sue.pay*(1+ 0.1)) 
> ```
>
> 但是硬编码会带来系统维护上的困难,每次实例化一个人员,都要对其做一次处理,所以,应该实现在类方法中,让每个实例都继承这个方法,进行封装,封装的逻辑就是把操作逻辑包装在界面之后.
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>         
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay
> ```

#### 3.运算符重载

> 现在已经有一个功能相当完备的类和实例,但是追踪对象还是不是很方便,需要手动的接受和打印**单个的属性**,如果能一次显示一个实例的有用信息,那还是不错的,
>
> 可以利用`__str__`进行运算符重载,让打印能有显示更多的信息
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>     
>     # __str__打印对程序员友好
>     def __str__(self):
>         return "[Person:%s,%s]" % (self.name ,self.pay)
>     
>     # __repr__ 打印对程序更友好
>     
>     __repr__ = __str__
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay)
>     print(sue,bob)
> ```

#### 4.通过子类定制行为

> Manager 类,对管理员默认的长薪资会增加 10%
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>     
>     # __str__打印对程序员友好
>     def __str__(self):
>         return "[Person:%s,%s]" % (self.name ,self.pay)
>     
>     # __repr__ 打印对程序更友好
>     
>     __repr__ = __str__
>     
> class Manager(Person):
>     def giveRaise(self,percent, bonus=0.10):
>         # 类方法总是可以在实例中调用,这里相当于生成了一个实例对象
>         return Person.giveRaise(self,(percent + bonus))
>     
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay)
>     print(sue,bob)
>     tom = Manager("Tom Jones",'mgr',50000)
>     tom.giveRaise(0.1)
>     print(tom)
> ```

#### 5.定制构造函数

> 现在代码已经能正常工作了,但是 tom 明明是一个管理者,但是打印出来的效果依然是 Person,普通员工,而且创建对象的时候,必须手动给 Tom 添加上 mgr 标签,但是 Manager 类已经暗示了他是一个管理者,手动添加就有点多余,这已经由类暗示了. 这是因为 Manager 类继承了 Person 类的`__str__`导致的.当然可以在 Manger 添加 `__str__` ,但是这样由超类 Person创建出来的子类都需要修改,所以,还是要修改超类的方法,以便其他子类继承.
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>     
>     # __str__打印对程序员友好
>     def __str__(self):
>         return "[Person:%s,%s]" % (self.name ,self.pay)
>     
>     # __repr__ 打印对程序更友好
>     
>     __repr__ = __str__
>     
> class Manager(Person):
>     def __init__(self,name,pay):
>         #Person.__init__(self,name,'mgr',pay)
>         super(Manager,self).__init__(name,'mgr',pay)
>     
>     def giveRaise(self,percent, bonus=0.10):
>         
>         return Person.giveRaise(self,(percent + bonus))
>     
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay)
>     print(sue,bob)
>     
>     tom = Manager("Tom Jones",50000)
>     tom.giveRaise(0.1)
>     print(tom)
> ```

#### 6.使用内省工具

> 现在类已经完整的展示了基本的OOP,但是还有2个问题应该在使用对象之前解决 
>
> 1.首先,打印　Tom 时,会显示为Person,这是因为 Manager 类继承了 Person 类的**str**导致的.应该尽可能的最确切的(也就是说最低层)的类来显示对象.这样会更准确. 
>
> 2.其次,当然可以在 Manger 添加 **str** ,但是这样由超类 Person创建出来的子类都需要修改,所以,还是要修改超类的方法,以便其他子类继承.这是基于对未来的考虑,增加对代码的维护

##### 特殊类属性

> ```python
> object.__dict__
> A dictionary or other mapping object used to store an object’s (writable) attributes.
>
> instance.__class__
> The class to which a class instance belongs.
>
> class.__bases__
> The tuple of base classes of a class object.
>
> definition.__name__
> The name of the class, function, method, descriptor, or generator instance.
> ```
>
> 对于实例,内置属性`instance.__class__`属性提供了一个从实例到类的继承类的链接,对于类`__bases__`提供了一个对超类的访问,`definition.__name__`能够把类,函数,方法等等的名称打印出来,使用这些内置属性来打印出实例的类的名字,而不是通过硬编码实现 内置的`object.__dict__`,提供了一个字典,保存了实例和类各自的命名空间对象,由于是字典,可以遍历的获取键和值,这样,可以使用这些来打印簇任何实例的属性,而不是通过硬编码实现.
>
> ```python
> class Person:
>     # 根据实际情况,没有工作,即没有收入
>     def __init__(self,name,job=None,pay=0):
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>     
>     # __str__打印对程序员友好
>     def __str__(self):
>         return "[Person:%s,%s]" % (self.name ,self.pay)
>     
>     # __repr__ 打印对程序更友好
>     
>     __repr__ = __str__
>     
> class Manager(Person):
>     def __init__(self,name,pay):
>         #Person.__init__(self,name,'mgr',pay)
>         super(Manager,self).__init__(name,'mgr',pay)
>     
>     def giveRaise(self,percent, bonus=0.10):
>         
>         return Person.giveRaise(self,(percent + bonus))
>     
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay)
>     print(sue,bob)
>     
>     tom = Manager("Tom Jones",50000)
>     tom.giveRaise(0.1)
>     print(tom)
>     
>     # 调用使用 __dict__ ,__class__,__bases__,__name__
>     jacbo = Person("Jacbo Lina")
>     print(jacbo)
>     print(jacbo.__class__)
>     print(jacbo.__class__.__name__)
>     l = [i for i in jacbo.__dict__.keys()]
>     print(l)
> ```

##### 一个通用的显示`__str__` 的工具

> ```python
> class AttrDisplay:
>     """
>     Provides an inheritable print overload method that displays instances whth their class names and 
>     a name=vlaue pair for each attribute stored on the instance itself(but not attrs inherited from 
>     its classes).Can be mixed into any class,and will work on any instance.
>     提供了一个可继承的print重载方法，打印实例时,会打印出实例链接的类的名字,和一个形如 name=value的键值对的字符串,这个
>     字符串是实例所有属性的组合.可以重载在任意的类中,对任何实例都是工作的
>     """
>
>     def gatherAttrs(self):
>         attrs = []
>         for key in sorted(self.__dict__):
>             attrs.append("%s = %s" % (key, getattr(self, key)))
>         return ','.join(attrs)
>
>     def __str__(self):
>         return '[%s : %s]' % (self.__class__.__name__, self.gatherAttrs())
>
>
> if __name__ == '__main__':
>     class TopTest(AttrDisplay):
>         count = 0
>
>         def __init__(self):
>             self.attr1 = TopTest.count
>             self.attr2 = TopTest.count + 1
>             TopTest.count += 2
>
>     class Subtest(TopTest):
>         pass
>
>     X, Y = TopTest(), Subtest()
>     print(X)
>     print(Y)
> ```

##### 工具类的命名考虑

> 这是对于大型的项目而言的,为了是自己命名的属性在和别人命名的属性在继承的时候相互覆盖,可以使用双下滑线 `__x` 这样的形式,使类的属性私有化

##### 类的最终形态

> 在最后,需要对类进行是使用注释来记录所做的工作. 使用功能性文档字符串来描述类,增加代码的可读性,和可维护性.
>
> ```python
> from classtools import AttrDisplay
>
> class Person(AttrDisplay):
>     """
>     create and process person records
>     """
>     
>     def __init__(self,name,job=None,pay=0):# 根据实际情况,没有工作,即没有收入
>         self.name = name 
>         self.job = job
>         self.pay = pay 
>         
>     def lastName(self):
>         return self.name.split(" ")[-1]
>     
>     def giveRaise(self,percent):
>         self.pay = int(self.pay * (1 + percent))
>     
>     # __repr__ 打印对程序更友好
>     
>     __repr__ =  AttrDisplay.__str__
>     
> class Manager(Person):
>     def __init__(self,name,pay):
>         #Person.__init__(self,name,'mgr',pay)
>         super(Manager,self).__init__(name,'mgr',pay)
>     
>     def giveRaise(self,percent, bonus=0.10):
>         
>         return Person.giveRaise(self,(percent + bonus))
>     
>     
> if __name__ == "__main__":
>     # 每个实例拥有自己的命名空间,属性的值可以不同
>     bob = Person('Bob Smith')
>     sue = Person('Sue Jones', job = 'dev', pay = 10000)
>     print(bob.name,sue.name)
>     print(bob.lastName(),sue.lastName())
>     sue.giveRaise(0.10)
>     print(sue.pay)
>     print(sue,bob)
>     
>     tom = Manager("Tom Jones",50000)
>     tom.giveRaise(0.1)
>     print(tom)
>     
>     # 调用使用 __dict__ ,__class__,__bases__,__name__
>     jacbo = Person("Jacbo Lina")
>     print(jacbo)
>     print(jacbo.__class__)
>     print(jacbo.__class__.__name__)
>     l = [i for i in jacbo.__dict__.keys()]
>     print(l)
> ```

#### 7.把对象存储到数据库中

> [shelve](../Built_in_func.md) 简单介绍
>
> 在shelve数据库中存储对象
>
> 新创建一个create.py文件
>
> ```python
> from person import Person, Manager  # load our lassed
>
> bob = Person('Bob Smith')  # re-create objects to be stored
> sue = Person('Sue Jones', job='dev', pay=10000)
> tom = Manager("Tom Jones", pay=500000)
>
> import shelve
>
> db = shelve.open('persondb')  # filename where objects are stored
> for object in (bob, sue, tom):  # use object's attr as key
>     db[object.name] = object  # store object on shelve by key
>
> db.close()  # close after making changes
> ```
>
> 读取
>
> 更新数据库 `updatedb.py`
>
> ```python
> import shelve 
> db=shelve.open("persondb")
> for key in sorted(db):
>     print(key,'=>',db[key])
> sue = db["Sue Jones"]
> sue.giveRaise(0.10)
> db["Sue Jones"] = sue
> db.close()
> ```
>
> 

