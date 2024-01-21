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

driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
time.sleep(1.5)
driver.find_element(By.XPATH, "//a[contains(.,'Register')]").click()
time.sleep(1.5)
driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("Tester7@gmail.com")
time.sleep(1.5)
driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("Tester7")
time.sleep(1.5)
driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("Tester777")
time.sleep(1)
driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label["
                              "1]/span[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Edit Profile')]")))

driver.find_element(By.XPATH, "//img[contains(@alt,'Cyprus.com')]").click()
time.sleep(1)

# Verify Text on Main Page!
try:
    driver.find_element(By.XPATH, "//*[text()='Find places in Cyprus by checking out the most popular categories']")
    print("Yes! there is")
except WDE:
    print("No! There no")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
time.sleep(2)

driver.quit()





