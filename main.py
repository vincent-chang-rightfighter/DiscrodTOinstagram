# inspires from instagram account : mcfallout.ig
# just imagine code how it works , and remake it to open source
# User post picture with messages on Discord and bot will post it to instagram.
import discord
import discord.ext
import requests
from PIL import Image
from io import BytesIO
import instagrapi

dc_client = discord.Client()
insta_client = instagrapi.Client()


# This list is the keyword in the message
# change words in itemlist
itemlist = ["share", "builds", "overclock"]


# fill to square function
async def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


@dc_client.event
async def on_ready():
    print(f'Now Login： {dc_client.user}')
    game = discord.Game('Instagram')
    await dc_client.change_presence(activity=game, status=discord.Status.online)


@dc_client.event
async def on_message(message):
    if message.author == dc_client.user:
        return

    if any(item in message.content for item in itemlist):

        if len(message.attachments) == 0:
            await message.reply("Dosen't find picture in message")
        else:
            data = BytesIO(await message.attachments[0].read())
            data_item = Image.open(data)
            data_item = data_item.convert("RGB")
            new_data = await expand2square(data_item, (255, 255, 255))
            new_data.save("img/show.jpg", subsampling=0, quality=100)
            hashtag = "-\n#PCSetUp #PCBuilding #PCbuilds"

            ig_caption = str(message.author)+"posted on" + \
                str(message.channel.name)+"\n" + \
                f'{message.content}\n\n{hashtag}'

            insta_client.login("BOT_USE_INSTAGRAM_ACCOUNT_ID",
                               open('pass.txt', 'r').read())

            try:
                media = insta_client.photo_upload('img/show.jpg', ig_caption)
            except Exception as e:
                print(e)
            else:
                short_code = str(media.dict().get('code'))
                reply_message = "\u2705This post has been posted to instagram. " + "<" + \
                    f'https://www.instagram.com/p/{short_code}/' + \
                    ">"
                await message.reply(reply_message)
                print("Posted\n")


dc_client.run(
    'DISCORD__BOT_TOKEN')
