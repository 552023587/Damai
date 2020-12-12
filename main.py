from selenium import webdriver
from lib import AppConfig
import os
import time
from selenium.webdriver.firefox.options  import Options
from lib import Cookie

url = AppConfig.readConfig("APP","url")
date = int(AppConfig.readConfig("APP","date"))
sku = int(AppConfig.readConfig("APP","sku")) 
set_options = Options()
set_options.add_argument("--headless")
firefox_login  = webdriver.Firefox(firefox_options=set_options)
#firefox_login.minimize_window()
firefox_login.get(url)
damai_cookie = Cookie.DaMai_Cookie(firefox_login)
firefox_login = damai_cookie.load()
#场次
select_lists = firefox_login.find_elements_by_xpath("//div[@class='perform__order__select perform__order__select__performs']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item']")
print("选择场次:"+str(date))
if date > 1:
    select_lists[date - 2].click()    
time.sleep(1)
#票档
select_lists = firefox_login.find_elements_by_xpath("//div[@class='perform__order__select']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item sku_item']")
time.sleep(1)    
print("选择票档:"+str(sku))
if sku > 1:
    select_lists[sku - 2].click()    
#选择购票数量
print("选择购票数量:"+AppConfig.readConfig("APP","buyNum"))
buyNum = firefox_login.find_element_by_xpath("//a[@class='cafe-c-input-number-handler cafe-c-input-number-handler-up']")
for i in AppConfig.readConfig("APP","buyNum"):
    buyNum.click()
#提交购买    
buyBtn = firefox_login.find_element_by_class_name("buybtn")  
if buyBtn.text == "立即购买":  
    buyBtn.click()
    time.sleep(1)   
    ##选择观影人
    print("选择观影人")
    people  = firefox_login.find_elements_by_xpath("//div[@class='next-col buyer-list-item']")
    for p in people:
        p.click()
    #提交订单
    print("提交订单")
    submit = firefox_login.find_element_by_xpath("//div[@class='submit-wrapper']/button[@class='next-btn next-btn-normal next-btn-medium']")
    submit.click()
    print("已完成购买，请立即支付")
else:
    print("已售罄")    

