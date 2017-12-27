## Pyinstaller 

> [项目主址](http://www.pyinstaller.org/)
>
> **简介：**
>
> PyInstaller是一个十分有用的第三方库，通过对源文件打包，Python程序可以在没有安装 Python的环境中运行，也可以作为一个独立文件方便传递和管理。
>
> **安装:**
>
> ```python
> pip3 install pyinstaller
> ```
>
> **使用**
>
> Go to your program’s directory and run:
>
> ```bash
> pyinstaller yourprogram.py
> ```
>
> 执行完成后，将会生成dist和build两个文件夹。（文件生成位置与cmd起始位置有关）其中 ，build 目录是 pyinstaller存储临时文件的目录，可以安全删除。最终的打包程序在dist内部的python_test文件夹下。目录中其他文件是可执行文件python_test.exe的动态链接库。
>
> 请注意 ，由于 ，由于 `PyInstaller` 不支持源文件名中有英文句号（ 英文句号（ .）存 在.
>
> 使用`pyinstaller`库需要注意以下问题：
>
> *  文件路径中 文件路径中 不能 出现 空格 和英文 句号（ .）；
> * 源文件必须是 源文件必须是 `UTF-8`编码， 暂不支持其他编码类型 ,采用 IDLE 编写的 源文件都保存为 源文件都保存为 源文件都保存为 UTF -8编码形式， 可直接使用。 
>
> 常用参数
>
> | 参数                 | 功能                  |
> | ------------------ | ------------------- |
> | -h, help           | 查看帮助                |
> | -v , version       | 查看版本号               |
> | -clean             | 清理打包过程中的临时文件        |
> | -D, --onedir       | 默认值,生成 dist目录       |
> | -F, --onefile      | 在dist文件夹中只生成独立的打包文件 |
> | -p DIR, --path DIR | 添加python文件使用的第三方库路径 |
> | -i , --icon        | 指定打包程序使用的图标(icon)文件 |

### 针对打包文件一闪而过

> - 打包文件需要安放完整
> - 可以把程序拖入`cmd` 窗口中查看报错
> - 可以在`build` 的目录中查找`warn*` 文件,其中有详细的报错信息
> - 可以在`*.py` 文件的末尾添加`input()` 函数,让程序使用手动确定结束.

