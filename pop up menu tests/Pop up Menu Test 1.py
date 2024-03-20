import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains


class Test_alert_popup_btn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_alert_popup_btn(self):
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

        expected_text = driver.find_element(By.XPATH,"//a[contains(.,'Popups')]")
        if expected_text.text == "Popups":
            print("The button text is written correctly")
        else:
            print("The button text is written wrong")

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Popups')]")))

        try:
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Popups')]"))
            print("Button is Clickable")
        except WDE:
            print("Button is Not Clickable")

        WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[3]/figure[1]/picture[1]/img[1]")))

        driver.minimize_window()
        try:
            EC.visibility_of_element_located((By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[3]/figure[1]/picture[1]/img[1]"))
            print("IMG is Ok")
        except WDE:
            print("IMG is Missing")

        time.sleep(0.5)
        driver.maximize_window()

        try:
            EC.visibility_of_element_located((By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[3]/figure[1]/picture[1]/img[1]"))
            print("IMG is Ok")
        except WDE:
            print("IMG is Missing")

        try:
            driver.find_element(By.LINK_TEXT,"Popups")
            print("This button contains Popups text")
        except WDE:
            print("This button is missing popups text")
        time.sleep(1)

        try:
            driver.find_element(By.XPATH, "//strong[contains(text(),'Welcome to your software automation practice websi')]")
            print("Text is present on the main page")
        except WDE:
            print("Text is NOT present on the main page")

        driver.find_element(By.LINK_TEXT, "Popups").click()
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//header/div[1]/a[1]/img[1]"))
            print("Head Button is Clickable")
        except WDE:
            print("Head Button is NOT Clickable")

        try:
            WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='alert']")))
            print("Button is Clickable")
        except:
            print("Button is NOT Clickable")

        driver.find_element(By.XPATH, "//b[contains(.,'Alert Popup')]").click()
        time.sleep(3)

        driver.switch_to.alert
        time.sleep(1)

    # Verify Text in popup box
        expected_text = "Hi there, pal!"
        acct_reg_actual_text = driver.switch_to.alert.text
        if expected_text == acct_reg_actual_text:
            print("Alert Popup text is correct", driver.switch_to.alert.text)
        else:
            print("Alert Popup text is wrong", driver.switch_to.alert.text)

        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

class Test_Conf_Popup_btn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_confirm_popup_btn(self):
        driver = self.driver
        driver.get("http://practice-automation.com/")
        driver.maximize_window()
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[contains(.,'Popups')]").click()
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//p[@id='confirmResult']"))
            print("Confirm Popup button is Clickable")
        except WDE:
            print("Confirm Popup button is NOT Clickable")
        time.sleep(1)

        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm']")))

        driver.find_element(By.XPATH, "//b[contains(.,'Confirm Popup')]").click()
        time.sleep(3)

        driver.switch_to.alert
        time.sleep(1)

        expected_text = "OK or Cancel, which will it be?"
        acct_reg_actual_text = driver.switch_to.alert.text
        if expected_text == acct_reg_actual_text:
            print("Confirm Popup text is correct", driver.switch_to.alert.text)
        else:
            print("Confirm Popup text is wrong", driver.switch_to.alert.text)
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(3)


        # Checking the text after clicking Ok!
        expected_text = "OK it is!"
        actual_text = "OK it is!"
        if expected_text == actual_text:
            print("Expected text is Present on page 'OK it is'")
        else:
            print("Expected text is NOT Preset on Page, Something went wrong")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//button[@id='confirm']"))
            print("Confirm Popup button is Clickable")
        except WDE:
            print("Confirm button is NOT Clickable")
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@id='confirm']").click()
        time.sleep(1)

        driver.switch_to.alert
        time.sleep(1)

        expected_text = "OK or Cancel, which will it be?"
        acct_reg_actual_text = driver.switch_to.alert.text
        if expected_text == acct_reg_actual_text:
            print("Confirm Popup text is correct", driver.switch_to.alert.text)
        else:
            print("Confirm Popup text is wrong", driver.switch_to.alert.text)
        time.sleep(1)
        driver.switch_to.alert.dismiss()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

        # Checking the text after clicking Cancel!
        expected_text = "Cancel it is!"
        actual_text = "Cancel it is!"
        if expected_text == actual_text:
            print("Expected text is Present on page 'Cancel it is!'")
        else:
            print("Expected text is NOT Present on Page, Something went wrong")
        time.sleep(1)

class Test_Prompt_popup_btn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_prompt_popup_btn(self):
        driver = self.driver
        driver.get("http://practice-automation.com/")
        driver.maximize_window()
        time.sleep(1)

        driver.find_element(By.XPATH, "//a[contains(.,'Popups')]").click()
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH,"//b[contains(.,'Prompt Popup')]"))
            print("Prompt Popup Button is Clickable")
        except WDE:
            print("Prompt Popup button is NOT Clickable")
        time.sleep(1)

        driver.find_element(By.XPATH, "//b[contains(.,'Prompt Popup')]").click()
        time.sleep(3)

        driver.switch_to.alert
        time.sleep(3)
        # Verify Text in popup box
        expected_text = "Hi there, what's your name?"
        acct_reg_actual_text = driver.switch_to.alert.text
        if expected_text == acct_reg_actual_text:
            print("Prompt Popup text is correct", driver.switch_to.alert.text)
        else:
            print("Prompt Popup text is wrong", driver.switch_to.alert.text)

        driver.switch_to.alert.send_keys("Sergey")
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH, "//p[contains(@id,'promptResult')]").text
            print(text)
        except WDE:
            print("Text NOT Found!")

        try:
            EC.element_to_be_clickable((By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[5]"))
            print("Tooltip btn is Clickable")
        except WDE:
            print("Tooltip btn is NOT Clickable")
            time.sleep(1)

        driver.find_element(By.XPATH, "//div[contains(@class,'tooltip_1')]").click()
        time.sleep(1)


        try:
            EC.text_to_be_present_in_element_value((By.XPATH, "//span[contains(@id,'myTooltip')]"),'Cool text')
            print("'Cool text' after clicking the btn the text is present")
        except WDE:
            print("'Cool text' after clicking the btn the text is NOT present")








    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()