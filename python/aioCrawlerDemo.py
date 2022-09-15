import asyncio
import aiohttp
import aiomysql
from aiohttp import client_exceptions
from bs4 import BeautifulSoup


async def request(session, url):
    while True:
        try:
            # proxy代理，此代理是我电脑上的代理 (群里的vpn)
            # 若不需要VPN就可以访问网站则可以不用设置代理
            async with session.get(url, proxy='http://127.0.0.1:7890') as response:  # 发起请求get请求
                # 若是图片则改为 return await response.read()，
                # 之后以 二进制形式保存本地
                # with open('imgName', 'wb') as f:
                return await response.text(encoding='utf8')
        except (client_exceptions.ServerDisconnectedError, aiohttp.client_exceptions.ClientOSError,
                aiohttp.client_exceptions.ClientPayloadError, asyncio.exceptions.TimeoutError):
            print('network error!')
            await asyncio.sleep(1)


async def parser(html, cursor, conn):
    # 利用BeautifulSoup解析html
    soup = BeautifulSoup(html, 'lxml')
    # 之后是获取网页的数据，
    for i in soup.findAll(attrs={'class': 'title'}):
        if '/' not in i.text:
            print(i.text)
            await cursor.execute("insert into movies (name) values (%s)", i.text)

    # 提交事务，若执行多条sql才提交事务，即有可能会造成数据库的死锁
    await conn.commit()


async def getNews(news, pool, semaphore):
    async with semaphore:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                async with aiohttp.ClientSession(headers=headers) as session:  # 创建一个session用于发起请求
                    html = await request(session, news)
                    await parser(html, cursor, conn)


async def main():
    # 数据库连接池配置
    # mysql默认的最大连接数是 151，若不够可以先在 mysql中修改
    # 此示例中数据库名为 movies
    # 表为：
    # DROP TABLE IF EXISTS `movies`;
    # CREATE TABLE `movies` (
    #   `name` varchar(255) DEFAULT NULL
    # );
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='121522734a',
                                      db='movies', loop=loop, minsize=5, maxsize=150)

    # 限制并发量为 100
    # 若运行后，刚开始CPU占用率很高，之后CPU占用率较小，则表明爬虫的速度并没有被电脑的性能限制，
    # 被网速限制了（校园网最快只有 5mbps 左右，即 5/8 Mb/s），
    # 那并发数就不必要开那么大了，开那么大只会浪费很多内存。
    semaphore = asyncio.Semaphore(100)

    tasks = [getNews(news, pool, semaphore) for news in allNews]
    await asyncio.gather(*tasks)

# 若要使用，只需将url全部放进一个叫做 allNews的 可迭代对象（如list）中，并配置好数据库即可
allNews = ['https://movie.douban.com/top250?start=%d' % i for i in range(0, 226, 25)]

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 '
                  'Safari/537.36',
}

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(asyncio.sleep(1))
loop.close()
