# TimeStamp

- サイズが大きすぎてnode_modulesは別にプッシュしました。「sample-win32-x64>resources>app」に保存してください。
- アプリ実行にはpython、flask(pythonモジュール)、python-shell(nodejsモジュール)、googlechrome(ウェブブラウザ)、chromedriver(chromeの拡張機能利用のため)、Selenium Python(pythonモジュール)が別途必要なのでインストールしてください。
  - Python公式ページからPython3.6をダウンロード    
  - おそらくpipもついてくるのでコマンドプロンプトにて「py -m pip install Flask」でFlaskをインストール 
  - すでにnpmは入っているので「cd sample-win32-x64/resources/app」「npm install -D pyton-shell」でpython-shellをインストール
  - https://support.google.com/chrome/answer/95346?co=GENIE.Platform%3DDesktop&hl=ja よりGoogle Chromeのダウンロードを行う(保存場所はどこでもOK）
  - https://sites.google.com/a/chromium.org/chromedriver/downloads　よりChrome Driverのダウンロードを行う(保存場所はどこでもOK）
  - ローカルディスク(C:)上に「chromedriver」というファイルを作り、Driverのzipファイルから解凍して取り出した「chromedriver.exe」を入れる。
    (つまりドライバへのPATHが「C:/chromedriver/chromedriver.exe」になる)
  - コマンドプロンプトにて「pip install selenium」でseleniumをインストール
  - 最後に「sample-win32-x64/resources/app」内にあるapp.pyを開き60~70行目あたりにあるユーザ名とパスワードを自分のOZOアカウントに変更する
  
- アプリを実行する際には「sample-win32-x64>sample.exe」をダブルクリックしてください
  　(前日等の打刻時間をDBから確認するには「cd sample-win32-x64/resources/app」「py sample.py」を実行してください)


## 問題点
- すべてのファイル合わせて130MB。アプリ本体の「sample.exe」とNodejs「node_modules」が重い。
  - electronで作っているので「sample.exe」が重いのは仕方ない
  - 「node_modules」も純正状態から複数Nodejsモジュールを追加しているので、個別インストールでは必要なモジュールがそろわない
  - なのでこれ以上小さくするのは不可能だと思う
