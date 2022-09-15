## 反射

能够**分析类能力**的程序称为**反射**



### 作用

1. 在运行时**分析类的能力**。
2. 在**运行时查看对象**，例如编写一个 toString 方法供所有类使用。
3. 实现**通用的数组操作代码**。
4. 利用 Method 对象，这个对象很像C++中的**函数指针**。



### Class类

​		在java运行时，会给每一个对象维护一个RTTI（Run-Time Type Identification）运行时类型信息，用来跟踪每个对象所属的类。保存每一个类的信息的是Class类，每一个类都有一个Class类，而不是每一个对象有一个。

​		

### 获取一个类的Class对象

1. Object 类中的 **getClass( ) 方法**可以返回一个 Class 类型的实例

```java
对象名.getClass();
```

2. 可以调用**静态方法 forName** 直接获得类名对应的 Class 实例，不需要创建一个这个类的对象。

   ```
   String className = "java.util.Random";
   Class cl = Class.forName(className);
   ```

3. 一个对象的属性class是这个对象对应类的Class对象

   ```java
   Class cl1 = Random.class; // if you import java util
   Class cl2 = int.class;
   Class cl3 = Double[].class;
   ```



### 常用方法

**getName()方法**

getName方法可以返回对象所属**类的名字**，若这个类在一个包中，会返回**包名和类名**



**newInstance()方法**

根据一个Class对象，生成一个对应类的实例

```
String className = "java.util.Random";
Random r = Class.forName(className).newInstance();
```

​		newlnstance 方法调用**默认的构造器** ( 没有参数的构造器 ) 初始化新创建的对象。 如果这个类没有默认的构造器 , 就会抛出一个异常



### 利用反射分析类

​		在 **java.lang.reflect 包**中有三个类 **Field** 、**Method** 和 **Constructor** 分别用于描述类的**域**、**方法**和**构造器**。这**三个类**都有一个叫做 **getName 的方法**，用来**返回项目的名称**。**Field 类**有一个 **getType 方法**，用来返回描述域**所属类型的 Class 对象**。 **Method** 和 **Constructor** 类有能够报告**参数类型**的方法，**Method 类**还有一个可以报告**返回类型**的方法 。 这**三个类**还有一个叫做 **getModifiers** 的方法 , 它将返回一个整型数值，用不同的位开关描述 public 和 static 这样的**修饰符使用状况**。另外，还可以利用 java.lang.reflect 包中的 Modifier 类的静态方法分析 getModifiers 返回的整型数值。例如，可以使用 **Modifier 类**中的 **isPublic 、 isPrivate 或 isFinal判断方法或构造器是否是 public、private 或 final**。我们需要做的全部工作就是调用 Modifier类的相应方法，并对返回的整型数值进行分析，另外，还可以利用 **Modifier. toString 方法**将**修饰符打印**出来 。
​		**Class 类**中的 **getFields**、 **getMethods** 和 **getConstructors** **方法**将分别返回类提供的 **public 域**、**方法**和**构造器数组**，其中包括**超类的公有成员**。Class 类的 **getDeclareFields**、**getDeclareMethods** 和 **getDeclaredConstructors 方法**将分别返回**类中声明的全部域**、**方法**和**构造器**，其中包括**私有和受保护成员**，但**不包括超类的成员** 。

