import os
import random

import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ.get('DISCOBOT_TOKEN')
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))  # 任意のチャンネルID(int)
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# 接続に必要なオブジェクトを生成
client = discord.Client()


def reply_by_word(word):
    if word == '/neko':
        return 'にゃーん'
    elif word == '/oya':
        return 'おやおやおやおや'


# 起動時に動作する処理
@client.event
async def on_ready():
    print('起動')
    serifs = ['共に夜明けを見届けましょう', '次の二千年へ踏み入る準備ができました', '素晴らしい', 'おやおや']
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(random.choice(serifs))


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # チャッtボット的な
    reply = reply_by_word(message.content)
    if reply is not None:
        await message.channel.send(reply)

    # 消し去る
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            import asyncio
            await message.channel.send('枢機に還す光(ｽﾊﾟﾗｸﾞﾓｽ)')
            await asyncio.sleep(1.5)
            await message.channel.send(file=discord.File(os.path.join(DATA_DIR, "DAluHMGW0AAT1_s.jpeg")))
            await message.channel.send('バゴーン（全てが破壊される音）')
            await asyncio.sleep(3)
            await message.channel.purge()
        else:
            await message.channel.send('おや？')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
