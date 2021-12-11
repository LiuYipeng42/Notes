---
title: mysql的DML(数据操作)语句
date: 2021-02-20 18:04:18
description: mysql的数据插入，数据修改及数据删除
---

&emsp;&emsp;

## 插入数据

```mysql
insert into tableName(字段名1, 字段名2 ... ) value (插入数据1, 插入数据2 ... );
```

&emsp;&emsp;字段名的顺序和数量不必与表的字段相同，缺少的字段会被视为默认值，默认值默认为null，默认值可以在创建表时修改

&emsp;&emsp;可以不写字段名，但一定要把每一个字段要插入的数值按照**表中字段的顺序和数量**写上去

```mysql
insert into tableName value (插入数据1, 插入数据2 ... );
```

&emsp;&emsp;

### 插入多行数据

```mysql
insert into tableName(字段名1, 字段名2 ... ) value (插入数据1, 插入数据2 ... ), (插入数据1, 插入数据2 ... ), (...) ...;
```

&emsp;&emsp;value后可以有多个小括号，一个括号表示一行数据

&emsp;&emsp;

## 修改数据

```mysql
update 表名 set 字段名1 = 值1, 字段名2 = 值2, ... where 条件; 
```

&emsp;&emsp;若不加 where 就会将表中的**所有数据修改**

&emsp;&emsp;

## 删除数据

```mysql
delete from 表名 where 条件;
```

&emsp;&emsp;若不加 where 就会将表中的**所有数据删除**

&emsp;&emsp;**delete的删除速度较慢**，因为delete并不是真正的删除，删除后还**可以将数据恢复（回滚）**。

&emsp;&emsp;若想**快速删除数据**可以使用如下语句：

```mysql
truncate table 表名;
```

&emsp;&emsp;此种删除语句删除速度快，但**数据不可恢复**。



