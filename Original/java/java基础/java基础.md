---
title: java基础
date: ‎2021-0‎2‎-0‎6
description:  java数据类型，循环，数组，文件，输入输出
---





### main方法

1. main 方法必须声明为 public
2. Java 中的 main 方法必须是静态的 。
3. main 方法没有为操作系统返回 “ 退出代码 ” . 如果 main 方法正常退出 , 那么 Java 应用程序的退出代码为 0，如果希望在终止程序时返回其他的代码, 那就需要调用 System.exit 方法 。



### **特殊值**

1. **正无穷大**： Double.POSITIVE_INFINITY

2. **负无穷大**：Double.NEGATIVE_JNFINITY 

3. **NaN**：Double.NaN( 以及相应的 Float 类型的常量)

4. **检测一个特定值是否等于** Double.NaN

   ​	错误：if ( x == Double.NaN )

   ​	正确：if ( Double.isNaN(x))



### **转义序列**

转义序列 \u 还可以出现在加引号的字符常量或字符串之外

```java
public static void main ( String \u005B\u05D args )
```

Unicode 转义序列会在解析代码之前得到处理

" \u0022+\u0022 ” 并不是一个由引号( U+0022) 包围加号构成的字符串。 实际上 , \u0022 会在解析之前转换为 '' , 这会得到也就是一个空字符串。

一定要当心注释中的 \u 。 注释   // \u00A0 is a newline 会产生一个语法错误 , 因为读程序时 \u00A0 会替换为一个换行符



### 常量

1. 关键字 final 指示常量：final double CM_PER INCH = 2.54 ;

2. 类常量可以在一个类中的多个方法中使用 

   public static final double CM PER INCH = 2.54 ;

3. final 关键字只是表示存储在变量中的对象引用不会再指示其他对象，不过这个对象可以更改



### 数学运算与常量

1. **幂运算**

   语句 :  double y = Math.pow (x , a ) ;

2. **整数取余**

   表达式 n % 2 ，如果 n 为负, 这个表达式则为 - 1 。

   floorMod( x, 12 )

3. **$\pi$** 和 **e** 常量

   Math.PI
   Math.E

4. **Math类**运算速度快，**StrictMath类**运算精度高

5. **强制类型转换**

   int x = ( int ) x;

   **整型值**和**布尔值**之间不能进行相互转换 。

6. **四舍五入**运算

```java
Math.round(1.56)
```

6. 当参与 / 运算的**两个操作数都是整数**时 , 表示整数除法

7. 可以为**数字字面量加下划线,** 如用 1_000_000 表示一百万 。 这些下划线只是为了让人更易读 。



### **位运算符**

将数值转换为二进制数，对二进制数的每一位进行运算

```
& (" and")
| ("or")
^ (" XOr ")
~ ("not")
```

- \<\< ：左移运算符，将运算符**左边的对象向左移动运算符右边指定的位数**（**在低位补0**） 
- \>\>  ："有符号"右移运算 符，将运算符**左边的对象向右移动运算符右边指定的位数**。使用符号扩展机制，也就是说，**如果值为正，则在高位补0，如果值为负，则在高位补1****. 
- \>\>\>： "无符号"右移运算 符，将运算符**左边的对象向右移动运算符右边指定的位数**。采用0扩展机制，也就是说，**无论值的正负，都在高位补0** 



### **枚举类型**

```java
public class practice {
    enum Light {
        RED , GREEN , YELLOW ;
    }
    public static void main(String[] args){
        Light l = Light.GREEN;
        System.out.println(l);
    }
}
```

<img src="java基础\27.png" alt="27" style="zoom:80%;" />



### 字符串

1. 和python中一样也为**不可变类型**
2. **截取部分字符串**

```java
String greeting = "Hello";
String s = greeting.substring(0, 3);  //截取部分字符串，相当于python中的切片
```

3. Java 语言允许使用 + 号**连接 (拼接) 两个字符串** 。

4. 用指定字符**拼接字符串**

```java
public class practice {
    public static void main(String[] args){
        System.out.println(String.join("/", "1", "2", "3"));
    }
}
```

5. 使用 equals 方法检测**两个字符串是否相等** 。 

```java
s.equals(t);
"Hello".equals(greeting);
```

不区分大小写

```java
" Hello ".equalsIgnoreCase(" hello ");
```

**不能使用 == 运算符检测两个字符串是否相等**，== 只能够确定两个字串是否放置在同一个位置上 。

只有字符串常量是共享的, 而 + 或 substring 等操作产生的结果并不是共享的 。



#### **字符串的长度**

char 数据类型是一个采用 UTF - 16 编码表示 Unicode **码点（codeprint）**的**代码单元** 。

一个码点对应一个字符。

大多数字符的码点用**一个代码单元**表示，**增补字符**的码点是用**两个代码单元**来表示的，如𝕆

str.length()，length 方法将返回采用 UTF 16 编码表示的给定字符串所需要的**代码单元数量** 。

```java
System.out.println(s.codePointCount(0, s.length()));  //输出的是码点的数量
```

```java
public class practice {
    public static void main(String[] args){
        String s = "\uD835\uDD46";
        System.out.println(s);
        System.out.println(s.length());
        System.out.println(s.codePointCount(0, s.length()));
    }
}

输出：
𝕆
2
1
```



s.charAt(n)将返回位置 n 的代码单元

得到第 i 个码点 , 应该使用下列语句

```java
public class practice {
	public static void main(String[] args){
    String greeting = "hello";
    int index = greeting.offsetByCodePoints(0,2);
    int cp = greeting.codePointAt(index);
    System.out.println(cp);
    }
}
```



String 变量还可以存放一个特殊的值 , 名为 null



#### **遍历字符串**

```java
int[] codePoints = str.codePoints().toArray()
```

将字符串的码点变成对应的int值，放到一个数组中。

```java
String str = new String(codePoints, 0, codePoints.length);
```

将int数组变成对应的字符串



#### **字符串API**

<img src="java基础\1.png" alt="1" style="zoom:80%;" />

<img src="java基础\2.png" alt="2" style="zoom:80%;" />



#### **拼接字符串**

如果需要用许多小段的字符串构建一个字符串，那么应该按照下列步骤进行。首先，构建一个空的字符串构建器：

```java
StringBuilder builder = new StringBuilder();
```

当每次需要添加一部分内容时，就调用append方法。

```java
builder.append(ch)；//appends a single character 
builder.append(str)；//appends a string
```

在需要构建字符串时就调用toString方法，将可以得到一个String对象，其中包含了构建器中的字符序列。

```java
String completedString = builder.toString()；
```



**StringBuilder 类中的重要方法**

<img src="java基础\5.png" alt="5" style="zoom:80%;" />





### 输入

通过控制台进行输如入, 首先需要构造一个 Scanner 对象, 并与 “ 标准输人流 ” System.in 关联 。

```java
import java.util.Scanner;

public class practice {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in); //nextLine 方法将输入一行 。
        String data = input.nextLine();
        System.out.println(data);
    }
}
```

<img src="java基础\6.png" alt="6" style="zoom:80%;" />

### 输出

与C语言类似

```java
public class practice {
    public static void main(String[] args){
        System.out.printf("%d", 123);
    }
}
```



可以使用静态的 String.format 方法创建一个格式化的字符串, 而不打印输出 :

```java
String message = String.format ("Hello, %s. Next year, you' ll be %d" ,name, age) ;
```

<img src="java基础\7.png" alt="7" style="zoom:80%;" />

<img src="java基础\8.png" alt="8" style="zoom:80%;" />



### 文件

#### 文件读取 

```java
import java.io.IOException;
import java.nio.file.*;
import java.util.*;
public class practice {
    public static void main(String[] args) throws IOException {
		Scanner in = new Scanner(Paths.get("file.txt" ), "UTF-8");       	 		     		 System.out.println(in.nextLine());
    }
}
```

#### 文件写入

```java
import java.io.IOException;
import java.io.PrintWriter;
public class practice {
public static void main(String[] args) throws IOException {
	PrintWriter out = new PrintWriter("file.txt" , "UTF-8");
	out.print("hhh\n");
    out.close(); //如果不关闭文件，文件停留在缓冲区, 不会写入文件中
    }
}
```



### 循环

#### **遍历数组中的每一个元素**

与python中的 for i in a: 相似

```java
public class practice {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5, 6};
        for (int element : a)
            System.out.println(element);
    }
}
```



#### **跳出多层循环**

##### break

```java
public class practice {
    public static void main(String[] args) {
        int i = 0;
        break_label:
        while(i<10){
            for (int j = 0;j<5;j++){
                System.out.println(i+" "+j);
                if (j > 2){
                    break break_label; //将会break出 break_label 所在的循环
                }
            }
            i++;
        }
        System.out.println("end");
    }
}
```



##### continue

```java
public class practice {
    public static void main(String[] args) {
        int i = 0;
        continue_label:
        while (i < 10) {
            i++;
            for (int j = 0; j < 6; j++) {
                System.out.println(i+" "+j);
                if (j > 3) {
                    continue continue_label;
                }
            }
        }
        System.out.println("end");
    }
}
```





### 大数值

**java.math** 包中的两个
很有用的类 : Biglnteger 和 BigDecimaL 这两个类可以处理包含任意长度数字序列的数值 。

将普通的数值转换为大数值 :

```java
Biglnteger a = Biglnteger.valueOf(100) ;
```

**BigDecimal** ：任意精度的浮点数运算 。

加法：

```java
Biglnteger c = a.add(b)
```

乘法：

```java
Biglnteger d = c.multiply(b.add(Biglnteger.valueOf(2))); // d = c * ( b + 2)
```





### **数组**

#### 初始化

##### **一维数组**

```java
int [] small Primes = { 2 , 3 , 5 , 7 , 11 , 13 } ;
small Primes = new int[] { 17 , 19 , 23 , 29 , 31 , 37 } ;
```

##### **二维数组**

```java
double[][] balances ;
```

数组的声明不可以定义数组的大小，但可以**利用new来创建任意大小的数组**，

可以不需要初始化，就可以**在任意位置赋值**，与C语言不同。

**创建不规则二维数组**

```java
import java.util.Arrays;

public class practice {
    public static void main(String[] args) {
        final int NMAX = 10 ;
        int [][] odds = new int [NMAX + 1][];
        for ( int n = 0; n <= NMAX ; n++) {
            odds[n] = new int[n + 1];
            for (int j=0;j<n;j++){
                odds[n][j] = j;
            }
        }
        for (int i=0;i<NMAX;i++)
            System.out.println(Arrays.toString(odds[i]));
    }
}
```





#### 复制

##### **浅复制**

```java
int[] a = b;
```

此时改变a中某一个的元素的值将改变b数组也会发生改变

##### **深复制**

```java
int[] copiedLuckyNumbers = Arrays.copyOf(luckyNumbers, luckyNumbers.length ) ;
```

第 2 个参数是**新数组的长度**

这个方法通常用来增加数组的大小 :

```java
luckyNumbers = Arrays.copyOf(luckyNumbers , 2*luckyNumbers.length );
```

如果数组元素是数值型 , 那么**多余的元素将被赋值为 0** ; 如果数组元素是**布尔型**, 则将赋值
为 **false** 。 相反, 如果长度小于原始数组的长度, 则**只拷贝最前面的数据元素** 。



#### **排序**

对a数组排序

```java
Arrays.sort(a);
```

Math.random 方法将返回一个 0 到 1 之间 ( 包含 0 、不包含 1 ) 的随机浮点数 。



#### 数组常用API

<img src="java基础\9.png" alt="9" style="zoom:80%;" />

<img src="java基础\10.png" alt="10" style="zoom:80%;" />



### 泛型数组

#### 创建

尖括号中的类型参数不允许是基本类型 

```java
ArrayList<Employee> staff = new ArrayList<>();
```

如果已经清楚或能够估计出数组可能存储的元素数量，就可以在填充数组之前调用ensureCapacity方法：

```java
staff.ensureCapacity(100);
```

这个方法调用将分配一个包含100个对象的内部数组。然后调用100次add，而不用重新分配空间。
另外，还可以把初始容量传递给ArrayList构造器：

```java
ArrayList<Employee> staff = new ArrayList<>（100）；
```



#### 添加

使用 **add 方法**可以将元素添加到数组列表中 。



#### 元素数目

**size 方法**将返回数组列表中包含的实际元素数目 。

一旦能够确认数组列表的大小不再发生变化，就可以调用trimToSize方法。这个方法将存储区域的大小调整为当前元素数量所需要的存储空间数目。垃圾回收器将回收多余的存储空间。
		一旦整理了数组列表的大小，添加新元素就需要花时间再次移动存储块，所以应该在确认不会添加任何元素时，再调用trimToSize。



#### 数组操作

<img src="java基础\22.png" alt="22" style="zoom:80%;" />

<img src="java基础\23.png" alt="23" style="zoom:80%;" />



### 传入任意数量的参数

​	例如计算若干个数值的最大值 。

```java
public static double max(double... values){
	double largest = Double.NECATIVE_INFINITY; 
    for(double v: values)
        if(v > largest)
            largest=v;
    return largest;
}
```

