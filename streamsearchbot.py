import requests
from youtubesearchpython import SearchVideos
from telegraph import Telegraph
from telethon.tl.types import InputWebDocument
from telethon import TelegramClient, events
from telethon import custom, events, Button
import re
import urllib
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from Configs import Config
from loggers import logging
import os
import re
from math import ceil
import requests
import telethon
from telethon import Button, custom, events, functions
bot = TelegramClient("bot", api_id=Config.API_ID, api_hash=Config.API_HASH)
torrentbot = bot.start(bot_token=Config.BOT_TOKEN)


@torrentbot.on(events.NewMessage(pattern="^/start$"))
async def search(event):
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    await event.reply(message=f"**Hello, {firstname}, I Am Inline Stream Search Bot.** \n**Using Me You Can Fetch Torrent Magnet, Youtube Videos Link, Jio Saavan Music Links** \n**(C) @Bot_Gram_Developers**",
                      buttons=[
                      [Button.switch_inline("✳️Search Youtube✳️", query="yt ", same_peer=True)],
                      [Button.switch_inline("✳️Search Torrent✳️", query="torrent ", same_peer=True)],
                      [Button.switch_inline("✳️Search JioMusic✳️", query="jm ", same_peer=True)],
                              ]
                     )
@torrentbot.on(events.NewMessage(pattern="^/repo$"))
async def search(event):
    await event.reply('<b><u>Here is My Repo</b></u> <code>https://github.com/Rocky572/StreamSearchRoBot</code>', parse_mode="HTML")

@torrentbot.on(events.InlineQuery(pattern=r"torrent (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    sedlyf = "https://api.sumanjay.cf/torrent/?query=" + starkisnub
    try:
        okpro = requests.get(url=sedlyf, timeout=10).json()
    except:
        pass
    sed = len(okpro)
    if sed == 0:
        resultm = builder.article(
                title="No Results Found.",
                description="Check Your Spelling / Keyword",
                text="**Please, Search Again With Correct Keyword, Thank you !**",
                buttons=[
                      [Button.switch_inline("Search Again", query="torrent ", same_peer=True)],
                              ]
            )
        await event.answer([resultm])
        return
    if sed > 30:
        for i in range(30):
            seds = okpro[i]["age"]
            okpros = okpro[i]["leecher"]
            sadstark = okpro[i]["magnet"]
            okiknow = okpro[i]["name"]
            starksize = okpro[i]["size"]
            starky = okpro[i]["type"]
            seeders = okpro[i]["seeder"]
            okayz = (f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` ")
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(await event.builder.article(
                title=okiknow,
                description=sedme,
                text=okayz,
                buttons=Button.switch_inline("Search Again", query="torrent ", same_peer=True),
            )
                               )
    else:
        for sedz in okpro:
            seds = sedz["age"]
            okpros = sedz["leecher"]
            sadstark = sedz["magnet"]
            okiknow = sedz["name"]
            starksize = sedz["size"]
            starky = sedz["type"]
            seeders = sedz["seeder"]
            okayz = (f"**Title :** `{okiknow}` \n**Size :** `{starksize}` \n**Type :** `{starky}` \n**Seeder :** `{seeders}` \n**Leecher :** `{okpros}` \n**Magnet :** `{sadstark}` ")
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(await event.builder.article(
                title=okiknow,
                description=sedme,
                text=okayz,
                buttons=[Button.switch_inline("Search Again", query="torrent ", same_peer=True)],
            ))
    await event.answer(results)


@torrentbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=20)
    mi = search.result()
    moi = mi["search_result"]
    if search == None:
        resultm = builder.article(
                title="No Results Found.",
                description="Check Your Spelling / Keyword",
                text="**Please, Search Again With Correct Keyword, Thank you !**",
                buttons=[
                      [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                              ]
            )
        await event.answer([resultm])
        return
    for mio in moi:
        mo = mio["link"]
        thum = mio["title"]
        fridayz = mio["id"]
        thums = mio["channel"]
        td = mio["duration"]
        tw = mio["views"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        okayz = (f"**Title :** `{thum}` \n**Link :** `{mo}` \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`")
        hmmkek = f'Channel : {thums} \nDuration : {td} \nViews : {tw}'
        results.append(await event.builder.article(
                title=thum,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline("Search Again", query="yt ", same_peer=True),
            )
                               )
    await event.answer(results)

@torrentbot.on(events.InlineQuery(pattern=r"jm (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = f"http://starkmusic.herokuapp.com/result/?query={starkisnub}"
    seds = requests.get(url=search).json()
    for okz in seds:
        fine = okz['album']
        okmusic = okz['music']
        hmmstar = okz['perma_url']
        singer = okz['singers']
        hmm = okz['duration']
        langs = okz['language']
        hidden_url = okz['media_url']
        okayz = (f"**Song Name :** `{okmusic}` \n**Singer :** `{singer}` \n**Song Url :** `{hmmstar}`"
                 f"\n**Language :** `{langs}` \n**Download Able Url :** `{hidden_url}`"
                 f"\n**Duration :** `{hmm}`")
        hmmkek = f'Song : {okmusic} Singer : {singer} Duration : {hmm} \nLanguage : {langs}'
        results.append(await event.builder.article(
                title=okmusic,
                description=hmmkek,
                text=okayz,
                buttons=Button.switch_inline("Search Again", query="jm ", same_peer=True),
            )
                               )
    await event.answer(results)
    
@torrentbot.on(events.InlineQuery)  # pylint:disable=E0602
async def inline_handler(event):
        builder = event.builder
        query = event.text
        replied_user = await torrentbot.get_me()
        firstname = replied_user.username
        if query == None or " ": 
            resulte = builder.article(
                title="Usage Guide.",
                description="(C) @StarkGanG",
                text=f"**How To Use Me?** \n**Youtube :** `@{firstname} yt <query>` \n**Example :** `@{firstname} yt why we lose song` \n\n**Torrent :** `@{firstname} torrent <query>` \n**Example :** `@{firstname} torrent avengers endgame ` \n\n**JioSaavan :** `@{firstname} jm <query>` \n**Example :** `@{firstname} jm dilbaar`",
                buttons=[
                      [Button.url("Contact Me", f"t.me/{firstname}")],
                      [Button.switch_inline("Search Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("Search Torrent", query="torrent ", same_peer=True)],
                      [Button.switch_inline("Search JioSaavn", query="jm ", same_peer=True)],
                ]
                             
            )
            await event.answer([resulte])
print("Your Stream Search Bot is Alive. Thank You !")
def startbot():
    torrentbot.run_until_disconnected()


if __name__ == "__main__":
    startbot()
