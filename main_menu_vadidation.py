import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
element_username = driver.find_element(By.NAME, "username")
element_username.send_keys("admin")
time.sleep(4)
element_password = driver.find_element(By.NAME, "password")
element_password.send_keys("admin123")
time.sleep(4)
element_login_btn = driver.find_element(By.XPATH, '//form/div[3]/button')
element_login_btn.click()
time.sleep(4)
driver.implicitly_wait(4)
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")
time.sleep(3)
driver.back()
driver.forward()
element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")

element = driver.find_element(By.XPATH, "//*/div[1]/div[1]/aside/nav/div[2]/ul/li[13]/a/span")
if element is not None:
    element.click()
    time.sleep(3)
    print("displayed")
else:
    print("The element was not found.")
    print("PIM is not displayed")
    driver.quit()