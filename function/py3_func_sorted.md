### `sorted` `sort`

#### 排序算法

> 排序是程序中经常使用到的算法,鲁润使用冒泡排序还是快速排序,排序的核心就是比较2个元素,如果是数字,我们可以通过直接比较,但是如果是字符串或者是2个字典,直接比较在数学上的大小,没有意义,因此,比较的过程必须通过函数抽象出来.
>
> Python的内置的`sorted()`函数可以对`list`进行排序,`list`也有一个属性和方法`sort()`同样具有对列表排序的效果,但是作用域**`IN　PLACE` ** ,侧重于本体做出了修改
>
> ```python
> sorted(iterable, key=None, reverse=False)
>     Return a new list containing all items from the iterable in ascending order.
>     
>     A custom key function can be supplied to customise the sort order, and the
>     reverse flag can be set to request the result in descending order.
>     
>     
>     
> sort(...)
>     L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
>
> ```
>
> ```python
> #默认是升序排列
> In [82]: sorted([36,5,-12,9,-21])
> Out[82]: [-21, -12, 5, 9, 36
> ```
>
> 此外,`sorted()` 函数还是一个高阶函数,它可以接受一个`key` 函数来控制实现自定义排序,比如,按照绝对值排序:
>
> ```python
> In [83]: sorted([36,5,-12,9,-21],key=abs)
> Out[83]: [5, 9, -12, -21, 36]
>
> ```
>
> `key` 指定的函数将作用于`list`的每一个元素上,并根据`key` 函数返回的结果进行排序.对比图如下.
>
> ```mermaid
> graph TD
> id1["原列表,可迭代序列"]
> id2["[36,5,-12,9,-21]"]
> id3["包含的每个元素"]
>
> id4((36))
> id5((5))
> id6(("-12"))
> id7((9))
> id8(("-21"))
>
> id9(36) 
> id10(5)
> id11(12)
> id12(9)
> id13(21)
>
> id14(5)
> id15(9)
> id16(12)
> id17(21)
> id18(36)
>
> id19((5))
> id20((9))
> id21(("-12"))
> id22(("-21"))
> id23((36))
>
> id1 --> id2
> id2 --> id3
> id3 --> id4
> id3 --> id5
> id3 --> id6
> id3 --> id7
> id3 --> id8
>
> id4 --> |"abs()"| id9
> id5 --> |"abs()"|id10
> id6 --> |"abs()"|id11
> id7 --> |"abs()"|id12
> id8 --> |"abs()"|id13
>
> id9 -.-> |"sort()"| id14
> id10  -.-> |"sort()"| id15
> id11  -.-> |"sort()"| id16
> id12 -.-> |"sort()"| id17
> id13 -.-> |"sort()"| id18
>
> id14 --> |"屏显"| id19
> id15  --> |"屏显"| id20
> id16  --> |"屏显"| id21
> id17  --> |"屏显"| id22
> id18  --> |"屏显"| id23
>
>
> ```
>
> 对于列表中的字符串:会默认按照`ASCII` 表中字母的顺序进行排序
>
> ```python
> In [87]: sorted(['bob','about','Zoo','Credit'])
> Out[87]: ['Credit', 'Zoo', 'about', 'bob']
>
> ```
>
> 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
>
> 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
>
> ```python
> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
> ['about', 'bob', 'Credit', 'Zoo']
> ```
>
> 要进行反向排序，不必改动key函数，可以传入第三个参数`reverse=True`：
>
> ```python
> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
>
> ['Zoo', 'Credit', 'bob', 'about']
>
> ```
>
> 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。
>
> 对于列表中的字典,假如默认按照年龄排序
>
> ```python
> In [95]: f 
> Out[95]: [{'name': 'abc', 'age': 21}, {'name': 'abcd', 'age': 22}]
>
> In [96]: def foo(x):
>    ....:     return x['age']
>    ....: 
>
> In [97]: sorted(f,key=foo)
> Out[97]: [{'name': 'abc', 'age': 21}, {'name': 'abcd', 'age': 22}]
> ```
>
> 简洁一点的还可以写成
>
> ```python'
> In [98]: sorted(f,key= lambda x: x['age'])
> Out[98]: [{'name': 'abc', 'age': 21}, {'name': 'abcd', 'age': 22}]
> ```

#### 关键点

> 使用sorted的关键点就在于能不能为sorted 实现一个映射函数