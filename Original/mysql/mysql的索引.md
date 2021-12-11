---
title: mysql的索引
date: 2021-02-17 15:34:11
description: mysql索引的语法，适用情况，分类，注意事项

---



## 索引

&emsp;&emsp;给某一个字段添加索引可以减少数据查询的时间，查询速度快，但需要额外的维护，因为数据在修改时可能需要对索引进行修改。

&emsp;&emsp;

### 与主键的关系

&emsp;&emsp;有**主键约束**和**唯一性约束**的字段会**自动添加索引**

&emsp;&emsp;

### 索引的适用情况

- 数据量庞大

- 该字段很少进行DML操作
- 该字段经常被查询

&emsp;&emsp;

### 语法

&emsp;&emsp;创建索引

```mysql
create index 索引名 on 表名(字段名);
```

&emsp;&emsp;删除索引

```mysql
drop index 索引名 on 表名;
```

&emsp;&emsp;

### 索引的分类

&emsp;&emsp;单一索引

&emsp;&emsp;复合索引

&emsp;&emsp;主键索引

&emsp;&emsp;唯一索引

&emsp;&emsp;

### 索引失效

&emsp;&emsp;**模糊查询**是若第一个通配符为 **%** 则索引会失效。





