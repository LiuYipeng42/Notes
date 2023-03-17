---
title: mysql的事务
date: 2021-02-17 10:42:16
description: mysql事务的语法，简单原理，特性
---



## 事务

1. 事务是一个完整的业务逻辑单元，相当于利用多个sql语句完成一件事

2. 事务在mysql中属于TCL语句，有commit（提交事务），rollback（回滚事务）和savepoint（保存点）

3. 和事务相关的语句只有DML（数据操作语句）语句

4. 事务的存在 是为了保证数据的完整性和安全性

&emsp;&emsp;

### 语法

#### 开始事务

​		begin; 或 emsp;&emsp;start transaction;

&emsp;&emsp;

#### 提交事务

&emsp;&emsp;commit;

&emsp;&emsp;

#### 回滚

**设置保存点**

&emsp;&emsp;savepoint 保存点名; 

**回到某一个保存点**

&emsp;&emsp;rollback to 保存点名;

**结束事务**

&emsp;&emsp;rollback;

&emsp;&emsp;结束事务后并不会修改数据

&emsp;&emsp;

回滚与游戏中的保存进度相似

&emsp;&emsp;

### 原理

&emsp;&emsp;事务机制开始后，会将想要运行的数据操作的**sql语句储存到操作历史记录**中，并不会在真实的数据中运行这些sql语句，这时相当于会生成一张**虚拟的表**，在这张虚拟的表中运每一个sql语句，在查询时会返回这张虚拟的表中的数据，之后若**提交事务**，提交之后才会在真实的数据中运行这些sql语句，然后会**清空**历史中储存的**sql语句**，**结束事务**。

&emsp;&emsp;

### 特性

&emsp;&emsp;四大特性 ACID：

&emsp;&emsp;A：**原子性**：事务是最小的工作单元，不可再分

&emsp;&emsp;C：**一致性**：事务必须保证多条DML语句同时成功或者同时失败

&emsp;&emsp;I：**隔离性**：事务A与事务B之间具有隔离

&emsp;&emsp;D：**持久性**：最终数据必须持久化到硬盘文件中，事务才算成功的结束

&emsp;&emsp;

#### 隔离性

1. **隔离级别**：

   第一级：**读未提交**（read uncommitted）

   &emsp;&emsp;事务T1将某一值修改但是还未提交，然后事务T2读取该值，此后T1因为某种原因撤销对该值的修改并提交，这就导致了T2所读取到的数据是无效的，存在**脏读现象**（Dirty Read）

   第二级：**读已提交**（read committed）

   &emsp;&emsp;在一个事务执行并提交之后，另一个事务才可以读取到修改后的数据，解决了脏读现象但存在**不可重复读**现象，即一个事务内两个相同的查询却可能返回不同数据，这是因为数据可能被更改。

   第三级：**可重复读**（repeatable read）

   &emsp;&emsp;在一个事务在修改数据前，会备份数据，这样每一个事务都有自己的备份数据。可以重复访问没有修改的数据，解决了脏读现象和不可重复读现象，但存在读取到的**数据不真实**的现象，因为读到的数据是备份的数据

   第四级：**序列化读/串行化读**（serializable）

   &emsp;&emsp;在一个事务在执行时不能执行另一个事务，必须按照一定顺序依次执行。

   &emsp;&emsp;解决了以上所有问题，但存在**效率较低**的问题

&emsp;&emsp;

2. mysql**默认的隔离级别**是第三级**可重复读**（repeatable read）

3. 可以通过如下语句**自定义隔离级别**

```mysql
set global transaction isolation level 级别名称;
```

&emsp;&emsp;例如：

```mysql
set global transaction isolation level read uncommitted;
```

4. **查看**数据库的**隔离级别**

```mysql
select @@global.tx_isolation;
```

