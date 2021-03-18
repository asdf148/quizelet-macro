import selenium
import time
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
url = "https://quizlet.com/kr/574810724/lesson-1-a-role-model-flash-cards/"
driver.get(url)

vocaArr = []
voca = []

length = 0
answer = ""

leave = ""
wrong = ""
right = ""

driver.find_element_by_css_selector(".AssemblyButtonBase.AssemblyTextButton.AssemblyTextButton--inverted.AssemblyButtonBase--small").click()
driver.find_element_by_css_selector(".UIButton.UIButton--social.UIButton--fill.UIButton--hero").click()
driver.implicitly_wait(5)
driver.find_element_by_name('identifier').send_keys("202615ljy@dsm.hs.kr")
driver.find_element_by_name('identifier').send_keys(Keys.ENTER)

driver.implicitly_wait(5)

driver.find_element_by_name('password').send_keys('wnduf0987@')
driver.find_element_by_name('password').send_keys(Keys.ENTER)

driver.implicitly_wait(20)

driver.find_element_by_css_selector(".UIIcon.UIIcon--x.UIModal-closeIcon.UIModal-closeIcon.UIIcon--xlarge").click()

# ////////////////////////////////////////////////////////////////////////////////////////////////////
driver.implicitly_wait(40)

driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[5].click()

driver.implicitly_wait(20)

driver.find_element_by_css_selector(".UIButton-wrapper").click()


sys.stdout = open("vocalist.txt", "w")

for j in range(0, 10):
    kos = driver.find_elements_by_css_selector(".FormattedText.notranslate.TermText.MatchModeQuestionGridTile-text.lang-ko")
    ens = driver.find_elements_by_css_selector(".FormattedText.notranslate.TermText.MatchModeQuestionGridTile-text.lang-en")
    time.sleep(1)
    for i in range(0, 6):
        print("영어: ", ens[i].text, "뜻: ", kos[i].text)
    driver.refresh()
    driver.implicitly_wait(20)

    driver.find_element_by_css_selector(".UIButton-wrapper").click()

sys.stdout.close()