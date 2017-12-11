"""
 定义:
 F0 = 0     (n=0)
 F1 = 1    (n=1)
 Fn = F[n-1]+ F[n-2](n=>2)
 费波那契数列由0和1开始，之后的费波那契系数就是由之前的两数相加而得出,0不是第一项，而是第零项.
 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""


# 使用循环实现fibon

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


aa = fibon(10)
print(aa)


# 使用生成器实现,一种迭代方式

def fibonx(max):
    # n, a, b = (1, 1, 1)
    n = a = b = 1
    while n < max:
        yield a
        a, b = b, a + b
        n += 1

    return "DONE"


for x in fibonx(10):
    print(x)


# 按照定义,直接递归,执行速度慢

def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print('fib1 ,', locals())
        return fib1(n - 1) + fib1(n - 2)


fib1(5)

# 改进算法,初始化

memo = {0: 0, 1: 1}


def fib2(n):
    if not n in memo:
        print('fib2 ,', locals())

        memo[n] = fib2(n - 1) + fib2(n - 2)
        print(memo)
    return memo[n]


fib2(5)


def fib3(n, a=0, b=1):
    print('fib3', locals())
    if n == 0:
        return a
    return fib3(n - 1, b, a + b)


fib3(5)