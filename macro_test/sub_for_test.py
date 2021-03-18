import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

driver.implicitly_wait(40)
driver.find_elements_by_css_selector(".SetPageModeButton-modeName")[2].click()

driver.implicitly_wait(10)

values = driver.find_elements_by_css_selector(".WriteProgress-value")

leave = values[0].text
wrong = values[1].text
right = values[2].text

print(leave)
print(wrong)
print(right)

driver.find_element_by_css_selector("AutoExpandTextarea-textarea").send_keys()