# coding:utf-8
# coding:gb2312

import time

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'  # test platform
desired_caps['deviceName'] = 'emulator-5554 '
desired_caps['platformVersion'] = '5.1.1'
desired_caps['appPackage'] = 'com.example.stamp'
desired_caps['appActivity'] = 'MainActivity'  # config the cap
desired_caps['newCommandTimeout'] = '30'  # set the session wait time


dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
dr.find_element_by_id('com.example.stamp:id/Radio_home').click()
# use ui automator viewer to find resource id
dr.find_element_by_id('com.example.stamp:id/Radio_order').click()
utext = dr.find_element_by_id('com.example.stamp:id/login_name')
utext.send_keys('13366040193')
# input username 'wolfhu' please confirm your choice
ptext = dr.find_element_by_id('com.example.stamp:id/login_prassword')
ptext.send_keys('111111a')
# input password '111111a'
time.sleep(10)
dr.find_element_by_id('com.example.stamp:id/login_login').click()
time.sleep(10)
dr.find_element_by_id('com.example.stamp:id/Radio_my').click()
time.sleep(20)
#   dfdffdf
dr.reset()
