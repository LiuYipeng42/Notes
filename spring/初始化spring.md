

1. 在设置的插件中安装 **Spring Assistant 插件**

   <img src="初始化spring\1.png" alt="1" style="zoom: 80%;" />



2. 利用 Spring Assistant 插件创建spring项目

   ![2](初始化spring\2.png)

   <img src="初始化spring\3.png" alt="3" style="zoom: 80%;" />

   若在使用默认的地址（https://start.spring.io/）时出现以下错误

   <img src="/home/lyp/文档/Books/Typora笔记/java/spring/初始化spring/5.png" alt="5" style="zoom:67%;" />

   可以使用**阿里云**的地址：https://start.aliyun.com



3. 打开 Spring Assistant 插件后，会有以下界面

   <img src="初始化spring\6.png" alt="6" style="zoom:80%;" />

   **Group Id：**
    		GroupID是项目组织唯一的标识符，实D际对应JAVA的包的结构，是main目录里java的目录结构。定义了项目属于哪个组，举个例子，如果你的公司是mycom，有一个项目为myapp，那么groupId就应该是com.mycom.myapp.

   **Artifact Id：**
    		ArtifactID是项目的唯一的标识符，实际对应项目的名称，就是项目根目录的名称。定义了当前maven项目在组中唯一的ID,比如，myapp-util,myapp-domain,myapp-web等。

   **Version：**
   		指定了myapp项目的当前版本，SNAPSHOT意为快照，说明该项目还处于开发中，是不稳定的版本。

   **Project name：**
   		声明了一个对于用户更为友好的项目名称，不是必须的，推荐为每个pom声明name，以方便信息交流。

   

4. 点击下一步会有以下界面，可以**选择需要的功能**

   <img src="初始化spring\7.png" alt="7" style="zoom:80%;" />

   可以选择以下功能

   开发工具：Spring Boot DevTools

   wed：Spring Web

   模板引擎：Thymeleaf

   关系型数据库：MySQL Driver

   

5. 点击下一步后会有以下界面，选择项目名称和项目位置

   <img src="初始化spring\8.png" alt="8" style="zoom:80%;" />



6. 若在选择功能时选择了第一次使用的功能，此时以下文件会出现错误

   ![9](初始化spring\9.png)
   
   若没有任何问题此时 IDEA 会自动下载缺少的东西
   
   若没有下载，可以点击 clean，然后在点击package，会开始下载

![10](初始化spring\10.png)

​	若点击package后出现以下错误

![4](初始化spring\4.png)

​	Could not transfer artifact ·····



可以在maven的setting.xml文件中添加阿里云镜像

    <mirrors>
        <mirror>
            <id>alimaven</id>
            <mirrorOf>central</mirrorOf>
            <name>aliyun maven</name>
            <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>
        </mirror>
        <mirror>
            <id>alimaven</id>
            <name>aliyun maven</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
            <mirrorOf>central</mirrorOf>
        </mirror>
    </mirrors>


如果还不行可以在设置中的 VM选项中加入如下内容

​	**-Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true**

<img src="初始化spring\11.png" alt="11" style="zoom:80%;" />

之后再次点击 clean 和 package 即可



7. 若出现**不能解析springframework 解决方案**的错误时

   可以在pom.xml配置文件中添加依赖

   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

   之后再次点击 clean 和 package 下载缺少的库