## time

### 官方文档

> [官方](https://docs.python.org/3/library/time.html)

### 常用

> | 函数                             | 描述                                       |
> | ------------------------------ | ---------------------------------------- |
> | time.altzone                   | 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用 |
> | time.asctime([tupletieme])     | 将时间元组转换为字符串                              |
> | time.localtime([sec])          | 将秒数转换为时间元组                               |
> | time.mktime(tuple)             | 将时间元组转换为本地时间                             |
> | time.sleep(secs)               | 休眠                                       |
> | time.strptime(string[,format]) | 将字符串解析为时间元组                              |
> | time.time()                    | 当前事件,返回新纪元开始后的秒数                         |
> | time.ctime()                   | 作用相当于asctime(localtime(secs))，未给参数相当于asctime() |
>
> 相互的转换关系如图
>
> ![time](../picture/time.jpg)

### 详解

> #### time.time()
>
> time.time() 获取当前时间(时间戳),以1970年1月1日0时0分0秒为计时起点，到当前的时间长度，不够友好
>
> ```python
> In [57]: time.time() 
> Out[57]: 1484991910.544831
> ```
>
> #### time.localtime()
>
> 获取本地时间，计算机显示的时间
>
> ```python
> In [58]:  time.localtime() 
> Out[58]: time.struct_time(tm_year=2017, tm_mon=1, tm_mday=21, tm_hour=17, tm_min=45, tm_sec=40,tm_wday=5, tm_yday=21, tm_isdst=0)
> ```
>
> 各个字段的含义:
> | 索引   | 属性       | 含义     |
> | ---- | -------- | ------ |
> | 0    | tm_year  | 年      |
> | 1    | tm_mon   | 月      |
> | 2    | tm_mday  | 日      |
> | 3    | tm_hour  | 时      |
> | 4    | tm_min   | 分      |
> | 5    | tm_sec   | 秒      |
> | 6    | tm_wday  | 一周中第几天 |
> | 7    | tm_yday  | 一年中第几天 |
> | 8    | tm_isdst | 夏时令    |
>
> #### time.gtime()
>
>  获取格林威治时间
>
> #### time.asctime()  
>
> 默认以time.localtime() 的值为参数，得到一个非常友好的输出
>
> ```python
> In [60]: time.asctime() 
> Out[60]: 'Sat Jan 21 17:58:25 2017'
> ```
>
> #### time.ctime()
>
>  和time.asctime()输出的一样，但是是以时间戳为参数的
>
> #### time.mktime()
>
> time.localtime()的逆过程，得到的是一个对计算机友好的值
>
> #### time.strftime()
>
> 将时间元组按照指定格式要求转换为字符串，如果不指定时间元组，默认以localtime()的值为准
>
> ```python
> strftime(...)
> 	strftime(format[, tuple]) -> string
> 		    
> 	Convert a time tuple to a string according to a format specification.
> 	See the library reference manual for formatting codes. When the time tuple
> 	is not present, current time as returned by localtime() is used.
> ```
>
> `format` 的格式
>
> | 格式   | 含义              | 取值范围                        |
> | ---- | --------------- | --------------------------- |
> | %y   | 去掉世纪的年份         | 00-99 如 '15'                |
> | %Y   | 完整的年份           | 如'2015'                     |
> | %j   | 指定日期是一年中第几天     | 001-366                     |
> | %m   | 返回月份            | 01-12                       |
> | %b   | 本地简化月份的名称       | 简写英文月份                      |
> | %B   | 本地完整月份的名称       | 完整英文月份                      |
> | %d   | 该月的第几日          | 如5月1， 返回"01"                |
> | %H   | 该日的第几时          | 24小时制 00-23                 |
> | %h   | 该日的第几时          | 12小时制 01-12                 |
> | %M   | 分钟              | 00-59                       |
> | %S   | 秒               | 00-59                       |
> | %U   | 该年中第几个星期(周日为起点) | 00-53                       |
> | %W   | 该年中第几个星期(周一为起点) | 00-53                       |
> | %w   | 一星期中的第几天        | 0-6                         |
> | %Z   | 时区              | 中国大陆CST,china standard time |
> | %x   | 日期              | 日/月/年                       |
> | %X   | 时间              | 时:分：秒                       |
> | %c   | 详细日期时间          | 日/月/年 时:分:秒                 |
> | %%   | '%'字符           | '%' 字符                      |
> | %p   | 上下午             | AM or  PM                   |
>
> #### time.striptime()
>
> 正好与，time.strftime()作用相反.striptime() 的作用是将字符串转换为时间元组，参数要指定2个，一个是时间字符串，一个是时间字符串队形的格式
>
> ```python
> In [67]: today = time.strftime('%y/%m/%d')
>
> In [68]: today
> Out[68]: '17/01/21'
>
> In [72]: time.strptime(today,'%y/%m/%d')
> Out[72]: time.struct_time(tm_year=2017, tm_mon=1, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5,tm_yday=21, tm_isdst=-1)
> ```

### calendar

> 此模块的函数都是日历相关的，例如打印某月的字符月历。
>
> 星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
>
> | 序号   | 函数及描述                                    |
> | ---- | ---------------------------------------- |
> | 1    | **calendar.calendar(year,w=2,l=1,c=6)**返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。 |
> | 2    | **calendar.firstweekday( )**返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。 |
> | 3    | **calendar.isleap(year)**是闰年返回True，否则为false。 |
> | 4    | **calendar.leapdays(y1,y2)**返回在Y1，Y2两年之间的闰年总数。 |
> | 5    | **calendar.month(year,month,w=2,l=1)**返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。 |
> | 6    | **calendar.monthcalendar(year,month)**返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。 |
> | 7    | **calendar.monthrange(year,month)**返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。 |
> | 8    | **calendar.prcal(year,w=2,l=1,c=6)**相当于 print calendar.calendar(year,w,l,c). |
> | 9    | **calendar.prmonth(year,month,w=2,l=1)**相当于 print calendar.calendar（year，w，l，c）。 |
> | 10   | **calendar.setfirstweekday(weekday)**设置每周的起始日期码。0（星期一）到6（星期日）。 |
> | 11   | **calendar.timegm(tupletime)**和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。 |
> | 12   | **calendar.weekday(year,month,day)**返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。 |

### datetime

> ```python
> In [140]: import datetime
>
> In [141]: today = datetime.date.today()  #实际是生成today对象后对today属性进行的一系列操作
>
> In [142]: today
> Out[142]: datetime.date(2017, 1, 21)  #生成式一个datetime.date对象
>
> In [143]: print today     #print 更好的输出体验，对人友好，对机器友好的函数__repr__
> 2017-01-21
>
> In [144]: print today.timetuple()   #时间元组
> time.struct_time(tm_year=2017, tm_mon=1, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0,
>  tm_wday=5, tm_yday=21, tm_isdst=-1)
>
> In [145]: print today.ctime()    #对人友好，time.localtime()
> Sat Jan 21 00:00:00 2017
>
> In [146]: print today.toordinal()   #时间戳
> 736350
> #不能直接对datetime.date.year/month/day操作，只能对today生成的对象操作
> In [147]: print today.year
> 2017
>
> In [149]: print today.month
> 1
>
> In [150]: print today.day
> 21
> #时间戳和格式化时间的装换
> In [151]: to = today.to
> today.today      today.toordinal  
>
> In [151]: to = today.toordinal()
>
> In [152]: to 
> Out[152]: 736350
>
> In [153]: print datetime.dat
> datetime.date           datetime.datetime       datetime.datetime_CAPI  
>
> In [153]: print datetime.date.fro
> datetime.date.fromordinal    datetime.date.fromtimestamp  
>
> In [153]: print datetime.date.fromordinal(to)
> 2017-01-21			
>
> time类
>
> datetime.datetime
> datetime.datetime.now()
> timedelta
> In [154]: now = datetime.datetime.now() 
> In [155]: now 
> Out[155]: datetime.datetime(2017, 1, 21, 20, 16, 48, 816530)
> #增加 5 小时
> In [156]: b = now + datetime.timedelta(hours = 5)
>
> In [157]: b 
> Out[157]: datetime.datetime(2017, 1, 22, 1, 16, 48, 816530)
>
> In [158]: print b 
> 2017-01-22 01:16:48.816530
> #增加2周
> In [159]: c =  now + datetime.timedelta(weeks = 2 )
>
> In [160]: print c 
> 2017-02-04 20:16:48.816530
> #计算时间差
> In [161]: d = c - b 
> In [162]: d 
> Out[162]: datetime.timedelta(13, 68400)
>
> In [163]: print d 
> 13 days, 19:00:00
> ```

