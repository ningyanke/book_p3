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