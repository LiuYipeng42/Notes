# BeanFactory

## BeanFactory的对象注册与依赖绑定方式

### 直接编码方式

​		使用的较少					

### 外部配置文件方式

​		Spring的IoC容器支持两种配置文件格式： Properties文件格式和XML文件格式。

Properties文件格式使用的较少，主要介绍XML文件格式

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN"
"http://www.springframework.org/dtd/spring-beans.dtd">

<beans>
    // bean 定义一个Bean实例的信息 通俗的讲就是一个对象
    // id 指定生成的Bean实例名称
    // name 指定生成的类的名字
    <bean id="newsProvider" class="..FXNewsProvider">   
        // property 用来配置Bean实例的依赖关系
        // name对应对象中的set方法，值为属性名
        // ref是另外一个 bean 的 id，代表依赖对象
        <property name="newsListener">                   
            <ref bean="djNewsListener"/>
        </property>
        <property name="newPersistener">
            <ref bean="djNewsPersister"/>
        </property>
    </bean>

    <bean id="djNewsListener"
        class="..impl.DowJonesNewsListener"> 
    </bean>

    <bean id="djNewsPersister"
        class="..impl.DowJonesNewsPersister">
    </bean>
</beans>
```



### 注解方式

​		在一个类的前面加上@Controller ，@Service， @Repository或@Component 来将这个类添加到容器中，然后在被注入对象的属性，setter方法或构造器上添加@Autowired注解，即可将相应类型的依赖注入到一个对象中。

各注解的解释：

**@Controller** 控制器（注入服务）
 		用于标注控制层，相当于struts中的action层

**@Service** 服务（注入dao）
 		用于标注服务层，主要用来进行业务的逻辑处理

**@Repository**（实现dao访问）
 		用于标注数据访问层，也可以说用于标注数据访问组件，即DAO组件

**@Component** （把普通pojo实例化到spring容器中，相当于配置文件中的 ）

​		泛指各种组件，就是说当我们的类不属于各种归类的时候（不属于@Controller、@Services等的时候），我们就可以使用@Component来标注这个类。



## XML

### XML配置文件的头部

在Spring 2.0版本之前，XML格式由Spring提供的DTD规定

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE beans PUBLIC "-//SPRING//DTD BEAN//EN" ➥ 9
"http://www.springframework.org/dtd/spring-beans.dtd">
<beans>
...
</beans>
```



​		从Spring 2.0版本之后， Spring在继续保持向前兼容的前提下，既可以继续使用DTD方式的DOCTYPE进行配置文件格式的限定，又引入了基于XML Schema的文档声明。

```xml-dtd
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:util="http://www.springframework.org/schema/util" 
xmlns:jee="http://www.springframework.org/schema/jee" 
xmlns:lang="http://www.springframework.org/schema/lang" 
xmlns:aop="http://www.springframework.org/schema/aop" 
xmlns:tx="http://www.springframework.org/schema/tx" 
xsi:schemaLocation="http://www.springframework.org/schema/beans 
http://www.springframework.org/schema/beans/spring-beans-2.0.xsd 
http://www.springframework.org/schema/util
http://www.springframework.org/schema/util/spring-util-2.0.xsd
http://www.springframework.org/schema/jee
http://www.springframework.org/schema/jee/spring-jee-2.0.xsd http://www.springframework.org/schema/lang 
http://www.springframework.org/schema/lang/spring-lang-2.0.xsd
http://www.springframework.org/schema/aop
http://www.springframework.org/schema/aop/spring-aop-2.0.xsd

http://www.springframework.org/schema/tx
http://www.springframework.org/schema/tx/spring-tx-2.0.xsd">
</beans>
```



### 基本标签

#### \<beans>

​		\<beans>是XML配置文件中最顶层的元素，它下面可以包含0或者1个\<description>和多个\<bean>以及\<import>或者\<alias>

#### \<description>

​		可以通过\<description>在配置的文件中指定一些描述性的信息。通常情况下，该元素是省略的。当然，如果愿意， \<description>随时可以为我们效劳。 

#### \<import>

​		通常情况下，可以根据模块功能或者层次关系，将配置信息分门别类地放到多个配置文件中。在想加载主要配置文件，并将主要配置文件所依赖的配置文件同时加载时，可以在这个主要的配置文件中通过\<import>元素对其所依赖的配置文件进行引用。

#### \<alias>

​		可以通过\<alias>为某些\<bean>起一些“外号”（别名） 

#### \<bean>

​		每个业务对象作为个体，在Spring的XML配置文件中是与\<bean> 元素一一对应的。

 

### 依赖注入配置

####  构造方法注入

​		在\<bean>中使用\<constructor-arg>

```xml-dtd
<bean id="djNewsProvider" class="..FXNewsProvider">
    <constructor-arg ref="djNewsListener"/>
    <constructor-arg>
    	<ref bean="djNewsPersister"/>
    </constructor-arg>
</bean>
```

​		有两种方式配置，可以使用 ref属性或\<ref>标签，ref表示要注入的依赖的\<bean>的id属性



#### setter方法注入

​		Spring为setter方法注入提供了\<property>元素，\<property>有一个**name属性**（ attribute），用来指定该\<property>将会注入的对象所对应的**实例变量名称**。之后通过value或者ref属性或者内嵌的其他元素来指定具体的依赖对象引用或者值，如以
下代码所示：

```xml-dtd
<bean id="djNewsProvider" class="..FXNewsProvider"> 2
	<property name="newsListener" ref="djNewsListener"/>
    <property name="newPersistener">
    	<ref bean="djNewsPersister"/>
    </property>
</bean>
```



### 对象的生命周期管理

​		容器中对象的生命周期管理由 \<bean> 的 scope属性来设置。类型有**singleton**，**prototype**，request、 session和global session类型，只有在支持Web应用的ApplicationContext中使用后三个scope才是合理的。



#### singleton

​		是spring默认的创建方式，在Spring的IoC容器中只存在一个实例，所有对该对象的引用将共享这个实例。该实例从容器启动，并因为第一次被请求而初始化之后，将一直存活到容器退出，也就是说，它与IoC容器“几乎”拥有相同的“寿命”



#### prototype

​		容器在接到该类型对象的请求的时候，会每次都重新生成一个新的对象实例给请求方。虽然这种类型的对象的实例化以及属性设置等工作都是由容器负责的，但是只要准备完毕，并且对象实例返回给请求方之后，容器就不再拥有当前返回对象的引用，请求方需要自己负责当前返回对象的后继生命周期的管理工作，包括该对象的销毁。



#### request

​		每 个 HTTP 请 求 创建 一 个 全 新的RequestProcessor对象供当前请求使用，当请求结束后，该对象实例的生命周期即告结束。从不是很严格的意义上说， request可以看作prototype的一种特例，除了场景更加具体之外，语意上差不多



#### session

​	对于Web应用来说，放到session中的最普遍的信息就是用户的登录信息，除了拥有session scope的bean的实例具有比request scope的bean可能更长的存活时间，其他方面真是没什么差别。



#### global session

​		global session只有应用在基于portlet的Web应用程序中才有意义，如果在普通的基于servlet的Web应用中使用了这个类型的scope，容器会将其作为普通的session类型的scope对待。



### 工厂方法与FactoryBean

​		接口的使用可以减少使用接口的类与接口实现类之间的过渡耦合，因为当接口的实现类变成另外一个实现类时，接口实现类改变之前与改变之后的数据类型都可以是接口名，不需要改变使用接口的类。此时可以再利用依赖注入，将实现类与接口对应起来，将接口的实现类自动注入到对应的接口变量中。

​		但若是要利用某一些第三方库的类，这些类可能并不能直接创建一个实例，需要借助一个工厂方法来返回一个此类的实例。这是就不能使用以前依赖注入的方法将实例注入到变量中。比如：

```java
public class Foo{
	private BarInterface barInterface;
	public Foo(){
        // 静态工厂方法
		barInterface = BarInterfaceFactory.getInstance();
	}
} 
```

或

```java
public class Foo{
	private BarInterface barInterface;
	public Foo(){
		// 非静态工厂方法
        barInterface = new BarInterfaceFactory().getInstance();
	}
} 
```



#### 静态工厂方法

​		将静态工厂方法的返回值添加到容器中，只需利用 \<bean> 的 factory-method 属性，如

```xml-dtd
<bean id="bar" class="...StaticBarInterfaceFactory" factory-method="getInstance"/>
```

​		class 属性指明 静态工厂方法所处的类，factory-method 指明静态工厂方法，若方法有参数，可以通过 \<constructor-arg> 来添加参数。



#### 非静态工厂方法

```xml-dtd
<bean id="barFactory" class="...NonStaticBarInterfaceFactory"/>
<bean id="bar" factory-bean="barFactory" factory-method="getInstance"/>
```

​		NonStaticBarInterfaceFactory是作为正常的bean注册到容器的，而bar的定义则与静态工厂方法的定义有些不同。现在使用factory-bean属性来指定工厂方法所在的工厂类实例，而不是通过class属性来指定工厂方法所在类的类型。指定工厂方法名则相同，都是通过factory-method属性进行的。

​		如果非静态工厂方法调用时也需要提供参数的话，处理方式是与静态的工厂方法相似的，都可以
通过 \<constructor-arg>来指定方法调用参数。



#### FactoryBean

​		可以使用 FactoryBean接口来方便的实现工厂方法的依赖注入。此接口定义如下：

```java
public interface FactoryBean {
    Object getObject() throws Exception;
    Class getObjectType();
    boolean isSingleton();
}
```

​		getObject()方法会返回该FactoryBean“生产”的对象实例。

​		getObjectType()方法仅返回getObject()方法所返回的对象的类型。

​		isSingleton()方法返回结果用于表明，工厂方法所 “生产” 的对象是否要以singleton形式存在于容器中。

​		使用一个类实现此接口后，使用正常的方式将 FactoryBean接口的实现类添加到容器中，将对应的 \<bean>的id 写到想要注入的对象的 \<bean>中即可。此时当真正依赖注入时，**并不会将 FactoryBean接口的实现类注入**，而是会将此实现类的 getObject() 方法的返回值注入。



## 基于注解的容器配置

### @Required

​		@Required注解 适用于 bean 属性设置器方法

https://www.docs4dev.com/docs/zh/spring-framework/5.1.3.RELEASE/reference/core.html#required

