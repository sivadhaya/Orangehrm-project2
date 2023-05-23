from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
#Check username textbox is visible while clicking the forget password link
driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
testbox = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
testbox.is_displayed()
print("status:", testbox.is_displayed())
time.sleep(3)
driver.find_element(By.NAME, "username").send_keys("dhayalan7255@gmail.com")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)
print("status : Link send succesfully")
driver.quit()

