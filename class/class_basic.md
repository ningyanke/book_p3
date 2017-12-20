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

> 

#### 3.运算符重载

#### 4.通过子类定制行为

#### 5.定制构造函数

#### 6.使用内省工具

#### 7.把对象存储到数据库中