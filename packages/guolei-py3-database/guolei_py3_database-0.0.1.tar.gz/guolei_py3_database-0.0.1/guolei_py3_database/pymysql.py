#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import functools
from typing import List

import pymysql
from pymysql import Connect
from pymysql.cursors import DictCursor


def get_connect(**kwargs) -> Connect:
    """
    get pymysql.Connect class object
    :param kwargs: pymysql.Connect __init__ parameters
    :return: pymysql.Connect class object
    """
    if not isinstance(kwargs, dict) or not len(kwargs):
        raise TypeError("kwargs must be a dictionary and not empty")
    if not "cursorclass" in kwargs.keys():
        kwargs["cursorclass"] = DictCursor
    return Connect(**kwargs)


def call_get_connect() -> Connect:
    """
    apply decorator call pymysql.Connect class object
    :return: pymysql.Connect class object
    def _call_connect():
        return {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'jtwy_smarty_community_dev_db',
        }

    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(**kwargs):
            return get_connect(**func(**kwargs))

        return wrapper_func

    return decorator_func


def close_connect(connect: Connect = None) -> bool:
    """
    close pymysql.Connect class object
    :param connect:
    :return: bool
    """
    if isinstance(connect, Connect):
        connect.close()
        return True
    return False


def call_close_connect(connect: Connect = None) -> bool:
    """
    apply decorator call close pymysql.Connect class object
    :param connect: pymysql.Connect class object
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


def call_execute(connect: Connect = None, is_closed_connect: bool = False) -> tuple:
    """
    apply decorator call pymysql.cursors.Cursor execute method
    :param connect: pymysql.Connect class object
    :param is_closed_connect: closed connect if True
    :return: tuple
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            func_results = func(*args, **kwargs)
            with connect.cursor() as cursor:
                try:
                    if isinstance(func_results, tuple):
                        cursor.execute(*func_results)
                    if isinstance(func_results, dict):
                        cursor.execute(**func_results)
                    if isinstance(func_results, str):
                        cursor.execute(func_results)
                    connect.commit()
                    return True, cursor.rowcount, cursor.lastrowid, None
                except Exception as error:
                    connect.rollback()
                    return False, -1, -1, error
                finally:
                    cursor.close()
            if is_closed_connect and isinstance(connect, Connect):
                connect.close()

        return wrapper_func

    return decorator_func


def call_execute_many(connect: Connect = None, is_closed_connect: bool = False) -> tuple:
    """
    apply decorator call pymysql.cursors.Cursor executemany method
    :param connect: pymysql.Connect class object
    :param is_closed_connect: closed connect if True
    :return: tuple
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            func_results = func(*args, **kwargs)
            with connect.cursor() as cursor:
                try:
                    if isinstance(func_results, tuple):
                        cursor.executemany(*func_results)
                    if isinstance(func_results, dict):
                        cursor.executemany(**func_results)
                    if isinstance(func_results, str):
                        cursor.executemany(func_results)
                    connect.commit()
                    return True, cursor.rowcount, None
                except Exception as error:
                    connect.rollback()
                    return False, -1, error
                finally:
                    cursor.close()
            if is_closed_connect and isinstance(connect, Connect):
                connect.close()

        return wrapper_func

    return decorator_func


def call_execute_fetch_one(connect: Connect = None, is_closed_connect: bool = False) -> tuple:
    """
    apply decorator call pymysql.cursors.Cursor fetchone method
    :param connect: pymysql.Connect class object
    :param is_closed_connect: closed connect if True
    :return: tuple
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            func_results = func(*args, **kwargs)
            with connect.cursor() as cursor:
                try:
                    if isinstance(func_results, tuple):
                        cursor.execute(*func_results)
                    if isinstance(func_results, dict):
                        cursor.execute(**func_results)
                    if isinstance(func_results, str):
                        cursor.execute(func_results)
                    return True, cursor.fetchone(), None
                except Exception as error:
                    return False, {}, error
                finally:
                    cursor.close()
            if is_closed_connect and isinstance(connect, Connect):
                connect.close()

        return wrapper_func

    return decorator_func


def call_execute_fetch_all(connect: Connect = None, is_closed_connect: bool = False) -> tuple:
    """
    apply decorator call pymysql.cursors.Cursor fetchall method
    :param connect: pymysql.Connect class object
    :param is_closed_connect: closed connect if True
    :return: tuple
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            func_results = func(*args, **kwargs)
            with connect.cursor() as cursor:
                try:
                    if isinstance(func_results, tuple):
                        cursor.execute(*func_results)
                    if isinstance(func_results, dict):
                        cursor.execute(**func_results)
                    if isinstance(func_results, str):
                        cursor.execute(func_results)
                    return True, cursor.fetchall(), None
                except Exception as error:
                    return False, [], error
                finally:
                    cursor.close()
            if is_closed_connect and isinstance(connect, Connect):
                connect.close()

        return wrapper_func

    return decorator_func


def call_execute_transaction(connect: Connect = None, is_closed_connect: bool = False) -> tuple:
    """
    apply decorator call pymysql.cursors.Cursor transaction method
    :param connect: pymysql.Connect class object
    :param is_closed_connect: closed connect if True
    :return: tuple
    """

    def decorator_func(func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            func_results = func(*args, **kwargs)
            with connect.cursor() as cursor:
                try:
                    connect.begin()
                    for func_result in func_results:
                        if isinstance(func_result, dict):
                            cursor.execute(**func_result)
                        if isinstance(func_result, tuple):
                            cursor.execute(*func_result)
                        if isinstance(func_result, str):
                            cursor.execute(func_result)
                    connect.commit()
                    return True, cursor.rowcount(), None
                except Exception as error:
                    connect.rollback()
                    return False, -1, error
                finally:
                    cursor.close()
            if is_closed_connect and isinstance(connect, Connect):
                connect.close()

        return wrapper_func

    return decorator_func
