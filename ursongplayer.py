from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

song_name=input("Enter Song Name:")
browser = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
browser.get('http://www.youtube.com')
browser.find_element_by_xpath("//*[@id='search']").send_keys(song_name)
browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="title-wrapper"]').click()



#browser.close()
