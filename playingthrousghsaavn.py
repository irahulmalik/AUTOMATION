from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

song_name=input("Enter Song Name:")
browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
browser.get('https://www.jiosaavn.com')
search=browser.find_element_by_xpath('//*[@id="search"]')#dopest way to define search
search.send_keys(song_name)
search.send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div/ol/li[1]/div[3]/div/div[1]/div/div/span/a').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div/section/div/div[2]/div/div/button').click()
#---------
#To play Radio
#browser.find_element_by_xpath('//*[@id="main"]/div/section/div/ul/li[1]/a').click()
#---------


#close_time=browser.find_element_by_xpath('//*[@id="main"]/div/section/div/div[3]/h2/text()[2]').text
#time.sleep(close_time)
#browser.close()
