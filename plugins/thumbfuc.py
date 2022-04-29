from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb,insert
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

@Client.on_message(filters.private & filters.command(['help']))
async def  help(client,message):
		insert(int(message.chat.id))
		await message.reply_text(text =f"""
	__/viewthumb__ : **View current thumbnil** 
	__/delthumb__  : **Delete thumbnil**
	
	**Dev contact @slogan_98**
	""",reply_to_message_id = message.message_id,
	 reply_markup=InlineKeyboardMarkup(
	 [
                [
                    InlineKeyboardButton("мσνιє яєqυєѕт gяσυρ 📲", url="https://t.me/WORLD_WIDE_MOVIES")],
                    [InlineKeyboardButton("🏐ᵘʳˡ ᵈᵒʷⁿˡᵒᵃᵈᵉʳ", url="https://t.me/youtube_instagram_downloaderbot")
                ]
            ]))



@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
		thumb = find(int(message.chat.id))
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**You dont have any custom Thumbnail.send a new  thumbnil**")
	
	
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Custom Thumbnail Deleted Successfully**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Your Custom Thumbnail Saved Successfully** ✅")
	
