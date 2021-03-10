from selenium import webdriver
import time
for i in range(0,1000):
    browser = webdriver.Chrome('C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe')
    browser.get('https://github.com/Priyadarshan2000')
    time.sleep(2)
    browser.close()
print("Done")
#browser.find_element_by_id('')
#browser.close()
