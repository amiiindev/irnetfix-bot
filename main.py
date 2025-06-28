from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

TOKEN = "7699370673:AAEG8JnbOJWBeIYJpC3uRs9Dm76UcbM3-z0"
CHANNEL_ID = "@irnetfix"  # آیدی کانالت

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user.id)
        if member.status in ['member', 'administrator', 'creator']:
            update.message.reply_text(
                "✅ خوش اومدی!\n\n📥 اینم کانفیگت:\n🔗 https://example.com/irnetfix-config"
            )
        else:
            raise
    except:
        keyboard = [
            [InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_ID.strip('@')}")],
            [InlineKeyboardButton("🔄 بررسی عضویت", callback_data='check')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(
            "❗️برای دریافت کانفیگ، باید اول عضو کانال بشی:", 
            reply_markup=reply_markup
        )

def check(update: Update, context: CallbackContext):
    query = update.callback_query
    user = query.from_user
    try:
        member = context.bot.get_chat_member(CHANNEL_ID, user.id)
        if member.status in ['member', 'administrator', 'creator']:
            query.edit_message_text(
                "✅ عضویت تایید شد!\n\n📥 کانفیگت:\n🔗 https://example.com/irnetfix-config"
            )
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
