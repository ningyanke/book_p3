## 小技巧

### 1.Python解决字符串去除全部标点符号

> 适用于标准的英文标点符号
>
> ```python
> '''引入sting模块'''
> import string
> ```
>
> ```python
> '''使用标点符号常量'''
> string.punctuation	
> ```
>
> ```python
> '''测试'''
> text = "ikdsf,,../dfso;ks.fd/s/d.f;lopsdf【】【】"
>
> '''去除字符串中的所有字符，可以增加自定义字符(去除中文字符)'''
>
> def strclear(text,newsign=''):
>     import string # 引入string模块
>     signtext = string.punctuation + newsign # 引入英文符号常量，可附加自定义字符，默认为空
>     signrepl = '@'*len(signtext) # 引入符号列表长度的替换字符
>     signtable = str.maketrans(signtext,signrepl) # 生成替换字符表
>     return text.translate(signtable).replace('@','') # 最后将替换字符替换为空即可
>
> strclear(text,'》【】')
> ```

