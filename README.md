# A simple demo of Python 3's asyncio library


## asyncio
From [python.org](https://docs.python.org/3/library/asyncio.html):

    asyncio is a library to write concurrent code using the async/await syntax.

Within a single threaded Python process you can easily have orders of magnitude performance gains where you need to make multiple I/O connections, for example crawling multiple pages of a website.

### History
* March 2014: Python 3.4 released introducing `asyncio` for the first time. It was flagged as "provisional" initially.
* September 2015: Python 3.5 added async and await syntax for coroutines were introduced as part of [PEP 492](https://www.python.org/dev/peps/pep-0492/)
* December 2016: Python 3.6 declares the `asyncio` API as stable, rather than provisional. Introduction of asynchronous generators (i.e using `yield` in a function defined with `async def function_name`).
* June 2018: Python 3.7 introduced a provisional `asyncio.run()` function making it far easier to call an async coroutine from synchronous code.


### asyncio Libraries
In the past two years there's been a mini explosion in external libraries (PyPI) being written using asyncio. Early in `asyncio`'s life, I think there were still many Legacy Python (Python 2) applications in use, preventing developers from taking advantage of it.
Now since most new Python libraries are written for Python 3 only, we've seen a big uptick in `asyncio` adoption.

Below are some of the asyncio HTTP libraries that have gained traction in recent years.

* [aiohttp](https://aiohttp.readthedocs.io) is the most popular Python async HTTP client. It also includes an async HTTP Server.
* [Sanic](https://sanicframework.org) is a Flask-like API, but using asyncio instead.
* [Quart](https://gitlab.com/pgjones/quart) takes Sanic's approach to the next level by trying to _exactly_ mimick the Flask API.
* [Starlette](https://www.starlette.io) is an async HTTP framework by Tom Christie, the creator of the Django REST Framework.
* [Django Channels](https://channels.readthedocs.io) is an attempt at introducing asynchronous code into Django's synchronous core to allow Django to do long-running connections to serve, for example, WebSockets.
* [Responder](https://python-responder.org) was started late last year by Kenneth Reitz (author of the almost ubiquitous [Requests](http://python-requests.org) library).
