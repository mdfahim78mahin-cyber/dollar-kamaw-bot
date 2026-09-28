import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ChatMemberStatus

# ═══════════════════════════════════════
# ✅ Environment Variables
# ═══════════════════════════════════════
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WEB_APP_URL = os.environ.get("WEB_APP_URL", "https://mdafahim78mahin-cyber.github.io/dollar-kamaw-bot/index.html")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Dollarkamaw10k_bot")

# 🚨 Force Join — চ্যানেল ও গ্রুপ
CHANNEL_USERNAME = "Dollarkamaw10k"       # 📢 চ্যানেল
GROUP_USERNAME = "dollarkamaw10"          # 👥 গ্রুপ

CHANNEL_URL = f"https://t.me/{CHANNEL_USERNAME}"
GROUP_URL = f"https://t.me/{GROUP_USERNAME}"

# ═══════════════════════════════════════
# 🎨 বাটনের টেক্সট
# ═══════════════════════════════════════
BUTTON_JOIN_CHANNEL = "📢 চ্যানেল জয়েন করুন"
BUTTON_JOIN_GROUP = "👥 গ্রুপ জয়েন করুন"
BUTTON_VERIFY = "✅ জয়েন করেছি — যাচাই করুন"
BUTTON_APP = "🚀 অ্যাপ ওপেন করুন"
BUTTON_CHANNEL_OFFICIAL = "📢 অফিসিয়াল চ্যানেল"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ═══════════════════════════════════════
# 🎨 WELCOME MESSAGE — আকর্ষণীয় ডিজাইন
# ═══════════════════════════════════════
def get_welcome_message(name):
    return f"""
╔══════════════════════════╗
   💵 <b>ডলার কামাও</b> 💵
╚══════════════════════════╝

🌟 হ্যালো <b>{name}</b>! 👋
🎉 <b>স্বাগতম!</b>
বাংলাদেশের <b>#১ আর্নিং প্ল্যাটফর্মে</b> আপনাকে স্বাগতম!

━━━━━━━━━━━━━━━━━━━━━━

💎 <b>আপনার জন্য যা যা আছে:</b>

🎬 <b>অ্যাড দেখুন</b>          → ৳ আয় করুন
🧠 <b>কুইজ খেলুন</b>           → ৳ জিতুন
⚡ <b>Boost Earn করুন</b>      → ইনস্ট্যান্ট টাকা
👥 <b>বন্ধু রেফার করুন</b>     → ৳ বোনাস
🎁 <b>ডেইলি বোনাস</b>          → প্রতিদিন ফ্রি
🏆 <b>লিডারবোর্ডে উঠুন</b>    → টপ আর্নার হোন

━━━━━━━━━━━━━━━━━━━━━━

💰 <b>সরাসরি বিকাশ/নগদে উইথড্র!</b>
🔒 <b>১০০% নিরাপদ ও বিশ্বস্ত</b>
⚡ <b>২৪-৪৮ ঘন্টায় পেমেন্ট</b>

━━━━━━━━━━━━━━━━━━━━━━

🚀 <b>এখনই শুরু করুন!</b>

👇 নিচের বাটনে ক্লিক করুন 👇
"""


# ═══════════════════════════════════════
# 🔒 JOIN REQUIRED MESSAGE
# ═══════════════════════════════════════
def get_join_required_message(name):
    return f"""
🔒 <b>চ্যানেল ও গ্রুপ জয়েন করুন!</b>

👋 হ্যালো <b>{name}</b>!

🎯 <b>ডলার কামাও</b> ব্যবহার করতে হলে
আমাদের <b>চ্যানেল</b> ও <b>গ্রুপে</b> জয়েন করতে হবে।

━━━━━━━━━━━━━━━━━━━━━━

📢 <b>কেন জয়েন করতে হবে?</b>

✅ নতুন অফার সবার আগে পাবেন
✅ বোনাস ও ইভেন্টের খবর
✅ পেমেন্ট আপডেট
✅ টিপস ও ট্রিকস
✅ সাপোর্ট সবার আগে

━━━━━━━━━━━━━━━━━━━━━━

👇 <b>প্রথমে ২টোতেই জয়েন করুন</b>
👇 <b>তারপর "✅ জয়েন করেছি" ক্লিক করুন</b>
"""


# ═══════════════════════════════════════
# 🎨 HELP MESSAGE
# ═══════════════════════════════════════
HELP_MESSAGE = """
💵 <b>ডলার কামাও — হেল্প সেন্টার</b>

━━━━━━━━━━━━━━━━━━━━━━

📋 <b>কমান্ড লিস্ট:</b>

/start — শুরু করুন
/help — সাহায্য
/app — অ্যাপ খুলুন

━━━━━━━━━━━━━━━━━━━━━━

🎯 <b>কীভাবে কামাবেন:</b>

1️⃣ /start দিন
2️⃣ চ্যানেল ও গ্রুপ জয়েন করুন
3️⃣ "অ্যাপ ওপেন করুন" ক্লিক করুন
4️⃣ Sign Up করুন
5️⃣ টাস্ক করে কামান
6️⃣ বিকাশ/নগদে উইথড্র করুন

━━━━━━━━━━━━━━━━━━━━━━

🆘 <b>সাপোর্ট:</b>
অ্যাপের ভেতরে সাপোর্ট সেকশনে যান

💵 <b>প্রতিদিন ডলার কামান!</b>
"""


# ═══════════════════════════════════════
# 🔍 CHECK JOIN FUNCTION
# ═══════════════════════════════════════
async def is_joined(user_id, chat_username, context):
    """ইউজার নির্দিষ্ট চ্যানেল/গ্রুপে জয়েন করেছে কিনা চেক"""
    try:
        member = await context.bot.get_chat_member(
            chat_id=f"@{chat_username}",
            user_id=user_id
        )
        valid = [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ]
        return member.status in valid
    except Exception as e:
        logger.error(f"Join check error ({chat_username}): {e}")
        return False


async def check_both_joins(user_id, context):
    """চ্যানেল ও গ্রুপ — দুইটোই চেক"""
    channel_joined = await is_joined(user_id, CHANNEL_USERNAME, context)
    group_joined = await is_joined(user_id, GROUP_USERNAME, context)
    return channel_joined, group_joined


# ═══════════════════════════════════════
# 🤖 /start HANDLER
# ═══════════════════════════════════════
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome + Force Join"""
    user = update.effective_user
    name = user.first_name or "বন্ধু"

    channel_joined, group_joined = await check_both_joins(user.id, context)

    if not (channel_joined and group_joined):
        # ❌ কেউ একজন জয়েন করেনি → Force Join
        keyboard = [
            [InlineKeyboardButton(text=BUTTON_JOIN_CHANNEL, url=CHANNEL_URL)],
            [InlineKeyboardButton(text=BUTTON_JOIN_GROUP, url=GROUP_URL)],
            [InlineKeyboardButton(text=BUTTON_VERIFY, callback_data="verify_join")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            get_join_required_message(name),
            parse_mode='HTML',
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    else:
        # ✅ দুইটাই জয়েন করেছে → Welcome
        keyboard = [
            [InlineKeyboardButton(
                text=BUTTON_APP,
                web_app=WebAppInfo(url=WEB_APP_URL)
            )],
            [InlineKeyboardButton(text=BUTTON_CHANNEL_OFFICIAL, url=CHANNEL_URL)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            get_welcome_message(name),
            parse_mode='HTML',
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )


# ═══════════════════════════════════════
# 🤖 /help
# ═══════════════════════════════════════
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MESSAGE, parse_mode='HTML')


# ═══════════════════════════════════════
# 🤖 /app
# ═══════════════════════════════════════
async def app_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    name = user.first_name or "বন্ধু"

    channel_joined, group_joined = await check_both_joins(user.id, context)

    if not (channel_joined and group_joined):
        keyboard = [
            [InlineKeyboardButton(text=BUTTON_JOIN_CHANNEL, url=CHANNEL_URL)],
            [InlineKeyboardButton(text=BUTTON_JOIN_GROUP, url=GROUP_URL)],
            [InlineKeyboardButton(text=BUTTON_VERIFY, callback_data="verify_join")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            get_join_required_message(name),
            parse_mode='HTML',
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        return

    keyboard = [[
        InlineKeyboardButton(
            text="🚀 ডলার কামাও খুলুন",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💵 <b>ডলার কামাও</b> অ্যাপ খুলতে নিচের বাটনে ক্লিক করুন:",
        parse_mode='HTML',
        reply_markup=reply_markup
    )


# ═══════════════════════════════════════
# 🔘 VERIFY BUTTON — callback
# ═══════════════════════════════════════
async def verify_join_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user = update.effective_user
    name = user.first_name or "বন্ধু"

    channel_joined, group_joined = await check_both_joins(user.id, context)

    if channel_joined and group_joined:
        # ✅ দুইটাই জয়েন
        try:
            await query.message.delete()
        except:
            pass

        keyboard = [
            [InlineKeyboardButton(
                text=BUTTON_APP,
                web_app=WebAppInfo(url=WEB_APP_URL)
            )],
            [InlineKeyboardButton(text=BUTTON_CHANNEL_OFFICIAL, url=CHANNEL_URL)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            get_welcome_message(name),
            parse_mode='HTML',
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    else:
        # ❌ এখনো বাকি
        missing = []
        if not channel_joined:
            missing.append("চ্যানেল")
        if not group_joined:
            missing.append("গ্রুপ")
        await query.answer(
            f"❌ আপনি এখনো {' ও '.join(missing)} জয়েন করেননি! আগে জয়েন করুন।",
            show_alert=True
        )


# ═══════════════════════════════════════
# ❗ ERROR HANDLER
# ═══════════════════════════════════════
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} caused error {context.error}")


# ═══════════════════════════════════════
# 🚀 MAIN
# ═══════════════════════════════════════
def main():
    if not BOT_TOKEN:
        logger.error("❌ BOT_TOKEN নেই! Environment Variables চেক করুন।")
        return

    logger.info(f"🚀 Starting: @{BOT_USERNAME}")
    logger.info(f"📢 Channel: @{CHANNEL_USERNAME}")
    logger.info(f"👥 Group: @{GROUP_USERNAME}")

    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("app", app_command))
    application.add_handler(CallbackQueryHandler(verify_join_callback, pattern="^verify_join$"))

    application.add_error_handler(error_handler)

    logger.info("✅ Bot is running...")
    application.run_polling()


if __name__ == '__main__':
    main()
