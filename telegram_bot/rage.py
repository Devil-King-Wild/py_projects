from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import qrcode
import os


updater = Updater("#### API KEY HERE  ####", use_context=True)


def start(update: Update, context: CallbackContext):
	print(update.message.from_user)
	update.message.reply_text("WHAT U WANT FROM ME!!")


def help(update: Update, context: CallbackContext):
	update.message.reply_text("just find ur self")

def cmd_list(update: Update, context: CallbackContext):
	print(update.message.from_user)
	update.message.reply_text(
		"LIST:\n/help\n/qrcode\n/myname")

def qr(update: Update, context):
	print(update.message.from_user)
	qr_url = context.args[0]
	QR_URL = qrcode.make(qr_url)
	QR_URL.save(f"req_qrcode.png")
	update.message.reply_photo(photo=open('req_qrcode.png', 'rb'))
	os.remove(f"req_qrcode.png")



def who_is_me(update: Update, context: CallbackContext):
	who_me = f"{update.message.from_user}"
	who_me_1 = who_me.replace(",", "\n")

	update.message.reply_text(f"{who_me_1}")





def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('qrcode', qr))
updater.dispatcher.add_handler(CommandHandler('list', cmd_list))
updater.dispatcher.add_handler(CommandHandler('myname', who_is_me))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

print("working")
