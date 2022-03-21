
import asyncio
import aiohttp
from pprint import pprint


async def main():
    test_url = "http://www.baidu.com"
    
    async with aiohttp.ClientSession() as session:
        for i in range(2):
            rsp = await session.get(test_url)
            pprint(rsp.status)
            pprint(rsp.headers)

asyncio.run(main())
