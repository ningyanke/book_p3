## os model

> Python3 os 模块中常用方法

### 1.对文件本体进行操作

> [官方文档](https://docs.python.org/3.6/library/os.html#module-os)

### 2. 文件操作

> | 函数               | 描述                             |
> | ---------------- | ------------------------------ |
> | os.listdir(path) | 返回指定目录下的文件名和目录名 <br />返回一个列表对象 |
> | os.mknod(path)   | 创建一个文件                         |
> | os.remove(path)  | 删除一个文件                         |
>

### 3.目录操作

> | 函数                     | 描述                                 |
> | ---------------------- | ---------------------------------- |
> | os.getcmd()            | 返回当前工作目录                           |
> | os.listdir(path)       | 返回指定目录下的文件名和目录名 <br />返回一个列表对象     |
> | os.mkdir(path)         | 创建一个文件                             |
> | os.rmdir(path)         | 删除path指定的空目录，如果目录非空，则抛出一个OSError异常 |
> | os.removedirs(path)    | 递归删除目录(多级目录)                       |
> | os.curdir<br />等同于`.`  | 返回`.` 当前目录                         |
> | os.pardir<br />等同于`..` | 返回`..` 父级目录                        |
> | os.chdir(path)         | 改变工作目录                             |
> |                        |                                    |
> |                        |                                    |
> |                        |                                    |
> |                        |                                    |
>
> 

### 4.系统

> | 函数                                    | 描述                                       |
> | ------------------------------------- | ---------------------------------------- |
> | os.name                               | 返回正在使用的工作平台                              |
> | os.sep                                | 取代操作系统的特定路径分割符                           |
> | os.getenv(key)<br />os.getenv("PATH") | 获取指定的环境变量                                |
> | os.putenv()                           | 设置环境变量                                   |
> | os.system()                           | 运行shell命令                                |
> | os.exit()                             | 终止当前进程                                   |
> | os.linesep                            | 返回当前系统的行终止符,linux \n ,windowns \r\n      |
> | os.path.split(path)                   | Split a pathname.  Returns tuple "(head, tail)" where "tail" is<br />everything after the final slash.  Either part may be empty. |
> | os.path.isfile(path)                  | 判断是否文件                                   |
> | os.path.isdir(path)                   | 判断时候目录                                   |
> | os.path.exists(path)                  | 判断一个路径是否存在                               |
> | os.path.getsize(path)                 | 获得文件大小,如果是目录返回'OL'                       |
> | os.path.abspath(path)                 | 获取绝对路径                                   |
> | os.path.isabs(path)                   | 判断path是否包含在绝对路径中                         |
> | os.path.splitext(path)                | 分离文件名和扩展名                                |
> | os.path.join(path,name)               | 连接目录与文件名或目录                              |
> | os.path.basename(path)                | 返回文件名                                    |
> | os.path.dirname(path)                 | 返回文件路径                                   |

### 5.文件和目录的属性

> | 函数                   | 描述         |
> | -------------------- | ---------- |
> | os.stat(path)        | 获取文件和目录的属性 |
> | os.chmod(path, mode) | 修改文件和目录的属性 |
> | os.chown(path)       | 修改所属者      |
> |                      |            |
> |                      |            |
> |                      |            |
> |                      |            |
> |                      |            |
> |                      |            |
>
> 

### 实例将放入`Jupter 笔记本 ` 

