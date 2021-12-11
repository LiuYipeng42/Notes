## spring目录及文件介绍

- **mvnw 和 mvnw.cmd**：这是 Maven 包装器（wrapper）脚本。借助这些脚本，即 便你的机器上没有安装 Maven，也可以构建项目。
- **pom.xml**：这是 Maven 构建规范
- **XXXApplication.java**：这是 Spring Boot 主类，它会启动该项目。XXX是项目名称。
- **application.properties**：这个文件起初是空的，但是它为我们提供了指定配置属性的地方。
- **static**：在这个文件夹下，你可以存放任意为浏览器提供服务的静态内容（图片、 样式表、JavaScript 等），该文件夹初始为空。
- **templates**：这个文件夹中存放用来渲染内容到浏览器的模板文件。这个文件夹 初始是空的，不过我们很快就会往里面添加 Thymeleaf 模板。
- **XXXApplicationTests.java**：这是一个简单的测试类，它能确保 Spring 应用 上下文可以成功加载。XXX是项目名称。

