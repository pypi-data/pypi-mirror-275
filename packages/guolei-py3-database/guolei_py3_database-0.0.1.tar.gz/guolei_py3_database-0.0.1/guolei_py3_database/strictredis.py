#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import functools

import redis


def get_connect(**kwargs):
    try:
        return redis.StrictRedis(**kwargs)
    except Exception as error:
        return False


def call_get_connect() -> redis.StrictRedis:
    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(**kwargs):
            return get_connect(**func(**kwargs))

        return wrapper_func

    return decorator_func


def close_connect(connect: redis.StrictRedis = None) -> bool:
    """
    close redis.StrictRedis class object
    :param connect:
    :return: bool
    """
    if isinstance(connect, redis.StrictRedis):
        connect.close()
        return True
    return False


def call_close_connect(connect: redis.StrictRedis = None) -> bool:
    """
    apply decorator call close redis.StrictRedis class object
    :param connect: redis.StrictRedis class object
    :return: bool
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(**kwargs):
            if func(**kwargs):
                return close_connect(connect=connect)
            return False

        return wrapper_func

    return decorator_func


def call_execute(connect: redis.StrictRedis = None, attr: str = None):
    """
    apply decorator call redis.StrictRedis  execute method
    :param connect: redis.StrictRedis  class object
    :return: any
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            if not attr:
                raise ValueError("attr must be set")
            if hasattr(connect, attr):
                _attr = getattr(connect, attr)
            func_results = func(*args, **kwargs)
            if isinstance(func_results, tuple):
                return _attr(*func_results)
            if isinstance(func_results, dict):
                return _attr(**func_results)
            if isinstance(func_results, str):
                return _attr(func_results)
            raise TypeError(f"{attr} is not callable")

        return wrapper_func

    return decorator_func
