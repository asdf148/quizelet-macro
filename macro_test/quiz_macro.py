import selenium
import time
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://quizlet.com/kr/574810724/lesson-1-a-role-model-flash-cards/"
driver.get(url)

vocaArr = []
voca = []

driver.find_element_by_css_selector(".AssemblyButtonBase.AssemblyTextButton.AssemblyTextButton--inverted.AssemblyButtonBase--small").click()
driver.find_element_by_css_selector(".UIButton.UIButton--social.UIButton--fill.UIButton--hero").click()
driver.find_element_by_name('identifier').send_keys("202615ljy@dsm.hs.kr")
driver.find_element_by_name('identifier').send_keys(Keys.ENTER)

driver.implicitly_wait(5)

driver.find_element_by_name('password').send_keys('wnduf0987@')
driver.find_element_by_name('password').send_keys(Keys.ENTER)

driver.implicitly_wait(20)

driver.find_element_by_css_selector(".UIIcon.UIIcon--x.UIModal-closeIcon.UIModal-closeIcon.UIIcon--xlarge").click()

# 단어 저장
driver.implicitly_wait(40)
driver.find_element_by_css_selector(".SetPageModeButton-modeName").click()

mean = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--firstSide.CardsItemSide--showing.has-text.showing-hint").get_attribute("aria-label")

english = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--secondSide.has-text.showing-hint").get_attribute("aria-label")


progress = driver.find_element_by_css_selector(".CardsControls-progressValue").text

sys.stdout = open("voca.txt","w")

driver.find_elements_by_css_selector(".CardsNavigationButton")[1].click()

while progress != "70/70":
    driver.implicitly_wait(10)
    mean = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--firstSide.CardsItemSide--showing.has-text").get_attribute("aria-label")
    english = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--secondSide.has-text").get_attribute("aria-label")
    progress = driver.find_element_by_css_selector(".CardsControls-progressValue").text
    print("영어: ",english,"\n","뜻: ",mean, "\n")
    driver.find_elements_by_css_selector(".CardsNavigationButton")[1].click()

sys.stdout.close()

# 단어 배열에 저장
r = open("voca.txt", mode ="r", encoding="euc-kr")

for i in range(0, 69):
    r.read(4)
    english = r.readline()
    r.read(3)
    mean = r.readline()
    r.readline()

    voca.append(english)
    voca.append(mean)

    vocaArr.append(voca)
    voca = []

r.close()

# 뒤로가기 추가 해야함

# 주관식

driver.implicitly_wait(40)
driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[2].click()

driver.implicitly_wait(10)

values = driver.find_elements_by_css_selector(".WriteProgress-value")

leave = values[0].text
wrong = values[1].text
right = values[2].text

print(not(int(leave) == 0 & int(wrong) == 0 & int(right) == 70))

while not(int(leave) == 0 & int(wrong) == 0 & int(right) == 70):

    time.sleep(2)

    print(leave)
    print(wrong)
    print(right)

    ques = driver.find_element_by_css_selector(".FormattedText.notranslate.lang-ko").get_attribute("aria-label")

    print("문제: ",ques)

    for i in range(0, 69):
        if vocaArr[i][1] == ques:
            print(vocaArr[i][0])
            answer = vocaArr[i][0]
            break

    driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(answer)
    driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(Keys.ENTER)

    leave = values[0].text
    wrong = values[1].text
    right = values[2].text