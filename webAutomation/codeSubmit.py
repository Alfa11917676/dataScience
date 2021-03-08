from selenium import webdriver
import time
browser=webdriver.Chrome('C:\\Users\\LENOVO\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://codechef.com')
time.sleep(10)
browser.close()
