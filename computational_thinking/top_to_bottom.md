## 自顶向下的设计

> 面向对象,面向过程都可以使用这种方法:

### 基本思想

> ![10011](../picture/10011.png)

### 顶层设计

> 步骤1: 打印程序的介绍信息就
>
> * pintIntro()
>
> 步骤2: 获得程序运行所需要的参数: ProbA, ProbB, n
>
> * probA, probB , n = getInputs()
>
> 步骤3:模拟n次比赛
>
> * winsA, winsB = simNgames(n, probA, probB) 
>
> 步骤4: 输出球员A和球员B获胜的比赛的次数和概率
>
> * printSummary(winsA, winsB)
>
> #### 第一阶段
>
> ![1](../picture/10014.png)
>
> #### 第二阶段
>
> ![17](../picture/10016.png)
>
> #### 第三阶段
>
> ![3](../picture/10017.png)

### 代码设计

> ```python
> #matchSim.py
> from random import * 
>  
> def main():
>     printIntro()
>     probA,probB,n = getInputs()
>     winsA, winsB = simNGames(n,probA,probB)
>     PrintSummary(winsA, winsB)
>  
> def printIntro():
>     print('This program simulates a game between two')
>     print('There are two players, A and B')
>     print('Probability(a number between 0 and 1)is used')
>  
> def getInputs():
>     a = eval(input('What is the prob.player A wins?'))
>     b = eval(input('What is the prob.player B wins?'))
>     n = eval(input('How many games to simulate?'))
>     return a,b,n
>  
> def simNGames(n,probA,probB):
>     winsA = 0
>     winsB = 0
>     for i in range(n):
>         scoreA,scoreB = simOneGame(probA,probB)
>         if scoreA >scoreB:
>             winsA = winsA + 1
>         else:
>             winsB = winsB + 1
>     return winsA,winsB
> def simOneGame(probA,probB):
>     scoreA = 0
>     scoreB = 0
>     serving = "A"
>     while not gameOver(scoreA,scoreB):
>         if serving == "A":
>             if random() < probA:
>                 scoreA = scoreA + 1
>             else:
>                 serving = "B"
>         else:
>             if random() < probB:
>                 scoreB = scoreB + 1
>             else:
>                 serving = "A"
>     return scoreA,scoreB
>  
> def gameOver(a,b):
>     return a==15 or b==15
>  
> def PrintSummary(winsA, winsB):
>     n = winsA + winsB
>     print('\nGames simulated:%d'%n)
>     print('Wins for A:{0}({1:0.1%})'.format(winsA,winsA/n))
>     print('Wins for B:{0}({1:0.1%})'.format(winsB,winsB/n))
>  
> if __name__ == '__main__':
>     main()
> ```

### 设计过程总结

> 自顶向下设计
>
> * 步骤1: 将算法表达为一系列小问题
> * 步骤2:为每个小问题设计接口
> * 步骤3: 通过将算法表达为接口关联的多个小问题来细化算法
> * 步骤4: 为每个小问题重复上述过程.

