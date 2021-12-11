---
title: mysql8首次安装密码设置
date: 2021-03-21 16:23:33
description: JDBC编程步骤: 注册驱动，获取连接，获取数据库操作对象，执行SQL语句，处理查询结果集，释放资源
---



### JDBC编程步骤

1. **注册驱动**

   让java知道用的是那一个数据库

2. **获取连接**

   表示JVM的进程和数据库之间的通道打开了

3. **获取数据库操作对象**

4. **执行SQL语句**

5. **处理查询结果集**

   若上一步执行的是select语句才有这一步

6. **释放资源**

   java和数据库的连接属于进程间的通信，使用完成后必须关闭



```mysql
import java.sql.*;


public class Exp {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet result = null;
        try {
            // 1.注册驱动
            // Driver driver = new com.mysql.cj.jdbc.Driver();
            // DriverManager.registerDriver(driver);
            // 以下方法最常用，因为参数是字符串，字符串可以从***.properties文件中读取
            // 若使用此种方法要多捕获一个ClassNotFoundException异常
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2.获取连接
            // url格式：协议://ip:端口/资源名称
            //         jdbc:mysql://数据库ip:数据库端口/数据库名称
            String url = "jdbc:mysql://127.0.0.1:3306/test";
            String user = "root";
            String password = "123456";
            conn = DriverManager.getConnection(url, user, password);

            // 3.获取数据库操作对象
            stmt = conn.createStatement();

            // 4.执行sql
            // executeUpdate 用于执行DML语句（insert update delete）, 
            // 返回值是执行的sql语句影响的记录的数量
            // executeQuery 用于执行DQL语句（select）, 返回值是ResultSet
            // ResultSet 是结果集，查询的结果储存在结果集中

            int count;
            // 插入
            String sql = "insert into EMP(empno, ename) values (42, 'zima_blue');";
            count = stmt.executeUpdate(sql);
            System.out.println(count);
            //删除
            sql = "delete from EMP where empno = 42;";
            count = stmt.executeUpdate(sql);
            System.out.println(count);
            //查询
            sql = "select * from EMP;";
            result = stmt.executeQuery(sql);

            // 5.处理查询结果集
            String num;
            String name;
            String job;
            // ResultSet结果集对象的next()可以将游标向下移动一行记录，
            // 方法返回一个布尔值，若有下一行数据就返回true，若没有就返回false
            while (result.next()){
                // result 的 getString 方法可以将游标所在记录的指定字段的数据转换成字符串
                // 参数可以是字段名，也可以是字段索引，字段索引的下标从 1 开始
                // 若在sql语句中对字段名起了别名，对应字段名要换成别名
                // 根据不同的数据类型还有 getInt 和 getDouble 方法
                num = result.getString(1);
                name = result.getString(2);
                job = result.getString(3);
                System.out.println(num + " " +name + " " + job);
            }

        } catch (SQLException | ClassNotFoundException throwables) {
            // SQlException是sql语句不符合语法数据库抛出的异常
            throwables.printStackTrace();
        } finally {
            // 6.释放资源
            // finally 可以保证资源一定得到释放
            // 释放的顺序按照获取顺序的反序
            try {
                if (result != null) {
                    result.close();
                }
                if (stmt != null) {
                    stmt.close();
                }
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException throwables) {
                throwables.printStackTrace();
            }

        }
    }
}

```

