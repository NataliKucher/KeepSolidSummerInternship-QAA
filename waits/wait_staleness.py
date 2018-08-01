from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.vpnunlimitedapp.com/en/pricing')
driver.find_element_by_xpath("//a[@class='prices_cnt--item']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pricing_title_in_header']/descendant::h2")))
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Change plan')]")))
element.click()
el2 = driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/descendant::h2")
driver.refresh()  # because el2 still place in the DOM 
wait.until(EC.staleness_of(el2))

driver.quit()
