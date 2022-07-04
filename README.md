# Discord To Instagram


## Usage
1. Install dependencies - `python3 -m pip install -r requirements.txt`

>安裝依賴 - `python3 -m pip install -r requirements.txt`
2. Modify main.py file 

>修改 main.py 檔案
3. Run the program - `python3 main.py` 

>執行程式 `python3 main.py` 


## Modify main.py 

### Fist

At same main.py path , 
Create a new pass.txt and enter the password in the content.
>在 main.y 相同目錄下
>新建 pass.txt 並在內容輸入密碼.

### line 17 
Change your keyword list
>更改為你的關鍵字

```py
itemlist = ["share", "builds", "overclock"]
```
### line 57
Change your instagram hash tag
>更改你的 IG 主題標籤

```py
hashtag = "-\n#PCSetUp #PCBuilding #PCbuilds"
```

### line 59
ig_caption variable is the text content sent to instagram.
>ig_caption 變數是發往 instagram 的文字內容.

```py
ig_caption = str(message.author)+"posted on" + \
    str(message.channel.name)+"\n" + \
    f'{message.content}\n\n{hashtag}'
```
variable 

str(message.author) is author who send it from discord.
>str(message.author) 是從 discord 發送它的作者

"posted on" can change to your language.

str(message.channel.name) which channel in discord was sent from.
>str(message.channel.name) 是從 discord 哪個頻道發送的。

message.content is the message content


### line 63

Replace to instagram account id 
>替換成 IG 頻道帳號

```py
insta_client.login("BOT_USE_INSTAGRAM_ACCOUNT_ID",open('pass.txt', 'r').read())
```

### line 80
Change your discord bot token 
>修改你的 discord bot token

```py
bot.run('YOUR Discord bot tokem')
```

若不清楚如何建立機器人及取得 token 可參考
[How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/)

***
# Important
### The robot must be manually restricted to one channel, and the other channels cannot have access privileges.
### 機器人必須手動限制在一個頻道,其餘頻道不能有訪問權限.
### Otherwise it will be triggered.
### 否則會被觸發.