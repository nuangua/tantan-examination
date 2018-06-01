# tantan-examination

## Examinations

* 给定一段html，内容如下

<pre><code>
<table border="1">
 <thead>
  <tr>
   <td>name</td>
   <td>age</td>
   <td>operate</td>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>user0</td>
   <td>18</td>
   <td><input type="button" value="delete" />delete</td>
  </tr>
 </tbody>
</table>

</code></pre>

给定一个文件data.json，内容如下
<pre><code>

[
 {'name': 'user1', 'age': 18},
 {'name': 'user2', 'age': 18}
]

</code></pre>


请用jquery实现ajax请求该json文件，将数据插入表格(并增加第三列删除按钮)，并实现delete按钮删除本行的功能。

**Exam1 Comment**: I'm not good at using jquery/javascript/ajax to write frontend directly. Actually, I use frontend framework like vuejs, regularjs for frontend development.
* [Exam1 Codes](https://github.com/nuangua/tantan-examination/blob/master/tantan_examination/exam1.html)

* 给定日志文件a.log，内容格式如下
<pre><code>
2018-01-01 12:20:24 "SELECT * FROM table1;"
2018-01-01 12:20:57 "DELETE FROM table1 WHERE id=1;"
2018-01-01 12:21:32 "SELECT * FROM table2;"
2018-01-01 12:21:42 "SELECT * FROM table2;"
2018-01-01 12:21:57 "UPDATE table2 SET age=18 WHERE id=1;"
</code></pre>

请用python实现：获取每分钟执行次数最多的SQL语句

**Exam2 Comment**: I spent lots of time on how to group the max executed sql sentences by datetime(every minute). The method what I use to is that after retrieving the datetime and sql sentences data from every line, the data is saved in a dictionary list as below, in this step we count out every unique sql sentence occurring times in every minute. Then the next step is just to iterate this list, and calculate which sql sentence's occuring times is the most in every minute.
Actually, we can also just save the data into sql database after retrieving data, then query/filter what we want with sql query sentence with group by.

`
{'2018-01-01 12:20': {'SELECT * FROM table1;': 1,  'DELETE FROM table1 WHERE id=1;': 1}, '2018-01-01 12:21': {'UPDATE table2 SET age=18 WHERE id=1;': 1, 'SELECT * FROM table2;': 2}}
`


## [Exam Anwsers](https://nuangua.github.io/tantan-examination/build/html/getting_started.html)

* [Exam2 Codes](https://github.com/nuangua/tantan-examination/blob/master/tantan_examination/exam2.py)

## Features

## Future Plans

## Latest Changes

## License

Copyright &copy; 2017