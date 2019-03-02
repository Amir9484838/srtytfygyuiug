# coding: utf8
from pyrogram import Filters
import time
from pyrogram import Client, MessageHandler
import logging
import requests
from pyrogram import Error
logging.basicConfig(level=logging.INFO)
bot = Client(
    "my_account",
    api_id=348759,
    api_hash="5dc6f4b54b1985199b42a069a5745306"
)


bot.start()

bot.send_message(468437664, 'Я был запущен!')

@bot.on_message(Filters.command("cleandown"))
def clean_down(client, message):
	try:
		begin_timer = time.time()
		start = message.reply_to_message.message_id
		chat = message.chat.id
		end = message.message_id
		pending = int(end) - int(start)
		pro_pending = int(end) / 100
		bot.send_message(message.chat.id, 'Чистка была запущена! Найдено сообщений: <b>{}</b>'.format(pending) + '. <b>\nВ среднем 500 сообщений удаляются за минуту</b>', parse_mode='HTML')
		bot.send_message(468437664, 'Чистка была запущена! Сообщений в очереди: ' + str(pending))
		print(chat)
		i = start
		while i < end:
			bot.delete_messages(chat, i)
			i = i + 1
			#bot.edit_message_text(chat, int(message.message_id) + 1, 'test ' + i) 
			if i == end:
				middle_timer = time.time()
				end_timer = int(middle_timer) - int(begin_timer)

				bot.delete_messages(chat, i)
				bot.delete_messages(chat, i + 1)
				bot.delete_messages(chat, i + 2)
				bot.send_message(chat, 'Чистка была успешно завершена! Удалено сообщений: <b>{}</b>'.format(pending) + '\nЧистка длилась (секунд): <b>{}</b>'.format(end_timer) , parse_mode='HTML')
				bot.send_message(468437664, 'Чистка была успешно завершена! Удалено сообщений: <b>{}</b>'.format(pending) + '\nЧистка длилась (секунд): <b>{}</b>'.format(end_timer) , parse_mode='HTML')


	except Exception as e:
		echat = message.chat.id
		bot.send_message(message.chat.id, 'Что-то пошло не так!\nВозможные причины:\n— Бот не может удалять сообщения (нет админки)\n— Не указан объект удаления. То есть не был сделан реплей (ответ на сообщение)')
		print(e)
		bot.send_message(468437664, 'New exception! \n' + str(e))
		bot.send_message(echat, 'Ошибка: ' + str(e))


@bot.on_message(Filters.command("cleanup"))
def clean_up(client, message):
	try:
		begin_timer = time.time()
		start = message.reply_to_message.message_id
		chat = message.chat.id
		end = message.message_id
		pending = int(end) - int(start)
		bot.send_message(message.chat.id, 'Чистка была запущена! Найдено сообщений:' + str(pending) + '. <b>В среднем 1000 сообщений удаляются за минуту</b>', parse_mode='HTML')
		bot.send_message(468437664, 'Чистка была запущена! Сообщений в очереди: ' + str(pending))
		print(chat)
		i = end 
		while i > start:
			bot.delete_messages(chat, i)
			i = i - 1
			if i == end:
				middle_timer = time.time()
				end_timer = int(middle_timer) - int(begin_timer)
				bot.delete_messages(chat, i)
				bot.delete_messages(chat, i - 1)
				bot.delete_messages(chat, i - 2)
				bot.send_message(chat, 'Чистка была успешно завершена! Удалено сообщений: <b>{}</b>'.format(pending) + '\nЧистка длилась (секунд): <b>{}</b>'.format(end_timer) , parse_mode='HTML')
				bot.send_message(468437664, 'Чистка была успешно завершена! Удалено сообщений: <b>{}</b>'.format(pending) + '\nЧистка длилась (секунд): <b>{}</b>'.format(end_timer), parse_mode='HTML')

	except Exception as e:
		bot.send_message(message.chat.id, 'Что-то пошло не так!\nВозможные причины:\n— Бот не может удалять сообщения (нет админки)\n— Не указан объект удаления. То есть не был сделан реплей (ответ на сообщение)')
		echat = message.chat.id
		bot.send_message(468437664, 'New exception! \n' + str(e))
		bot.send_message(echat, 'Ошибка: ' + str(e))


@bot.on_message(Filters.command("start"))
def clean(client, message):
	try:
		bot.send_message(message.chat.id, 'Привет! Данный бот создан для очистки групп. Для этого добавьте меня в вашу группу и дайте права на удаление сообщений.\n\n<b>Доступные команды:</b>\n<code>/CleanUp</code> — удаляет сообщения снизу вверх (от новых к старым).\n<code>/CleanDown</code> — удаляет сообщения сверху вниз (от старых к новым)\n' + ' \u2796\u2796\u2796\u2796\u2796\u2796\u2796\u2796\n@ChatKeeperBot — многофункциональный модератор групп, который поможет навести порядок. Репутация, фильтры, Facе-контроль и многое другое!', parse_mode='HTML')
	except Exception as e:
		bot.send_message(468437664, str(e))
		bot.send_message(message.chat.id, str(e))

	

@bot.on_message(Filters.command("spam"))
def spam(client, message):
	try: 
		i = 1
		while i < 100:
			bot.send_message(message.chat.id, 'Spam ' + str(i))
			i = i + 1
			time.sleep(0.1)
	except Exception as e:
		bot.send_message(message.chat.id, str(e))

