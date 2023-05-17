# FastAPI
### User Stories
* Google Sheet：[Easy Book Backend](https://docs.google.com/spreadsheets/d/1HTl5BOC7ZXuf7exj2tgmnfYX3fG0ITDtNtZGPZHH7Ic/edit?usp=share_link)

### Clone & Set Up
1. docker-compose.yml
```docker
services:
  backend:
    build: . # 設定上下文目錄，以該目錄為準指定Dockerfile
    restart: always
    volumes:
      - (這邊要放自己的local路徑)/EasyBookBackend/my-app:/data
```
