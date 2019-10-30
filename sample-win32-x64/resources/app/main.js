//webアプリをデスクトップアプリへの変更処理

// Electron側の初期設定
const {PythonShell} = require('python-shell');
const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
let mainWindow;

// アプリを閉じた時にquit
app.on('window-all-closed', function() {
  app.quit();
});

// アプリ起動後の処理
app.on('ready', function() {
  PythonShell.run('./resources/app/app.py', null, function (err, result) {  // exe:'./resources/app/app.py'    edit: './app.py'
    if (err) throw err;
    console.log(result);
  });
  const rq = require('request-promise');
  const mainAddr = 'http://localhost:5000';

  const openWindow = function() {
    mainWindow = new BrowserWindow({
      width: 400, maxWidth:400, height: 700, alwaysOnTop:true,
      icon:'./resources/app/tokei3.png'});
    mainWindow.setPosition(1180,10);
    mainWindow.loadURL(mainAddr);

    // 開発ツールを有効化
    // mainWindow.webContents.openDevTools();

    // 終了処理
    mainWindow.on('closed', function() {
      // キャッシュを削除
      electron.session.defaultSession.clearCache(() => {})
      mainWindow = null;
    });
  };

  const startUp = function() {
    rq(mainAddr)
      .then(function(htmlString) {
        console.log('server started');
        openWindow();
      })
      .catch(function(err) {
        startUp();
      });
  };

  startUp();
});
