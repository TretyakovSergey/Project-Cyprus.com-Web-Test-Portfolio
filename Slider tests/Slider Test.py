import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains

class TestSlider(unittest.TestCase):
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

        driver.find_element(By.XPATH, "//a[contains(.,'Sliders')]").click()
        time.sleep(1)

        try:
            text = driver.find_element(By.XPATH, "//h1[contains(.,'Slider')]").text
            print(text)
        except WDE:
            print("I don't see the description")
        time.sleep(1)

        expected_text = driver.find_element(By.XPATH, "//body/div[@id='box']/div[@id='main']/div[1]/div[1]/main[1]/div[1]/article[1]/div[1]/div[1]/div[1]/p[1]")
        if expected_text.text == "This is a range slider. You can adjust it by using drag-and-drop operation or by clicking a given area of the slider. As you move the slider, the current value will be updated.":
            print("Expected text is correct")
        else:
            print("Expected text is NOT correct")
        time.sleep(1)

    # Moving Slider
        move = ActionChains(driver)
        thumb = driver.find_element(By.XPATH, "//input[@id='slideMe']")
        move.click_and_hold(thumb).move_by_offset(13,0).release().perform()
        time.sleep(1)
        move.click_and_hold(thumb).move_by_offset(-100,0).release().perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()