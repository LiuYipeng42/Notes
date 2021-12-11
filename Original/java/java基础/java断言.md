### java断言

#### 语法

```java
assert 条件;
```

或

```java
assert 条件:表达式;
```

表达式是断言失败后程序的输出，

例：

```java
assert true;
System.out.println("断言1没有问题");

assert false : "断言失败，此表达式的信息将会在抛出异常的时候输出";
System.out.println("断言2没有问题");
```



#### 断言的开启

**命令行开启**

在运行程序时用 -enableassertions 或 -ea 选项启用： 

```cmd
java -enableassertions MyApp
```



**IDEA开启**

1. 

![1](java断言\1.png)

2. 

2. <img src="java断言\2.png" alt="2" style="zoom: 50%;" />

3. <img src="java断言\3.png" alt="3" style="zoom: 50%;" />



#### 断言的使用情景

1. 断言失败是致命的、不可恢复的错误。

2. 断言检查只用于开发和测阶段