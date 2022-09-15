---
title: css基础
date: 2021-02-22 15:24:23
description: css的三种使用方法，css选择器
---

## CSS基础

### css的使用

1. 直接在标签的**style属性**中使用

   ```html
   <div style="border: 1px solid red;">div标签1</div>
   ```

​	只能作用于**一个标签**

2. 在 head标签中使用 **style标签**

   style标签专门用来**定义css样式代码**

   ```html
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
       <style type="text/css">
           div{
               border: 1px solid red;
           }
       </style>
   </head>
   ```

   可以作用于一个html文件，即**一个页面**

3. 在 head标签中使用 **link标签**

   link标签专门用来**引入css样式代码**，**href属性**要有css样式代码的地址

   ```html
   <head>
       <meta charset="UTF-8">
       <title>Title</title>
       <link rel="stylesheet" type="text/css" href="1.css"/>
   </head>
   ```

   可以作用于**任意**一个引入css样式代码的**页面**

&emsp;&emsp;

### 选择器

**标签名选择器**

&emsp;&emsp;直接用**标签名**

```css
div{
   border: 1px solid yellow;
   color: blue;
   font-size: 30px;
}
```

&emsp;&emsp;

**id选择器**

&emsp;&emsp;使用符号 **#** 加上 **id属性值**

```css
#id001{
   color: blue;
   font-size: 30px;
   border: 1px yellow solid;
}
```

可以影响对应 id属性的标签的样式

```html
<div id="id001">div标签</div>
```

&emsp;&emsp;

**class选择器**

&emsp;&emsp;使用符号 **.** 加上 **class属性值**

```css
.class01{
   color: blue;
   font-size: 30px;
   border: 1px solid yellow;
}
```

&emsp;&emsp;可以影响对应 class属性的标签的样式

```html
<span class="class01">span标签class01</span>
```

&emsp;&emsp;

**组合选择器**

&emsp;&emsp;**后代**选择器：		以**空格** 分隔
&emsp;&emsp;**子元素**选择器：	以大于 **>** 号分隔
&emsp;&emsp;**相邻兄弟**选择器：以加号 **+** 分隔
&emsp;&emsp;**普通兄弟**选择器：以波浪号 **～** 分隔

&emsp;&emsp;

&emsp;&emsp;以**逗号 , 分隔**的**多个选择器**表示，一个标签只要满足一个选择器就会被选择器影响。即逗号表示 ” 或 “ 的意思

```css
.class01 , #id01{
    color: blue;
    font-size: 20px;
    border:  yellow 1px solid;
}
```



