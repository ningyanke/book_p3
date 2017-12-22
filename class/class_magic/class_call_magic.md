## 如何调用魔法函数

> 魔法方法和内建函数之间的映射
>
> | 魔法方法                         | 什么时候被调用                          | 解释                      |
> | ---------------------------- | -------------------------------- | ----------------------- |
> | `__new__(cls [,...])`        | `instance = MyClass(arg1, arg2)` | `__new__`在实例创建时调用       |
> | `__init__(self [,...])`      | `instance = MyClass(arg1, arg2)` | `__init__`在实例创建时调用      |
> | `__add__`                    | `instance + object`              | `__add__` 实例出现在 `+` 运算时 |
> | `__str__`                    | `print instance`                 | 打印实例对象时                 |
> | `__sub__`                    | `instance - object`              | `__sub__`实例出现在`-`运算时    |
> | `__del__`                    | `x` 对象被收回时                       | `x` 对象被收回时              |
> | `__call__`                   | `x(*args,**kwargs)`              | 函数被调用                   |
> | `__getattribute__`           | `x.any`                          | 属性获取时                   |
> | `__getattr__`                | `x.undefined`                    | 不存在的                    |
> | `__setattr__`                | `x.any = value`                  | 属性赋值语句                  |
> | `__delattr__`                | `del x.any`                      | 属性被删除                   |
> | `__getitem__`                | `x[key],x[i:j]`                  | 有for循环或迭代器,索引           |
> | `__setitem__`                | `x[key]=value x[i:j]=sequence`   | 索引赋值语句                  |
> | `__delitem__`                | `del x[key], del x[i:j]`         | 索引和切片删除时                |
> | `__len__`                    | `len(x)`                         | 长度                      |
> | `__bool__`                   | `bool(x)`                        | 布尔值测试                   |
> | `__lt__,__gt__`              |                                  |                         |
> | `__le__,__ge__`              |                                  |                         |
> | `__eq__,__ne__`              |                                  |                         |
> | `__iter__,__next__`          |                                  | 迭代环境中,                  |
> | `__contains__`               | `item in x` 任何可迭代                | 成员关系测试                  |
> | `__index__`                  |                                  |                         |
> | `__get__,__set__,__delete__` | `x.attr,x.attr=value,del x.attr` | 描述符                     |
> |                              |                                  |                         |
> |                              |                                  |                         |
> |                              |                                  |                         |
> |                              |                                  |                         |
> |                              |                                  |                         |
> |                              |                                  |                         |
>
> 
>
> 

