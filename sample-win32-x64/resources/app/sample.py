##打刻時間確認用プログラム
import sqlite3
import datetime

#データベースの指定
dbpath = "test.db"
c = sqlite3.connect(dbpath)
cur = c.cursor()

# # ##一回目テーブル作るときのみ
#cur.execute("""create table sample_table(date varchar(8),start varchar(8),rest_start varchar(8),rest_stop varchar(8),stop varchar(8),total varchar(8))""")

# # ##テスト
# t=('20190904','11:00','13:00','13:00','17:00','5:00')
# cur.execute('insert into sample_table values(?,?,?,?,?,?)',t)
#DB初期化
#cur.execute('delete from sample_table')

#中身の確認
cur.execute('SELECT * FROM sample_table')
results = cur.fetchall()
print(results)

c.commit()
c.close()