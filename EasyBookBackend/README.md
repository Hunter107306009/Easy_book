# FastAPI
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

### Start Up
Step.1 - start up DB
```cmd
docker compose up db -d
```

Step.2 - start up Backend
```cmd
docker compose up backend
```
