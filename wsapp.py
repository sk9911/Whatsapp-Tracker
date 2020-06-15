from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from notify_run import Notify

print('Welcome to Whatsapp activity tracker!')
target = input('Enter the name of the person(as in your contacts) or their phone number to track ')

## ENTER THE ENDPOINT ATTRIBUTE HERE
notify = Notify(endpoint='https://notify.run/XXXXXXXXXXXXXXXX')
options = webdriver.ChromeOptions() 
options.add_argument('--headless')
options.add_argument('profile-directory=Default')
driver = webdriver.Chrome(ChromeDriverManager().install(), options= options)
driver.get("http://web.whatsapp.com")

wait = WebDriverWait(driver, 600)

element = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_2FVVk cBxw-']//div[@class='_3FRCZ copyable-text selectable-text']")))

time.sleep(1)

# NameBox = driver.find_element_by_xpath("//div[@class='_2FVVk cBxw-']//div[@class='_3FRCZ copyable-text selectable-text']")
element.click()
element.send_keys(target , Keys.ENTER)

time.sleep(1)
notif = []
a=0
while a>-1:

    if a==0:
        try:
            try:
                driver.find_element_by_xpath("//span[@class='_3-cMa _3Whw5']")
                notify.send(f'{target} is online')
                a=1
                time.sleep(1)
                
            except:
                notify.send(f'{target} is offline')
                time.sleep(1)
                a=2
                
        except:
            print('Error')
            a=-3

    elif a==1:
        try:
            try:
                driver.find_element_by_xpath("//span[@class='_3-cMa _3Whw5']")
                time.sleep(1)
                
            except:
                notify.send(f'{target} is offline')
                time.sleep(1)
                a=2
        except:
            print('Error')
            a=-3

    elif a==2:
        try:
            try:
                driver.find_element_by_xpath("//span[@class='_3-cMa _3Whw5']")
                notify.send(f'{target} is online')
                a=1
                time.sleep(1)
                
            except:
                # notify.send('Tejas is offline')
                time.sleep(1)
                
        except:
            print('Error')
            a=-3
    
