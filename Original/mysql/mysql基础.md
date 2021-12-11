---
title: mysql的DML(数据操作)语句
date: 2021-02-11 23:11:32
description: mysql中对数据库的操作，Sql语句的分类，基本语法，表设计的三范式

---

&emsp;&emsp;

## 常用mysql命令

### 登录

```mysql
mysql -u root -p123456
```

&emsp;&emsp;-p后不能有空格

&emsp;&emsp;

### 数据库操作

#### 显示已有数据库

```mysql
show databases;
```

#### 查询当前使用的数据库

```mysql
select database();
```

#### 创建数据库

```mysql
create database databaseName;
```

#### 选择数据库

```mysql
use databaseName;
```

#### 删除数据库

```mysql
drop database databaseName;
```

#### 查询mysql版本

```mysql
select version();
```

#### 运行sql脚本

```mysql
source /home/zimablue/databaseName.sql;
```

#### 导出数据库

```mysql
mysqldump 数据库名>导出地址+文件名.sql -uroot -p123456
```

#### 导出表

```mysql
mysqldump 数据库名 表名>导出地址+文件名.sql -uroot -p123456
```



## SqL语句分类

&emsp;&emsp;**DQL**(数据查询语言)：查询语句，凡是select语句都是DQL。

&emsp;&emsp;**DML**(数据操作语言)：insert delete update，对表当中的数据进行增删改。

**&emsp;&emsp;DDL**(数据定义语言)：create drop alter，对表结构的增删改

&emsp;&emsp;**TCL**(事务控制语言)：commit提交事务，rollback回滚事务。(TCL中的T是Transaction)

&emsp;&emsp;**DCL**(数据控制语言)：grant授权、revoke撤销权限等

&emsp;&emsp;

## 语法

1. sql语句以“ ; ”结尾

2. sql语句不区分大小写

3. 在sql语句中使用**中文**时要用 “ '' ” 单引号

4. mysql对一个字段名起别名：字段名 别名



&emsp;&emsp;

## 表设计的三范式

&emsp;&emsp;第一范式（1NF）：要求数据达到原子性，使数据不可再分，每一张表都有主键；

&emsp;&emsp;第二范式（2NF）：使每一行**数据具有唯一性**，并**消除**数据之间的“**部分依赖**”，使一个表中的非主键字段，完											全依赖于主键字段；

&emsp;&emsp;第三范式（3NF）：使每个字段都独立地依赖于主键字段（独立性），而要消除其中部分非主键字段的内部依											赖——这种内部依赖会构成“传递依赖”

