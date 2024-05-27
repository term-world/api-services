import inspect
from typing import Callable
from functools import wraps
from django.urls import path, include

class Route:

    def __init__(self):
        self.urls = []

    def endpoint(version):
        def create_endpoint(fn: Callable):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                return fn(*args, **kwargs)
            wrapper.version = version
            wrapper.decorated = True
            return wrapper
        return create_endpoint

    def add_endpoints(self):
        pass

    def add_url(self, endpoint: str = "", fn: Callable = callable(None)) -> None:
        if not fn:
            return
        self.urls.append(
            path(endpoint, fn)
        )

