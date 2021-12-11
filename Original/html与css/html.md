---
title: html基础
date: 2021-02-20 12:40:55
description: 网页的组成，html基础语法，html的各种标签
---

# html基础

## 网页的组成

&emsp;&emsp;**内容**：看到的信息和数据，用html展示

&emsp;&emsp;**表现**：内容的展示形式，用css实现

&emsp;&emsp;**表现**：页面中元素与输入设备的交互相应，用javascript实现

&emsp;&emsp;

## html组成

1. 开头的

```html
<!DOCTYPE html>
```

&emsp;&emsp;表示**约束和声明**

2. **html标签**表示**html的开始**，html标签中一般分为两部分，分别是：head和body

3. **head标签**表示**头部信息**，一般包含三部分内容：title标签，css样式，js代码

4. **body标签**是整个html页面显示的**主体内容**

```html
<!DOCTYPE html>

<html lang="en"> <!--lang="zh_CN" 表示中文-->

<head>
    <!--charset="UTF-8" 表示当前页面使用UTF-8字符集 -->
    <meta charset="UTF-8">
    <title>某东</title>
</head>

<body>
hello
<button onclick="alert('hhh')">按钮</button>
<!--
    onclick表示单击(点击)事件
    alert() 是javaScript语言提供的一个警告框函数.
    它可以接收任意参数.参数就是警告框的函数信息
-->
1<br/>2 <!--换行-->
<hr/> <!--分割线-->
3
</body>

</html>
```

&emsp;&emsp;head标签中的**meta标签**，可以指定页面使用的**字符集**

&emsp;&emsp;head标签中的**title标签**，表示**标题**，显示在浏览器的标签栏上

**&emsp;&emsp;button标签**表示**按钮**，其中的**onclick属性**若值为alert()，则可以弹出一个警示窗口，文字内容在括号内

&emsp;&emsp;**br标签**表示**换行**

**&emsp;&emsp;hr标签**表示**分割线**

&emsp;&emsp;

## 标签语法

&emsp;&emsp;**标签不能交叉嵌套**

&emsp;&emsp;正确：

```html
<div><span>hhh</span></div>
```

&emsp;&emsp;错误：

```html
<div><span>hhh</div></span>
```

&emsp;&emsp;

&emsp;&emsp;**标签必须正确关闭(闭合)**

1. 有文本内容的标签

   &emsp;&emsp;正确：

   ```html
   <div>早安，尚硅谷</div>
   ```

   &emsp;&emsp;错误：

   ```html
   错误：<div>早安，尚硅谷
   ```

2. 没有文本内容的标签

   &emsp;&emsp;正确：

   ```html
   <br />1
   ```

   &emsp;&emsp;错误：

   ```html
   <br >2
   ```

&emsp;&emsp;

&emsp;&emsp;**属性必须有值，属性值必须加引号**

&emsp;&emsp;正确：

```html
<font color="blue">hhh</font>
```

&emsp;&emsp;错误：

```html
<font color=blue>hhh</font>
```

```html
<font color>hhh</font>
```

&emsp;&emsp;

&emsp;&emsp;**注释不能嵌套**

&emsp;&emsp;正确：

```html
<!-- 注释内容 -->
```

&emsp;&emsp;错误：

```html
<!-- 注释内容 <!-- 注释内容 -->-->xxxxxxxxxx <!-- 注释内容 <!-- 注释内容 -->--><br >2
```

&emsp;&emsp;

## style属性

&emsp;&emsp;style 属性规定元素的行内样式（inline style）。

&emsp;&emsp;style 属性将**覆盖任何全局的样式设定**，例如在 <style\> 标签或在外部样式表中规定的样式。

&emsp;&emsp;在 HTML5 中, style 属性可用于**任何的 HTML 元素** (它会验证任何HTML元素。但不一定是有用)。

&emsp;&emsp;语法如下，可以设置标签的样式

```html
<span style="color: red; font-family: 宋体,serif; font-size: xx-large; ">我是字体标签
</span>

```

&emsp;&emsp;

## 特殊字符

常用的特殊字符:

```
<:   &lt;
>: 	 &gt;
空格: &nbsp;  在html中使用普通的空格键，不管用了多少个，都会只显示一个
```

```html
我是&lt;br&gt;标签<br/>
hhhh&nbsp;&nbsp;hhhh
```

&emsp;&emsp;

## 标题标签

&emsp;&emsp;h1 - h6 都是标题标签，h1 最大，h6 最小

&emsp;&emsp;**style 属性**可以设置标题格式，style 属性中的 text-align 可以指定**对其位置**
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;left          左对齐(默认)
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;center    剧中
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;right       右对齐

&emsp;&emsp;**语法：**

```html
<h1 style="text-align: left">标题1</h1>
<h2 style="text-align: center">标题2</h2>
<h3 style="text-align: right">标题3</h3>
<h4>标题4</h4>
<h5>标题5</h5>
<h6>标题6</h6>
```

&emsp;&emsp;

## 超链接

1. **a标签**可以实现超链接

2. a标签的 **href属性** 可以设置连接的地址

3. a标签的 **target属性**设置哪个目标进行跳转，

   若 target 属性值为 **_self** 表示在当前页面(默认值)跳转

   若 target 属性值为 **_blank** 表示在打开的新页面进行跳转

```html
<a href="http://localhost:8080">百度</a><br/>
<a href="http://localhost:8080" target="_self">百度_self</a>
<a href="http://localhost:8080" target="_blank">百度_blank</a>
```

&emsp;&emsp;

## img标签

1. **img标签**是图片标签，用来**显示图片**
   &emsp;&emsp;**src属性**可以设置**图片的路径**
   &emsp;&emsp;**width属性**设置图片的**宽度**
   &emsp;&emsp;**height属性**设置图片的**高度**
   &emsp;&emsp;**style属性**设置图片**样式**
   &emsp;&emsp;**alt属性**设置当指定路径**找不到图片**时，用来代替**显示的文本内容**

2. 在web中路径分为**相对路径**和**绝对路径**两种
   **相对路径**:
   &emsp;&emsp;**.**&emsp;   &emsp;  &emsp;表示**当前**文件所在的目录
   &emsp;&emsp;**..**&emsp;&emsp;&emsp;&emsp;表示当前文件所在的**上一级目录**
           **文件名**  &emsp;表示**当前文件所在目录的文件**，相当于 ./文件名，./ 可以省略

   **绝对路径**:
   &emsp;&emsp;正确格式是:  http://ip:port/工程名/资源路径

   &emsp;&emsp;错误格式是:  盘符:/目录/文件名

```html
<img src="1.jpg" width="200" height="260" style="border: 1px" alt="图片找不到"/>
<img src="../2.jpg" width="200" height="260" />
<img src="../imgs/3.jpg" width="200" height="260" />
```

&emsp;&emsp;

## 表格标签

1. **table标签**是表格标签

   可以利用以下属性进行设置：

   &emsp;&emsp;**width** 设置表格宽度

   &emsp;&emsp;**height** 设置表格高度

   &emsp;&emsp;**border** 设置表格标签（已弃用）

   &emsp;&emsp;**align** 设置单元格文本对齐方式（已弃用）

   &emsp;&emsp;**cellspacing** 设置**单元格间距**（已弃用）

2. 对于 **table标签**中**已弃用**的属性，可以在 style属性中设置，css也可以

   - 如 **border**属性更换为

     在每一个单元格中设置，宽度与颜色必须都设置，css如下所示

     ```css
     td {
         border: 1px solid red;
     }
     ```

   - **align** 属性的功能由 style属性中的 **margin** 来实现：

     **居中**为

     ```html
     <table style="margin:0 auto;">
     ```

     **左对齐**

     ```html
     <table style="margin-left: 0;">
     ```

     **右对齐**

     ```html
     <table style="margin-right: 0;">
     ```

   - **cellspacing** 属性更换为

     ```html
     <table style="border-collapse: collapse;">
     ```

3. 在 **table标签** 中可以有以下标签

   &emsp;&emsp;**tr** 是**行标签**

   &emsp;&emsp;**th** 是表**头标签**

   &emsp;&emsp;**td**  是**单元格标签**

   &emsp;&emsp;**b** 是**加粗标签**

4. 对于每一个 **td 单元格标签**，可以利用colspan和rowspan属性进行**单元格的合并**

   &emsp;&emsp;**colspan** 属性设置**跨列合并**单元格，属性的值表示合并个数
   &emsp;&emsp;**rowspan** 属性设置**跨行合并**单元格，属性的值表示合并个数

```html
<table width="500" height="500" cellspacing="0" border="1">
    <tr>
        <td colspan="2">1.1</td>
        <td>1.3</td>
        <td>1.4</td>
		<td>1.5</td>
    </tr>
    <tr>
        <td rowspan="2">2.1</td>
        <td>2.2</td>
		<td>2.3</td>
		<td>2.4</td>
		<td>2.5</td>
    </tr>
    <tr>
        <td>3.2</td>
        <td>3.3</td>
        <td>3.4</td>
        <td>3.5</td>
	</tr>
    <tr>
        <td>4.1</td>
        <td>4.2</td>
        <td>4.3</td>
        <td colspan="2" rowspan="2">4.4</td>
    </tr>
    <tr>
        <td>5.1</td>
        <td>5.2</td>
        <td>5.3</td>
    </tr>
</table>
```

&emsp;&emsp;

## iframe标签

1. **ifarme标签**可以在页面上开辟一个小区域**显示一个单独的页面**
2. 可以通过 **width** 和 **height 属性**设置区域大小
3. ifarme 和 **a标签** （超链接标签）组合使用的步骤:
   1. 在 iframe标签 中使用 **name属性** 定义一个名称
   2. 在 a标签 的 **target属性** 上设置iframe的 name 的属性值

```html
<iframe src="3.标题标签.html" width="500" height="400" name="abc"></iframe>

<a href="0-标签语法.html" target="abc">0-标签语法.html</a>
<a href="1.font标签.html" target="abc">1.font标签.html</a>
<a href="2.特殊字符.html" target="abc">2.特殊字符.html</a>
```

&emsp;&emsp;

## 列表

1. **ul标签** 是无序列表标签，每一项的前面**没有序号**

2. **ol标签** 是有序列表标签，每一项前面**有序号**

3. **li标签**  是列表项，表示列表中每一项的标签

4. **style属性**中的 list-style-type 可以修改列表项前面的符号

```html
<ul style="list-style-type: none">
    <li>h</li>
    <li>hh</li>
    <li>hhh</li>
    <li>hhhh</li>
</ul>
<ol style="list-style-type: -moz-ethiopic-numeric">
    <li>h</li>
    <li>hh</li>
    <li>hhh</li>
    <li>hhhh</li>
</ol>
```

&emsp;&emsp;

## 表单

1. **form标签**就是表单

   &emsp;&emsp;**action属性**设置提交的目标**服务器地址**
   &emsp;&emsp;**method属性**设置**提交的方式**GET(默认值)或POST

2. **input标签**可以向用户展示输入的位置，**type属性**可以指定用户输入的类型

   -  type属性为**text**，表示**文字输入框**

     **value属性**可以设置**默认显示内容**

     ```html
     <input type="text" value="默认值"/>
     ```

   - type属性为**password**，表示**密码输入框**

     **value属性**可以设置**默认显示内容**

     ```html
     <input type="password" value="abc"/>
     ```

   - type属性为**radio**，表示**单选框**，**name属性**可以对其进行**分组**

     **checked属性**为"checked"表示**默认选中**

     ```html
     <input type="radio" name="sex" value="boy"/>男
     <input type="radio" name="sex" checked="checked" value="girl"/>女
     ```

   - type属性为**checkbox**，表示**复选框**

     **checked属性**为"checked"表示**默认选中**

     ```html
     <input type="checkbox" checked="checked"/>Java
     <input type="checkbox"/>C++
     ```

   - type属性为**reset**，表示**重置按钮**

     **value属性**修改**按钮上的文本**

     ```html
     <input type="reset"/>
     ```

   - type属性为**submit**，表示**提交按钮**

     **value属性**修改**按钮上的文本**

     ```html
     <input type="submit"/>
     ```

   - type属性为**button**，表示**按钮**

     **value属性**修改**按钮上的文本**

   - type属性为**file**，表示**文件上传域**

     ```html
     <input type="file"/>
     ```

   - type属性为**hidden**，表示**隐藏域**，当我们要发送某些信息，而这些信息，不需要用户参与，就可以使用隐藏域（提交的时候同时发送给服务器）

3. **select标签**可以创建单选或**多选菜单**，即下拉列表框

   ```html
   <select>
       <option>--请选择国籍--</option>
       <option selected="selected">中国</option>
       <option>美国</option>
       <option>日本</option>
   </select>
   ```

   &emsp;&emsp;**option 标签**是下拉列表框中的**选项** 

   &emsp;&emsp;selected="selected"设置默认选中

4. **textarea标签** 表示多行文本**输入框** （起始标签和结束标签中的内容是默认值）
   &emsp;&emsp;**rows 属性**设置可以显示几行的高度
   &emsp;&emsp;**cols 属性**设置每行可以显示几个字符宽度

5. **form标签**中的各种input标签，select标签和option标签等有具体功能的标签，每一个都要**放到 label标签**中

   ```html
   <label>
       <textarea rows="10" cols="20">我才是默认值</textarea>
   </label>
   ```

6. 以上标签的信息要想发送到目标服务器，必须都加上 **name属性**，来代表这个值

7. 表单提交的时候，**数据没有发送给服务器**的三种情况：
   &emsp;&emsp;1、表单项**没有name属性值**
   &emsp;&emsp;2、单选、复选（下拉列表中的option标签）都需要添加 **value属性**，以便发送给服务器
   &emsp;&emsp;3、表单项不在所提交的 form标签 中

8. GET与POST

   GET请求的特点是：
   &emsp;&emsp;1、浏览器地址栏中的地址是：action属性[+?+请求参数]
                 请求参数的格式是：name=value&name=value
   &emsp;&emsp;2、不安全
   &emsp;&emsp;3、它有数据长度的限制

   POST请求的特点是：
   &emsp;&emsp;1、浏览器地址栏中只有action属性值
   &emsp;&emsp;2、相对于GET请求要安全
   &emsp;&emsp;3、理论上没有数据长度的限制

&emsp;&emsp;

## 其他的标签


**div标签**：默认独占一行
**span标签**：它的长度是封装数据的长度
**p标签**：段落标签，默认会在段落的上方或下方各空出一行来（如果已有就不再空）





