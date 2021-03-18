import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://google.com"
driver.get(url)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gLFyf.gsfi"))).send_keys("아무거나")
# gLFyf gsfi
# driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys("아무거나")