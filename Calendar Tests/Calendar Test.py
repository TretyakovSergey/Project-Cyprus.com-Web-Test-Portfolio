import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains

class TestCalendarDate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Calendar_date(self):
        driver = self.driver
        driver.get("https://practice-automation.com/")
        driver.maximize_window()
        time.sleep(1)

        driver.delete_all_cookies()

        expected_title = "Home | Practice Automation"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print("Title page is correct", driver.title)
        else:
            print("Title page is wrong", driver.title)

        time.sleep(1)

        expected_url = "https://practice-automation.com/"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print("Page URL is correct", driver.current_url)
        else:
            print("Page URL is Wrong", driver.current_url)

        time.sleep(1)

    # Scroll the page to see the button
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)

    # Checking Clickable button

        try:
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Calendars')]"))
            print("Calendars btn is Clickable")
        except WDE:
            print("Calendars btn is  NOT Clickable")
        time.sleep(2)

        driver.find_element(By.XPATH, "//a[contains(text(),'Calendars')]").click()
        time.sleep(2)

        expected_title = "Calendars | Practice Automation"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print("Title Second page is correct", driver.title)
        else:
            print("Title Second page is wrong", driver.title)

    # Verify Text on Header Page
        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Calendars')]").text
            print(text)
        except WDE:
            print("Text on Header is NOT present")
        time.sleep(1)

    # Verify BTN on Clickable

        try:
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Home')]"))
            print("Home btn is Clickable")
        except WDE:
            print("Home btn is NOT Clickable")
        time.sleep(1)

    # Verify Text before to write Date
        try:
            text = driver.find_element(By.XPATH, "//label[contains(.,'Select or enter a date (YYYY-MM-DD)')]").text
            print(text)
        except WDE:
            print("I Don't See Text")
        time.sleep(1)

        driver.find_element(By.XPATH, "//label[contains(.,'Select or enter a date (YYYY-MM-DD)')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@data-date,'29')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[1]/form[1]/p[1]/button[1]").click()
        time.sleep(1)

    # Verify Text after sending date
        try:
            text = driver.find_element(By.XPATH, "//h4[@id='contact-form-success-header']").text
            print(text)
        except WDE:
            print("The Text did NOT appear")
        time.sleep(1)

    # Date Check
        try:
            text = driver.find_element(By.XPATH, "//div[contains(@class,'field-value')]").text
            print(text)
        except WDE:
            print("I don't see the Date")
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, "Go back").click()
        time.sleep(1)

class TestCalendarDateHandel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Calendar_date_handel(self):
        driver = self.driver
        driver.get("https://practice-automation.com/")
        driver.maximize_window()
        time.sleep(1)

        driver.delete_all_cookies()

    # Scroll the page to see the button
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[contains(text(),'Calendars')]").click()
        time.sleep(2)

        expected_title = "Calendars | Practice Automation"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print("Title Second page is correct", driver.title)
        else:
            print("Title Second page is wrong", driver.title)

        # Verify Text on Header Page
        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Calendars')]").text
            print(text)
        except WDE:
            print("Text on Header is NOT present")
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@data-format='yy-mm-dd']").send_keys("1992-03-11")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@data-format='yy-mm-dd']").submit()
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH,"//h4[@id='contact-form-success-header']").text
            print(text)
        except WDE:
            print("Your date is doesn't sent")
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH, "//div[contains(@class,'field-value')]").text
            print(text)
        except WDE:
            print("I don't see you choosing date")
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, "Go back").click()
        time.sleep(1)

class TestCalendarHandleTwo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_Calendar_date_handel(self):
        driver = self.driver
        driver.get("https://practice-automation.com/")
        driver.maximize_window()
        time.sleep(1)

        driver.delete_all_cookies()

    # Scroll the page to see the button
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[contains(text(),'Calendars')]").click()
        time.sleep(1)

        # Verify Text on Header Page
        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Calendars')]").text
            print(text)
        except WDE:
            print("Text on Header is NOT present")
        time.sleep(1)

        driver.find_element(By.XPATH, "//label[@class='grunion-field-label date']").click()
        time.sleep(1)

    # Double click
        option_next = driver.find_element(By.XPATH,"//a[contains(.,'Next')]")
        actionChains = ActionChains(driver)
        actionChains.double_click(option_next).perform()
        time.sleep(1.5)

        driver.find_element(By.XPATH, "//a[contains(.,'Next')]").click()
        time.sleep(1.5)

        option_previous = driver.find_element(By.XPATH, "//a[contains(.,'Previous')]")
        actionChains = ActionChains(driver)
        actionChains.double_click(option_previous).perform()
        time.sleep(1.5)

        driver.find_element(By.XPATH, "//a[contains(.,'Previous')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@data-date,'24')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[1]/form[1]/p[1]/button[1]").click()
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH, "//h4[@id='contact-form-success-header']").text
            print(text)
        except WDE:
            print("You are didn't choose date")
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH, "//div[@class='field-value']").text
            print(text)
        except WDE:
            print("I don't see the selected date")
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, "Go back").click()



    def tearDown(self):
        self.driver.quit()

        if __name__ == "__main__":
            unittest.main()