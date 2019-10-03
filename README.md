# OzoEasyTimer

- サイズが大きすぎてnode_modulesは別にプッシュしました。「sample-win32-x64>resources>app」に保存してください。
- アプリ実行にはpython、flask(pythonモジュール)、python-shell(nodejsモジュール)が別途必要なのでインストールしてください。 
  - Python公式ページからPython3.6をダウンロード    
  - おそらくpipもついてくるのでコマンドプロンプトにて「py -m pip install Flask」でFlaskをインストール 
  - すでにnpmは入っているので「cd sample-win32-x64/resources/app」「npm install -D pyton-shell」でpython-shellをインストール
- アプリを実行する際には「sample-win32-x64>sample.exe」をダブルクリックしてください
- 前日等の打刻時間を確認するには「cd sample-win32-x64/resources/app」「py sample.py」を実行してください

## 問題点
- すべてのファイル合わせて130MB。アプリ本体の「sample.exe」とNodejs「node_modules」が重い。
  - electronで作っているので「sample.exe」が重いのは仕方ない
  - 「node_modules」も純正状態から複数Nodejsモジュールを追加しているので、個別インストールでは必要なモジュールがそろわない
  - これ以上小さくするのは不可能だと思う
