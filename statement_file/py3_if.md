##### 条件语句`if`
>基本形态
>```python
>if 表达式1:
>    语句
>elif 表达式2:
>    语句
>	.
>	.
>elif 表达式n:
>	语句
>else:
>    语句
>```
>嵌套`if`
>```python
>if 表达式1:
>    语句
>    if 表达式2:
>        语句
>    elif 表达式3:
>        语句
>    else:
>        语句
>elif 表达式4:
>    语句
>else:
>    语句
>```
>三元表达式
>三元操作，是条件语句中比较简练的一种赋值方式
>```python
>#变量名　= '语句　if 条件表达式　else 语句'
>A = Y if X else Z
>#如果X为真，那么就执行A=Y
>#如果X为假，就执行A=Z
>```
>简单练习
>求一个数是否可以整除２和３
>```python
>num = int(input("输入一个大于０的整数:"))
>if num % 2 == 0:
>	if num % 3 ==0:
>		print("{}　能整除２和３".format(num))
>	else:
>		print("{}　能整除２不能整除３".format(num))
>else:
>	if num % 3 ==0:
>		print("{}　能整除3不能整除２".format(num))
>	else:
>		print("{}　不能整除２不能整除３".format(num))
>```
