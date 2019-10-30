#pip install selenium
#別途chromeとchromeのwebドライバをインストールしパスを通す
#self.driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep 

#text=('20191016', '11:00', '12:00', '13:00', '16:00', '0:02')
text=('20191016', '11:00', '12:00', '12:00', '16:00', '0:02')
# text[0],text[1]
date="10月16日(水)"

class Ozo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ozo(self):
        driver = self.driver
        driver.get("https://avantcorp.ozo-cloud.jp/ozo3/default.cfm?version=diva")
        driver.find_element_by_id("login_user").click()
        driver.find_element_by_id("login_user").clear()
        driver.find_element_by_id("login_user").send_keys("kazuki.furukori@avantcorp.com")
        driver.find_element_by_id("login_pwd").clear()
        driver.find_element_by_id("login_pwd").send_keys("Jv2&3bP%dJ")
        driver.find_element_by_id("login_form").submit()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='旧ワークフロー'])[1]/following::p[7]").click()
        driver.find_element_by_link_text(date).click()
        driver.find_element_by_id("db_SYUKKIN_JIKOKU1").click()
        driver.find_element_by_id("db_SYUKKIN_JIKOKU1").clear()
        driver.find_element_by_id("db_SYUKKIN_JIKOKU1").send_keys(text[1])
        driver.find_element_by_id("db_TAISYUTU_JIKOKU1").clear()
        driver.find_element_by_id("db_TAISYUTU_JIKOKU1").send_keys(text[4])
        driver.find_element_by_id("db_RESTSTR_JIKOKU1").click()
        driver.find_element_by_id("db_RESTSTR_JIKOKU1").clear()
        if(text[2]!=text[3]):
            driver.find_element_by_id("db_RESTSTR_JIKOKU1").send_keys(text[2])
            driver.find_element_by_id("db_RESTEND_JIKOKU1").click()
            driver.find_element_by_id("db_RESTEND_JIKOKU1").clear()
            driver.find_element_by_id("db_RESTEND_JIKOKU1").send_keys(text[3])
        driver.find_element_by_id("db_RESTEND_JIKOKU2").click()
        sleep(1) #OZO内での合計労働時間計算を待つ
        driver.find_element_by_id("db_SYUKKIN_JIKAN").click()
        driver.find_element_by_id("db_SYUKKIN_JIKAN").send_keys(Keys.CONTROL, Keys.INSERT) # コピー
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='実績残業'])[1]/following::span[7]").click()
        self.accept_next_alert = True
        sleep(1)
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='備考'])[1]/following::input[27]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='備考'])[1]/following::input[27]").clear()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='備考'])[1]/following::input[27]").send_keys(Keys.SHIFT, Keys.INSERT)#ペースト
        driver.find_element_by_name("db_COMMENT").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='削除'])[2]/preceding::span[1]").click()
        #self.assertEqual(u"登録します。よろしいですか？", self.close_alert_and_get_its_text())
        sleep(10)
        #driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

unittest.main()

# if __name__ == "__main__":
#     unittest.main()
