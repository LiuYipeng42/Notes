---
title: mysql的存储引擎
date: 2021-02-16 12:22:11
description: mysql的常用存储引擎MyISAM，innoDB，MEMORY的优缺点

---



### 完整的建表语句

```mysql
create table 表名 (
    字段名 数据类型 约束,
    ...
) engine = innoDB default charset = utf8;
```

&emsp;&emsp;默认采用的存储引擎是 innoDB 

&emsp;&emsp;默认字符集是 utf8

&emsp;&emsp;不同的存储引擎有不同的优缺点

&emsp;&emsp;

&emsp;&emsp;show engies; 可以显示支持的存储引擎

&emsp;&emsp;

### 常用存储引擎

#### MyISAM：

&emsp;&emsp;优点：可被压缩，节省存储空间。可以转换为只读表，提高检索效率

&emsp;&emsp;缺点：不支持事务

&emsp;&emsp;

#### innoDB:

&emsp;&emsp;优点：支持事务，外键，行级锁等，数据较为安全

&emsp;&emsp;缺点：无法被压缩，无法转换成只读

&emsp;&emsp;

#### MEMORY：

&emsp;&emsp;缺点：不支持事务。数据容易丢失，因为所有数据存储在内存中

&emsp;&emsp;优点：查找速度最快



