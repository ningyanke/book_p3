###### `break`和`continue`语句及循环中的`else`子句
>循环控制语句
>
>| 控制语句 | 描述 |
>|--------|--------|
>|break |在语句执行过程中终止循环，并且跳出整个循环体,任何对应的else语句都将不执行 |
>|continue|在语句执行过程中终止本次循环，并且跳出该次循环，执行下一次循环|
>|pass|pass是空语句，为了保持程序结构的完整性|
>```python
>"""
>break终止循环语句，并且跳出循环语句块
>"""
>for letter in 'Runoob':M
>    if letter == 'b':
>        break
>    print("当前字母为:",letter)
>>>
>var = 10
>while var > 0:
>    print("当前变量值为：",var)
>    var -= 1
>    if var == 5:
>        break
>print("good bye")
>"""
>当前字母为: R
>当前字母为: u
>当前字母为: n
>当前字母为: o
>当前字母为: o
>当前变量值为： 10
>当前变量值为： 9
>当前变量值为： 8
>当前变量值为： 7
>当前变量值为： 6
>跳出了整个循环体，后面的没有再次执行了
>"""
>#continue跳出本次循环，执行下次循环
>>>
>for letter in 'Runoob':  # 第一个实例
>    if letter == 'o':  # 字母为 o 时跳过输出
>        continue
>    print('当前字母 :', letter)
>>>
>var = 10  # 第二个实例
>while var > 0:
>    var = var - 1
>    if var == 5:  # 变量为 5 时跳过输出
>        continue
>    print('当前变量值 :', var)
>print("Good bye!")
>'''
>当前字母 : R
>当前字母 : u
>当前字母 : n
>当前字母 : b
>当前变量值 : 9
>当前变量值 : 8
>当前变量值 : 7
>当前变量值 : 6
>当前变量值 : 4
>当前变量值 : 3
>当前变量值 : 2
>当前变量值 : 1
>当前变量值 : 0
>跳出了本次循环，执行了下次循环
>'''
>```
