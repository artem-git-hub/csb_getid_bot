import telebot
from config import *
from other_func import add_user

bot = telebot.TeleBot(TOKEN)

CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]


@bot.message_handler(commands=['start', 'help'])
def start(message):
	add_user(message.from_user.id, message.from_user.username)
	bot.send_message(message.chat.id, "Напиши мне что угодно кроме /start и /help, а я дам тебе твой телеграм id", parse_mode='html')




@bot.message_handler(content_types = CONTENT_TYPES)
def get_text(message):
	add_user(message.from_user.id, message.from_user.username)
	bot.send_message(message.chat.id, "Твой tg id",  parse_mode='html')
	bot.send_message(message.chat.id, f"<b>{message.from_user.id}</b>",  parse_mode='html')



bot.polling(none_stop = True, interval = 0)
