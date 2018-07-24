from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.vpnunlimitedapp.com/en')

driver.find_element_by_xpath("//div[@class='pulse2']").click()
element = driver.find_element_by_xpath("//div[@class='iframeWrap']/descendant::video")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(element))

driver.quit()
