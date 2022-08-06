#system libraries
import os
import sys
import random
from random import randint
import time
from datetime import datetime
#selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


# Custom module
from modules.cswait import SWait
from modules.airmode import RestartPhone
curdir = os.path.dirname(__file__)

# Config here
chrome_path = 'E:/1 GOOGLE'
def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)
now = datetime.now()
str_now = now.strftime("%Hh%Mm%Ss__%m-%d-%Y")
backup_name = 'follow_tw_'+str_now+'.txt'
backup_path = os.path.join(curdir,backup_name)

for i in range(3,105):
    driver_path = os.path.join(curdir, 'webdriver/chromedriver.exe')
    options = Options()
    options.binary_location = chrome_path+"/chrome_"+str(i)+"/GoogleChromePortable.exe"
    options.add_argument("user-data-dir="+chrome_path+"/chrome_"+str(i)+"/Data/profile")
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    # driver.implicitly_wait(4)
    cswait = SWait(driver)
    links = ["https://twitter.com/moon3dge"]
    for link in links:
        driver.get(link)
        time.sleep(randint(2,4))
        result = cswait.click_by_xpath(4,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div')
        time.sleep(randint(2,4))
        result = cswait.click_by_xpath(4,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div')
        
    #     if result == 'success':
    #         append_new_line(backup_path,'Twitter '+str(i)+' follow: '+link)
    #     time.sleep(randint(6, 12))
    time.sleep(3)
    RestartPhone()
    driver.close()
    time.sleep(10)
    print(" Xong : ",str(i))

else:
    print("Hết rồi chạy cái del gì")

#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div
