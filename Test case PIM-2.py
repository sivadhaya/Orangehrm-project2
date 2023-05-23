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
print("status : sucessfully login")

#Switching from dashboard to Admin page
driver.switch_to.parent_frame()

#Admin page details
driver.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()
time.sleep(5)
print(driver.title)
actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title==expected_title:
    print("title is same")
else:
    print("title is different")

#Validate below options displayed in admin page
admin_page_options = driver.find_element(By.XPATH, "//nav[@aria-label='Topbar Menu']//ul")
print(admin_page_options.text)
admin_page_options.is_displayed()
time.sleep(5)
print("status:", admin_page_options.is_displayed())
driver.quit()