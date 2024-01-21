from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

website_url = "https://cyprus.com/"
driver = webdriver.Chrome()
driver.get(website_url)
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# generated brand new Browser session
driver.delete_all_cookies()

# Check page Title
expected_title = "Cyprus.com - Make the Most of Cyprus Using our Comprehensive Portal"
acct_reg_actual_title = driver.title
if expected_title == acct_reg_actual_title:
    print('"Cyprus" page Title is correct:', driver.title)
else:
    print('"Cyprus" page Title is wrong:', driver.title)


# Check page URL
expected_url = "https://cyprus.com/"
actual_url = driver.current_url
if expected_url == actual_url:
    print('"Cyprus.com" page URL is correct:', driver.current_url)
else:
    print('"Cyprus.com" page URL is wrong:', driver.current_url)


mainPageTitle = "Cyprus.com - Make the Most of Cyprus Using our Comprehensive Portal"
assert driver.title == mainPageTitle


driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/*[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")))
try:
    driver.find_element(By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")
    print("Welcome!")
except WDE:
    print("Something went wrong!")

time.sleep(1.5)

driver.find_element(By.XPATH, "//a[@href='https://cyprus.com/info/?mode=edit-profile']").click()

# Verify Account page Title
expected_title = "My Account - Cyprus.com"
acct_reg_actual_title = driver.title
if expected_title == acct_reg_actual_title:
    print('"My Account" page Title is correct:', driver.title)
else:
    print('"My Account" page Title is wrong:', driver.title)

try:
    driver.find_element(By.XPATH, "//a[contains(text(),'+ Add Listing')]")
    print("Ok!")
except WDE:
    print("Error!")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='first_name']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("John")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='last_name']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Week")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='address']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("Cyprus, Limassol")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").send_keys("357 96 000 000")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='description']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Test Portfolio")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Logout')]")))
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
try:
    WebDriverWait(driver,5).until(EC.url_to_be("https://cyprus.com/"))
    print("Test Complete!")
except WDE:
    print("Test Dosen't complet")

driver.quit()

#-------------------------- Same Test With Different personal information -------------------------------------------------


website_url = "https://cyprus.com/"
driver = webdriver.Chrome()
driver.get(website_url)
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.maximize_window()
time.sleep(1)

# generated brand new Browser session
driver.delete_all_cookies()

# Check page Title
expected_title = "Cyprus.com - Make the Most of Cyprus Using our Comprehensive Portal"
acct_reg_actual_title = driver.title
if expected_title == acct_reg_actual_title:
    print('"Cyprus" page Title is correct:', driver.title)
else:
    print('"Cyprus" page Title is wrong:', driver.title)


# Check page URL
expected_url = "https://cyprus.com/"
actual_url = driver.current_url
if expected_url == actual_url:
    print('"Cyprus.com" page URL is correct:', driver.current_url)
else:
    print('"Cyprus.com" page URL is wrong:', driver.current_url)


mainPageTitle = "Cyprus.com - Make the Most of Cyprus Using our Comprehensive Portal"
assert driver.title == mainPageTitle


driver.find_element(By.XPATH, "//header/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/*[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")))
try:
    driver.find_element(By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")
    print("Welcome!")
except WDE:
    print("Something went wrong!")

time.sleep(1.5)

driver.find_element(By.XPATH, "//a[@href='https://cyprus.com/info/?mode=edit-profile']").click()

# Verify Account page Title
expected_title = "My Account - Cyprus.com"
acct_reg_actual_title = driver.title
if expected_title == acct_reg_actual_title:
    print('"My Account" page Title is correct:', driver.title)
else:
    print('"My Account" page Title is wrong:', driver.title)

try:
    driver.find_element(By.XPATH, "//a[contains(text(),'+ Add Listing')]")
    print("Ok!")
except WDE:
    print("Error!")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='first_name']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Quality")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='last_name']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Assurance")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='address']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("Cyprus, Larnaca")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").send_keys("357 96 333 333")
time.sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='description']").clear()
time.sleep(0.5)
driver.find_element(By.XPATH, "//textarea[@id='description']").send_keys("Hello World! this is my small selenium test for Git-Hub, Test Portfolio!")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']").click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Logout')]")))
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
try:
    WebDriverWait(driver,5).until(EC.url_to_be("https://cyprus.com/"))
    print("Test Complete!")
except WDE:
    print("Test Dosen't complet")

driver.quit()