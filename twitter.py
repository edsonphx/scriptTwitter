from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

time.sleep(3)

inputLogin = driver.find_element_by_name("session[username_or_email]")
inputLogin.send_keys("Edson2021_")

inputPass = driver.find_element_by_name("session[password]")
inputPass.send_keys("MINHASENHACRETA123123")
inputPass.submit()

time.sleep(3)

i = 0
driver.get("https://twitter.com/search?f=live&q=(to:Edson2021_)")
time.sleep(3)
driver.refresh()

time.sleep(2)

x = len(driver.find_elements_by_xpath("//div[@style='padding-bottom: 0px;']/div/div"))-1
print(x)
while(i < x):
    i = i+1
    driver.find_element_by_xpath("//div[@style='padding-bottom: 0px;']/div/div[{}]".format(i)).click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@aria-label='Responder']").click()
    time.sleep(1)
    comment = driver.find_element_by_xpath("//div[@aria-label='Texto do Tweet']")
    comment.send_keys("AGORA TEM BOT DE TWITTER TBM PORAAAAAAA")
    time.sleep(0.5)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
    driver.get("https://twitter.com/search?f=live&q=(to:Edson2021_)since:2020-08-01")
    time.sleep(3)
    driver.refresh()
    time.sleep(2)

print("Acabou porra!")
time.sleep(10)

driver.close()
