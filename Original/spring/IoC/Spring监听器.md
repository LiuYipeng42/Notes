# Spring容器内部事件发布



​		自定义事件发布有三个组成部分**自定义事件**，**自定义事件监听器**和**事件发布者**。自定义事件监听器用于**接收**自定义事件，事件发布者用于**通知**自定义事件监听器和**发布**自定义事件：

1. **自定义事件**：

   ​		ApplicationEvent类型的事件，ApplicationEvent是一个**抽象类**，Spring提供了三个实现，分别为ContextClosedEvent，ContextHandleEvent和ContextRefreshedEvent。

2. **事件发布者**：

   ​		实现了 ApplicationEventMulticaster接口的类是一个事件发布者，Spring提供了两个实现，AbstractApplicationEvent-Multicaster和 SampleApplicationEventMulticaster分别实现了**事件监听器的管理**和**事件的发布功能**。

   ​		**ApplicationContext容器**本身可以完成事件的发布，因为ApplicationContext容器实现了 ApplicationEventPublisher接口。ApplicationContext容器利用此接口中的方法调用 ApplicationEventMulticaster接口的实现类完成事件的发布。

3. **自定义事件监听器**：

   ​		实现了 ApplicationListener接口的类是一个自定义事件监听器，ApplicationContext容器在启动时，会自动识别并加载ApplicationListener类型的 Bean定义。

   ​		负责**监听容器内所有的ApplicationEvent类型的事件**，一旦容器内有时间发布，就会将通知发到容器内的事件监听器。

   事件发布者会将自定义事件类的实例发送给自定义事件监听器中用于**处理事件发生的方法**。



几个类的关系如下图所示：

![1](Spring监听器\1.png)



自定义内部事件发布的步骤：

1. 创建一个自定义事件，即创建一个继承 ApplicationEvent抽象类的类。

2. 创建一个自定义事件监听器，即创建一个实现 ApplicationListener接口的类。

   <img src="Spring监听器\3.png" alt="2" style="zoom: 50%;" />

3. 使用事件发布者发布事件。在**想要监听的类**上实现 ApplicationEventPublisherAware接口或ApplicationContextPublisherAware接口，这两个接口都会将 ApplicationContext容器作为事件发布者注入对象。然后在**想要监听的方法**上创建自定义的事件，并利用注入的事件发布者发布即可完成事件发发布。

   <img src="Spring监听器\2.png" alt="2" style="zoom: 50%;" />

4. 最后，将**自定义事件监听器**和**想要监听的类**通过配置文件（xml等）**注册到容器中**即可，**自定义事件的类不需要注入**，此类只是作为一个数据类型。



