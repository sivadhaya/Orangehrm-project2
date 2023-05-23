from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

#Login functionality

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
print("status:sucessfully login")

#Switching from dashboard to Admin page

driver.switch_to.parent_frame()

#Admin page details

driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()

#Validate admin MENU options

Menuoptions = driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']")
print(Menuoptions.text)
Menuoptions.is_displayed()
print("status:", Menuoptions.is_displayed())
time.sleep(5)

driver.quit()