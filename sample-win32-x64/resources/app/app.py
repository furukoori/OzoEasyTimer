#HTMLとCSS、時刻計算の処理
from flask import Flask ,render_template
app = Flask(__name__)
import datetime
import math


# #apacheでの実装用コード
# import sys
# import io
# import cgi
# import cgitb
# cgitb.enable()
#
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# sys.stdin = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# sys.stderr = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# #ここまで

start_time=0
rest_start_time=0
rest_stop_time=0
stop_time=0
start_time2 = datetime.datetime.now()
rest_stop_time2 = datetime.datetime.now()
rest_start_time2 =datetime.datetime.now()

dt_now = datetime.datetime.now()
y = dt_now.year
m = dt_now.month
d = dt_now.day
wd_num = dt_now.weekday()
#datetimeから曜日（日本語で）出力
yobi = ["月","火","水","木","金","土","日"]
wd = yobi[wd_num]
#print ("Content-Type: text/html\n")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep 

#text=('20191016', '11:00', '12:00', '13:00', '16:00', '0:02')
# text[0],text[1]
# date="10月16日(水)"
# text=('20191016',start_time, rest_start_time, rest_stop_time, stop_time)
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
        driver.find_element_by_id("login_user").send_keys("******@avantcorp.com")#ユーザ名
        driver.find_element_by_id("login_pwd").clear()
        driver.find_element_by_id("login_pwd").send_keys("***********")#パスワード
        driver.find_element_by_id("login_form").submit()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='旧ワークフロー'])[1]/following::p[7]").click()
        driver.find_element_by_link_text(text[0]).click()
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
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='備考'])[2]/following::span[1]").click()
        #driver.find_element_by_link_text(u"登録").click()#ページの状態によって参照に失敗することあり
        sleep(2)
        self.assertEqual(u"登録します。よろしいですか？", self.close_alert_and_get_its_text())
        sleep(7)
        driver.close()
    
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

@app.route("/")
def main():
    props = {"start_time":start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("index.html", props=props)

@app.route("/start.html")
def start():
    dt_now = datetime.datetime.now()
    global start_time, start_time2
    start_time =dt_now.strftime("%H:%M")
    start_time2 = dt_now
    props = {"start_time":start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("start.html",props=props, start_time=start_time, start_time2=start_time2)

@app.route("/restart.html")
def start2():
    dt_now = datetime.datetime.now()
    global rest_start_time, rest_start_time2
    rest_start_time =dt_now.strftime("%H:%M")
    rest_start_time2 = dt_now
    props = {"start_time":start_time,"rest_start_time":rest_start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("restart.html",props=props, rest_start_time=rest_start_time, rest_start_time2=rest_start_time2)

@app.route("/stop.html")
def stop():
    dt_now = datetime.datetime.now()
    global rest_stop_time, rest_stop_time2
    rest_stop_time =dt_now.strftime("%H:%M")
    rest_stop_time2 = dt_now
    props = {"start_time":start_time,"rest_start_time":rest_start_time, "rest_stop_time":rest_stop_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("stop.html",props=props, rest_stop_time=rest_stop_time, rest_stop_time2=rest_stop_time2)

@app.route("/end.html")
def end():
    dt_now = datetime.datetime.now()
    global start_time, rest_start_time, rest_stop_time, stop_time, start_time2, rest_start_time2, rest_stop_time2, stop_time2,worktime
    stop_time =dt_now.strftime("%H:%M")
    stop_time2 = dt_now
    #休憩をはさむ場合
    if rest_start_time != rest_stop_time:
        t1= stop_time2 - start_time2 #休憩以外の労働時間
        t2= rest_stop_time2 - rest_start_time2 #休憩時間
        delta = t1 -t2
        delta = delta.total_seconds()
        min,s = divmod(delta, 60)
        if min>= 1:
            h,min = divmod(min,60)
            h = math.floor(h)
            min = math.floor(min)
            min = "{0:02d}".format(min)
            s = math.floor(s*100)/100#勤怠は分単位なのでsは考慮しない #勤務時間と総時間の誤差は出るかも
        elif min==0:
            min = 00
            h=0
        props = {"start_time":start_time,"rest_start_time":rest_start_time, "rest_stop_time":rest_stop_time , "stop_time":stop_time, "worktime_h":h, "worktime_min":min, "y":y, "m":m, "d":d, "wd":wd}
    #休憩を挟まない場合 #休憩時間が１分未満だと休憩なしにカウントされる
    elif rest_start_time == rest_stop_time:
        t1= stop_time2 - start_time2 #労働時間
        delta = t1
        delta = delta.total_seconds()
        min,s = divmod(delta, 60)
        if min>=1:
            h,min = divmod(min,60)
            h = math.floor(h)
            min = math.floor(min)
            min = "{0:02d}".format(min)
            s = math.floor(s*100)/100 #勤怠は分単位なのでsは考慮しない
        elif min==0: 
            min = 00
            h=0
        props = {"start_time":start_time,"rest_start_time":stop_time, "rest_stop_time":"該当なし" , "stop_time":"該当なし", "worktime_h":h, "worktime_min":min, "y":y, "m":m, "d":d, "wd":wd}
    # #DBへ保存
    import sqlite3
    dbpath = "./resources/app/test.db"
    #dbpath = "test.db"
    c = sqlite3.connect(dbpath)
    cur = c.cursor()
    #書き込み
    date = datetime.date.today()
    date = date.strftime("%Y%m%d")
    wt = "{}:{}".format(h,min)
    t = [date, start_time, rest_start_time, rest_stop_time, stop_time, wt]
    cur.execute('insert into sample_table values(?,?,?,?,?,?)',t)
    #DB確認
    cur.execute('SELECT * FROM sample_table')
    results = cur.fetchall()
    print(results)
    c.commit()
    c.close()
    #ozoへ渡す変数
    global text
    date=""
    date= str(m) +"月"+ str(d) +"日("+ wd +")"
    #text=(date,start_time, rest_start_time, rest_stop_time, stop_time)
    #10月16日(水)
    text=("10月31日(木)", start_time, rest_start_time, rest_stop_time, stop_time)
    return render_template("end.html",props=props)
    #このend関数は最後の処理なので下の行のようにグローバル変数として返す必要はない（と思う）
    #return render_template("end.html",props=props, stop_time=stop_time, stop_time2=stop_time2, worktime_h=h, worktime_min=min)

@app.route("/exit.html")
def exit():
    unittest.main()
    return render_template("exit.html")


if __name__ == "__main__":
    app.run()
    #unittest.main()