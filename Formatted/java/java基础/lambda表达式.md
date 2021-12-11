---&emsp;  
title: lambda表达式&emsp;  
date: ‎2021-0‎2‎-0‎6&emsp;  
description:  lambda表达式的语法，作用。变量作用域，函数式接口，方法引用和构造器引用&emsp;  
---&emsp;  
&emsp;  
## lambda表达式&emsp;  
&emsp;  
### 语法&emsp;  
&emsp;  
1. (参数) -> 表达式&emsp;  
&emsp;  
​&emsp;&emsp;例：(int a, int b) -> a + b&emsp;  
&emsp;  
2. 如果代码要完成的计算无法放在一个表达式中，就可以像写方法一样，把这些代码放在{}中，并包含显式的return语句。例如：&emsp;  
&emsp;  
   ```java
   （String first，String second）->{
   	if (first.length() < second.length())
   		return -1；
   	else if（first.length() > second.length()）
   		return 1；
   	else return 0；
   }
   ```
&emsp;  
3. 即使lambda表达式**没有参数**，仍然要提供空括号，就像无参数方法一样&emsp;  
&emsp;  
4. 如果可以推导出一个lambda表达式的参数类型，则可以**忽略其类型**，若只有一个参数，则可以**省略括号**&emsp;  
&emsp;  
5. 无需指定lambda表达式的**返回类型**。lambda表达式的返回类型总是会由上下文推导得出。&emsp;  
&emsp;  
### 作用&emsp;  
&emsp;  
使用lambda表达式的重点是**延迟执行**（deferred execution）。毕竟，如果想要立即执行代码，完全可以直接执行，而无需把它包装在一个lambda表达式中。之所以希望以后再执行代码，这有很多原因，如：&emsp;  
&emsp;  
1. 在一个单独的线程中运行代码；&emsp;  
2. 多次运行代码；&emsp;  
3. 在算法的适当位置运行代码（例如，排序中的比较操作）；&emsp;  
4. 发生某种情况时执行代码（如，点击了一个按钮，数据到达，等等）；&emsp;  
5. 只在必要时才运行代码。&emsp;  
&emsp;  
### 变量作用域&emsp;  
&emsp;  
lambda表达式可以在lambda表达式中访问外围方法或类中的变量&emsp;  
&emsp;  
例：&emsp;  
&emsp;  
```java
public static void repeatMessage(String text, int delay){
    ActionListener listener = event -> System.out.println(text);
    new Timer(delay, listener);
}
```
&emsp;  
text变量并不是lambda表达式中的。&emsp;  
&emsp;  
类似text变量的变量称为自由变量，自由变量被lambda表达式**捕获**（captured）。一个lambda表达式转换为包含一个方法的对象，这样自由变量的值就会复制到这个对象的实例变量中。&emsp;  
&emsp;  
lambda表达式中捕获的变量必须实际上是**最终变量** ( effectively final ) ，实际上的最终变量是指，这个**变量初始化之后就不会再为它赋新值**，例如String。&emsp;  
&emsp;  
lambda表达式中声明与一个**局部变量同名的参数**或局部变量是不合法的。&emsp;  
&emsp;  
在一个lambda 表达式中使用this 关键字时，是指创建这个lambda表达式的方法的this参数。&emsp;  
&emsp;  
### 函数式接口&emsp;  
&emsp;  
对于只有一个抽象方法的接口，需要这种接口的对象时，就可以提供一个lambda表达式。这种接口称为**函数式接口**，也可以理解为给一个方法传入一段代码进行运行。&emsp;  
&emsp;  
例：&emsp;  
&emsp;  
```java
public interface Predicate<T>
	boolean test(T t);
}
```
&emsp;  
ArrayList类有一个removelf方法，它的参数就是一个Predicate。&emsp;  
&emsp;  
下面的语句将从一个数组列表删除所有null值：&emsp;  
&emsp;  
接口：&emsp;  
&emsp;  
```java
class deletNull implements Predicate<T>{
    boolean test(T t){
    	if (t == null)
            return true;
        return false;
    }
}
```
&emsp;  
创建一个deletNull类的对象，然后将此对象传入removelf方法&emsp;  
&emsp;  
lambda表达式：&emsp;  
&emsp;  
```java
list.removeIf(e->e==null)；
```
&emsp;  
或&emsp;  
&emsp;  
```java
Predicate p = e->e==null;
list.removeIf(p);
```
&emsp;  
可以**将一个lambda表达式赋值**给一个对应接口类型的变量。&emsp;  
&emsp;  
#### 创建函数式接口&emsp;  
&emsp;  
创建函数式接口尽量使用**已有的接口**&emsp;  
&emsp;  
<img src="lambda表达式\1.png" alt="1" width='700px' />&emsp;  
&emsp;  
​                           <img src="lambda表达式\2.png" alt="1" width='700px' />&emsp;  
&emsp;  
例如：&emsp;  
&emsp;  
```java
public static void repeat(int n, Runnable action){
    for(inti=0;i<n;i++) 
        action.run(); // 因为接口只是一个类，所以要用接口中要实现的方法
}
```
&emsp;  
用以下代码使用&emsp;  
&emsp;  
```java
repeat(10, 0 -> System.out.println("Hello,World!"))；
```
&emsp;  
也可以利用**创建的接口**&emsp;  
&emsp;  
例如：&emsp;  
&emsp;  
接口&emsp;  
&emsp;  
```java
public interface IntConsumer{
    void accept(intvalue);
}
```
&emsp;  
方法&emsp;  
&emsp;  
```java
public static void repeat(int n, IntConsumer action){
    for(inti=0;i<n;i++)
        action.accept(i);
}
```
&emsp;  
调用&emsp;  
&emsp;  
```java
repeat(10, i -> System.out.println("Countdown:" + (9 - i)));
```
&emsp;  
### 方法引用&emsp;  
&emsp;  
若有现成的方法可以达到你想要传递到某个方法的作用，则可以使用**方法引用**。&emsp;  
&emsp;  
::操作符分隔方法名与对象或类名，主要有3种情况：&emsp;  
&emsp;  
1. **object::instanceMethod**&emsp;  
2. **Class::staticMethod**&emsp;  
3. **Class::instanceMethod**&emsp;  
&emsp;  
在**前2种情况**中，方法引用等价于提供方法参数的 lambda 表达式。&emsp;  
&emsp;  
例：System.out::println 等价于 x -> System.out.println（x）。&emsp;  
&emsp;  
对于**第3种情况**，第1个参数会成为方法的目标。&emsp;  
&emsp;  
例：String::compareTolgnoreCase 等价于 (x，y) -> x.compareTolgnoreCase(y)。&emsp;  
&emsp;  
可以在方法引用中使用 **this**，**super** 参数。&emsp;  
&emsp;  
例如，this::equals 等同于 x -> this.equals(x)。&emsp;  
&emsp;  
### 构造器引用&emsp;  
&emsp;  
构造器引用与方法引用很类似，只不过方法名为new。&emsp;  
&emsp;  
例如，Person::new是Person构造器的一个引用。&emsp;  
&emsp;  
可以用**数组类型**建立构造器引用。&emsp;  
&emsp;  
例如，int[]::new 等价于 x -> new int[x]。&emsp;  
&emsp;  
&emsp;  
