---
title: mysql的DML(数据操作)语句
date: 2021-02-15 22:56:37
description: mysql的数据查询基础语法，查询中的排序，连接查询，完整的DQL语句
---

&emsp;&emsp;

##  DQL语句

### 查询

#### 查询字段

```mysql
select '字段名','字段名',... from tableName;
```

&emsp;&emsp;

##### 在对查询出的数据进行命名

&emsp;&emsp;例如将num显示为Number

```mysql
select num as Number from tableName;
```

&emsp;&emsp;**真实的字段名并没有改变**

&emsp;&emsp;其中 as 关键字可以省略

&emsp;&emsp;

#### 查看表中所有数据

```
select * from tableName;
```

&emsp;&emsp;

#### 条件查询

##### 语法

```mysql
select '字段名1','字段名2',... from '表名' where 条件;
```

&emsp;&emsp;在条件中，若条件中有字符串，则**字符串**用**单引号**括住

&emsp;&emsp;在数据库中**null不是一个值**，代表什么也没有，**为空**，0与null不相等

&emsp;&emsp;当运算符**优先级不确定**时要利用**括号**来解决

&emsp;&emsp;

##### 运算符

| 运算符                  | 说明                                                         |
| ----------------------- | ------------------------------------------------------------ |
| =                       | 等于                                                         |
| <> 或 !=                | 不等于                                                       |
| <                       | 小于                                                         |
| <=                      | 小于等于                                                     |
| >                       | 大于                                                         |
| \>=                     | 大于等于                                                     |
| ... between ... and ... | 为左闭右开区间，左边的数要小与右边的数，也可以使用**字符**   |
| is null                 | 为null（is not null不为空）                                  |
| and                     | 并且                                                         |
| or                      | 或者                                                         |
| in(数值，数值)          | 包含，相当与多个 or，可以与not一起使用，not in(数值，数值)   |
| not                     | not可以取非，用于is或in中                                    |
| like                    | like为模糊**查询**，支持%（任意的任意多个字符）或下划线_（任意的单个字符）匹配。 |

**模糊查找**

&emsp;&emsp;例如：

```mysql
select name from tableName where name like '%\_%';
```

&emsp;&emsp;查找name中有 '_' 的数据，**'\‘ 为转义字符**。

&emsp;&emsp;

#### 查询去重

&emsp;&emsp;在select后加distinct

```mysql
select distinct num from tableName;
```

&emsp;&emsp;

### 查询中的排序

#### 语法

```mysql
select '字段名1','字段名2',... from '表名' order by '字段名';
```

&emsp;&emsp;

#### 升序和降序

&emsp;&emsp;**默认为升序**，可在结尾添加asc（升序）和desc（降序）来选择。

&emsp;&emsp;例如：

```mysql
select '字段名1','字段名2',... from '表名' order by '字段名' desc;
```

```mysql
select '字段名1','字段名2',... from '表名' order by 字段名所在的列的数字 desc;
```

&emsp;&emsp;

#### 多字段排序

```mysql
select '字段名1','字段名2', ... from '表名' order by '字段名' desc, '字段名' asc, ...;
```

&emsp;&emsp;会先按照第一个字段降序，若**遇到相等的情况**，再按照第二个字段升序，依次类推。

&emsp;&emsp;

### 查询与排序结合

&emsp;&emsp;**语法格式**

```mysql
select ... from ... where ... order by ...
```

&emsp;&emsp;

### 分组函数 (Group Function)

#### 多行处理函数

1. 分组函数也叫**多行处理函数**，

2. 所有的分组函数都是对某一组数据进行操作的，只有五个函数，有：

   count 计数

   sum 求和

   avg 平均值

   max 最大值

   min 最小值

3. 分组函数会**自动忽略null**，不需要用 is not null 来选择

   例如：

```mysql
select sum(num) from tableName;
```

&emsp;&emsp;&emsp;&emsp;对查询出的数进行求和

4. 分组函数**不可以使用在 where 语句中**。分组函数是在group by语句执行并分完组之后才会执行，而group by是在where执行之后才会执行。此时若有group by语句，where执行时分组函数还不能运行，因为group by语句没有执行。若没有group by语句，where执行后整张表会被作为一组，但where执行时，依旧没有完成分组，where执行时分组函数也不能运行，所以会出错。
5. **count(*)**统计的是**总记录的数量**，而不是某个字段中数据的个数。**count(字段)**统计的是某一字段中**不为null的数据总数**



#### 单行处理函数

&emsp;&emsp;直接在字段上运算

&emsp;&emsp;例如：

```mysql
select (num1 + num2)*42 from tableName;
```

&emsp;&emsp;将每一行的 num1 字段和 num2 字段的数相加后，再乘42后，最后将每一行的结果输出

&emsp;&emsp;运算时要注意null，因为只要数学表达式中有**null出现**，最终**结果都为null**。

&emsp;&emsp;可以利用 **ifnull() 函数**来处理null，例如：

```mysql
select (num1 + ifnull(num2, 0))*42 from tableName;
```

&emsp;&emsp;若num2为null，则会被当作 0 来处理。

&emsp;&emsp;

#### 分组查询与分组函数

1. **group by**：按照某个字段或者某些字段进行分组

2. 分组函数一般都会和group by联合使用，这也是这些函数被称为分组函数的原因。并且**分组函数都是在group by语句执行之后才会执行**的。当一个sql语句没有group by的话，整张表被作为一组数据。

   例：

   ```mysql
   select max(字段名) from 表名 group by 字段名;
   ```

   先按照某一个字段名进行分类（相同的为一类），然后找出每一类的最大值。

3. 分组查询后，select后查询的字段只能是**分组查询用到的字段**和**分组函数**

4. 可以进行**多字段分组**，例：

```mysql
select max(字段名) from 表名 group by 字段名1, 字段名2;
```

&emsp;&emsp;先按照第一个字段进行分组，然后在分好的每组中再按照第二个字段分组。

5. **having**：having是对分组后的数据进行再次过滤，与where相似，但可以使用分组函数，因为group by已经执行。**可以用where完成的目标要尽量用where**，因为having处理的是分组之后的数据，过滤之后舍弃了很多处理后（分组）的数据，效率低。若用where可以在分组前过滤掉不符合条件的数据，这些数据不会被分组，效率高。



### 连接查询

&emsp;&emsp;连接查询**分类**：

&emsp;&emsp;**内连接**：等值连接，非等值连接，自连接

&emsp;&emsp;**外连接**：左连接，右连接

&emsp;&emsp;**全连接**

&emsp;&emsp;

#### 内连接

**内连接**：假设A和B表进行连接，使用内连接的话，凡是A表和B表能够匹配上的记录查询出来。

**inner join**：表明将连个表连接起来，可简写为 **join**

**on**：后面写上连接的条件，on后可以**加上where**做进一步的过滤

&emsp;&emsp;

##### 等值连接

&emsp;&emsp;条件是**等量关系**，即若几张表中的几个字段的值相等，则将数据连接起来组成一条记录

**例：**

```
DEPT表：
+--------+------------+----------+
| deptno | dname      | loc      |
+--------+------------+----------+
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | SALES      | CHICAGO  |
+--------+------------+----------+
EMP表：
+--------+--------+
| ename  | deptno |
+--------+--------+
| SMITH  |     20 |
| ALLEN  |     10 |
| WARD   |     30 |
| JONES  |     20 |
| MARTIN |     30 |
| BLAKE  |     30 |
| CLARK  |     10 |
+--------+--------+
```

&emsp;&emsp;在EMP表中按照deptno将每一个ename与DEPT中相应的dname对应。

&emsp;&emsp;**笛卡尔积现象**

```mysql
select EMP.ename, DEPT.dname from EMP join DEPT;
```

```
+--------+------------+
| ename  | dname      |
+--------+------------+
| SMITH  | SALES      |
| SMITH  | RESEARCH   |
| SMITH  | ACCOUNTING |
| ALLEN  | SALES      |
| ALLEN  | RESEARCH   |
| ALLEN  | ACCOUNTING |
.	.	.21 rows in set (0.00 sec)
```

&emsp;&emsp;此语句会出现**笛卡尔积现象**，即所要查询的字段按照顺序遍历所有可能出现的情况，查询结果共有21行。

&emsp;&emsp;在后面用关键字 on 加上筛选条件可以得到想要的结果，但查询次数不变依旧是21行，只是将结果筛选了出来。

```mysql
select EMP.ename, DEPT.dname from EMP join DEPT on EMP.deptno = DEPT.deptno;
```

&emsp;&emsp;EMP.deptno与DEPT.deptno分别表示表EMP中的deptno和表DEPT中的deptno

```mysql
select e.ename, d.dname from EMP as e join DEPT as d on e.deptno = d.deptno;
```

&emsp;&emsp;as关键词可以给表起别名，e和d分别是EMP和DEPT的**别名**，这样写更方便。也可以将 as 省略

```mysql
select e.ename, d.dname from EMP e join DEPT d on e.deptno = d.deptno;
```

&emsp;&emsp;

##### 非等值连接

&emsp;&emsp;连接条件中的关系是**非等量关系**

&emsp;&emsp;**例：**

```
SALGRADE表
+-------+-------+-------+  
| grade | losal | hisal | losal是最小值 hisal是最小值
+-------+-------+-------+
|     1 |   700 |  1200 |
|     2 |  1201 |  1400 |
|     3 |  1401 |  2000 |
|     4 |  2001 |  3000 |
|     5 |  3001 |  9999 |
+-------+-------+-------+
EMP表：
+--------+---------+
| ename  | sal     |
+--------+---------+
| SMITH  |  800.00 |
| ALLEN  | 1600.00 |
| WARD   | 1250.00 |
| JONES  | 2975.00 |
| MARTIN | 1250.00 |
| BLAKE  | 2850.00 |
| CLARK  | 2450.00 |
+--------+---------+
```

&emsp;&emsp;在EMP表中，对于每条记录的sal字段的数据，按照SALGRADE表的标准进行分类，即找到对应的grade。

```mysql
select e.ename, e.sal from EMP e join SALGRADE s where e.sal between s.losal and s.hisal;
```

&emsp;&emsp;

##### 自连接

&emsp;&emsp;将一张表看作两张表。自连接也可以分为等值与不等值连接

**例：**

```
+-------+--------+------+   empno：员工编号
| empno | ename  | mgr  |	ename：员工姓名
+-------+--------+------+	mgr：每一个员工领导的编号
|  7369 | SMITH  | 7902 |		 
|  7499 | ALLEN  | 7698 |
|  7521 | WARD   | 7698 |
|  7566 | JONES  | 7839 |
|  7654 | MARTIN | 7698 |
|  7698 | BLAKE  | 7839 |
|  7782 | CLARK  | 7839 |
|  7788 | SCOTT  | 7566 |
|  7839 | KING   | NULL |
|  7844 | TURNER | NULL |
|  7876 | ADAMS  | 7788 |
|  7900 | JAMES  | NULL |
|  7902 | FORD   | 7566 |
|  7934 | MILLER | 7782 |
+-------+--------+------+
```

&emsp;&emsp;将每一个员工与其领导的名字对应

```mysql
select e.ename as '员工名', m.ename as '领导名' from EMP e join EMP m on e.mgr = m.empno;
```

&emsp;&emsp;可以**多次利用一张表**，并可以将一张表**起不同的别名**。

&emsp;&emsp;这里的as关键词也是起别名的意思，只不过改的是最终查询结果中显示的字段名，也可以省略。

```mysql
select e.ename as '员工名', m.ename as '领导名' from EMP e join EMP m on e.mgr = m.empno;
```

&emsp;&emsp;

#### 外链接

**&emsp;&emsp;外连接**：假设A和B表进行连接，使用外连接的话，AB两张表中有一张表是主表，一张表是副表，主要查询主表中的数据，捎带着查询副表，当副表中的数据没有和主表中的数据匹配上，副表自动模拟出NULL与之匹配。分为左外连接与右外连接。

&emsp;&emsp;

&emsp;&emsp;**left outer join**：将两个表以**左外连接**的方式连接起来**左边**的表为**主表**，与内连接的inner可以省略一样，outer可省略

​        **right outer join**：将两个表以**右外连接**的方式连接起来**右边**的表为**主表**，与内连接的inner可以省略一样，outer可省略

左外连接有右外连接的写法，右外连接也会有对应的左外连接的写法。

&emsp;&emsp;

&emsp;&emsp;以自连接的例子为例。

&emsp;&emsp;**例：**

```
+-------+--------+------+	empno：员工编号
| empno | ename  | mgr  |	ename：员工姓名
+-------+--------+------+	mgr：每一个员工领导的编号
|  7369 | SMITH  | 7902 |
|  7499 | ALLEN  | 7698 |
|  7521 | WARD   | 7698 |
|  7566 | JONES  | 7839 |
|  7654 | MARTIN | 7698 |
|  7698 | BLAKE  | 7839 |
|  7782 | CLARK  | 7839 |
|  7788 | SCOTT  | 7566 |
|  7839 | KING   | NULL |
|  7844 | TURNER | 7698 |
|  7876 | ADAMS  | 7788 |
|  7900 | JAMES  | 7698 |
|  7902 | FORD   | 7566 |
|  7934 | MILLER | 7782 |
+-------+--------+------+
```

&emsp;&emsp;将每一个员工与其领导的名字对应

&emsp;&emsp;若利用**自连接查询**，即

```mysql
select e.ename as '员工名', m.ename as '领导名' from EMP e join EMP m on e.mgr = m.empno;
```

&emsp;&emsp;ename为KING的记录的在查询结果中并没有。因为这个员工没有领导。

&emsp;&emsp;

&emsp;&emsp;若利用**左外连接**，即

```mysql
select e.ename as '员工名', m.ename as '领导名' from EMP e left join EMP m on e.mgr = m.empno;
```

&emsp;&emsp;与自连接的区别是，jion前加了**left关键字**，表明左边的表（EMP e）是主表。

&emsp;&emsp;

&emsp;&emsp;若利用**右外连接**，即

```mysql
select e.ename as '员工名', m.ename as '领导名' from EMP m right join EMP e on e.mgr = m.empno;
```

&emsp;&emsp;jion前加了**right关键字**，表明右边的表（EMP e）是主表。

&emsp;&emsp;

#### 全连接

&emsp;&emsp;使用较少

&emsp;&emsp;

#### 三张表以上的连接查询

&emsp;&emsp;例如：

```mysql
select ... from A a jion B b on ... join C c on ...; 
```

&emsp;&emsp;表明先进行表A与表B的内连接查询，查询得到的结果再与C进行内连接查询

```mysql
select ... from A a jion B b on ... left join C c on ...;
```

&emsp;&emsp;表明先进行表A与表B的内连接查询，查询得到的结果再与C进行外连接查询，并且表A与表B的查询结果作为主表。

&emsp;&emsp;

### 子查询

&emsp;&emsp;**子查询：**一个mysql语句嵌套在另一个mysql语句中

&emsp;&emsp;子查询**可以出现的位置**：

1. select后 
2. from后
3. where后

&emsp;&emsp;

### union

&emsp;&emsp;可以将两个查询结果的表相接

```mysql
select ... from ...unionselect ... from ... ;
```

&emsp;&emsp;

### limit

&emsp;&emsp;limit是**mysql特有**的sql语句，可以取结果集中的部分数据

#### 语法：

```mysql
limit startIndex, length
```

&emsp;&emsp;startIndex表示起始位置

&emsp;&emsp;length表示取几条数据

&emsp;&emsp;limit位于**sql语句的最后**

**&emsp;&emsp;例：**

```mysql
select ... from ... limit startIndex, length;
```

&emsp;&emsp;可以不写startIndex，这时startIndex视为 0

```mysql
select ... from ... limit length;
```

&emsp;&emsp;

&emsp;&emsp;

### 完整DQL语句

```mysql
       select ... from ... where ... group by ... having ... order by ... limit ...
执行顺序   5         1        2           3           4           6			  7
```

&emsp;&emsp;或

```mysql
       select ... from ... join ... on ... group by ... having ... order by ... limit ...
执行顺序   6         1        2       3         4           5			7			8
```

