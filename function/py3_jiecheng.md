### 综合运用`reduce`,`map`,`filter`,`lambda`

#### 1.计算 `5! + 4! + 3! + 2! + 1!`

> 要计算阶乘想加,可以观看阶乘的结构;
>
> ```python
>  """
>  5! 5 * 4 * 3 * 2 * 1
>  4!     4 * 3 * 2 * 1
>  3!         3 * 2 * 1 
>  2!             2 * 1 
>  1!                 1 
>  """
> ```
>
> 可以简单的使用`map()` 函数,作用于列表中每个元素,抽象得到阶乘的结果:
>
> 最后使用`reduce()`函数,作用于列表,使列表中的每个元素依次递加,最后输出结果.
>
> ```python
> from functools import reduce
>
>
> # 定义一个阶乘函数
> def _power(x):
>     result = 1  #哨兵法
>     while x >= 1:
>         result = result * x
>         x -= 1
>     return result
>
>
> a = list(map(_power, [1, 2, 3, 4, 5]))
> print(a)
>
>
> # 定义相加函数
>
> def _foo(x, y):
>     return x + y
>
>
> b = reduce(_foo, a)
>
> print(b)
> ```
>
> 当然也可以简化的使用`lambda` 函数
>
> `lambda x, y:x +y ` 
>
> 用一个表达式表示
>
> ```python
> print(reduce(lambda x ,y: x +y , map(_power,[1,2,3,4,5])))
> ```
>
> 

#### 2.求100以内的质数

> ```python
> def foo(x):
>     for i in range(1, x + 1):
>         if x % i == 0 and i != 1 and i != x:
>             return x
>
>
> aa = list(filter(foo, [x for x in range(1, 101)]))
>
> print(aa)
>
>
> def _foo1(x):
>     if x not in aa:
>         return x
>
>
> bb = list(filter(_foo1, [x for x in range(2, 101)]))
>
> print("bb", bb)
> ```
>
> 

