# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"Hᴇʟʟᴏ Tʜᴇʀᴇ, Iᴀᴍ Eʟɪɴᴀ Vɪᴅᴇᴏ Sᴛʀᴇᴀᴍɪɴɢ Bᴏᴛ ✨ [ ](https://telegra.ph/file/6ac4eac769bd785f27281.jpg) \n\n Lᴇᴛs Eɴᴊᴏʏ Cɪɴᴇᴍᴀᴛɪᴄ Vɪᴇᴡ Oғ Gʀᴏᴜᴘ Vɪᴅᴇᴏ Pʟᴀʏᴇʀ Wɪᴛʜ Yᴏᴜʀ Fʀɪᴇɴᴅs ✨❤️ "
            f"\n\n 𝑹𝒆𝒈𝒂𝒓𝒅𝒔 🥀 : @Pratheek_XD ",
            reply_markup=InlineKeyboardMarkup(
            [[
                    InlineKeyboardButton(
                        "💞 Sᴜᴍᴍᴏɴ Mᴇ 💞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ], [
                    InlineKeyboardButton(
                        "💥 Hᴏᴡ Tᴏ Usᴇ Mᴇ", callback_data="cbhowtouse")
                ], [
                    InlineKeyboardButton(
                        "✨ Gʀᴏᴜᴘ", url="https://t.me/SHIZUKA_VC_SUPPORT"),
                    InlineKeyboardButton(
                        "📣 Cʜᴀɴɴᴇʟ", url="https://t.me/aboutpratheek")
                ], [
                    InlineKeyboardButton(
                        "🥀 Dᴇᴠ", url="https://t.me/pratheek06")
                ], [
                    InlineKeyboardButton(
                        "❓ Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs ❔", callback_data="cbcmds"),
                ]]
            )
            )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **Press The Button Below To Read The Explanation And See The List Of Available Commands !**

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Aᴅᴍɪɴ ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sᴜᴅᴏ ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Bᴀsɪᴄ ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /leaveall - order userbot to leave from all group

        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
