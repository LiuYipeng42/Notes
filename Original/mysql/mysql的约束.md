---
title: mysql中的约束
date: 2021-02-15 20:30:04
description: mysql约束的非空约束，唯一约束，主键约束和外键约束
---



# mysql中的约束

## 常见的约束

非空约束（not null）：约束的字段不能为NULL

唯一约束（unique）：约束的字段不能重复

主键约束（primary key）：约束的字段既不能为NULL，也不能重复

外建约束（foreign key）：

检查约束（check）：oracle数据库中有check约束，但mysql中没有

若插入的数据不符合约束，则会报错。

&emsp;&emsp;

## 非空约束

&emsp;&emsp;not null指定的字段的数据不能为NULL

&emsp;&emsp;在创建表时加not null

```mysql
create table 表名(字段名 数据类型 not null ...);
```

&emsp;&emsp;

## 唯一约束

&emsp;&emsp;unique指定的字段的**数据不能**为出现**重复**，但**null可以重复**，因为null不是一个值

&emsp;&emsp;一个字段的约束是**列级约束**，多个字段的约束是**表级约束**

&emsp;&emsp;

### 一个字段

&emsp;&emsp;在创建表时给想要进行唯一约束的字段加unique

```mysql
create table 表名(字段名 数据类型 unique ...);
```

&emsp;&emsp;

### 多个字段

&emsp;&emsp;**多个字段联合起来不重复**，可以在单个字段中重复

&emsp;&emsp;例：

```mysql
create table 表名(字段名1 int(42), 字段名2 int(42), ... unique(字段名1, 字段名2));
```

&emsp;&emsp;**unique(**字段名1, 字段名2**)** 可以**位于括号中的任意位置**

&emsp;&emsp;

## 主键约束

&emsp;&emsp;

主键字段：被主键约束约束的字段

主键值：主键字段的每一个值

&emsp;&emsp;

### 主键的作用

1. 表的设计三范式的要求，第一范式要求任何一张表都应该有主键

2. 有主键约束的字段的每一个数据都是相应记录是**唯一标识**，主键中的数据**不能为null**，**不能重复**。

&emsp;&emsp;

### 主键的分类

&emsp;&emsp;根据主键的**字段数量**划分

&emsp;&emsp;&emsp;&emsp;**单一主键**：**最常用**

&emsp;&emsp;&emsp;&emsp;**复合主键**：（多个字段联合起来添加一个主键约束，**不建议使用**，因为违反了三范式）

&emsp;&emsp;根据主键的**性质**来划分

&emsp;&emsp;&emsp;&emsp;**自然主键**：一个和业务没有任何关系的自然数，**最常用**

&emsp;&emsp;&emsp;&emsp;**业务主键**：主键值和系统的业务挂钩，如政府的数据库将每一个人的身份证号作为主键，**不建议使用**。

&emsp;&emsp;

### 语法

#### 单一主键语法

&emsp;&emsp;在创建表时给想要进行主键约束的字段加primary key

```mysql
create table 表名(字段名 数据类型 primary key ...);
```

&emsp;&emsp;**一张表的主键约束只能有一个**

&emsp;&emsp;

#### 复合主键语法

&emsp;&emsp;与唯一约束的多字段相同

例：

```mysql
create table 表名(字段名1 int(42), 字段名2 int(42), ... primary key(字段名1, 字段名2));
```

&emsp;&emsp;**primary key(**字段名1, 字段名2**)** 可以**位于括号中的任意位置**

&emsp;&emsp;

### 主键值自增加

&emsp;&emsp;mysql可以对一个主键的值按照顺序进行自增操作，不需要手动插入数据

&emsp;&emsp;在 primary key 后添加 auto_increment 就可以

&emsp;&emsp;例如：

&emsp;&emsp;**单一主键：**

```mysql
create table 表名(字段名 数据类型 primary key auto_increment ...);
```

&emsp;&emsp;

## 外键约束

&emsp;&emsp;外键约束可以将两张表联系起来

&emsp;&emsp;

### 语法

&emsp;&emsp;例如：

```mysql
create table A(
    'A字段1' int(42) primary key, 
    'A字段2' char(42)
);
```

```mysql
create table B(
    'B字段1' char(42), 
    'B字段2' int(42),
	foreign key('B字段2') references A('A字段1')
);
```

&emsp;&emsp;references 关键字表明B表中有外键约束的字段 **'B字段2**' **引用** 表A的字段 '**A字段1**'，字段 **'B字段2**' 的值只能是 '**A字段1**' 中的值。**B**表称为**父表**，**A**表称为**子表**。

&emsp;&emsp;

1. 一张表中有外键约束的字段 （'B字段2' ）的值只能是其所引用的字段（ 'A字段1'）下的值，所以在创建表时要**先创建父表**，**再创建子表**。

2. 有外键约束的字段也**可以有null**。

3. 有外键约束的字段所引用的两一张表的字段**必须有唯一性**（有主键约束或唯一约束）