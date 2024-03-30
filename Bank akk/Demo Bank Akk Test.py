import select
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.action_chains import ActionChains

username = "demo"
password = "demo"
smscode = "0000"
class Test_BSBP_Bank_Akk(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_bank_bsbp_authorization(Authorization):
        driver = Authorization.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        driver.maximize_window()
        time.sleep(1)

        driver.delete_all_cookies()


        try:
            WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//img[@id='logo']")))
            print("Everything OK! Let's Start!")
        except WDE:
            print("Something Went Wrong")

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)

        expected_url = "https://idemo.bspb.ru/welcome"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print("URL is Correct", driver.current_url)
        else:
            print("URL is Wrong", driver.current_url)
        time.sleep(1)

        expected_text = "Internet-bank"
        actual_text = driver.find_element(By.XPATH, "//div[@class='environment print-hidden']").text
        if expected_text == actual_text:
            print("Text in Header is Correct", actual_text)
        else:
            print("Text in Header is Wrong", actual_text)

    def test_clickable_btn_BSPB_User_Akk(Clickable_btn):
        driver = Clickable_btn.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb"
                   ".ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch"
                   "&force_new_session=true")
        driver.maximize_window()
        time.sleep(1)

        driver.delete_all_cookies()

        username = "demo"
        password = "demo"
        smscode = "0000"

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)
        driver.maximize_window()
        time.sleep(1)

        expected_url = "https://idemo.bspb.ru/welcome"
        actual_url = driver.current_url
        if expected_url == actual_url:
            print("URL is Correct", driver.current_url)
        else:
            print("URL is Wrong", driver.current_url)
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-email']"))
            driver.find_element(By.XPATH, "//span[@class='icon-email']").click()
            time.sleep(1)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            print("Email btn is Clickable")
        except WDE:
            print("Email btn is NOT Clickable")
        time.sleep(1)


        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-special-offers2']"))
            driver.find_element(By.XPATH, "//span[@class='icon-special-offers2']").click()
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            print("Special Offers btn is Clickable")
        except WDE:
            print("Special Offers btn is NOT Clickable")
        time.sleep(1)


        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-phone']"))
            driver.find_element(By.XPATH, "//span[@class='icon-phone']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "(//button[@class='close'])[2]").click()
            print("Phone btn is Clickable")
        except WDE:
            print("Phone btn is NOT Clickable")
        time.sleep(1)



        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-cog']"))
            driver.find_element(By.XPATH, "//span[@class='icon-cog']").click()
            time.sleep(1)
            driver.execute_script("window.history.go(-1)")
            time.sleep(1)
            print("Settings btn is Clickable")
        except WDE:
            print("Settings btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Main')]"))
            driver.find_element(By.XPATH, "//span[contains(.,'Main')]").click()
            #driver.execute_script("window.history.go(-1)")
            print("Main btn is Clickable")
        except WDE:
            print("Main btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Accounts')]"))
            driver.find_element(By.XPATH, "//span[contains(.,'Accounts')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Acc btn is Clickable")
        except WDE:
            print("Acc btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Payments')]"))
            driver.find_element(By.XPATH, "//span[contains(.,'Payments')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Payment btn is clickanble")
        except WDE:
            print("Paymen btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Cards')]"))
            driver.find_element(By.XPATH, "//span[contains(.,'Cards')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Cards btn is Clickable")
        except WDE:
            print("Cards btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//a[@id='deposits-index']"))
            driver.find_element(By.XPATH, "//a[@id='deposits-index']").click()
            driver.execute_script("window.history.go(-1)")
            print("Deposit btn is Clickable")
        except WDE:
            print("Deposit btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Loans')]"))
            driver.find_element(By.XPATH, "//span[contains(text(),'Loans')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Loans btn is Clickable")
        except WDE:
            print("Loans btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Currency')]"))
            driver.find_element(By.XPATH, "//span[contains(.,'Currency')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Currency btn is Clickable")
        except WDE:
            print("Currency btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Insurance')]"))
            driver.find_element(By.XPATH, "//span[contains(text(),'Insurance')]").click()
            driver.execute_script("window.history.go(-1)")
            print("Insurance btn is Clickable")
        except WDE:
            print("Insurance btn is NOT Clickable")
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-door']"))
            driver.find_element(By.XPATH, "//span[@class='icon-door']").click()
            time.sleep(1)
      #     driver.execute_script("window.history.go(-1)")
            print("Exit btn is Clickable")
        except WDE:
            print("Exit btn is NOT Clickable")
        time.sleep(1)

    def test_send_message(message_link):
        driver = message_link.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb"
                   ".ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch"
                   "&force_new_session=true")
        driver.maximize_window()
        time.sleep(1)
        driver.delete_all_cookies()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)

        try:
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-email']"))
            print("Message btn is Clickable!")
        except WDE:
            print("Message btn is NOT Clickable")
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@class='icon-email']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='new-message-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[contains(@name,'message.topicName')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[contains(text(),'Other')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//textarea[contains(@name,'message.text')]").send_keys("HI, I lost my credit card can you block it Please! Thank you")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@id,'send-button')]").click()
        time.sleep(1)
        try:
            text = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[2]/div[2]/span[1]/div[1]").text
            print(text)
        except WDE:
            print(text)

    def test_order_card(order_card):
        driver = order_card.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

        driver.maximize_window()
        time.sleep(1)
        driver.delete_all_cookies()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//span[contains(.,'Cards')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body/div[@id='outer-wrapper']/div[@id='inner-wrapper']/div[@id='body']/div[@id='contentbar']/div[@id='cards-vertical-container']/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[12]").click()
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,0900)')
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@data-ref='50']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//select[@id='card-branch']").click()
        time.sleep(1)

        text = "Комендантский: 197371, г.Санкт-Петербург, Комендантский пр., дом 17, корп.1, лит.А, пом.23-Н"
        actual_text = driver.find_element(By.XPATH, "//body/div[@id='default-dialog']/div[1]/div[2]/form[1]/div[3]/div[2]/div[1]/select[1]/option[10]").text

        if text == actual_text:
            print("Text is Correct", actual_text)
        else:
            print("Text is Wrong", actual_text)

        driver.find_element(By.XPATH, "//body/div[@id='default-dialog']/div[1]/div[2]/form[1]/div[3]/div[2]/div[1]/select[1]/option[10]").click()
        time.sleep(1)

        driver.execute_script('window.scrollBy(0,0700)')
        time.sleep(1)

        driver.find_element(By.XPATH, "//button[@id='forward']").click()
        time.sleep(1)
        try:
            attention_text = driver.find_element(By.XPATH, "//li[contains(.,'We will also open a new account for you')]").text
            print("Text is Correct", attention_text)
        except WDE:
            print("I don't see text")
        time.sleep(1)

        try:
            delivery_date = driver.find_element(By.XPATH, "//body/div[@id='default-dialog']/div[1]/div[2]/form[1]/div[3]/div[5]/div[1]").text
            print("Your Order Will Be delivered", delivery_date)
        except WDE:
            print("Wrong delivery date")
        time.sleep(1.5)

        iframe = driver.find_element(By.XPATH, "//iframe[@id='confirmation-frame']")
        driver.switch_to.frame(iframe)
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='otp-input']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='otp-input']").send_keys("0000")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='confirm']").click()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)

        try:
            accept_text = driver.find_element(By.XPATH, "//div[contains(text(),'Card was successfully ordered!')]").text
            print(accept_text)
        except WDE:
            print("An error occurred, the card was not ordered")
        time.sleep(1)

    def test_loans(loans):
        driver = loans.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        driver.maximize_window()
        time.sleep(1)
        driver.delete_all_cookies()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//span[contains(.,'Loans')]").click()
        time.sleep(1)
        try:
            text_loans = driver.find_element(By.XPATH, "//h1[contains(.,'Loans')]").text
            print(text_loans)
        except WDE:
            print("Text is NOT present")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='loan-application-btn']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='personal-loan-apply']").click()
        time.sleep(1)
        try:
            apl_text = driver.find_element(By.XPATH, "//div[contains(text(),'Applying for loan is not possible right now')]").text
            print(apl_text)
        except WDE:
            print("I don't See Text")
        time.sleep(1)
        driver.execute_script('window.scrollBy(0,0900)')
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[2]/div[5]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/span[1]").click()
        time.sleep(1)
        try:
            crd_dtls = driver.find_element(By.XPATH, "//h1[contains(text(),'Credit limit details')]").text
            print(crd_dtls)
        except WDE:
            print("I Don't See Credit Details")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='makeMinPayment']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[contains(@name,'payment.time')]").click()
        driver.find_element(By.XPATH, "//td[@class='day active'][contains(.,'30')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='amount']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='amount']").send_keys("1 000")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Save as draft')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(.,'Loans')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[@id='loan-application-btn']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='credit-card-loan-apply']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[2]/div[5]/table[1]/tbody[1]/tr[1]/td[1]/a[1]/span[1]").click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Credit limit details')]")))
        driver.find_element(By.XPATH, "//a[contains(text(),'Pay off all debt')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='loanPartialRepaymentAmount']").send_keys("50 000")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@value='reducePayments']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[contains(.,'I agree with terms of new repayment schedule')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='send-button']").click()
        time.sleep(1)
        iframe = driver.find_element(By.XPATH, "//iframe[@id='confirmation-frame']")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, "//button[@id='confirm']").click()
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(1)
        try:
            msg = driver.find_element(By.XPATH, "//div[contains(@class,'alert alert-success')]").text
            print(msg)
        except WDE:
            print("You don't have message")
        time.sleep(1)



    def test_deposit_link(deposit_link):
        driver = deposit_link.driver
        driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
        time.sleep(1)
        driver.maximize_window()
        driver.delete_all_cookies()
        time.sleep(1)

        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").clear()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[@id='login-button']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='otp-code']").send_keys(smscode)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@id='login-otp-button']").click()
        time.sleep(1)

        driver.find_element(By.XPATH, "//span[contains(.,'Deposits')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[contains(@id,'btn-show-rates')]").click()
        time.sleep(1)
        try:
            vrf_text = driver.find_element(By.XPATH, "//h1[contains(.,'New deposit')]").text
            print(vrf_text)
        except WDE:
            print("Something went wrong!")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@value='EUR']").click()
        driver.find_element(By.XPATH, "//input[@value='181']")
        time.sleep(2)
        driver.execute_script('window.scrollBy(0,0600)')
        time.sleep(1)
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/div[2]/form[1]/table[1]/tbody[1]/tr[3]/td[7]/a[1]").click()
        time.sleep(2)
        try:
            chg_text = driver.find_element(By.XPATH, "//h1[contains(.,'Deposits New deposit')]").text
            print(chg_text)
        except WDE:
            print("Text is wrong")
        time.sleep(1)
        try:
            tpe_text = driver.find_element(By.XPATH, "//div[@id='deposit-type']").text
            print(tpe_text)
        except WDE:
            print("Type Line is Empty")
        time.sleep(1)
        try:
            date_text = driver.find_element(By.XPATH, "//label[contains(text(),'End date')]").text
            print(date_text)
        except WDE:
            print("I don't see this line")
        time.sleep(1)
        driver.find_element(By.XPATH, "//i[@class='icon-calendar']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//td[@class='day'][contains(.,'25')]").click()
        time.sleep(1)
        try:
            amount_text = driver.find_element(By.XPATH, "//label[contains(text(),'Amount')]").text
            print(amount_text)
        except WDE:
            print("Amount text is NOT Visible")
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[contains(@id,'amount')]").send_keys("500")
        time.sleep(1)
        try:
            interest_percent = driver.find_element(By.XPATH, "//div[@id='deposit-rate']").text
            print(interest_percent)
        except WDE:
            print("Percent is NOT Visible")
        time.sleep(1)
        try:
            Estmd_interst = driver.find_element(By.XPATH, "//body/div[@id='outer-wrapper']/div[@id='inner-wrapper']/div[@id='body']/div[@id='contentbar']/div[3]/form[1]/div[6]").text
            print(Estmd_interst)
        except WDE:
            print("Estimated text is NOT Visible")
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@id='submit-button']").click()
        time.sleep(1)

















