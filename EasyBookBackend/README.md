# FastAPI
## Init Backend
### User Stories
* Google Sheet：[Easy Book Backend](https://docs.google.com/spreadsheets/d/1HTl5BOC7ZXuf7exj2tgmnfYX3fG0ITDtNtZGPZHH7Ic/edit?usp=share_link)

### Clone & Set Up
1. docker-compose.yml
```docker
services:
  backend:
    ...
    volumes:
      - [這邊要放自己的local路徑]/EasyBookBackend/my-app:/data
    ...
```
2. database.env
```SQL
ACCOUNT=自己設一個帳號
PASSWORD=自己設一個密碼
ADDRESS=Docker上的IP位址:3306
DATABASE=easybook
```
> 不知道Docker的IP位址可以用下面的語法來查詢：
1. **MAC** : docker inspect [Container ID] | grep IPAddress
2. **Windows** : docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' [Container ID]

* DB Container ID：打開Docker Dashboard後，在DB的Name下面有一串可以copy的數字+字串
![dockerIP](https://github.com/Hunter107306009/Easy_book/blob/648f8574e7a282d439de9f652539376504842407/EasyBookBackend/image/docker_DB_IP.png)

### Start Up
> Step.1 - start up DB
```cmd
docker compose up db -d
```
DB啟動後，開啟MySQL workbench連線：
Host Name: `127.0.0.1` Port: `3308`
進去後就可以看到一開始init的DB了。

> Step.2 - start up Backend
* 先把main.py裡的這段程式碼取消註解(這段是用來自動建DB的，我把紹耘建的schema都寫進後端了)
![dockerIP](https://github.com/Hunter107306009/Easy_book/blob/648f8574e7a282d439de9f652539376504842407/EasyBookBackend/image/DB_startup.png)
紹耘建的schema：(會員、餐廳、候位ID我都改成DB裡的AutoIncrement了)
![dockerIP](https://github.com/Hunter107306009/Easy_book/blob/648f8574e7a282d439de9f652539376504842407/EasyBookBackend/image/update_DB.png)

* 接下來在cmd執行這行指令就可以了～
```cmd
docker compose up backend
```
* 只要有看到下面這樣就算start up成功！
```docker
easybookbackend-backend-1  | INFO:     Application startup complete.
```
然後就可以在搜尋引擎輸入`127.0.0.1:8001/docs#/`就可以看到FastAPI的Swagger UI介面了。
* **成功後要記得把上面的程式碼再註解起來唷！不然DB會一直drop create，原本丟進去的資料會不見！**

## Backend Structure
### Routers
* 這層是依照網頁主題分類去區分py檔案，這次專案一共分成member、restaurant、book這三個主題。
* 最接近前端的，在routers裡寫的都可以在Swagger UI上看到。

### Services
> Business.py
* 主要在做處理DB撈出來後的資料，例如：計算某個會員的累積消費金額。
* 同時也需要寫一些validation，例如：member name是string，但前端傳來int，這時就需要回傳error。

> crud.py
* 從DB撈資料出來
* 用python的SQLAlchemy來寫

> schema.py
* 定義從前端要傳過來哪些資料，以及定義這些資料的型態。(與google sheet的input欄位相同)

### Utils
* 這層是DB的一些設定，平常不太會動到。

