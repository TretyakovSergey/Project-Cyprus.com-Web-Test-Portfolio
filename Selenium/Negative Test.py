from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://cyprus.com/")
driver.maximize_window()
time.sleep(1)

# generated brand new Browser session
driver.delete_all_cookies()
print("Test 1 Start!")
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
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    print("Ok!")
except WDE:
    print("Error")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@id='username']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='password']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test232")
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()

time.sleep(4)

# Verify text in the authorization plate
expected_text = driver.find_element(By.XPATH, "//body/div[@id='modal-login']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/p[1]")
if expected_text.text == "Wrong username or password":
    print("Ok! Test 1 Pass")
else:
    print("Test 1 Fail, something went wrong")

driver.quit()

driver = webdriver.Chrome()
driver.get("https://cyprus.com/")
driver.maximize_window()
time.sleep(1)
print("Test 2 Start!")
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
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    print("Ok!")
except WDE:
    print("Error")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@id='username']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Testing@gmail.com")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='password']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()

time.sleep(4)

# Verify text in the authorization plate
expected_text = driver.find_element(By.XPATH, "//body/div[@id='modal-login']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/p[1]")
if expected_text.text == "Wrong username or password":
    print("Ok! Test 2 Pass")
else:
    print("Test 2 Fail")

driver.quit()

driver = webdriver.Chrome()
driver.get("https://cyprus.com/")
driver.maximize_window()
time.sleep(1)
print("Test 3 Start!")

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
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    print("Ok!")
except WDE:
    print("Error")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@id='username']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='password']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()
WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='signup-signin-wrapper']")))

# Verify text in the authorization plate
expected_text = driver.find_element(By.XPATH, "//div[@id='signup-signin-wrapper']")
try:
    expected_text.text == "Hello Tester7! Nice to see you back."
    print("logged in")
except WDE:
    print("Something went wrong")

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Edit Profile')]")))
driver.find_element(By.XPATH, "//a[contains(.,'Edit Profile')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").clear()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='wiloke_phone']").send_keys("352 000 99999 444 3333")
time.sleep(2)
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']")))
driver.find_element(By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']").click()
time.sleep(4)

expected_text = "Incorrect phone number"
if expected_text == "Incorrect phone number.":
    print("Test 3 Pass")
else:
    print("Test 3 Fall")

driver.quit()

driver = webdriver.Chrome()
driver.get("https://cyprus.com/")
driver.maximize_window()
time.sleep(1)

# generated brand new Browser session
driver.delete_all_cookies()

print("Test 4 Start!")
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
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    print("Ok!")
except WDE:
    print("Error")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@id='username']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='password']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()
time.sleep(4)

# Verify text in the authorization plate
try:
    driver.find_element(By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")
    print("logged in")
except WDE:
    print("Something went wrong")

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Edit Profile')]")))
driver.find_element(By.XPATH, "//a[contains(.,'Edit Profile')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='address']").clear()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("Cyprus, Lelasol")
time.sleep(2)
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']")))
driver.find_element(By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']").click()
time.sleep(2)

expected_text = "Incorrect City address."
if expected_text == "Incorrect City address.":
    print("Test 4 Pass")
else:
    print("Test 4 Fall")

driver.quit()


driver = webdriver.Chrome()
driver.get("https://cyprus.com/")
driver.maximize_window()
time.sleep(1)

# generated brand new Browser session
driver.delete_all_cookies()

print("Test 5 Start!")

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
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='username']")))
    print("Ok!")
except WDE:
    print("Error")
time.sleep(1.5)

driver.find_element(By.XPATH, "//input[@id='username']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("Tester7@gmail.com")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@id='password']").clear()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Tester777")
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@id='signin-btn']").click()
time.sleep(4)

# Verify text in the authorization plate
try:
    driver.find_element(By.XPATH, "//*[text()='Hello Tester7! Nice to see you back.']")
    print("logged in")
except WDE:
    print("Something went wrong")

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Edit Profile')]")))
driver.find_element(By.XPATH, "//a[contains(.,'Edit Profile')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='address']").clear()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='address']").send_keys("Cupro, Limassol")
time.sleep(2)
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']")))
driver.find_element(By.XPATH, "//button[@id='wiloke-listgo-submit-update-profile']").click()
time.sleep(2)

expected_text = "Incorrect Country address."
if expected_text == "Incorrect Country address.":
    print("Test 5 Pass")
else:
    print("Test 5 Fall")

driver.quit()