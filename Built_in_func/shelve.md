## shelve Python对象持久化

> shelve 是一个持久的,dictionary-like 的对象,键对应的值可以是python的任何数据类型(pickle模块处理过的类型).这包括这包括大多数类实例，递归数据类型和包含大量共享子对象的对象。键是字符串数据类型
>
> `shelve.open(filename, flag='c', protocol=None, writeback=False)`
>
> 打开一个持久字典.
>
> filename : 指定一个底层数据库的名字,但是会创建大量的相关文件,默认情况下,以读写的形式打开数据库
>
> flag: 
>
> * flag='r' : 只读
> * flag="w" 读写
> * flag="w" 打开一个数据库进行读写操作,如果不存在,会创建
> * flag="n" 总是以读写的方式打开一个新的数据库
>
> protocol:默认情况下使用pickles 版本3 来序列化值
>
> wirteback:果可选的writeback参数设置为True，则所有被访问的条目也被缓存在内存中, and written back on [`sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync) and [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close)
>
> 举例
>
> ```python
> with shelve.open('spam') as db:
>     db['eggs'] = 'eggs'
> ```
>
> shelve对象支持字典支持的所有方法.
>
> `Shelf.close()`
>
> 同步并关闭持久性字典对象