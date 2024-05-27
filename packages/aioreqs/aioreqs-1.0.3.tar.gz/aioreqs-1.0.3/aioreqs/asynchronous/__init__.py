import typing
import asyncio
import requests
import functools
import concurrent.futures


# ==------------------------------------------------------------== #
# Decorators                                                       #
# ==------------------------------------------------------------== #
def coroutine(func: callable = None, *, pool: concurrent.futures.ThreadPoolExecutor | None = None):

    def outer_wrapper(wrapped_func: callable):

        @functools.wraps(wrapped_func)
        async def inner_wrapper(*args, **kwargs):

            # If thread pool wasn't passed
            if pool is None:
                return await asyncio.to_thread(wrapped_func, *args, **kwargs)

            # Executing function in given thread pool
            return await asyncio.get_event_loop().run_in_executor(pool, lambda: wrapped_func(*args, **kwargs))

        return inner_wrapper

    if func is None:
        return outer_wrapper

    return outer_wrapper(func)


# ==------------------------------------------------------------== #
# Classes                                                          #
# ==------------------------------------------------------------== #
class AsyncSession():
    """Creates requests session for making async HTTP/HTTPS requests."""

    def __init__(self, thread_pool: concurrent.futures.ThreadPoolExecutor = None) -> None:
        self.thread_pool = thread_pool
        self.session = requests.Session()

    async def get(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a GET request."""

        @coroutine(pool=self.thread_pool)
        def inner() -> requests.Response:
            return self.session.get(url, *args, **kwargs)

        return await inner()

    async def post(self, url: str, *args, **kwargs) -> requests.Response:
        """Sends a POST request."""

        @coroutine(pool=self.thread_pool)
        def inner() -> requests.Response:
            return self.session.post(url, *args, **kwargs)

        return await inner()

    async def patch(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a PATCH request."""

        @coroutine(pool=self.thread_pool)
        def inner() -> requests.Response:
            return self.session.patch(url, *args, **kwargs)

        return await inner()

    async def put(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a PUT request."""

        @coroutine(pool=self.thread_pool)
        def inner() -> requests.Response:
            return self.session.put(url, *args, **kwargs)

        return await inner()

    async def delete(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a DELETE request."""

        @coroutine(pool=self.thread_pool)
        def inner() -> requests.Response:
            return self.session.delete(url, *args, **kwargs)

        return await inner()


# ==------------------------------------------------------------== #
# Async functions                                                  #
# ==------------------------------------------------------------== #
async def get(url: str, *args: typing.Any, thread_pool: concurrent.futures.ThreadPoolExecutor = None, **kwargs: typing.Any) -> requests.Response:
    """Sends a GET request."""

    @coroutine(pool=thread_pool)
    def inner() -> requests.Response:
        return requests.get(url, *args, **kwargs)

    return await inner()


async def post(url: str, *args: typing.Any, thread_pool: concurrent.futures.ThreadPoolExecutor = None, **kwargs: typing.Any) -> requests.Response:
    """Sends a POST request."""

    @coroutine(pool=thread_pool)
    def inner() -> requests.Response:
        return requests.post(url, *args, **kwargs)

    return await inner()


async def patch(url: str, *args: typing.Any, thread_pool: concurrent.futures.ThreadPoolExecutor = None, **kwargs: typing.Any) -> requests.Response:
    """Sends a PATCH request."""

    @coroutine(pool=thread_pool)
    def inner() -> requests.Response:
        return requests.patch(url, *args, **kwargs)

    return await inner()


async def put(url: str, *args: typing.Any, thread_pool: concurrent.futures.ThreadPoolExecutor = None, **kwargs: typing.Any) -> requests.Response:
    """Sends a PUT request."""

    @coroutine(pool=thread_pool)
    def inner() -> requests.Response:
        return requests.put(url, *args, **kwargs)

    return await inner()


async def delete(url: str, *args: typing.Any, thread_pool: concurrent.futures.ThreadPoolExecutor = None, **kwargs: typing.Any) -> requests.Response:
    """Sends a DELETE request."""

    @coroutine(pool=thread_pool)
    def inner() -> requests.Response:
        return requests.delete(url, *args, **kwargs)

    return await inner()
