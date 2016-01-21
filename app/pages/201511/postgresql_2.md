Title: postgresql学习2——使用
Author: honmaple 
Date: 2015-11-24
Category: linux
Tags: [sql,postgresql,linux]
Slug: postgresql_2.md
Summary: postgresql的简单使用


## python
[参考资料](http://www.yiibai.com/html/postgresql/2013/080998.html)
### 安装psycopg2
推荐使用venv虚拟环境  

    pip install psycopg2 

这个API打开一个连接到PostgreSQL数据库。如果成功打开数据库时，它返回一个连接对象  

    psycopg2.connect(database="testdb", user="postgres", password="cohondob", host="127.0.0.1", port="5432") 

该程序创建一个光标将用于整个数据库使用Python编程。  

    connection.cursor()

此例程执行SQL语句。可被参数化的SQL语句（即占位符，而不是SQL文字）。 psycopg2的模块支持占位符用％s标志  

    cursor.execute(sql [, optional parameters])

该程序执行SQL命令对所有参数序列或序列中的sql映射  

    curosr.executemany(sql, seq_of_parameters)

这个程序执行的存储数据库程序给定的名称。该程序预计为每一个参数，参数的顺序必须包含一个条目。  

    curosr.callproc(procname[, parameters])

这个只读属性，它返回数据库中的行的总数已修改，插入或删除最后 execute*().  

    cursor.rowcount

此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用commit()是不可见的，从其他的数据库连接。  

    connection.commit()

此方法会回滚任何更改数据库自上次调用commit（）方法  

    connection.rollback()

此方法关闭数据库连接。请注意，这并不自动调用commit（）。如果你只是关闭数据库连接而不调用commit（）方法首先，那么所有更改将会丢失！  

    connection.close()

这种方法提取的查询结果集的下一行，返回一个序列，或者无当没有更多的数据是可用的。  

    cursor.fetchone()

这个例程中取出下一个组的查询结果的行数，返回一个列表。当没有找到记录，返回空列表。该方法试图获取尽可能多的行所显示的大小参数。  

    cursor.fetchmany([size=cursor.arraysize])

这个例程获取所有查询结果（剩余）行，返回一个列表。空行时则返回空列表  

    cursor.fetchall()

#### 可以看出,psycopg2的操作与sqlite类似除了连接数据库
