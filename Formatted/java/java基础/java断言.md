### java断言&emsp;  
&emsp;  
#### 语法&emsp;  
&emsp;  
```java
assert 条件;
```
&emsp;  
或&emsp;  
&emsp;  
```java
assert 条件:表达式;
```
&emsp;  
表达式是断言失败后程序的输出，&emsp;  
&emsp;  
例：&emsp;  
&emsp;  
```java
assert true;
System.out.println("断言1没有问题");

assert false : "断言失败，此表达式的信息将会在抛出异常的时候输出";
System.out.println("断言2没有问题");
```
&emsp;  
#### 断言的开启&emsp;  
&emsp;  
**命令行开启**&emsp;  
&emsp;  
在运行程序时用 -enableassertions 或 -ea 选项启用： &emsp;  
&emsp;  
```cmd
java -enableassertions MyApp
```
&emsp;  
**IDEA开启**&emsp;  
&emsp;  
1. &emsp;  
&emsp;  
![1](java断言\1.png)&emsp;  
&emsp;  
2. &emsp;  
&emsp;  
2. <img src="java断言\2.png" alt="2" width='700px' />&emsp;  
&emsp;  
3. <img src="java断言\3.png" alt="3" width='700px' />&emsp;  
&emsp;  
#### 断言的使用情景&emsp;  
&emsp;  
1. 断言失败是致命的、不可恢复的错误。&emsp;  
&emsp;  
2. 断言检查只用于开发和测阶段&emsp;  
