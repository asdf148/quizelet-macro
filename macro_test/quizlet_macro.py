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
voca = ""

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

# 단어 저장
# ~~~~~
# driver.implicitly_wait(40)
# driver.find_element_by_css_selector(".SetPageModeButton-modeName").click()

# mean = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--firstSide.CardsItemSide--showing.has-text.showing-hint").get_attribute("aria-label")
# ~~~~~
# print(mean)
# ~~~~~
# english = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--secondSide.has-text.showing-hint").get_attribute("aria-label")
# ~~~~~
# print(english)

# ~~~~~
# progress = driver.find_element_by_css_selector(".CardsControls-progressValue").text
# ~~~~~
# print(progress)

# ~~~~~
# sys.stdout = open("voca.txt","w")
# ~~~~~
# print("영어: ",english,"\n","뜻: ",mean, "\n")

# driver.find_elements_by_css_selector(".CardsNavigationButton")[1].click()

# mean = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--firstSide.CardsItemSide--showing.has-text").get_attribute("aria-label")
# print(mean)
# english = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--secondSide.has-text").get_attribute("aria-label")
# print(english)

# progress = driver.find_element_by_css_selector(".CardsControls-progressValue").text
# print(progress)

# sys.stdout = open("voca.txt","a")
# print("영어: ",english,"\n","뜻: ",mean,"\n\n")


# CardsItemSide CardsItemSide--firstSide CardsItemSide--showing has-text showing-hint
# CardsItemSide CardsItemSide--firstSide CardsItemSide--showing has-text
# CardsItemSide CardsItemSide--firstSide CardsItemSide--showing has-text
# CardsItemSide CardsItemSide--firstSide CardsItemSide--showing has-text

# CardsItemSide CardsItemSide--secondSide has-text showing-hint
# CardsItemSide CardsItemSide--secondSide has-text
# CardsItemSide CardsItemSide--secondSide has-text
# ~~~
# while progress != "70/70":
#     driver.implicitly_wait(10)
#     mean = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--firstSide.CardsItemSide--showing.has-text").get_attribute("aria-label")
#     english = driver.find_element_by_css_selector(".CardsItemSide.CardsItemSide--secondSide.has-text").get_attribute("aria-label")
#     progress = driver.find_element_by_css_selector(".CardsControls-progressValue").text
#     # sys.stdout = open("voca","a")
#     print("영어: ",english,"\n","뜻: ",mean, "\n")
#     driver.find_elements_by_css_selector(".CardsNavigationButton")[1].click()

# sys.stdout.close()
# ~~~~
# 단어 배열에 저장
r = open("voca.txt", mode ="r", encoding="euc-kr")
# english = sys.stdout.readline()
# print(english)
# mean = sys.stdout.readline()
# print(mean)

# sys.stdout.close()
# ~~~~~~
for i in range(0, 70):
    r.read(4)
    english = r.readline()

    length = len(english)-2
    english = english[:length]
    english = english[1:]

    r.read(3)
    mean = r.readline()

    length = len(mean)-2
    mean = mean[:length]
    mean = mean[2:]

    r.readline()

    if i == 0:
        voca = {mean: english}
    else:
        voca[mean] = english

r.close()
# ~~~~
# ?driver.find_element_by_css_selector("SetPageModeButton-modeName").click()

# driver.find_element_by_css_selector(".UIIcon.UIIcon--wedge-right").click()


# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "password"))).send_Keys("wnduf0987@")
# element = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".whsOnd.zHQkBf"), "Project INTEGRATED_BUILD_SYSTEM_TOOL"))
# element = driver.find_element_by_css_selector(".whsOnd.zHQkBf")
# print(element)

# password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']" )))
# password.send_keys('wnduf0987@')

# element.send_keys('wnduf0987@')
# driver.find_element_by_css_selector(".whsOnd.zHQkBf").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector(".VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.qIypjc.TrZEUc.lw1w4b").click()

# 뒤로가기 버튼 누르기
# ~~~~~
# driver.implicitly_wait(40)
# driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[2].click()

# driver.implicitly_wait(10)

# values = driver.find_elements_by_css_selector(".WriteProgress-value")

# leave = values[0].text
# wrong = values[1].text
# right = values[2].text

# print(not(int(leave) == 0 & int(wrong) == 0 & int(right) == 70))

# while not(int(leave) == 0 & int(wrong) == 0 & int(right) == 70):

#     time.sleep(2)

#     print(leave)
#     print(wrong)
#     print(right)
# ~~~~~
    # driver.find_element_by_css_selector("AutoExpandTextarea-textarea").send_keys()
# ~~~
    # ques = driver.find_element_by_css_selector(".FormattedText.notranslate.lang-ko").get_attribute("aria-label")

    # print("문제: ",ques)

    # for i in range(0, 70):
    #     if vocaArr[i][1] == ques:
    #         print(vocaArr[i][0])
    #         answer = vocaArr[i][0]
    #         break

    # driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(answer)
    # driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(Keys.ENTER)

    # leave = values[0].text
    # wrong = values[1].text
    # right = values[2].text
# ~~~~~

# 학습하기(보류)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# driver.implicitly_wait(40)

# driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[1].click()

# driver.implicitly_wait(40)

# driver.find_element_by_css_selector(".UIButton.UIButton--hero").click()


# driver.implicitly_wait(40)

# try:
#     value = driver.find_elements_by_css_selector(".UIHeading.UIHeading--four")[2]
#     progress = value.text
# except:
#     value = null

# try:
#     value1 = driver.find_elements_by_css_selector(".bkgntm5")[2]
#     progress1 = value1.text
# except:
#     value1 = null

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# print(value, value1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# while int(progress) != 70:
#     try:
#         ans = driver.find_elements_by_css_selector(".MultipleChoiceQuestionPrompt-termOption")
#         print(ans)
#         progress = value.text
#         # progress1 = value1.text

#         ques = driver.find_element_by_css_selector(".FormattedText.notranslate.lang-ko").get_attribute("aria-label")
#         for_break = False
#         for i in range(0, 69):
#             for j in range(0, 1):
#                 if vocaArr[i][j] == ques:
#                     if j == 0:
#                         answer = vocaArr[i][1]
#                         for_break = True
#                         break
#                     else:
#                         answer = vocaArr[i][0]
#                         for_break = True
#                         break
#             if for_break == True:
#                 break
#         for i in range(0, 4):
#             if ans[i].text == answer:
#                 driver.find_elements_by_css_selector(".MultipleChoiceQuestionPrompt-termOption")[i].click()
#                 break
#         time.sleep(2)

#     except NoSuchElementException:
#         print("단답")

#     try:
#         ques = driver.find_element_by_css_selector(".FormattedText.notranslate.lang-ko").get_attribute("aria-label")
#         progress = value.text
#         # progress1 = value1.text

#         print(ques)

#         for_break = False
#         for i in range(0, 70):
#             for j in range(0, 2):
#                 if vocaArr[i][j] == ques:
#                     if j == 0:
#                         answer = vocaArr[i][1]
#                         for_break = True
#                         break
#                     else:
#                         answer = vocaArr[i][0]
#                         for_break = True
#                         break
#             if for_break == True:
#                 break
#         print(answer) 
#         driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(answer)
#         driver.find_element_by_css_selector(".AutoExpandTextarea-textarea").send_keys(Keys.ENTER)

#         time.sleep(2)

#     except NoSuchElementException:
#         print("사지선다")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FormattedText notranslate lang-en

# ans = driver.find_elements_by_css_selector(".MultipleChoiceQuestionPrompt-termOption")

# if ans[0]:

# 카드 맞추기

driver.implicitly_wait(40)

driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[5].click()

driver.implicitly_wait(20)

driver.find_element_by_css_selector(".UIButton-wrapper").click()

kos = driver.find_elements_by_css_selector(".FormattedText.notranslate.TermText.MatchModeQuestionGridTile-text.lang-ko")
ens = driver.find_elements_by_css_selector(".FormattedText.notranslate.TermText.MatchModeQuestionGridTile-text.lang-en")


# for i in range(0, 6):
#     print("뜻", kos[i].text)
#     print("영어", ens[i].text)

# for i in range(0, 6):
#     print("뜻", kos[i])
#     print("영어", ens[i])

for i in range(0, 6):
    ens = driver.find_elements_by_css_selector(".FormattedText.notranslate.TermText.MatchModeQuestionGridTile-text.lang-en")
    kos[i].click()
    # print(kos[i].text)
    # print(voca[kos[i].text])
    for j in range(0, len(ens)):
        if voca[kos[i].text] == ens[j].text:
            ens[j].click()
            break
    # for j in range(0, 70):
    #     if kos[i].text == vocaArr[j][1]:
            
    #         break
    # for j in range(0, len(ens)):
    #     if ens[j].text == en:
    #         ens[j].click()
    #         break

# for i in range(0, 69):
    #     if vocaArr[i][1] == ques:
    #         print(vocaArr[i][0])
    #         answer = vocaArr[i][0]
    #         break

# 1.뜻 선택 2.맞는 영어 찾기 3.영어 선택