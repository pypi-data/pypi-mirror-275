# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctrip-app-ui
# FileName:     libs.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/04/24
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import logging
from time import sleep
from functools import wraps
from airtest.core.error import *
from typing import Any, Callable
from poco.exceptions import PocoNoSuchNodeException, PocoTargetTimeout

logger = logging.getLogger("root")


def airtest_exception_format(func):
    """
    airtest测试框架异常捕获格式化
    :param func:
    :return:
    """

    @wraps(func)
    def _deco(*args, **kwargs):
        try:
            result = func(*args, **kwargs) or None
        except (AdbError, AdbShellError) as e:
            result = (e.stdout + e.stderr).decode()
        except AirtestError as e:
            result = e
        except TimeoutError as e:
            result = e
        return result

    return _deco


class SleepWait(object):

    def __init__(self, wait_time: int = 1) -> None:
        self.wait_time = wait_time

    def __call__(self, func: Callable) -> Any:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result = result if isinstance(result, bool) else (result if result else None)
            sleep(self.wait_time)
            return result

        return wrapper


class LoopFindElement(object):

    def __init__(self, loop: int = 1) -> None:
        self.loop = loop

    def __call__(self, func: Callable) -> Any:
        def wrapper(*args, **kwargs):
            result = None
            for i in range(self.loop):
                # 1秒钟查找一次
                sleep(1)
                try:
                    result = func(*args, **kwargs) or None
                    break
                except PocoNoSuchNodeException as e:
                    logger.error("第{}次查找失败，失败原因：{}".format(i, str(e)))
            return result

        return wrapper


class LoopClickElement(object):

    def __init__(self, loop: int = 1) -> None:
        self.loop = loop

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs) -> bool:
            is_success = False
            for i in range(self.loop):
                try:
                    is_success = func(*args, **kwargs)
                    if is_success is True:
                        break
                except PocoNoSuchNodeException as e:
                    logger.error("第{}次查找失败，失败原因：{}".format(i, str(e)))
                # 1秒钟查找一次
                sleep(1)
            return is_success

        return wrapper


class LoopFindElementSubmit(object):

    def __init__(self, action: str, loop: int = 1) -> None:
        self.loop = loop
        self.action = action

    def __call__(self, func: Callable) -> Any:
        def wrapper(*args, **kwargs) -> bool:
            flag = False
            for i in range(self.loop):
                try:
                    func(*args, **kwargs)
                    flag = True
                    break
                except (PocoNoSuchNodeException, PocoTargetTimeout):
                    logger.error("元素未找到，第{}次点击【{}】失败".format(i + 1, self.action))
                except Exception as e:
                    logger.error(e)
                    break
                # 1秒钟查找一次
                sleep(1)
            return flag

        return wrapper


class LoopExcute(object):

    def __init__(self, action: str, loop: int = 1, sleep: int = 1) -> None:
        self.loop = loop
        self.sleep = sleep
        self.action = action

    def __call__(self, func: Callable) -> Any:
        def wrapper(*args, **kwargs) -> bool:
            flag = False
            for i in range(self.loop):
                if i > 1:
                    logger.warning("尝试第{}次{}".format(i, self.action))
                flag = func(*args, **kwargs)
                if flag is True:
                    break
                sleep(self.sleep)
            if flag is False and self.loop > 2:
                logger.warning("{}次尝试{}都失败".format(self.loop, self.action))
            return flag

        return wrapper


class LoopFindElementObject(object):

    def __init__(self, action: str, loop: int = 1, sleep: int = 1) -> None:
        self.loop = loop
        self.sleep = sleep
        self.action = action

    def __call__(self, func: Callable) -> Any:
        def wrapper(*args, **kwargs) -> dict:
            for i in range(self.loop):
                if i > 1:
                    logger.warning("尝试第{}次{}".format(i, self.action))
                attr = func(*args, **kwargs)
                if attr:
                    return attr
                sleep(self.sleep)
            if self.loop > 2:
                logger.warning("{}次尝试{}都失败".format(self.loop, self.action))
            return dict()

        return wrapper
