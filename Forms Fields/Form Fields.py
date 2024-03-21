import unittest
import time
import fake
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from faker import Faker



fake = Faker()
class TestFormField(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_field_form(self):
        driver = self.driver
        driver.get("https://practice-automation.com/")
        time.sleep(1)

        driver.delete_all_cookies()

    # Verify Page Title
        expected_title = "Home | Practice Automation"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print("Title page is correct", driver.title)
        else:
            print("Title page is wrong", driver.title)

        time.sleep(1)

    # Verify Page URL
        expected_url = "https://practice-automation.com/"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print("Page URL is correct", driver.current_url)
        else:
            print("Page URL is Wrong", driver.current_url)

        time.sleep(1)

    # Verify Button on Clickable
        try:
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Form Fields')]"))
            print("Form Fields BTN is Clickable")
        except WDE:
            print("Form Fields BTN is NOT Clickable")
        time.sleep(1)

    # Verify Text on the button
        text = driver.find_element(By.XPATH, "//*[contains(text(), 'Form Fields')]").text
        expected_text = driver.find_element(By.XPATH, "//*[contains(text(), 'Form Fields')]")
        if expected_text.text == "Form Fields":
            print("Text on the btn is Correct", text)
        else:
            print("Text on the btn is Wrong")
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[contains(.,'Form Fields')]").click()

        WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//span[@aria-current='page']")))

        driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Jhon")
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='drink1']").click()
        time.sleep(1)

    # Scroll the page to see the button
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@value='Yellow']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//select[@id='siblings']").click()
        time.sleep(1)
        select = Select(driver.find_element(By.XPATH, "//select[@id='siblings']"))
        time.sleep(2)
        select.select_by_visible_text("Maybe")
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(fake.email())
        time.sleep(1)
        driver.find_element(By.XPATH, "//textarea[@id='message']").send_keys("Hello World!")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//button[@id='submit-btn']"))
            print("Submit btn is Clickable")
        except WDE:
            print("Submit btn is NOT Clickable")
        time.sleep(1)

        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@id='submit-btn']").click()
        time.sleep(1)

        driver.switch_to.alert
        time.sleep(1)

        expected_text = "Message received!"
        acct_reg_actual_text = driver.switch_to.alert.text
        if expected_text == acct_reg_actual_text:
            print("Popup text is Correct", driver.switch_to.alert.text)
        else:
            print("Popup text is wrong", driver.switch_to.alert.text)
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)


    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

