###集合


####定义
>集合使用`set`或者`{}`创建，和字典的键对应，其值是不可变的，只能使用字符串，数字，或者元组
>集合的显示用 `{}`来显示，但是并没有键值对的对应
>集合的元素不能重复，而且是无序的
>利用`set()`建立起来的集合是可变集合，可变集合都是unhashable类型的

####创建集合
>```python
>set() -> new empty set object
>set(iterable) -> new set object
>```
>#####1.创建一个空集合
>```python
>In [161]: a =set()
>>
>In [162]: type(a)
>Out[162]: set
>>
>In [163]: a
>Out[163]: set()
>>#虽然结合可以使用 {} 来创建，但是空集合不行
>In [169]: a = {}
>>
>In [170]: type(a)
>Out[170]: dict
>```
>#####2.创建集合
>```python
>In [164]: s1 = set('Python')
>>
>In [165]: s1
>Out[165]: {'P', 'h', 'n', 'o', 't', 'y'}
>```

####集合的内置函数
>#####1).`add`,`update`
>
>```python
>add(...)
>    Add an element to a set.
>>
>    This has no effect if the element is already present.
>```
>`set.update`既可以添加集合类型的，也可以是其他不可变类型的
>
>```python
>update(...)
>    Update a set with the union of itself and others.
>```
>
>例子
>```python
>In [182]: a_set = {'i','l'}
>
>In [183]: a_set.add('o')
>
>In [184]: a_set
>Out[184]: {'i', 'l', 'o'}
>
>In [185]: a_set.update('ve')
>
>In [186]: a_set
>Out[186]: {'e', 'i', 'l', 'o', 'v'}
>
>In [187]: a_set.update({'p','y'})
>
>In [188]: a_set
>Out[188]: {'e', 'i', 'l', 'o', 'p', 'v', 'y'}
>```
>######2).pop,remove,discard,clear
>`pop`,从集合中任意删除一个元素，并返回结果
>```python
>pop(...)
>    Remove and return an arbitrary set element.
>    Raises KeyError if the set is empty.
>```
>`remove`,从集合中删除指定的元素，而且必须存在于集合中
>```python
>remove(...)
>    Remove an element from a set; it must be a member.
>    If the element is not a member, raise a KeyError.
>```
>`discard`,从集合中删除指定的元素，如果元素不在集合中，do nothing
>```python
>discard(...)
>    Remove an element from a set if it is a member.
>    If the element is not a member, do nothing.
>```
>`set.clear`
>```python
>clear(...)
>    Remove all elements from this set.
>```
