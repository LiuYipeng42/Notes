---&emsp;  
title: mysql的视图&emsp;  
date: 2021-02-17 11:56:44&emsp;  
description: mysql视图的创建，删除和查询&emsp;  
---&emsp;  
&emsp;  
## 视图&emsp;  
&emsp;  
&emsp;&emsp;&emsp;  
&emsp;  
**创建视图**&emsp;  
&emsp;  
```mysql
create view 视图名称 as select ... from ...;
```
&emsp;  
&emsp;&emsp;利用查询出来的数据创建视图&emsp;  
&emsp;  
&emsp;&emsp;&emsp;  
&emsp;  
**删除视图**&emsp;  
&emsp;  
```mysql
drop view 视图名称;
```
&emsp;  
&emsp;&emsp;&emsp;  
&emsp;  
**查询视图**&emsp;  
&emsp;  
```mysql
select ... from 视图名;
```
&emsp;  
&emsp;&emsp;&emsp;  
&emsp;  
&emsp;&emsp;对视图进行增删查改会直接影响到原始数据&emsp;  
&emsp;  
&emsp;  
