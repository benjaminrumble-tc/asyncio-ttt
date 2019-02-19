#!/usr/bin/env python3
"""fetchs a bunch of HTTP resources using aiohttp"""
import asyncio
import time

import aiohttp


async def main():
    """an async function"""
    start = time.time()
    urls = [
        f'https://httpbin.org/get?request={i}' for i in range(20)
    ]

    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            *(session.get(url) for url in urls)
        )

    end = time.time()
    print(f'{end - start} seconds')

if __name__ == "__main__":
    asyncio.run(main())