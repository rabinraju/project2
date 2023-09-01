from selenium.webdriver import ActionChains
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
time.sleep(1)
element_admin = driver.find_element(By.XPATH, "//span[text()='Admin']")
element_admin.click()
time.sleep(5)
# Go to Admin page and Validate "Title" of the page as "OrangeHRM".
assert driver.title == "OrangeHRM"
page_title = driver.title
print("the title of the current page is : " + page_title)
time.sleep(3)
# Validate the below options are displaying on Admin page:
user_management_element = driver.find_element(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item'][1]")
user_management_element.click()
time.sleep(3)
assert user_management_element.is_displayed()
print("the is user is : " + user_management_element.text)
driver.implicitly_wait(2)
management_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu' and @role='menu' and "
                                                    "@data-v-429cfcf3='']")
management_dropdown_value = management_dropdown.get_attribute("value")
print("The value of the dropdown is : " + management_dropdown.text)
elem_user = driver.find_element(By.XPATH, "//a[text()='Users']")
elem_user.click()
driver.implicitly_wait(2)
# try:
job_element = driver.find_element(By.XPATH, "//span[text()='Job '] ")
job_element.click()
time.sleep(2)
assert job_element.is_displayed()
print("the is user is: " + job_element.text)
driver.implicitly_wait(2)
job_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
job_dropdown_value = job_dropdown.get_attribute("value")
print("The value of the dropdown is" + job_dropdown.text)
elem_title = driver.find_element(By.XPATH, "//a[text()='Job Titles']")
if elem_title:
    elem_title.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    job_element = driver.find_element(By.XPATH, "//span[text()='Job '] ")
    job_element.click()
    driver.implicitly_wait(2)
    job_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    job_dropdown_value = job_dropdown.get_attribute("value")
elem_pay = driver.find_element(By.XPATH, "//a[text()='Pay Grades']")
if elem_pay:
    elem_pay.click()
    time.sleep(3)
else:
    pass

if job_element:
    job_element = driver.find_element(By.XPATH, "//span[text()='Job '] ")
    job_element.click()
    driver.implicitly_wait(2)
    job_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    job_dropdown_value = job_dropdown.get_attribute("value")
    time.sleep(3)

elem_Categories = driver.find_element(By.XPATH, "//a[text()='Job Categories']")
if elem_Categories:
    elem_Categories.click()
    time.sleep(3)
else:
    pass

if job_element:
    job_element = driver.find_element(By.XPATH, "//span[text()='Job '] ")
    job_element.click()
    driver.implicitly_wait(2)
    job_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    job_dropdown_value = job_dropdown.get_attribute("value")
    time.sleep(3)

elem_Shifts = driver.find_element(By.XPATH, "//a[text()='Work Shifts']")
if elem_Shifts:
    elem_Shifts.click()
    time.sleep(4)
else:
    elem_employment = driver.find_element(By.XPATH, "//a[text()='Employment Status']']")
    elem_employment.click()
    time.sleep(4)
    driver.implicitly_wait(5)

# try:
organization_element = driver.find_element(By.XPATH, "//span[text()='Organization ']")
organization_element.click()
time.sleep(2)
assert organization_element.is_displayed()
print("the is user is : " + organization_element.text)
driver.implicitly_wait(2)
organization_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
organization_dropdown_value = organization_dropdown.get_attribute("value")
print("The value of the dropdown is :" + organization_dropdown.text)
elem_General = driver.find_element(By.XPATH, "//*/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a")
if elem_General:
    elem_General.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    organization_element = driver.find_element(By.XPATH, "//span[text()='Organization ']")
    organization_element.click()
    driver.implicitly_wait(2)
    Organization_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    Organization_dropdown_value = Organization_dropdown.get_attribute("value")
elem_Structure = driver.find_element(By.XPATH, "//*/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a")
if elem_Structure:
    elem_Structure.click()
    time.sleep(3)
else:
    pass
if organization_element:
    organization_element = driver.find_element(By.XPATH, "//span[text()='Organization ']")
    organization_element.click()
    driver.implicitly_wait(2)
    organization_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    organization_dropdown_value = organization_dropdown.get_attribute("value")
    time.sleep(3)
elem_Locations = driver.find_element(By.XPATH, "//*/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a")
if elem_Locations:
    elem_Locations.click()
    time.sleep(3)
    driver.implicitly_wait(3)

# try:
qualifications_element = driver.find_element(By.XPATH, "//span[text()='Qualifications ']")
qualifications_element.click()
time.sleep(2)
assert qualifications_element.is_displayed()
print("the is user is: " + qualifications_element.text)
driver.implicitly_wait(2)
qualifications_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
qualifications_dropdown_value = qualifications_dropdown.get_attribute("value")
print("The value of the dropdown is: " + qualifications_dropdown.text)
elem_skill = driver.find_element(By.XPATH, "//a[text()='Skills']")
if elem_skill:
    elem_skill.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    qualifications_element = driver.find_element(By.XPATH, "//span[text()='Qualifications ']")
    qualifications_element.click()
    driver.implicitly_wait(2)
    qualifications_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = qualifications_dropdown.get_attribute("value")
elem_education = driver.find_element(By.XPATH, "//a[text()='Education']")
if elem_education:
    elem_education.click()
    time.sleep(3)
else:
    pass
if qualifications_element:
    qualifications_element = driver.find_element(By.XPATH, "//span[text()='Qualifications ']")
    qualifications_element.click()
    driver.implicitly_wait(2)
    qualifications_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = qualifications_dropdown.get_attribute("value")
    time.sleep(3)

elem_Licenses = driver.find_element(By.XPATH, "//a[text()='Licenses']")
if elem_Licenses:
    elem_Licenses.click()
    time.sleep(3)
else:
    pass

qualifications_element = driver.find_element(By.XPATH, "//span[text()='Qualifications ']")
if qualifications_element:
    qualifications_element.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    qualifications_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = qualifications_dropdown.get_attribute("value")

elem_Memberships = driver.find_element(By.XPATH, "//a[text()='Memberships']")
if elem_Memberships:
    elem_Memberships.click()
    time.sleep(3)
else:
    pass

# try:
nationalities_element = driver.find_element(By.XPATH, "//a[text()='Nationalities']")
nationalities_value = nationalities_element.get_attribute("text")
print("the value  is: " + nationalities_value)
nationalities_element.click()
time.sleep(3)

# try:
corporate_banking_element = driver.find_element(By.XPATH, "//a[text()='Corporate Branding']")
corporate_banking_value = corporate_banking_element.get_attribute("text")
print("the value of is corporate_banking: " + corporate_banking_value)
corporate_banking_element.click()
time.sleep(3)
element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
ActionChains(driver).click(element_btn).perform()
time.sleep(1)
driver.implicitly_wait(3)
configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
configuration_element.click()
assert configuration_element.is_displayed()
print("The user is: " + configuration_element.text)
driver.implicitly_wait(2)

# try:
configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
configuration_dropdown_value = configuration_dropdown.get_attribute("value")
print("The value of the dropdown is: " + configuration_dropdown.text)
driver.implicitly_wait(5)
elem_email = driver.find_element(By.XPATH, "//a[text()='Email Configuration']")
if elem_email:
    elem_email.click()
    time.sleep(2)
    driver.implicitly_wait(3)
    element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
    ActionChains(driver).click(element_btn).perform()
    time.sleep(1)
    driver.implicitly_wait(3)
    configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
    configuration_element.click()
    driver.implicitly_wait(2)
    configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    configuration_dropdown_value = configuration_dropdown.get_attribute("value")
elem_emailSubscriptions = driver.find_element(By.XPATH, "//a[text()='Email Subscriptions']")
if elem_emailSubscriptions:
    elem_emailSubscriptions.click()
    time.sleep(3)
else:
    pass
element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
ActionChains(driver).click(element_btn).perform()
time.sleep(1)
driver.implicitly_wait(3)
if configuration_element:
    configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
    configuration_element.click()
    driver.implicitly_wait(2)
    configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = configuration_dropdown.get_attribute("value")
    time.sleep(3)
elem_Localization = driver.find_element(By.XPATH, "//a[text()='Localization']")
if elem_Localization:
    elem_Localization.click()
    time.sleep(3)
else:
    pass
element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
ActionChains(driver).click(element_btn).perform()
time.sleep(1)
driver.implicitly_wait(3)
if configuration_element:
    configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
    configuration_element.click()
    driver.implicitly_wait(2)
    configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = configuration_dropdown.get_attribute("value")
    time.sleep(3)
elem_Language = driver.find_element(By.XPATH, "//a[text()='Language Packages']")
if elem_Language:
    elem_Language.click()
    time.sleep(3)
else:
    pass
element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
ActionChains(driver).click(element_btn).perform()
time.sleep(1)
driver.implicitly_wait(3)
if configuration_element:
    configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
    configuration_element.click()
    driver.implicitly_wait(2)
    configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = configuration_dropdown.get_attribute("value")
    time.sleep(3)
elem_Social = driver.find_element(By.XPATH, "//a[text()='Social Media Authentication']")
if elem_Social:
    elem_Social.click()
    time.sleep(3)
else:
    pass
element_btn = driver.find_element(By.XPATH, "//span[text()='More ']")
ActionChains(driver).click(element_btn).perform()
time.sleep(1)
driver.implicitly_wait(3)
if configuration_element:
    configuration_element = driver.find_element(By.XPATH, "//a[text()='Configuration ']")
    configuration_element.click()
    driver.implicitly_wait(2)
    configuration_dropdown = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
    qualifications_dropdown_value = configuration_dropdown.get_attribute("value")
    time.sleep(3)
elem_Register = driver.find_element(By.XPATH, "//a[text()='Register OAuth Client']")
if elem_Register:
    elem_Register.click()
    time.sleep(3)
    driver.implicitly_wait(5)
else:
    pass
driver.quit()
