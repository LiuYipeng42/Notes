# Java对动态语言的支持

## 动态语言

​		动态类型语言的关键特征是它的**类型检查**的主体过程是**在运行期而不是编译期**进行的。java 类型检查就是静态分派，所以 java在编译期完成的静态分派，java语言就是静态语言。

​		动态语言（如Python）在编译时并不会关心一个引用是什么类型，此变量的类型是否有要调用的方法与属性，若没有则只会在运行期抛出异常。



## Java与动态语言

​		Java虽是静态语言，但 Java 虚拟机的目标是同一个虚拟机之上可以实现静态类型语言的严谨与动态类型

语言的灵活。所以 Java对动态语言进行了一些支持。



### java.lang.invoke 包

​		这个包的主要目的是在之前单纯依靠符号引用来确定调用的目标方法这条路之外，提供一种新的**动**
**态确定目标方法的机制，称为“方法句柄”（Method Handle）**。

```java
class ClassA {
    public void println(String s) {
    	System.out.println(s);
    }
}

public class MethodHandleTest {
    
	private static MethodHandle getPrintlnMH(Object reveiver) throws Throwable {
        // MethodType：代表“方法类型”，包含了方法的返回值（methodType()的第一个参数）和
        // 具体参数（methodType()第二个及以后的参数）。
        MethodType mt = MethodType.methodType(void.class, String.class);
        // lookup()方法来自于 MethodHandles.lookup，
        // 这句的作用是在指定类中查找符合给定的方法名称、方法类型，并且符合调用权限的方法句柄。
        // 因为这里调用的是一个虚方法，按照 Java 语言的规则，方法第一个参数是隐式的，
        // 代表该方法的接收者，也即 this 指向的对象，
        // 这个参数以前是放在参数列表中进行传递，现在提供了 bindTo()方法来完成这件事情。
        return 
            lookup().findVirtual(reveiver.getClass(), "println", mt).bindTo(reveiver);
    }
    
    public static void main(String[] args) throws Throwable {
        Object obj = System.currentTimeMillis() % 2 == 0 ? System.out : new ClassA();
        // 无论 obj 最终是哪个实现类，下面这句都能正确调用到 println 方法并输出 hello。
        getPrintlnMH(obj).invokeExact("hello");
    }
}
```

​		代码在编译期并不能获得 obj引用的准确类型，也编译期并没有进行类型检查，检查此对象是否有println方法（因为并没有直接调用此方法），而是在运行时利用 Java代码进行类型检查。

​		方法 getPrintlnMH()中实际上是模拟了 invokevirtual 指令的执行过程，只不过它的分派逻辑并非固化在 Class 文件的字节码上，而是通过一个由用户设计的 Java 方法来实现。而这个方法本身的返回值（MethodHandle 对象），可以视为对最终调用方法的一个“引用”。



### invokedynamic 指令

​		java.lang.invoke 包用上层代码和 API 来实现在运行期进行类型检查，而invokedynamic 指令则是<u>用字节码和 Class 中其他属性、常量来完成运行期进行类型检查</u>。

​		每一处含有 invokedynamic 指令的位置都被称作**动态调用点（DynamicallyComputed Call Site）** ，这条指令的第一个参数不再是代表方法符号引用的 CONSTANT_Methodref_info 常量，而是变为 JDK 7 时新加入的 **CONSTANT_InvokeDynamic_info 常量**，从这个新常量中可以得到 3 项信息：**引导方法**（Bootstrap Method，该方法存放在新增的 BootstrapMethods 属性中）、**方法类型**（MethodType）和**名称**。引导方法是有固定的参数，并且返回值规定是 java.lang.invoke.CallSite 对象，这个对象代表了真正要执行的目标方法调用。根据 CONSTANT_InvokeDynamic_info 常量中提供的信息，虚拟机可以找到并且执行引导方法，从而获得一个 CallSite 对象，最终调用到要执行的目标方法上。



