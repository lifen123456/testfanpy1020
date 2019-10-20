#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-04 10:29
# @Author  : Fen.Li
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
# #最大化
# driver.maximize_window()
# sleep(2)
# #最小化
# driver.minimize_window()
# sleep(2)
# #窗口大小
# driver.set_window_size(800,600)
driver.get("http://www.baidu.com")
# #最大化
# driver.maximize_window()
# sleep(2)
# #最小化
# driver.minimize_window()
# sleep(2)
# #窗口大小
# driver.set_window_size(800,600)
# sleep(2)
driver.get("https://cn.bing.com/")
sleep(2)
#回退
driver.back()
sleep(2)
#前进
driver.forward()
sleep(2)
#刷新
driver.refresh()
sleep(2)
#driver.quit()
