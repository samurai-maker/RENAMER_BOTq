from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filename to rename it__
	
	
	__For movie,series,documentry enquiries visit our group using below 
        'мσνιє яєqυєѕт gяσυρ' button__
	**For more use /help**
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [
                [
                    InlineKeyboardButton("мσνιє яєqυєѕт gяσυρ 📲", url="https://t.me/WORLD_WIDE_MOVIES")],
                    [InlineKeyboardButton("➕ ѕнαяє мє ➕", url="https://telegram.me/share/url?url=%20t.me/wwm_rename_bot")
                ]
            ]))



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
