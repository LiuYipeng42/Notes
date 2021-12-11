---
title: mysql表的操作
date: 2021-02-15 13:45:33
description: 表的创建，删除，修改，复制，插入，显示创建语句

---

# mysql表的操作

&emsp;&emsp;table是数据库的基本组成单元，所有的数据都以表格的形式组织，可读性强

&emsp;&emsp;一个表包括行和列：

&emsp;&emsp;**行**：记录/数据

&emsp;&emsp;**列**：字段 (column)

&emsp;&emsp;

## mysql命令

#### 显示已有表

```mysql
show tables;
```

&emsp;&emsp;

#### 查看表结构

```mysql
desc tableName;
```

&emsp;&emsp;

#### 查看创建表时所用的语句

```mysql
show create table tableName;
```

&emsp;&emsp;

## sql的DML(数据操作)语句

#### 删除表

```mysql
drop tableName;
```

&emsp;&emsp;或

```mysql
drop table if exists tableName;
```

&emsp;&emsp;

#### 创建表

##### 语法

```mysql
creatr table tableName('字段名1' 数据类型(数据大小), '字段名2' 数据类型(数据大小) ... );
```

&emsp;&emsp;可以通过default设置每个**字段的默认值**

```mysql
creatr table tableName('字段名1' 数据类型(数据大小) default 数值, '字段名2' 数据类型(数据大小) ... );
```

&emsp;&emsp;

##### 常见数据类型

```mysql
int			整数型
bigint		长整型
float		浮点型
char		定长字符串(比varchar快，但会造成空间浪费)
varchar		可变字符串(会根据字符串的长度自动分配空间，但运行速度比char慢)
date		日期类型
BLOB		二进制大对象(储存图片，视频等流媒体信息，使用java的IO流来储存) 
CLOB		字符大对象(储存较大文本)
```

&emsp;&emsp;

#### 表的复制

```mysql
create table 表名 as select ... from ...;
```

&emsp;&emsp;将select查询出来的表作为一场新表创建

&emsp;&emsp;

#### 将查询结果插入到一张表

```mysql
insert into 表名 select ... from ...;
```

&emsp;&emsp;将select查询出来的表插入到一场表中

&emsp;&emsp;

## 表结构的修改

&emsp;&emsp;表的修改的mysql语句属于sql语句中的DDL（数据定义语言），

&emsp;&emsp;表的修改出现的情况较少，若出现则可以使用navicat修改。

