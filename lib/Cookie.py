if __name__ == "__main__":
   import Global
else:
   from lib import Global
import re
import json

class DaMai_Cookie:

   def __init__(self,driver):
         self.driver = driver
   def load(self):
      self.driver.delete_all_cookies()
      with open('cookies.txt','r') as cookief:
         #使用json读取cookies 注意读取的是文件 所以用load而不是loads
         cookieslist = json.load(cookief)
         for cookie in cookieslist:
            self.driver.add_cookie(cookie)
      return self.driver

    