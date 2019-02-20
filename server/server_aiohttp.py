#!/usr/bin/env python3
"""server using aiohttp"""
import aiohttp
from aiohttp import web

session = aiohttp.ClientSession()

async def handle_index(request):
    """index handler"""
    async with session.get('https://httpbin.org/get?request=1') as resp:
        json_response = await resp.json()
        return web.json_response(json_response)

def make_app():
    app = web.Application()
    app.add_routes([
        web.get('/', handle_index),
    ])
    return app

if __name__ == "__main__":
    app = make_app()
    aiohttp.web.run_app(app)