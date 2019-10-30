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

@app.route("/")
def main():
    props = {"start_time":start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("index.html", props=props)

@app.route("/start.html")
def start():
    dt_now = datetime.datetime.now()
    global start_time, start_time2
    start_time =dt_now.strftime("%H:%M:%S")
    start_time2 = dt_now
    props = {"start_time":start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("start.html",props=props, start_time=start_time, start_time2=start_time2)

@app.route("/restart.html")
def start2():
    dt_now = datetime.datetime.now()
    global rest_start_time, rest_start_time2
    rest_start_time =dt_now.strftime("%H:%M:%S")
    rest_start_time2 = dt_now
    props = {"start_time":start_time,"rest_start_time":rest_start_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("restart.html",props=props, rest_start_time=rest_start_time, rest_start_time2=rest_start_time2)

@app.route("/stop.html")
def stop():
    dt_now = datetime.datetime.now()
    global rest_stop_time, rest_stop_time2
    rest_stop_time =dt_now.strftime("%H:%M:%S")
    rest_stop_time2 = dt_now
    props = {"start_time":start_time,"rest_start_time":rest_start_time, "rest_stop_time":rest_stop_time, "y":y, "m":m, "d":d, "wd":wd}
    return render_template("stop.html",props=props, rest_stop_time=rest_stop_time, rest_stop_time2=rest_stop_time2)

@app.route("/end.html")
def end():
    dt_now = datetime.datetime.now()
    global start_time, rest_start_time, rest_stop_time, stop_time, start_time2, rest_start_time2, rest_stop_time2, stop_time2,worktime
    stop_time =dt_now.strftime("%H:%M:%S")
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
            s = math.floor(s*100)/100#勤怠は分単位なのでsは考慮しない
        elif min==0:
            min = 00
            h=0
        props = {"start_time":start_time,"rest_start_time":rest_start_time, "rest_stop_time":rest_stop_time , "stop_time":stop_time, "worktime_h":h, "worktime_min":min, "y":y, "m":m, "d":d, "wd":wd}
    #休憩を挟まない場合
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
    c = sqlite3.connect(dbpath)
    cur = c.cursor()
    #書き込み
    date = datetime.date.today()
    date = date.strftime("%Y%m%d")
    wt = "{}:{}".format(h,min)
    t = [date, start_time, rest_start_time, rest_stop_time, stop_time, wt]
    cur.execute('insert into sample_table values(?,?,?,?,?,?)',t)
    # #DB確認
    # cur.execute('SELECT * FROM sample_table')
    # results = cur.fetchall()
    # print(results)
    c.commit()
    c.close()
    return render_template("end.html",props=props)
    #このend関数は最後の処理なので下の行のようにグローバル変数として返す必要はない（と思う）
    #return render_template("end.html",props=props, stop_time=stop_time, stop_time2=stop_time2, worktime_h=h, worktime_min=min)

if __name__ == "__main__":
    app.run()
