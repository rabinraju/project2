import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By

my_driver = webdriver.Edge()
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
my_driver.maximize_window()
time.sleep(3)
forgot_link = my_driver.find_element(By.XPATH, "//p[text()='Forgot your password? ']")
forgot_link.click()
time.sleep(2)
empty_username = my_driver.find_element(By.NAME, "username")
empty_username.send_keys(" ")
click_reset_button = my_driver.find_element(By.XPATH, "//button[text()=' Reset Password ']")
if empty_username.get_attribute("value") == "":
    print("Reset Password link sent successfully")
else:
    click_reset_button.click()
    time.sleep(2)
    print("Required")
# Valid_username
valid_username1 = my_driver.find_element(By.NAME, "username")
valid_username1.send_keys("Admin")
click_reset_button1 = my_driver.find_element(By.XPATH, "//button[text()=' Reset Password ']")
if valid_username1.get_attribute("value") == "":
    print("Required")
else:
    click_reset_button1.click()
    time.sleep(2)
    print("Reset Password link sent successfully")

# my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset")
# time.sleep(2)
my_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
time.sleep(3)
my_driver.back()
my_driver.forward()
my_driver.implicitly_wait(2)
invalid_username = my_driver.find_element(By.NAME, "username")
invalid_username.send_keys("nonsympathiser")
click_reset_button = my_driver.find_element(By.XPATH, "//button[text()=' Reset Password ']")
if invalid_username.get_attribute("value") == "":
    print("Required")
else:
    click_reset_button.click()
    time.sleep(5)
    print("Reset Password link sent successfully")
my_driver.quit()

