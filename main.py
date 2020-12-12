from selenium import webdriver
from lib import AppConfig
import os
import time
from selenium.webdriver.firefox.options  import Options
from lib import Cookie

url = AppConfig.readConfig("APP","url")
date = int(AppConfig.readConfig("APP","date"))
sku = int(AppConfig.readConfig("APP","sku")) 
retry = int(AppConfig.readConfig("APP","retry")) 
set_options = Options()
if int(AppConfig.readConfig("APP","backend")) == 1:
    set_options.add_argument("--headless")
firefox_login  = webdriver.Firefox(firefox_options=set_options)
#firefox_login.minimize_window()
while(1):
    firefox_login.get(url)
    damai_cookie = Cookie.DaMai_Cookie(firefox_login)
    firefox_login = damai_cookie.load()
    #场次
    select_lists = firefox_login.find_elements_by_xpath("//div[@class='perform__order__select perform__order__select__performs']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item']")
    print("选择场次:"+str(date))
    if date > 1:
        select_lists[date - 2].click()    
        select_txt = select_lists[date - 2].text
    else:
        select_txt = firefox_login.find_element_by_xpath("//div[@class='perform__order__select perform__order__select__performs']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item active']").text
    print("选择场次:"+select_txt)
    time.sleep(1)
    #票档
    select_lists = firefox_login.find_elements_by_xpath("//div[@class='perform__order__select']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item sku_item']")
    time.sleep(1)    
    if sku > 1:
        select_lists[sku - 2].click()  
        select_txt = select_lists[sku - 2].text  
    else:
        select_txt = firefox_login.find_element_by_xpath("//div[@class='perform__order__select']/div[@class='select_right']/div[@class='select_right_list']/div[@class='select_right_list_item sku_item active']").text
    print("选择票档:"+select_txt)
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
        time.sleep(3)
        #弹窗
        alert = firefox_login.find_elements_by_xpath("//div[@class='next-feedback-title']")
        if len(alert) > 0:
            print(alert[0].text)
        else:    
            retry = 0
            print("已完成购买，请立即支付")
        if retry == 0:
            break    
    else:
        print("已售罄")    

