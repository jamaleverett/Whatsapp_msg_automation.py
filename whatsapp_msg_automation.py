from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

contact ="Jamal"
text = "Hey, this was sent using Selenium! Pretty cool, right?!"

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

inp_xpath_search = "//input[@title='Search or start new chat']"
input_box_search = WebDriverWait(browser,50) .until(lambda browser:
browser.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send.keys(contact)
time.sleep(2)

selected_contact = browser.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = browser.find_element_by_xpath(inp_xpath)
time.sleep(2)
input_box.send_keys(text + Keys.ENTER)
time.sleep(2)
browser.quit()

