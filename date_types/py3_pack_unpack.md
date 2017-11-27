###Unpacking---sequence 



#### 1. 解压序列赋值给多个变量

>任何的序列(或者说可迭代对象)都可以通过一个简单的赋值语句解压并赋值给多个变量，唯一的前提就是变量的数量必须跟序列元素的数量是一直的
>
>```python
>In [28]: p = (4,5)
> 
>In [29]: x, y = p 
> 
>In [30]: x 
>Out[30]: 4
> 
>In [31]: y 
>Out[31]: 5
> 
>In [32]: data = ["ACME",50,91.1,[1,2,3]]
>In [33]: a, b, c, d  = data
> 
>In [34]: print(a,b,c,d)
>ACME 50 91.1 [1, 2, 3]
> 
>In [35]: a,b,c,(num1,num2,num3) = data
> 
>In [36]: print(a,b,c,(num1,num2,num3))
>ACME 50 91.1 (1, 2, 3)
>
>#如果变量个数和序列元素的个数不匹配，会产生一个异常
>```

####  2. 解压可迭代对象赋值给多个变量

>python的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期末的时候，你想统计下家庭作业的平均成绩，但是要排除掉第一个和最后一个分数，如果只有四个分数，你可能直接去简单的手动赋值，但是如果有24个呢？这个时候星号表达式就派上用场了.
>
>```python
>def drop_fist_last(grades):
>  first, *middle, last = grades
>  return avg(middle)
>```
>
>另外的情况，假如你有一些用户的记录列表，每条记录包含一个名字，邮件，接着是不固定的电话号码，你可以像下面一样分解这个记录.
>
>```python
>In [37]: record = ('Dave','dave@example.com','7-77','6-66')
>In [38]: name,email,*phone_number = record
>In [39]: name
>Out[39]: 'Dave'
>In [40]: email
>Out[40]: 'dave@example.com'
>In [41]: phone_number
>Out[41]: ['7-77', '6-66']
>```
>
>注意： 解压出来的永远是一个` list `列表，变量的类型是列表类型

##### 3. PEP-3132的解释

> 解压可迭代对象赋值给多个变量，也就是sequence unpacking 用于解出一个列表，也就是，变量的类型永远是一个列表。这个主要来源于Python官方的`PEP-3132`
>
> > ```python
> > This PEP proposes a change to iterable unpacking syntax, allowing to specify a “catch-all” name which will be assigned a list of all items not assigned to a “regular” name.
> > ```
>
> 翻译成中文就是：这个提案提议对可迭代对象解包语法进行修改，允许指定一个**“catch-all”**（我理解为**“通吃”**）名字，这个名字将在**“常规”**(**“regular”**)名字被赋值后接收所有剩下的元素。
>
> 一个示例胜过千言:
>
> ```python
> >>> a, *b, c = range(5) 
> >>> a 
> 0 
> >>> c 
> 4 
> >>> b 
> [1, 2, 3]
> ```
>
> 在提案的Rationale 部分，文章提到新的语法让以前类似first, rest = seq[0], seq[1:]式子对序列(sequence)的拆解操作更加简洁，甚至可能更高效。那么，如果用新的语法，这个式子可以这么写:first, *rest = seq
>
>  在Specification 部分，文章指出一个出现在简单赋值式子左边的元组(tuple)或列表(list)最多只能包含一个带星号(*)的表达式(文章把除星号表达式之外的表达式称为强制(mandatory)表达式)。星号表达式将在强制表达式被赋值完之后接收剩下的元素，星号表达式可能没有接收到元素，这时候它是一个空的列表。
>
>  如果seq是一个有至少3个元素的可切片的序列，以下3个赋值操作都是等价的：
>
> ```python
> a, b, c = seq[0], list(seq[1:-1]), seq[-1] 
> a, *b, c = seq 
> [a, *b, c] = seq
> ```
>
> 星号表达式只能出现在元组或者列表中，单独出现在简单赋值表达式的左边会出现错误，例如*a = range(5)，*a, = range(5)或[*a] = range(5)则是对的。而且在简单赋值式子左边出现的每一个强制表达式都要确保被赋值，如果式子右边的元素不够，也会导致错误。
>
>  这个提案也适用于在隐式赋值上下文中的元组，例如在for语句:
>
> ```python
> for a, *b in [(1, 2, 3), (4, 5, 6, 7)]:
> print(b)
> #结果会输出:
> [2, 3] 
> [5, 6, 7]
> ```
>
> 文章的剩下部分超出了常用范围，就不讨论了。” name.@�<�S