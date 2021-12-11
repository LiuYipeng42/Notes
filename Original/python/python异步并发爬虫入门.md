---
title: Python异步爬虫入门
date: 2021-06-21 19:40:35
description: python利用asyncio，aiohttp和aiomysql实现异步爬虫
---



# Python异步爬虫入门

&emsp;&emsp;

## 同步与异步

&emsp;&emsp;**同步**：执行一个操作之后，等待结果，然后才继续执行后续的操作

&emsp;&emsp;**异步**：执行一个操作后，此操作没有执行完毕，就可以去执行其他的操作，然后等待通知再回来执行刚才没执行完的操作

&emsp;&emsp;**阻塞**：进程给CPU传达一个任务之后，一直等待CPU处理完成，然后才执行后面的操作

&emsp;&emsp;**非阻塞**：进程给CPU传达任务后，继续处理后续的操作，隔断时间再来询问之前的操作是否完成。这样的过程其实也叫轮								询

&emsp;&emsp;

## 协程

&emsp;&emsp;协程，英文**Coroutine**，是一种基于线程之上，但又比线程更加轻量级的存在，可以由程序员自己写程序来管理，而线程的调度是由操作系统来完成的。

&emsp;&emsp;**协程与线程的关系**

<img src="python异步并发爬虫入门/1.jpg" alt="1" style="zoom:67%;" />

&emsp;&emsp;

&emsp;&emsp;协程常用于**I/O密集型**的程序，不适合CPU密集型的程序

&emsp;&emsp;

&emsp;&emsp;

## asyncio 

&emsp;&emsp;asyncio是python的**异步框架**

&emsp;&emsp;

### 核心概念

#### Eventloop

&emsp;&emsp;事件循环是每个 asyncio 应用的核心。 事件循环会运行异步任务和回调，执行网络 IO 操作，以及运行子进程。

&emsp;&emsp;把一些异步函数注册到这个事件循环上，若这些异步函数都有await语句，则循环会依次调用这些异步函数，但并不会等待一个异步函数执行完，遇到await语句之后会调用其他异步函数。

&emsp;&emsp;

#### Coroutine

&emsp;&emsp;协程(Coroutine)本质上是一个函数，特点是在代码块中可以将执行权交给其他协程。

&emsp;&emsp;

#### Future

&emsp;&emsp;它代表了一个「未来」对象，异步操作结束后会把最终结果设置到这个Future对象上。Future是对协程的封装，日常开发基本不需要直接用这个底层Future类的。

&emsp;&emsp;

#### Task

&emsp;&emsp;Future是协程的封装，Future对象提供了很多任务方法(如完成后的回调、取消、设置任务结果等等)，但是开发者并不需要直接操作Future这种底层对象，而是用Future的子类Task协同的调度协程以实现并发。

&emsp;&emsp;

### async/await关键字

#### **async关键字**

&emsp;&emsp;async用来定义一个函数为协程，协程的特点是能在函数执行过程中挂起，去执行其他协程。

&emsp;&emsp;**协程的定义**方法如下：

```python
async def coroutineName():
    print('this is a coroutine')
```

&emsp;&emsp;

#### await关键字

&emsp;&emsp;当**轮询**到某个协程时，若运行到此协程中的**await**，开始**处理下一个协程**，当await后面的任务完成时，该事件才**再次被唤醒**。所以，只要是和IO任务类似的、**耗费时间的任务**都需要使用await来进行中断，达到异步的目的。

&emsp;&emsp;await 后面只能跟**协程**或有**\__await\_\_属性**的对象，即**可等待对象**。可等待对象有**协程（Coroutine）**，**任务（Task）**和**Future**

&emsp;&emsp;

### asyncio基本代码格式

&emsp;&emsp;

```python
import asyncio


async def delay(n):
    await asyncio.sleep(n)
    print(n)


async def main():
    task1 = asyncio.create_task(delay(1))
    task2 = asyncio.create_task(delay(2))
    
    await task1
    await task2


asyncio.run(main())
```

&emsp;&emsp;

```python
import asyncio


async def delay(n):
    await asyncio.sleep(n)
    print(n)


async def main():
    await asyncio.gather(*[delay(1), delay(2)])
    # await asyncio.wait(*[delay(1), delay(2)])


asyncio.run(main())
```

&emsp;&emsp;

#### asyncio.create_task(*coro*, *, name=None)

&emsp;&emsp;将 *coro* 协程 封装为一个 Task并调度其执行。返回 Task 对象。

&emsp;&emsp;

#### asyncio.run(*coro*, *, debug=False)

&emsp;&emsp;此函数会运行传入的协程，负责管理 asyncio 事件循环，终结异步生成器，并关闭线程池。当有其他 asyncio 事件循环在同一线程中运行时，此函数不能被调用。

&emsp;&emsp;此函数总是会创建一个新的事件循环并在结束时关闭之。它应当被用作 asyncio 程序的主入口点，理想情况下应当只被调用一次。

&emsp;&emsp;**asyncio.get_event_loop()**与**asyncio.get_running_loop()**低层级函数，都可以获取一个事件循环对象，通过此对象来给事件循环中添加协程，与asyncio.run()的功能相同。但不应该使用低层级函数来手动创建和关闭事件循环，使用asyncio.run()函数更好。

&emsp;&emsp;

#### asyncio.gather(*aws, loop=None, return_exceptions=False)

&emsp;&emsp;**并发**运行 *aws* 序列中的 可等待对象。

&emsp;&emsp;如果 *aws* 中的某个可等待对象为**协程**，它将自动被转换成一个**任务**调度。

&emsp;&emsp;如果所有可等待对象都成功完成，**返回一个由所有返回值聚合而成的列表**。结果值的顺序与 *aws* 中可等待对象的顺序一致。

&emsp;&emsp;

#### asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)

&emsp;&emsp;**并发**地运行 *aws* 可迭代对象中的可等待对象，**并进入阻塞状态直到满足 *return_when*** 所指定的条件。

&emsp;&emsp;如指定 ***timeout*** (float 或 int 类型) 则它将被用于控制返回之前**等待的最长秒数**。此函数不会引发 asyncio.TimeoutError异常。当超时发生时，未完成的 Future 或 Task 将在指定秒数后被返回。

&emsp;&emsp;此函数会返回一个包含**(done, pending)**的元组，done表示已完成的任务列表，pending表示未完成的任务列表。
&emsp;&emsp;&emsp;&emsp;**①**只有当给wait()传入timeout参数时才有可能产生pending列表。
&emsp;&emsp;&emsp;&emsp;**②**通过wait()返回的结果集是按照事件循环中的任务完成顺序排列的，所以其往往和原始任务顺序不同。

&emsp;&emsp;

#### 错误的代码

```python
import asyncio


async def delay(n):
    await asyncio.sleep(n)
    print(n)


async def main():

    await delay(1)
    await delay(2)


asyncio.run(main())
```

&emsp;&emsp;此代码并没有并发执行两个协程，而是**串行**的执行了，最终耗时3秒

&emsp;&emsp;

### RuntimeError: Event loop is closed异常

&emsp;&emsp;若出现RuntimeError: Event loop is closed异常则将

```python
asyncio.run(main())
```

&emsp;&emsp;改为

```python
loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
```

&emsp;&emsp;但若在后面加上loop.close()，同样会发生此异常。在查看 asyncio.run() 的源码后发现此方法在最后也执行了loop.close()，所以应该是 loop.close()造成了异常。所以更改代码后，没有执行loop.close()，没有发生异常。

&emsp;&emsp;大多数情况下并不需要手动关闭事件循环，但若想利用 loop.close()手动关闭事件循环，可以使用以下代码

```python
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(asyncio.sleep(1))
loop.close()
```

&emsp;&emsp;

## aiohttp

&emsp;&emsp;用例子来说明

### 爬取豆瓣Top250电影名称

```python
import aiohttp
import asyncio

from bs4 import BeautifulSoup

movies = []


async def request(session, url):
    async with session.get(url) as response:  # 发起请求get请求
        return await response.text(encoding='utf8')  # 获取网页html


async def parser(html):
    soup = BeautifulSoup(html, "lxml")
    for i in soup.findAll(attrs={'class': 'title'}):
        if '/' not in i.text:
            movies.append(i.text)


async def download(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        # 创建一个session用于发起请求，可以设置headers和cookies
        html = await request(session, url)
        await parser(html)


async def main():
    tasks = [download(url) for url in urls]
    await asyncio.gather(*tasks)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}
urls = ['https://movie.douban.com/top250?start=%d' % i for i in range(0, 226, 25)]

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

for i in movies:
    print(i)
```

&emsp;&emsp;

### 下载图片

```python
import aiohttp
import asyncio


async def request(session, url):
    async with session.get(url) as response:
        return await response.read()  # 以字节流形式获取s，用于获取图片或视频


async def download(url):
    async with aiohttp.ClientSession() as session:
        with open(url.split("/")[-1], 'wb') as f:
            f.write(await request(session, url))


async def main():
    tasks = [download(baseUrl + img) for img in images]
    await asyncio.gather(*tasks)


baseUrl = 'https://cdn-2.tstatic.net/tribunnews/foto/bank/images/'

images = ['bea-cukai-berikan-fasilitas-kawasan-berikat-0607.jpg',
          'pemusnahan-barang-ilegal-oleh-bea-cukai-soekarno-hatta.jpg',
          'pemerintah-berikan-penurunan-bea-masuk-0707.jpg',
          'strategi-bea-cukai-tekan-peredaran-rokok-ilegal.jpg',
          'pemerintah-sahkan-persetujuan-kemitraan-ekonomi-komprehensif-indonesia-australia.jpg',
          'barang-bukti-upaya-penyelundupan-narkotika-0708.jpg',
          'pelaku-rokok-ilegal-0708.jpg',
          'bea-cukai-madura-komitmen-rintis-kiht-di-madura.jpg',
          'patroli-laut-direktorat-jenderal-bea-dan-cukai.jpg',
          'sinergi-bea-cukai-dan-tni-al-0709.jpg']

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```

&emsp;&emsp;

### async with···as

&emsp;&emsp;首先来了解 **with···as语法**。

&emsp;&emsp;with语句用于包装带有使用**上下文管理器定义的方法**的代码块的执行，**上下文管理器定义的方法**包括**\_\_enter\_\_(self)**和**\_\_exit_\_(self)**。

&emsp;&emsp;**上下文**，即context，和文章的上下文的意思相似，需要理解文章的某一部分，需要去理解这一部分的上面和下面的部分。程序同理，程序执行到了子程序，子程序要运行出结果，要用到程序之前的一些结果(包括但不限于外部变量值，外部对象等等)。

&emsp;&emsp;**上下文管理器** 是一个对象，它定义了在执行 with语句时要建立的运行时上下文。 上下文管理器处理进入（\_\_enter\_\_(self)方法）和退出（\_\_exit_\_(self)方法）所需运行时上下文以执行代码块。

&emsp;&emsp;以下面的代码为例来理解：

```python
with open('test.txt', 'r') as file:
	print(file.read())
```

&emsp;&emsp;此代码的作用是读取并输出 test.txt文件中的内容。要执行读取并输出文件内容的代码 print(file.read()) ，条件是要打开此文件，打开此文件就是代码 print(file.read()) 运行的上下文。所以，with语句就作为上下文管理器去打开文件，创建一个上下文，当读取并输出完成后，with作为上下文管理器就会将文件关闭。

&emsp;&emsp;open()是一个函数，是没有\_\_enter\_\_(self)和\_\_exit\_\_(self)方法，但若想要为了让一个对象兼容with语句，必须在这个对象的类中声明这两个方法，\_\_enter\_\_(self)方法用于创建上下文，将返回值赋值给 as后面的变量，\_\_exit_\_(self)方法用于关闭上下文。

&emsp;&emsp;with···as语法只是为了方便写代码，可以利用其他的代码来代替，例如 **try ··· except ··· finally ···** （  https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with  ）。

&emsp;&emsp;**async with···as** 语法与 **with···as** 语法的作用相似。async with···as是**异步上下文管理器**，async with···as也有进入和退出上下文的方法，分别是**\_\_aenter\_\_ (self)**和**\_\_aexit\_\_(self)** ，这两个方法都要返回一个 awaitable类型的对象。

&emsp;&emsp;官方文档示例：

```python
class AsyncContextManager:
    async def __aenter__(self):
        await log('entering context')  # 也可以不使用 await，直接返回一个awaitable类型的对象

    async def __aexit__(self, exc_type, exc, tb):
        await log('exiting context')
```

&emsp;&emsp;

## aiomysql

&emsp;&emsp;**aiomysql**基于PyMySQL的异步操作数据库的库，API与PyMySQL大致相同，不在详细介绍。

&emsp;&emsp;

### 基本使用方法

#### 查询数据

&emsp;&emsp;官方文档示例

```python
import asyncio
import aiomysql


async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='', db='mysql',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT Host, User FROM user")
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))
```

&emsp;&emsp;

#### 插入/更新数据

```python
import asyncio
import aiomysql


async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='', db='mysql',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("update user set name='hhh' where Host = '127.0.0.1'")
        await cur.execute("insert into user (Host, User) values (%s, %s)", ('127.0.0.1', 'hhhh'))
        await conn.commit()
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))
```

&emsp;&emsp;与PyMySQL相同，在更改数据库中的内容时需要commit。

&emsp;&emsp;

#### 创建并使用数据库连接池

官方文档示例

```python
import asyncio
import aiomysql


async def test_example(loop):
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='mysql', loop=loop)
    # 可以通过minsize与maxsize参数控制连接池的大小
    
    async with pool.acquire() as conn:
    	# acquire() 从连接池中获取一个数据库连接
        async with conn.cursor() as cur:
            await cur.execute("SELECT 42;")  # the answer to life, universe and everything
            print(cur.description)
            (r,) = await cur.fetchone()
            assert r == 42
    pool.close()
    await pool.wait_closed()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))
```

&emsp;&emsp;

&emsp;&emsp;

### 爬取豆瓣Top250电影名称并存入数据库

```python
import asyncio
import aiohttp
import aiomysql
from bs4 import BeautifulSoup


async def request(session, url):
    async with session.get(url) as response:  # 发起请求get请求
        return await response.text(encoding='utf8')


async def parser(html, cur):
    soup = BeautifulSoup(html, "lxml")
    for i in soup.findAll(attrs={'class': 'title'}):
        if '/' not in i.text:
            await cur.execute("insert into movies (name) values (%s)", i.text)


async def download(url, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            async with aiohttp.ClientSession(headers=headers) as session:  
                # 创建一个session用于发起请求，可以设置headers和cookies
                html = await request(session, url)
                await parser(html, cur)
        await conn.commit()


async def main():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='',
                                      db='', loop=loop, minsize=10)

    tasks = [download(url, pool) for url in urls]
    await asyncio.gather(*tasks)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}

urls = ['https://movie.douban.com/top250?start=%d' % i for i in range(0, 226, 25)]

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


```

&emsp;&emsp;

### RuntimeError: readexactly() called while another coroutine is already waiting for incoming data 异常

&emsp;&emsp;在使用aiomysql时并不能在多个协程中使用同一个数据库连接，否则容易出现RuntimeError: readexactly() called while another coroutine is already waiting for incoming data异常。当一个协程正在利用一个数据库连接处理数据时，由于使用了 await，会去运行其他协程，若其他的协程也使用此数据库连接处理数据，此时当然会出错，所以出现了此异常，所以要为每一个协程创建一个数据库连接，但这样会占用较多的数据库的资源，使数据库性能下降，所以要使用数据库连接池（  https://www.cnblogs.com/cocoxu1992/p/11031908.html  ）。





