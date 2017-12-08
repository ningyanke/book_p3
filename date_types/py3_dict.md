### 字典
#### 定义
>字典是另一种可变容器模型，且可存储任意类型对象。
>字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
>``d = {key1 : value1, key2 : value2 }
>键必须是唯一的，但值则不必。
>值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组



####创建字典
>```python
>dict() -> new empty dictionary
>dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs
>dict(iterable) -> new dictionary initialized as if via:
>d = {}    
>for k, v in iterable:
>	d[k] = v
>dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list.  For example:  dict(one=1, two=2)"
>```
>##### 1.创建空字典
>```python
>In [132]: d = {}
>
>In [133]: d1 = dict()
>```
>##### 2.直接创建字典
>```python
>In [136]: d2 = {"name":'xiaoming','site':'china'}
>
>In [137]: d3 = dict(name='xiaoming',site='china')
>
>In [139]: d3
>Out[139]: {'name': 'xiaoming', 'site': 'china'}
>```
>##### 3.利用元祖创建字典
>```python
>In [140]: d4 = dict((['first',1],['second',2]))
>
>In [141]: d4
>Out[141]: {'first': 1, 'second': 2}
>```
>##### 4.使用内建函数`dict.fromkeys`
>```python
>In [142]: dict.fromkeys.__doc__
>Out[142]: 'Returns a new dict with keys from iterable and values equal to value.'
>```
>这样生成的是一个完全新的字典
>```python
>In [143]: {}.fromkeys(('a','b'),'1')
>Out[143]: {'a': '1', 'b': '1'}
>```
>##### 5.使用`zip()`
>```python
>In [144]: zip((1,2,3),('a','b','c'))
>Out[144]: <zip at 0x7f02710ea7c8>
>
>In [145]: dict(zip((1,2,3),('a','b','c')))
>Out[145]: {1: 'a', 2: 'b', 3: 'c'}
>```
>在Python3中`zip()`生成的是一个内建对象,返回的是一个`tuple`
>```python
>zip(iter1 [,iter2 [...]]) --> zip object
>Return a zip object whose .__next__() method returns a tuple where the i-th element comes from the i-th iterable argument.  The .__next__() method continues until the shortest iterable in the argument sequence is exhausted and then it raises StopIteration.
>```
>#####6.列表生成式转换为字典
>`dict1 = {(x,j) for x in a for j in b}`

####字典键的特性
>字典值可以是任何python对象，既可以是标准的对象，也可以是用户定义的，但键不可以
>1).不允许同一个键出现2次，如果一个键被赋值2次，后一个值会被记住
>```python
>In [149]: dict1 = {'name':'jack'}
>
>In [150]: dict1['name'] = 'python'
>
>In [151]: dict1
>Out[151]: {'name': 'python'}
>```
>2).键必须是不可变，所以可以用数字，字符串或元组，而列表不行
>   ```python
>In [152]: dict1 = {['name']:'[python'}
>---------------------------------------------------------------------------
>TypeError           Traceback (most recent call last)
><ipython-input-152-2f8e42b5737d> in <module>()
>----> 1 dict1 = {['name']:'[python'}
>
>TypeError: unhashable type: 'list'
>   ```

####嵌套
>
>    ```python
>citys={
>    '北京':{
>        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
>        '海淀':['圆明园','苏州街','中关村','北京大学'],
>        '昌平':['沙河','南口','小汤山',],
>        '怀柔':['桃花','梅花','大山'],
>        '密云':['密云A','密云B','密云C']
>    },
>    '河北':{
>        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
>        '张家口':['张家口A','张家口B','张家口C'],
>        '承德':['承德A','承德B','承德C','承德D']
>    }
>}
>    ```

####字典的内置方法
|序号|函数及描述|
|--|----------|
|1 |	radiansdict.clear()<br>删除字典内所有元素
|2	|radiansdict.copy()<br>返回一个字典的浅复制
|3 |	radiansdict.fromkeys()<br>创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
|4	|radiansdict.get(key, default=None)<br>返回指定键的值，如果值不在字典中返回default值
|5	|key in dict<br>如果键在字典dict里返回true，否则返回false
|6	| radiansdict.items()<br>以列表返回可遍历的(键, 值) 元组数组
|7	| radiansdict.keys()<br>以列表返回一个字典所有的键
|8	|radiansdict.setdefault(key, default=None)<br>和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
|9	| radiansdict.update(dict2)<br>把字典dict2的键/值对更新到dict里
|10 |	radiansdict.values()M<br>以列表返回字典中的所有值
|11 |	pop(key[,default])<br>删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
|12 |	popitem()<br>随机返回并删除字典中的一对键和值(一般删除末尾对)。|
