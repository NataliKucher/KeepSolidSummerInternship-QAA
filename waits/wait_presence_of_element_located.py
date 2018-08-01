from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://www.vpnunlimitedapp.com/en/pricing')
browser.find_element_by_xpath("//div[@class='prices_cnt--item__header']").click()
wait = WebDriverWait(browser, 10) 
element = wait.until(EC.presence_of_element_located((By.XPATH,"//h2[text()='Login using an existing KeepSolid ID']")))
browser.quit()