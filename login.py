from selenium import webdriver
from lib import AppConfig
import os
import time
import json
from lib import Cookie

url = AppConfig.readConfig("APP","url")
firefox_login  = webdriver.Firefox()
firefox_login.get(url)
#自动登录-验证码
# firefox_login.switch_to.window(firefox_login.window_handles[0])
# print(firefox_login.window_handles)
# firefox_login.switch_to.frame("alibaba-login-box")
# login_tab = firefox_login.find_elements_by_xpath("//div[@id='login-tabs']/div[@class='login-tabs-tab']")
# login_tab[0].click()
# login_mobile = firefox_login.find_element_by_id("fm-sms-login-id")
# login_mobile.send_keys("123123123123123")
# time.sleep(1)
# verify_btn = firefox_login.find_element_by_xpath("//a[@class='send-btn-link']")
# verify_btn.click()
# print("验证码已发送，请在15秒内填写")
# time.sleep(15)
# login_btn = firefox_login.find_element_by_class_name('sms-login')
# login_btn.click()
time.sleep(30)
with open('cookies.txt','w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(firefox_login.get_cookies()))

firefox_login.close()
