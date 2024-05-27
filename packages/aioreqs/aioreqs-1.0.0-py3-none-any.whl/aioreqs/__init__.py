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

    @coroutine
    def get(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a GET request."""

        return self.session.get(url, *args, **kwargs)

    @coroutine
    def post(self, url: str, *args, **kwargs) -> requests.Response:
        """Sends a POST request."""

        return self.session.post(url, *args, **kwargs)

    @coroutine
    def patch(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a PATCH request."""

        return self.session.patch(url, *args, **kwargs)

    @coroutine
    def put(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a PUT request."""

        return self.session.put(url, *args, **kwargs)

    @coroutine
    def delete(self, url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
        """Sends a DELETE request."""

        return self.session.delete(url, *args, **kwargs)


# ==------------------------------------------------------------== #
# Async functions                                                  #
# ==------------------------------------------------------------== #
@coroutine
def get(url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
    """Sends a GET request."""

    return requests.get(url, *args, **kwargs)


@coroutine
def post(url: str, *args, **kwargs) -> requests.Response:
    """Sends a POST request."""

    return requests.post(url, *args, **kwargs)


@coroutine
def patch(url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
    """Sends a PATCH request."""

    return requests.patch(url, *args, **kwargs)


@coroutine
def put(url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
    """Sends a PUT request."""

    return requests.put(url, *args, **kwargs)


@coroutine
def delete(url: str, *args: typing.Any, **kwargs: typing.Any) -> requests.Response:
    """Sends a DELETE request."""

    return requests.delete(url, *args, **kwargs)
