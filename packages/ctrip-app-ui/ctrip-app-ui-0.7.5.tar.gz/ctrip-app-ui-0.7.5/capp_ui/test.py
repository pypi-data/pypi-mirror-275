# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctrip-app-ui
# FileName:     test.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/04/25
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from domain_service import CtripAppService


def test_service():
    app = CtripAppService(device_id="66J5T19627007749", enable_debug=False, platform="Android", port=0)
    app.device.wake()
    app.restart()
    app.hide_navigation_bar()


if __name__ == '__main__':
    test_service()
