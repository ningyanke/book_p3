## python 进度条

> 实现原理
>
> print会输出一个\n，也就是换行符，这样光标移动到了下一行行首，接着输出，之前已经通过stdout输出的东西依旧保留，而且保证我们在下面看到最新的输出结果。
>
> 进度条不然，我们必须再原地输出才能保证他是一个进度条，否则换行了怎么还叫进度条？
>
> 最简单的办法就是，再输出完毕后，把光标移动到行首，继续在那里输出更长的进度条即可实现，新的更长的进度条把旧的短覆盖，就形成了动画效果。
>
> 可以想到那个转义符了吧，那就是 \r。
>
> 转义符\r就可以把光标移动到行首而不换行，转义符\n就把光标移动到行首并且换行
>
> 

### 项目地址

> [github地址](https://github.com/tqdm/tqdm) 
>
> 需要说明的是这只是一个在解释器中运行的工具

