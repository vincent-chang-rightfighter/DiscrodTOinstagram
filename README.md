# Discord To Instagram


## Usage
1. Install dependencies - `python3 -m pip install -r requirements.txt`

>安裝依賴 - `python3 -m pip install -r requirements.txt`
2. Modify main.py file 

>修改 main.py 檔案
3. Run the program - `python3 main.py` 

>執行程式 `python3 main.py` 


## Modify main.py 

#### line 63

Replace to instagram account id 
>替換成 IG 頻道帳號

```py
insta_client.login("BOT_USE_INSTAGRAM_ACCOUNT_ID",open('pass.txt', 'r').read())
```
At same path , 
Create a new pass.txt and enter the password in the content.
>在同個目錄下
>新建 pass.txt 並在內容輸入密碼.

#### line 80
Change your discord bot token 
>修改你的 discord bot token
[How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/)

```py
bot.run('YOUR Discord bot tokem')
```

***
# Important
## The robot must be manually restricted to one channel, and the other channels cannot have access privileges.
### 機器人必須手動限制在一個頻道,其餘頻道不能有訪問權限.
## Otherwise it will be triggered.
### 否則會被觸發.

