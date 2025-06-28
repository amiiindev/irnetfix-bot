from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# 👇 اطلاعات رباتت رو اینجا بذار
TOKEN = "7578386725:AAHbfl9wCGIEWucPXzqhb-wEvwds3m05nPc"
CHANNEL_ID = "@irnetfix"  # آیدی کانال تو

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user.id)
        if member.status in ['member', 'administrator', 'creator']:
            update.message.reply_text("✅ خوش اومدی! اینم کانفیگت:\n\n🔗 https://example.com/irnetfix-config")
        else:
            raise Exception("Not member")
    except:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_ID.strip('@')}")],
            [InlineKeyboardButton("🔄 بررسی عضویت", callback_data='check')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("❗️برای دریافت کانفیگ باید عضو کانال بشی:", reply_markup=reply_markup)

def check(update: Update, context: CallbackContext):
    query = update.callback_query
    user = query.from_user
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user.id)
        if member.status in ['member', 'administrator', 'creator']:
            query.edit_message_text("✅ تایید شد! اینم کانفیگت:\n\n🔗 https://example.com/irnetfix-config")
        else:
            query.answer("❌ هنوز عضو نشدی!", show_alert=True)
    except:
        query.answer("❌ هنوز عضو نشدی!", show_alert=True)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(check, pattern='check'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
