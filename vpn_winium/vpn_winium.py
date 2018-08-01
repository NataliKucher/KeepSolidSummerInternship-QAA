from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Remote(
 command_executor='http://localhost:9999',
 desired_capabilities={
     "app": r"C:\Program Files (x86)\VPN Unlimited\vpn-unlimited.exe"})
driver.find_element_by_name('signInWidget').click()





