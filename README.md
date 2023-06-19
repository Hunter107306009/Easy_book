# Easy Book
Provide a platform for consumers to register as members for restaurant reservations. Establish a membership system on the platform based on the frequency of visits or the amount of consumption. Additionally, create a record of transactions and accumulate member points. Restaurants can also register on this platform and automatically allocate table numbers based on the number of guests for reservations. The platform also includes a blacklist management feature.

For more detailed information about the frontend and backend processes, please refer to the corresponding folder.

## Suggested Reading Order
1. 資料庫題目說明 : 包含專案的基本介紹、需求分析
2. ERmodel.jpg : 根據需求分析畫出 ER model
3. Relation_schema.pdf : 根據 ER model 轉成 schema
4. 系統架構 : 清楚介紹本專案系統的完整功能
5. EasyBookBackend\EazyBookFronted: 前後端程式碼 
7. EasyBook_FinalProject : 最終期末展示報告！
## Contributors

| 組員   | 系級     | 學號      | 工作分配                       |
|--------|----------|-----------|--------------------------------|
| 吳泓澈 | 資碩工一 | 111753116 | 組長、DEMO、前端開發           |
| 朱筑筠 | 資碩工一 | 111753113 | 報告、簡報製作、後端開發             |
| 李家蓁 | 資碩工一 | 111753129 | 前端開發                     |
| 陳品伃 | 資碩計一 | 112753204 | 後端開發、README整理          |
| 羅鈺涵 | 資碩計一 | 112753208 | 後端開發                       |
| 楊迪奇 | 資碩計一 | 111753231 | 後端開發                        |
| 羅紹耘 | 資碩計一 | 111753217 | 資料庫建置                       |

## Fronted
> 使用工具
* React
* Node.js

> Clone & Set Up
* [Easy Book Fronted](https://github.com/Hunter107306009/Easy_book/tree/main/EasyBookFrontend)

## Backend
> 使用工具
* FastAPI
* Docker
* MySQL

> Clone & Set Up
* [Easy Book Backend](https://github.com/Hunter107306009/Easy_book/tree/main/EasyBookBackend)

  
> Packages we use

``` Python
fastapi==0.95.0
fastapi-login==1.8.3
fastapi-utils==0.2.1
mysql-connector-python==8.0.32
numpy==1.21.3
pandas==1.3.4
pydantic==1.10.2
uvicorn==0.21.1
SQLAlchemy==1.4.46
PyMySQL==1.0.2
cryptography
```
全部都包含在docker內，只要下指令```docker compose up backend```就會自動安裝了
