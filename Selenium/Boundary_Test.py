import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE


class TestChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        driver.maximize_window()
        time.sleep(1)
        print("Boundary test Start!")



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
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//ins[contains(.,'Register')]")))
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='popup-email']")))
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("b#@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("#b")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("#b")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(3)

        expected_text = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/p[1]")
        if expected_text.text == "Sorry, the email b#@gmail.com is already existed! Please try another one.":
            print("User can't register")
        else:
            print("Opps User Registred!")


        driver.find_element(By.XPATH, "//div[@class='wil-modal__close'][contains(.,'Close')]").click()
        time.sleep(1)

#    def setUp(self):
#       self.driver = webdriver.Chrome()
#        self.driver.maximize_window()

    def test_chrome2(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 2 Start!")

# generated brand new Browser session
        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("a2%!@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("a2@!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("a1@#")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(4)

        expected_text = driver.find_element(By.XPATH, "/html[1]/body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/p[1]")
        if expected_text.text == "Sorry, the email a2%!@gmail.com is already existed! Please try another one.":
            print("Test 2 Pass")
        else:
            print("Test 2 Fall")


        driver.find_element(By.XPATH, "//div[@class='wil-modal__close'][contains(.,'Close')]").click()
        time.sleep(2)
    def test_chrome3(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 3 Start!")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        try:
            EC.visibility_of_element_located((By.CLASS_NAME, "Already have an account?"))
            print("Text Present")
        except WDE:
            print("No Text")
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("abc,./@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("fap&!$")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("zxc`/?")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(2)

        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        expected_url = "https://cyprus.com/"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print('Test Pass!', driver.current_url)
        else:
            print('Test Fall', driver.current_url)

    def test_chrome4(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 4 Start!")

        driver.delete_all_cookies()

        expected_url = "https://cyprus.com/"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print('"Cyprus.com" page URL is correct:', driver.current_url)
        else:
            print('"Cyprus.com" page URL is wrong:', driver.current_url)
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("qwer;'/.@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("qwer()-=")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("qwer=!-#")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(1.5)

        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome5(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        driver.maximize_window()
        time.sleep(0.5)
        driver.maximize_window()
        time.sleep(0.5)
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 5 Start!")
        driver.delete_all_cookies()

        expected_url = "https://cyprus.com/"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print('"Cyprus.com" page URL is correct:', driver.current_url)
        else:
            print('"Cyprus.com" page URL is wrong:', driver.current_url)
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("a@r$a.f/s>@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("dfghv.,/'[")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("fghjv$%^&*")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,"//button[@id='signup-btn']").click()
        time.sleep(0.5)
    # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)



    def test_chrome6(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(0.5)
        driver.maximize_window()
        time.sleep(0.5)
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 6 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("ppflvk;'.,@#@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("cvbtyf.,<>?!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("123456<>()$")
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH,"//button[@id='signup-btn']").click()
        time.sleep(0.5)
    # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome7(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        print("Boundary Test 7 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("1234dfg,./#$@*@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("9876lkj*()#@!$")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("123fcvg?><:}{!")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

    # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome8(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        print("Boundary Test 8 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("poiuytfr+_-)*(#$@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("=-098765fdcvhgjk")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("=-09876!")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

        # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)


    def test_chrome9(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 9 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys(",./?';[]{fcgvbhtrf@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys(".?/.,;';:cvbfjdurt")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("\.|'/.,*(qwertyuio")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

        # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome10(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)
        print("Boundary Test 10 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys(",/.,<>?;'.:[]}{+-sssssaasdfhgvcnb@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys(",.<>/?;':,[]}{=-poiuytrewqasdfgh")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("1234567890987654{}[]-=_+)(!@#$%^")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

        # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome11(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(0.5)
        print("Boundary Test 11 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("asdffgvbcfglort!@#$%^&*()_+'{}@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("dfgcvbnhbvcfvbg?><<>:'{}][+$@#$")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("010203040506070)(*$%#@!%^&%$#@")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

        # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)

    def test_chrome12(self):
        driver = self.driver
        driver.get("https://cyprus.com/")
        time.sleep(1)
        driver.maximize_window()
        time.sleep(0.5)
        print("Boundary Test 12 Start")

        driver.delete_all_cookies()

        driver.find_element(By.XPATH, '//*[@class="user__icon"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//ins[contains(.,'Register')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-email']").send_keys("aaaaaaaaaaaaaa<>!@#$%^&*()_+@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-username']").send_keys("ddddddddddddd<>,./?|\{}::;[")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='popup-password']").send_keys("11111111111111<!>,./\@#$!)(%")
        time.sleep(1)
        driver.find_element(By.XPATH,"//body[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/label[1]/span[1] ").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='signup-btn']").click()
        time.sleep(0.5)

        # Checking the title so that it does not change, if the title changes, the test fails.
        expected_title = "My Account - Cyprus.com"
        acct_reg_actual_title = driver.title
        if expected_title == acct_reg_actual_title:
            print('"Your Test Fall', driver.title)
        else:
            print('"Your Test Pass', driver.title)

        driver.find_element(By.XPATH, "//div[@class='wil-modal__close']").click()
        time.sleep(1)



    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()