## Java对并发的支持

​		在Java诞生之时，Java设计者们就考虑了并发的问题，但受限于当时的技术和需求，只是对其进行了简单的支持。
随着时代更替（**多核处理器**的普及，提高了程序员对**处理器的使用效率**的诉求），并发成为了一个需要关注的功能点。

​		这里，博主将概述Java各个版本（截止到JDK8）对于并发的支持的发展，便于理解这些类、接口，为何出现，又为了解决哪些问题。



### JDK1.4及之前

1. 1.synchronized、volatile关键字
2. Object的wait()、notify()、notifyAll()方法
3. Thread类，以及Runnable接口
4. final 不变属性以及一些不变的类，比如String
5. 基础但已经不被推荐使用的集合 Vector、HashTable



​		在这个时期，Java对并发做的支持比较**底层**，需要程序员**手动管理**需要同步的类或对象。这种情况下，除非程序员对并发有非常深的理解，才能用好这些内容。（**过于底层，不易理解，编程困难**）
而且由于synchronized是重量级锁，需要经常切换线程，效率比较低。（**并发效率不高**）



### JDK1.5

1. AtomicXXX类
2. Lock显式锁（Lock、ReadWriteLock、Condition等接口）
3. Callable、Future接口
4. Executor执行器、ExecutorService两个接口以及实现类
5. 并发集合BlockingQueue、ConcurrentMap、ConcurrentHashMap、CopyOnWriteArrayList



​		在这个时期，Java对并发进行了大刀阔斧的改进。

- 新增的**原子操作类型**比volatile关键字更易用且高效（简化并发编程，优化性能）；
- **Lock显示锁**不同于synchronized引入了一种新的机制（引入一种轻量的锁）；
- **执行器**使用了线程池机制，简化并发操作。（简化并发编程）
- 新增的并发集合比起之前的Vector、HashTable（仅在方法上添加synchronized关键词），引入了更多机制，性能也更高。



### JDK1.6

1. 优化后的synchronized关键字，使用分级锁机制。

​		这个时期，对同步关键字进行了优化、之前只存在一种**重量级锁**，后引入了**偏向锁**、**轻量级锁**，减少了线程切换的次数。（从语法上优化了并发性能），优化后的synchronized关键字性能可以和Lock媲美。



### JDK7

1. Fork/Join框架（分解/合并框架）
2. TransferQueue接口以及实现类
3. ThreadLocalRandom 支持并发随机数
4. Phaser工具类 阶段性并发工具类

​		在这个时期，提供了使用**分治技术**的Fork/Join框架等。



### JDK8

1. XXXAdder加法器、XXXAccumulator累加器（优化后的原子类型操作）
2. CompletableFuture（Future升级版本）
3. StampedLock （ReadWriteLock改进版本）
4. 静态commonPool（为ForkJoinPool提供了多一种选择）
5. StampedLock（新增在写，读和乐观读的三种模式转化的锁）