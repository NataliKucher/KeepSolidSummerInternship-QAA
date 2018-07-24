from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.vpnunlimitedapp.com/en/pricing')

driver.find_element_by_xpath("//h4[@class='price_name' and text()='1 year']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='log_change_plan_btn']"))).click()

element = driver.find_element_by_xpath("//h2[text()='Login using an existing KeepSolid ID']")
wait = WebDriverWait(driver, 10)
driver.refresh()
wait.until(EC.staleness_of(element))

driver.quit()
