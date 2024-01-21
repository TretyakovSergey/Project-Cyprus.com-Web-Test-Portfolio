from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#--------------------------------- Test for Shopping TAB ---------------------------------------------

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
time.sleep(1)

try:
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cyprus.com']")))
    print("Ok!")
except WDE:
    print("error")
driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(1)

try:
    driver.find_element(By.XPATH, "//*[text()='Find places in Cyprus by checking out the most popular categories']")
    print("This Text is Present on this page")
except WDE:
    print("This Text is Missing on this page")
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Shopping']")))
driver.find_element(By.XPATH, "//img[@alt='Shopping']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//img[@alt='Shopping']").click()

# Verify description when clicking on the Shopping link
try:
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='header-page__title'][contains(.,'Shopping')]")))
    print("The Inscription in the Header is VISIBLE!")
except WDE:
    print("The Inscription in the Header is NOT VISIBLE")

driver.find_element(By.XPATH, "//a[@href='/listing-location/limassol/']").click()

# Verify Page Title

expected_title = "Limassol Archives - Cyprus.com"
acct_reg_actual_title = driver.title
if expected_title == acct_reg_actual_title:
    print("Title is Right!")
else:
    print("Title is Wrong")
time.sleep(1.5)
driver.find_element(By.XPATH, "//a[contains(.,'CyCarHire')]").click()
WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Description')])[1]")))
try:
    driver.find_element(By.XPATH, "//*[text()='Opening Hours'")
    print("Opening hours are present")
except WDE:
    print("Opening hours are NOT available")

# Verify buttons to be clickable
try:
    EC.element_to_be_clickable((By.XPATH, "(//a[@href='#tab-review'])[1]"))
    print("Reviews button is Clickable")
except WDE:
    print("Reviews buttons is NOt Clickable")

try:
    EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Location & Map')])[1]"))
    print("Location & Map button is Clickable")
except WDE:
    print("Location & Map button is NOT Clickable")

try:
    EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Photo Gallery')])[1]"))
    print("Photo Gallery button is Clickable")
except WDE:
    print("Photo Gallery button is NOT Clickable")

driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()

# Verify DropDown menu
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Listings")))
driver.find_element(By.LINK_TEXT, "Listings").click()

listings = driver.find_element(By.LINK_TEXT, "Listings")
action = ActionChains(driver)
action.move_to_element(listings)
time.sleep(2)
try:
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'IT & Media')])[2]")))
    print("Ok!")
except WDE:
    print("Not")

driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
print("Test Shopping TAB Complete!")

driver.quit()

#-------------------------------- Test for Restaurant TAB --------------------------------------------

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
time.sleep(1)

try:
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cyprus.com']")))
    print("Ok!")
except WDE:
    print("error")
driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(1)

WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Restaurants')]")))
try:
    EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Restaurants')]"))
    print("Rts button is Clickable")
except WDE:
    print("Rts button is NOT Clickable")
driver.find_element(By.XPATH, "//span[contains(.,'Restaurants')]").click()

try:
    EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cyprus.com']"))
    driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
    print("Button is Clickable")
except WDE:
    print("Button is NOT Clickable")

driver.find_element(By.XPATH, "//span[contains(.,'Restaurants')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[contains(.,'Highest Rated')]").click()
time.sleep(2)

# Verify text that should be present in the Restaurant link
try:
    EC.text_to_be_present_in_element_value(By.LINK_TEXT, "//*[@text()='Skinny Fox']")
    print("This link contains the correct text")
except WDE:
    print("This link contains incorrect text")

driver.find_element(By.XPATH, "//a[contains(.,'Skinny Fox')]").click()
time.sleep(1.5)

try:
    EC.visibility_of_element_located((By.XPATH, "(//i[@class='fa fa-star'])[5]"))
    print("The Rating corresponds to that indicated on the link")
except WDE:
    print("The Rating does not correspond to the one indicated in the link")

time.sleep(1.5)

try:
    EC.visibility_of_element_located((By.XPATH, "//*[@text()='Skinny Fox is a contemporary European restaurant featuring a diverse selection of gourmet dishes with international influences.']"))
    print("Description is present")
except WDE:
    print("No description")

time.sleep(1.5)

try:
    EC.visibility_of_element_located((By.XPATH, "//div[@class='wiloke_price-range']"))
    print("Description of the average check is present")
except WDE:
    print("There is no description of the average check")

time.sleep(1)

driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Destinations").click()

destinations = driver.find_element(By.LINK_TEXT, "Destinations")
action = ActionChains(driver)
action.move_to_element(destinations)

time.sleep(1.5)

try:
    EC.visibility_of_element_located((By.XPATH, "(//div[contains(@class,'thumbnail')])[3]"))
    print("Dropdown menu is visible")
except WDE:
    print("Dropdown menu is not visible")

driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
time.sleep(1.5)
print("Test Restaurant TAB Complete")
driver.quit()

#------------------------------------------ Test for NightLife TAB -------------------------------------------

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
time.sleep(1)

driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(1.5)

driver.find_element(By.XPATH, "//img[@alt='Nightlife']").click()
time.sleep(1.5)

# Verify functionality of the slider (Radius km)
move = ActionChains(driver)
thumb = driver.find_element(By.XPATH, "//body/div[@id='wrap-page']/section[@id='main']/div[2]/div[1]/div[1]/div["
                                      "1]/div[1]/div[1]/form[1]/div[6]/div[2]/span[1]")
time.sleep(1)
driver.find_element(By.XPATH, '//body[1]/div[2]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div['
                              '6]/div[2]')

move.click_and_hold(thumb).move_by_offset(-300, 0).release().perform()
time.sleep(3)

# Verify IMG in Header
if driver.find_element(By.XPATH, "//div[@class='header-page__inner']"):
    print("Hidde")
else:
    print("image displayed")

# Verify Title in the Header Img

if driver.find_element(By.XPATH, "//h1[contains(.,'Nightlife')]"):
    print("Τitle in header is not visible")
else:
    print("Title in header is visible")

time.sleep(1.5)

driver.find_element(By.XPATH, "//img[@alt='Cyprus.com']").click()
time.sleep(1.5)
WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="user__avatar"]')))
driver.find_element(By.XPATH, '//*[@class="user__avatar"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(.,'Logout')]").click()
time.sleep(1.5)
print("Test NightLife TAB Complete")

driver.quit()
