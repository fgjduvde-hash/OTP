# ============================================================
#  █████╗ ██╗      █████╗ ███████╗██╗  ██╗██████╗ ██╗   ██╗
# ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔══██╗╚██╗ ██╔╝
# ███████║██║     ███████║███████╗█████╔╝ ██████╔╝ ╚████╔╝ 
# ██╔══██║██║     ██╔══██║╚════██║██╔═██╗ ██╔══██╗  ╚██╔╝  
# ██║  ██║███████╗██║  ██║███████║██║  ██╗██║  ██║   ██║   
# ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
#
#            𝑨𝑳 𝑨𝑺𝑲𝑹𝒀 - OFFICIAL VERSION V2
# ============================================================
# Developer  : AL ASKRY
# Owner ID   : 8183361604
# Channel    : @Alaskry0
# Group      : @Alaskey9
# Contact    : https://t.me/askry47
# Username   : Alaskry90
# Password   : 998877
# ============================================================

import time
import requests
import json
import re
import os
from datetime import datetime, date, timedelta
from pathlib import Path
import sqlite3
import telebot
from telebot import types
import threading
import random
import traceback

# ======================
# 🔐 إعدادات API الأساسية
# ======================
TIMESMS_URL      = "https://www.timesms.org"
TIMESMS_USERNAME = "Alaskry90"
TIMESMS_PASSWORD = "998877"
TIMESMS_TOKEN    = "QlFXRTRSQkpHgVRaXGFQYoaGhoCJjVVzaGllREOPWFmFTpJFUlFW"

API_URL   = TIMESMS_URL
API_TOKEN = TIMESMS_TOKEN

# ======================
# 🔗 إعدادات الروابط والقنوات
# ======================
CHANNEL_1_URL = "https://t.me/Alaskry0"
CHANNEL_2_URL = "https://t.me/Alaskry0"
OWNER_1_LINK = "https://t.me/askry47"
OWNER_2_LINK = "https://t.me/askry47"

# ======================
# 🤖 إعدادات البوت
# ======================
BOT_TOKEN = "8661336424:AAHBj8dcDKlU2GSksmuG0i1Wou3N_bevgdM"
CHAT_IDS = ["-1003855416638"]
REFRESH_INTERVAL = 2
ADMIN_IDS = [8183361604]
OWNER_ID = 8183361604
DB_PATH = "/app/bot.db"

DEVELOPER_TAG = "👨‍💻 المطور: عسكري | @askry47"
FOOTER = "\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"

# ======================
# 🌐 اللغات المتاحة
# ======================
LANGUAGES = {
    "ar": {
        "welcome": "مرحباً بك في بوت AL ASKRY 🦂",
        "choose_country": "🌍 اختر دولتك 👇",
        "no_countries": "⚠️ لا توجد دول متاحة حالياً.",
        "waiting_otp": "⏳ في انتظار OTP...",
        "number": "📱 الرقم",
        "country": "🌍 الدولة",
        "banned": "🚫 أنت محظور.",
        "join_first": "🔒 يجب الاشتراك في القنوات أولاً ثم اضغط تأكيد",
        "sub_confirmed": "✅ تم التحقق من الاشتراك",
        "not_subbed": "❌ لم تشترك بعد",
        "instructions": """📜 <b>تعليمات الاستخدام:</b>

1️⃣ اضغط على دولتك
2️⃣ ستحصل على رقم مؤقت
3️⃣ استخدم الرقم في التطبيق المطلوب
4️⃣ سيصلك OTP تلقائياً هنا

⚠️ <b>تنبيه:</b> الأرقام مشتركة، لا تستخدم لأغراض مخالفة.

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "platforms": """🌍 <b>المنصات المتاحة:</b>

✅ WhatsApp
✅ Telegram  
✅ Facebook
✅ Instagram
✅ Twitter/X
✅ TikTok
✅ Snapchat
✅ Google
✅ Amazon
✅ PayPal
✅ Microsoft
✅ Apple
✅ Netflix
✅ Spotify
✅ Discord
✅ وأكثر...

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "terms": """📜 <b>الشروط والأحكام:</b>

1️⃣ الاستخدام للأغراض القانونية فقط
2️⃣ ممنوع الاستخدام في الاحتيال
3️⃣ ممنوع مشاركة الأرقام مع الغير
4️⃣ الأرقام مؤقتة وقابلة للتغيير
5️⃣ المخالفة تؤدي للحظر الفوري

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "my_account": "🧾 <b>حسابك:</b>\n\n🆔 الـ ID: <code>{uid}</code>\n👤 الاسم: {name}\n📞 رقمك الحالي: <code>{num}</code>\n🌍 دولتك: {country}\n🔗 الإحالات: {refs} مستخدم\n💰 رصيد الإحالات: {bal}",
        "referrals": "💰 <b>نظام الإحالات:</b>\n\n🔗 رابطك الخاص:\n<code>https://t.me/{bot_user}?start=ref_{uid}</code>\n\n👥 مستخدمين أحلتهم: {refs}\n💰 رصيدك: {bal} نقطة\n\n📢 شارك رابطك واكسب نقاط!",
        "change_lang": "🌐 اختر لغتك:",
    },
    "en": {
        "welcome": "Welcome to AL ASKRY Bot 🦂",
        "choose_country": "🌍 Choose Your Country 👇",
        "no_countries": "⚠️ No countries available now.",
        "waiting_otp": "⏳ Waiting for OTP...",
        "number": "📱 Number",
        "country": "🌍 Country",
        "banned": "🚫 You are banned.",
        "join_first": "🔒 Please join channels first then click Confirm",
        "sub_confirmed": "✅ Subscription verified",
        "not_subbed": "❌ Not subscribed yet",
        "instructions": """📜 <b>How to use:</b>

1️⃣ Choose your country
2️⃣ You'll get a temp number
3️⃣ Use it in the required app
4️⃣ OTP will arrive automatically

⚠️ <b>Note:</b> Numbers are shared. Do not misuse.

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "platforms": """🌍 <b>Available Platforms:</b>

✅ WhatsApp
✅ Telegram  
✅ Facebook
✅ Instagram
✅ Twitter/X
✅ TikTok
✅ Snapchat
✅ Google
✅ Amazon
✅ PayPal
✅ Microsoft
✅ Apple
✅ Netflix
✅ Spotify
✅ Discord
✅ And more...

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "terms": """📜 <b>Terms & Conditions:</b>

1️⃣ Legal use only
2️⃣ Fraud is prohibited
3️⃣ Do not share numbers
4️⃣ Numbers are temporary
5️⃣ Violations lead to ban

👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>""",
        "my_account": "🧾 <b>Your Account:</b>\n\n🆔 ID: <code>{uid}</code>\n👤 Name: {name}\n📞 Your Number: <code>{num}</code>\n🌍 Country: {country}\n🔗 Referrals: {refs}\n💰 Balance: {bal}",
        "referrals": "💰 <b>Referral System:</b>\n\n🔗 Your Link:\n<code>https://t.me/{bot_user}?start=ref_{uid}</code>\n\n👥 Users Referred: {refs}\n💰 Balance: {bal} pts\n\n📢 Share your link & earn!",
        "change_lang": "🌐 Choose your language:",
    },
    "fr": {
        "welcome": "Bienvenue sur AL ASKRY Bot 🦂",
        "choose_country": "🌍 Choisissez votre pays 👇",
        "no_countries": "⚠️ Pas de pays disponibles.",
        "waiting_otp": "⏳ En attente d'OTP...",
        "number": "📱 Numéro",
        "country": "🌍 Pays",
        "banned": "🚫 Vous êtes banni.",
        "join_first": "🔒 Rejoignez les canaux d'abord",
        "sub_confirmed": "✅ Abonnement vérifié",
        "not_subbed": "❌ Pas encore abonné",
        "instructions": "📜 Voir la version arabe pour les instructions.",
        "platforms": "🌍 Voir la version arabe pour les plateformes.",
        "terms": "📜 Voir la version arabe pour les conditions.",
        "my_account": "🧾 <b>Votre Compte:</b>\n\n🆔 ID: <code>{uid}</code>\n👤 Nom: {name}\n📞 Numéro: <code>{num}</code>\n🌍 Pays: {country}",
        "referrals": "💰 Système de parrainage - Voir version arabe.",
        "change_lang": "🌐 Choisissez votre langue:",
    }
}

# ======================
# 🗺️ أكواد الدول
# ======================
COUNTRY_CODES = {
    "1": ("USA/Canada", "🇺🇸"), "7": ("Kazakhstan", "🇰🇿"), "20": ("Egypt", "🇪🇬"),
    "27": ("South Africa", "🇿🇦"), "30": ("Greece", "🇬🇷"), "31": ("Netherlands", "🇳🇱"),
    "32": ("Belgium", "🇧🇪"), "33": ("France", "🇫🇷"), "34": ("Spain", "🇪🇸"),
    "36": ("Hungary", "🇭🇺"), "39": ("Italy", "🇮🇹"), "40": ("Romania", "🇷🇴"),
    "41": ("Switzerland", "🇨🇭"), "43": ("Austria", "🇦🇹"), "44": ("UK", "🇬🇧"),
    "45": ("Denmark", "🇩🇰"), "46": ("Sweden", "🇸🇪"), "47": ("Norway", "🇳🇴"),
    "48": ("Poland", "🇵🇱"), "49": ("Germany", "🇩🇪"), "51": ("Peru", "🇵🇪"),
    "52": ("Mexico", "🇲🇽"), "53": ("Cuba", "🇨🇺"), "54": ("Argentina", "🇦🇷"),
    "55": ("Brazil", "🇧🇷"), "56": ("Chile", "🇨🇱"), "57": ("Colombia", "🇨🇴"),
    "58": ("Venezuela", "🇻🇪"), "60": ("Malaysia", "🇲🇾"), "61": ("Australia", "🇦🇺"),
    "62": ("Indonesia", "🇮🇩"), "63": ("Philippines", "🇵🇭"), "64": ("New Zealand", "🇳🇿"),
    "65": ("Singapore", "🇸🇬"), "66": ("Thailand", "🇹🇭"), "81": ("Japan", "🇯🇵"),
    "82": ("South Korea", "🇰🇷"), "84": ("Vietnam", "🇻🇳"), "86": ("China", "🇨🇳"),
    "90": ("Turkey", "🇹🇷"), "91": ("India", "🇮🇳"), "92": ("Pakistan", "🇵🇰"),
    "93": ("Afghanistan", "🇦🇫"), "94": ("Sri Lanka", "🇱🇰"), "95": ("Myanmar", "🇲🇲"),
    "98": ("Iran", "🇮🇷"), "211": ("South Sudan", "🇸🇸"), "212": ("Morocco", "🇲🇦"),
    "213": ("Algeria", "🇩🇿"), "216": ("Tunisia", "🇹🇳"), "218": ("Libya", "🇱🇾"),
    "220": ("Gambia", "🇬🇲"), "221": ("Senegal", "🇸🇳"), "222": ("Mauritania", "🇲🇷"),
    "223": ("Mali", "🇲🇱"), "224": ("Guinea", "🇬🇳"), "225": ("Ivory Coast", "🇨🇮"),
    "226": ("Burkina Faso", "🇧🇫"), "227": ("Niger", "🇳🇪"), "228": ("Togo", "🇹🇬"),
    "229": ("Benin", "🇧🇯"), "230": ("Mauritius", "🇲🇺"), "231": ("Liberia", "🇱🇷"),
    "232": ("Sierra Leone", "🇸🇱"), "233": ("Ghana", "🇬🇭"), "234": ("Nigeria", "🇳🇬"),
    "235": ("Chad", "🇹🇩"), "236": ("Central African Republic", "🇨🇫"),
    "237": ("Cameroon", "🇨🇲"), "238": ("Cape Verde", "🇨🇻"), "239": ("Sao Tome", "🇸🇹"),
    "240": ("Equatorial Guinea", "🇬🇶"), "241": ("Gabon", "🇬🇦"), "242": ("Congo", "🇨🇬"),
    "243": ("DR Congo", "🇨🇩"), "244": ("Angola", "🇦🇴"), "245": ("Guinea-Bissau", "🇬🇼"),
    "248": ("Seychelles", "🇸🇨"), "249": ("Sudan", "🇸🇩"), "250": ("Rwanda", "🇷🇼"),
    "251": ("Ethiopia", "🇪🇹"), "252": ("Somalia", "🇸🇴"), "253": ("Djibouti", "🇩🇯"),
    "254": ("Kenya", "🇰🇪"), "255": ("Tanzania", "🇹🇿"), "256": ("Uganda", "🇺🇬"),
    "257": ("Burundi", "🇧🇮"), "258": ("Mozambique", "🇲🇿"), "260": ("Zambia", "🇿🇲"),
    "261": ("Madagascar", "🇲🇬"), "262": ("Reunion", "🇷🇪"), "263": ("Zimbabwe", "🇿🇼"),
    "264": ("Namibia", "🇳🇦"), "265": ("Malawi", "🇲🇼"), "266": ("Lesotho", "🇱🇸"),
    "267": ("Botswana", "🇧🇼"), "268": ("Eswatini", "🇸🇿"), "269": ("Comoros", "🇰🇲"),
    "350": ("Gibraltar", "🇬🇮"), "351": ("Portugal", "🇵🇹"), "352": ("Luxembourg", "🇱🇺"),
    "353": ("Ireland", "🇮🇪"), "354": ("Iceland", "🇮🇸"), "355": ("Albania", "🇦🇱"),
    "356": ("Malta", "🇲🇹"), "357": ("Cyprus", "🇨🇾"), "358": ("Finland", "🇫🇮"),
    "359": ("Bulgaria", "🇧🇬"), "370": ("Lithuania", "🇱🇹"), "371": ("Latvia", "🇱🇻"),
    "372": ("Estonia", "🇪🇪"), "373": ("Moldova", "🇲🇩"), "374": ("Armenia", "🇦🇲"),
    "375": ("Belarus", "🇧🇾"), "376": ("Andorra", "🇦🇩"), "377": ("Monaco", "🇲🇨"),
    "378": ("San Marino", "🇸🇲"), "380": ("Ukraine", "🇺🇦"), "381": ("Serbia", "🇷🇸"),
    "382": ("Montenegro", "🇲🇪"), "383": ("Kosovo", "🇽🇰"), "385": ("Croatia", "🇭🇷"),
    "386": ("Slovenia", "🇸🇮"), "387": ("Bosnia", "🇧🇦"), "389": ("North Macedonia", "🇲🇰"),
    "420": ("Czech Republic", "🇨🇿"), "421": ("Slovakia", "🇸🇰"),
    "423": ("Liechtenstein", "🇱🇮"), "500": ("Falkland Islands", "🇫🇰"),
    "501": ("Belize", "🇧🇿"), "502": ("Guatemala", "🇬🇹"), "503": ("El Salvador", "🇸🇻"),
    "504": ("Honduras", "🇭🇳"), "505": ("Nicaragua", "🇳🇮"), "506": ("Costa Rica", "🇨🇷"),
    "507": ("Panama", "🇵🇦"), "509": ("Haiti", "🇭🇹"), "591": ("Bolivia", "🇧🇴"),
    "592": ("Guyana", "🇬🇾"), "593": ("Ecuador", "🇪🇨"), "595": ("Paraguay", "🇵🇾"),
    "597": ("Suriname", "🇸🇷"), "598": ("Uruguay", "🇺🇾"), "670": ("Timor-Leste", "🇹🇱"),
    "673": ("Brunei", "🇧🇳"), "674": ("Nauru", "🇳🇷"), "675": ("Papua New Guinea", "🇵🇬"),
    "676": ("Tonga", "🇹🇴"), "677": ("Solomon Islands", "🇸🇧"), "678": ("Vanuatu", "🇻🇺"),
    "679": ("Fiji", "🇫🇯"), "680": ("Palau", "🇵🇼"), "685": ("Samoa", "🇼🇸"),
    "686": ("Kiribati", "🇰🇮"), "687": ("New Caledonia", "🇳🇨"), "688": ("Tuvalu", "🇹🇻"),
    "689": ("French Polynesia", "🇵🇫"), "691": ("Micronesia", "🇫🇲"),
    "692": ("Marshall Islands", "🇲🇭"), "850": ("North Korea", "🇰🇵"),
    "852": ("Hong Kong", "🇭🇰"), "853": ("Macau", "🇲🇴"), "855": ("Cambodia", "🇰🇭"),
    "856": ("Laos", "🇱🇦"), "960": ("Maldives", "🇲🇻"), "961": ("Lebanon", "🇱🇧"),
    "962": ("Jordan", "🇯🇴"), "963": ("Syria", "🇸🇾"), "964": ("Iraq", "🇮🇶"),
    "965": ("Kuwait", "🇰🇼"), "966": ("Saudi Arabia", "🇸🇦"), "967": ("Yemen", "🇾🇪"),
    "968": ("Oman", "🇴🇲"), "970": ("Palestine", "🇵🇸"), "971": ("UAE", "🇦🇪"),
    "972": ("Israel", "🇮🇱"), "973": ("Bahrain", "🇧🇭"), "974": ("Qatar", "🇶🇦"),
    "975": ("Bhutan", "🇧🇹"), "976": ("Mongolia", "🇲🇳"), "977": ("Nepal", "🇳🇵"),
    "992": ("Tajikistan", "🇹🇯"), "993": ("Turkmenistan", "🇹🇲"),
    "994": ("Azerbaijan", "🇦🇿"), "995": ("Georgia", "🇬🇪"),
    "996": ("Kyrgyzstan", "🇰🇬"), "998": ("Uzbekistan", "🇺🇿"),
}

# ======================
# 📦 متغيرات مؤقتة
# ======================
temp_combos = {}
user_states = {}
maintenance_mode = False

# ======================
# 🔀 خلط الأرقام
# ======================
def shuffle_numbers(numbers):
    try:
        random.shuffle(numbers)
    except:
        pass
    return numbers

# ======================
# 🗄️ قاعدة البيانات
# ======================
def init_db():
    if not os.path.exists('/app'):
        os.makedirs('/app', exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        country_code TEXT,
        assigned_number TEXT,
        is_banned INTEGER DEFAULT 0,
        private_combo_country TEXT DEFAULT NULL,
        language TEXT DEFAULT 'ar',
        referral_by INTEGER DEFAULT NULL,
        referral_count INTEGER DEFAULT 0,
        referral_balance INTEGER DEFAULT 0,
        joined_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS admins (
        user_id INTEGER PRIMARY KEY,
        added_by INTEGER,
        added_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS combos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_code TEXT UNIQUE,
        custom_name TEXT,
        numbers TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS otp_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dt TEXT, num TEXT, cli TEXT, message TEXT,
        otp TEXT, country TEXT, service TEXT,
        sent_to_user INTEGER, sent_to_group INTEGER,
        timestamp TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS bot_settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS custom_buttons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT,
        url TEXT,
        section TEXT DEFAULT 'main'
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS force_sub_channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel_url TEXT,
        channel_name TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS api_panels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        url TEXT,
        token TEXT,
        is_active INTEGER DEFAULT 1
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS manual_panels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        numbers TEXT,
        is_active INTEGER DEFAULT 1
    )''')

    settings = [
        ('channel_1', CHANNEL_1_URL), ('channel_2', CHANNEL_2_URL),
        ('owner_1', OWNER_1_LINK), ('owner_2', OWNER_2_LINK),
        ('force_sub', 'on'), ('maintenance', 'off'),
        ('refresh_interval', str(REFRESH_INTERVAL)),
        ('cache_time', '60'), ('bot_start_image', ''),
        ('bot_sections_image', ''), ('bot_channels_image', ''),
        ('otp_group_link', 'https://t.me/Alaskey9'),
    ]
    for key, value in settings:
        c.execute("INSERT OR IGNORE INTO bot_settings (key, value) VALUES (?, ?)", (key, value))

    for admin_id in ADMIN_IDS:
        c.execute("INSERT OR IGNORE INTO admins (user_id, added_by) VALUES (?, ?)", (admin_id, OWNER_ID))

    try:
        c.execute("ALTER TABLE combos ADD COLUMN custom_name TEXT")
    except:
        pass

    conn.commit()
    conn.close()

init_db()

# ======================
# 🔧 دوال الإعدادات
# ======================
def get_setting(key, default=""):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT value FROM bot_settings WHERE key=?", (key,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else default

def set_setting(key, value):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("REPLACE INTO bot_settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

# ======================
# 👥 دوال المستخدمين
# ======================
def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row

def save_user(user_id, username="", first_name="", last_name="",
              country_code=None, assigned_number=None,
              private_combo_country=None, language=None, referral_by=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    existing = get_user(user_id)
    if existing:
        if country_code is None: country_code = existing[4]
        if assigned_number is None: assigned_number = existing[5]
        if private_combo_country is None: private_combo_country = existing[7]
        if language is None: language = existing[8] if len(existing) > 8 else 'ar'
        if referral_by is None: referral_by = existing[9] if len(existing) > 9 else None

    c.execute("""
        INSERT INTO users (user_id, username, first_name, last_name,
            country_code, assigned_number, is_banned, private_combo_country,
            language, referral_by)
        VALUES (?, ?, ?, ?, ?, ?, 0, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            first_name=excluded.first_name,
            last_name=excluded.last_name,
            country_code=COALESCE(excluded.country_code, country_code),
            assigned_number=COALESCE(excluded.assigned_number, assigned_number),
            private_combo_country=COALESCE(excluded.private_combo_country, private_combo_country),
            language=COALESCE(excluded.language, language)
    """, (user_id, username, first_name, last_name,
          country_code, assigned_number, private_combo_country,
          language or 'ar', referral_by))
    conn.commit()
    conn.close()

def get_user_language(user_id):
    user = get_user(user_id)
    if user and len(user) > 8 and user[8]:
        return user[8]
    return 'ar'

def set_user_language(user_id, lang):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET language=? WHERE user_id=?", (lang, user_id))
    conn.commit()
    conn.close()

def get_lang(user_id):
    lang = get_user_language(user_id)
    return LANGUAGES.get(lang, LANGUAGES['ar'])

def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE is_banned=0")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return users

def ban_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=1 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def unban_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned=0 WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()

def is_banned(user_id):
    user = get_user(user_id)
    return user and user[6] == 1

def get_user_referral_count(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users WHERE referral_by=?", (user_id,))
    count = c.fetchone()[0]
    conn.close()
    return count

# ======================
# 👮 دوال الأدمن
# ======================
def get_all_admins():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT user_id FROM admins")
    admins = [row[0] for row in c.fetchall()]
    conn.close()
    return admins

def add_admin(user_id, added_by):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO admins (user_id, added_by) VALUES (?, ?)", (user_id, added_by))
    conn.commit()
    conn.close()

def remove_admin(user_id):
    if user_id == OWNER_ID:
        return False
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM admins WHERE user_id=?", (user_id,))
    conn.commit()
    conn.close()
    return True

def is_admin(user_id):
    return user_id == OWNER_ID or user_id in get_all_admins()

def is_owner(user_id):
    return user_id == OWNER_ID

# ======================
# 📞 دوال الكومبو والأرقام
# ======================
def get_combo_name(country_code):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute("SELECT custom_name FROM combos WHERE country_code=?", (country_code,))
        row = c.fetchone()
    except:
        row = None
    conn.close()
    if row and row[0]:
        return row[0]
    if country_code in COUNTRY_CODES:
        return COUNTRY_CODES[country_code][0]
    return "Unknown"

def get_all_combos():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT country_code FROM combos")
    combos = [row[0] for row in c.fetchall()]
    conn.close()
    return combos

def assign_number_to_user(user_id, number):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET assigned_number=? WHERE user_id=?", (number, user_id))
    conn.commit()
    conn.close()

def get_user_by_number(number):
    if not number:
        return None
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # محاولة المطابقة المباشرة أولاً
    c.execute("SELECT user_id FROM users WHERE assigned_number=?", (number,))
    row = c.fetchone()
    if row:
        conn.close()
        return row[0]
    # تنظيف الرقم من + والأصفار الزائدة للمقارنة المرنة
    clean = re.sub(r'\D', '', str(number))
    if clean.startswith('00'):
        clean = clean[2:]
    elif clean.startswith('0') and len(clean) <= 11:
        clean = clean[1:]
    # البحث عن كل الأرقام المخصصة ومقارنتها
    c.execute("SELECT user_id, assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number != ''")
    rows = c.fetchall()
    conn.close()
    for uid, stored in rows:
        s = re.sub(r'\D', '', str(stored))
        if s.startswith('00'):
            s = s[2:]
        elif s.startswith('0') and len(s) <= 11:
            s = s[1:]
        if clean == s or clean.endswith(s) or s.endswith(clean):
            return uid
    return None

def release_number(old_number):
    if not old_number:
        return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE users SET assigned_number=NULL WHERE assigned_number=?", (old_number,))
    conn.commit()
    conn.close()

def get_combo(country_code, user_id=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT numbers FROM combos WHERE country_code=?", (country_code,))
    row = c.fetchone()
    conn.close()
    return json.loads(row[0]) if row else []

def save_combo(country_code, numbers, custom_name=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if not custom_name and country_code in COUNTRY_CODES:
        custom_name = COUNTRY_CODES[country_code][0]
    c.execute("REPLACE INTO combos (country_code, custom_name, numbers) VALUES (?, ?, ?)",
              (country_code, custom_name, json.dumps(numbers)))
    conn.commit()
    conn.close()

def delete_combo(country_code):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM combos WHERE country_code=?", (country_code,))
    conn.commit()
    conn.close()

def get_available_numbers(country_code, user_id=None):
    all_numbers = get_combo(country_code, user_id)
    if not all_numbers:
        return []
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT assigned_number FROM users WHERE assigned_number IS NOT NULL AND assigned_number != ''")
    used_numbers = set(row[0] for row in c.fetchall())
    conn.close()
    available = [num for num in all_numbers if num not in used_numbers]
    return available

# ======================
# 🔑 دوال OTP
# ======================
def log_otp_to_db(dt, num, cli, message, otp, country, service, sent_to_user=0, sent_to_group=0):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""INSERT INTO otp_logs (dt, num, cli, message, otp, country, service,
        sent_to_user, sent_to_group, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (dt, num, cli, message, otp, country, service,
         sent_to_user, sent_to_group, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def is_otp_already_sent(message):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT 1 FROM otp_logs WHERE message=? LIMIT 1", (message,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

def get_otp_logs(limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM otp_logs ORDER BY id DESC LIMIT ?", (limit,))
    logs = c.fetchall()
    conn.close()
    return logs

# ======================
# 🎯 دوال المساعدة
# ======================
def html_escape(text):
    if not text:
        return ""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))

def mask_number(number):
    if not number or number == "N/A":
        return "N/A"
    number = str(number).strip()
    if len(number) > 8:
        return number[:7] + "••" + number[-4:]
    return number

def extract_otp_from_message(message):
    if not message:
        return "N/A"
    patterns = [
        r'(?:code|رمز|كود|verification|تحقق|otp|pin)[:\s\-]*[‎]?(\d{3,8})',
        r'(\d{3,4})[\s\-]?(\d{3,4})',
        r'\b(\d{4,6})\b',
        r'(\d{3})-(\d{3})',
        r'whatsapp.*?(\d{3,6})',
    ]
    message_clean = message.lower()
    for pattern in patterns:
        matches = re.findall(pattern, message_clean, re.IGNORECASE)
        if matches:
            if isinstance(matches[0], tuple):
                combined = ''.join(str(x) for x in matches[0])
                return combined.zfill(6)
            return str(matches[0]).zfill(6)
    numbers = re.findall(r'\b\d{4,6}\b', message)
    return numbers[0] if numbers else "N/A"

def detect_service_from_cli(cli, message):
    cli_lower = (cli or "").lower()
    msg_lower = message.lower()
    services = {
        "whatsapp": ["whatsapp", "واتساب"], "facebook": ["facebook", "فيسبوك", "fb"],
        "instagram": ["instagram", "انستقرام"], "telegram": ["telegram", "تيليجرام"],
        "google": ["google", "جوجل"], "twitter": ["twitter", "تويتر"],
        "tiktok": ["tiktok", "تيك توك"], "snapchat": ["snapchat", "سناب"],
        "amazon": ["amazon", "امازون"], "paypal": ["paypal", "باي بال"],
        "microsoft": ["microsoft", "مايكروسوفت"], "apple": ["apple", "ابل"],
        "netflix": ["netflix", "نتفليكس"], "spotify": ["spotify", "سبوتيفاي"],
        "discord": ["discord", "ديسكورد"], "uber": ["uber", "اوبر"],
    }
    for service, keywords in services.items():
        for keyword in keywords:
            if keyword in cli_lower or keyword in msg_lower:
                return service.upper()
    return cli.upper() if cli else "GENERAL"

def get_country_from_number(num):
    if not num:
        return "Unknown", "🌍"
    clean_num = re.sub(r'\D', '', str(num))
    for code, (name, flag) in COUNTRY_CODES.items():
        if clean_num.startswith(code):
            return name, flag
    return "Unknown", "🌍"

def is_maintenance():
    return get_setting('maintenance', 'off') == 'on'

def is_force_sub_enabled():
    return get_setting("force_sub", "on") != "off"

# ======================
# 🤖 إنشاء بوت Telegram
# ======================
bot = telebot.TeleBot(BOT_TOKEN)

# ======================
# 🔒 الاشتراك الإجباري
# ======================
FORCE_SUB_CHANNELS = ["https://t.me/Alaskry0", "https://t.me/Alaskey9"]

def check_user_joined(user_id):
    try:
        for ch in FORCE_SUB_CHANNELS:
            username = ch.split("/")[-1]
            member = bot.get_chat_member(f"@{username}", user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        return True
    except:
        return False

def send_force_sub(message):
    lang = get_lang(message.from_user.id)
    markup = types.InlineKeyboardMarkup()
    for ch in FORCE_SUB_CHANNELS:
        markup.add(types.InlineKeyboardButton("📢 Join Channel", url=ch))
    markup.add(types.InlineKeyboardButton("✅ Confirm", callback_data="check_sub"))
    bot.send_message(message.chat.id, lang['join_first'], reply_markup=markup)

# ======================
# 📨 دوال الإرسال
# ======================
def format_otp_message(msg_data):
    dt = msg_data.get('dt', 'N/A')
    num = msg_data.get('num', 'N/A')
    cli = msg_data.get('cli', 'N/A')
    message = msg_data.get('message', 'N/A')

    otp = extract_otp_from_message(message)
    service = detect_service_from_cli(cli, message)
    country_name, country_flag = get_country_from_number(num)

    try:
        dt_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        formatted_time = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    except:
        formatted_time = dt

    masked_num = mask_number(num)
    otp_display = otp if otp != "N/A" else "N/A"

    message_html = f"""<blockquote>{country_flag} <b>{country_name} {service} RECEIVED!</b> ✨</blockquote>
<blockquote>⏰ <b>Time:</b> {formatted_time}</blockquote>
<blockquote>🌍 <b>Country:</b> {country_name} {country_flag}</blockquote>
<blockquote>⚙️ <b>Service:</b> {service}</blockquote>
<blockquote>📞 <b>Number:</b> {masked_num}</blockquote>
<blockquote>🔑 <b>OTP:</b> {otp_display}</blockquote>
<blockquote>📩 <b>Full Message:</b>
{html_escape(message)}</blockquote>

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    return message_html, otp, country_name, service

class CRAPI:
    def __init__(self):
        self.base_url  = TIMESMS_URL
        self.username  = TIMESMS_USERNAME
        self.password  = TIMESMS_PASSWORD
        self.token     = TIMESMS_TOKEN
        self.session   = None
        self.last_login = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/html, */*',
        }

    # ─── تسجيل الدخول ───
    def login(self):
        try:
            self.session = requests.Session()
            self.session.headers.update(self.headers)

            login_page = self.session.get(
                f"{self.base_url}/login",
                timeout=15, allow_redirects=True
            )

            csrf = ""
            try:
                for pattern in [
                    r'name=["\']_token["\'][^>]*value=["\']([^"\']+)["\']',
                    r'value=["\']([^"\']+)["\'][^>]*name=["\']_token["\']',
                    r'<input[^>]*name=["\']token["\'][^>]*value=["\']([^"\']+)["\']',
                ]:
                    m = re.search(pattern, login_page.text)
                    if m:
                        csrf = m.group(1)
                        break
            except:
                pass

            login_data = {
                'username': self.username,
                'password': self.password,
                'user':     self.username,
                'pass':     self.password,
                'email':    self.username,
            }
            if csrf:
                login_data['_token'] = csrf

            resp = self.session.post(
                f"{self.base_url}/login",
                data=login_data,
                timeout=15,
                allow_redirects=True
            )
            print(f"[TIMES] 🔐 Login: {resp.status_code} | {resp.url}")
            self.last_login = datetime.now()
            return True
        except Exception as e:
            print(f"[TIMES] ❌ Login error: {e}")
            return False

    # ─── استخراج الرسائل من جدول HTML ───
    def _scrape_table(self, html):
        msgs = []
        try:
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)
            for row in rows:
                cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL | re.IGNORECASE)
                if len(cells) < 4:
                    continue
                clean = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
                clean = [re.sub(r'\s+', ' ', c) for c in clean]
                # صفوف timesms: date | range | number | cli | client | message
                if re.search(r'\d{4}-\d{2}-\d{2}', clean[0]):
                    msgs.append({
                        'dt':      clean[0],
                        'num':     clean[2] if len(clean) > 2 else '',
                        'cli':     clean[3] if len(clean) > 3 else '',
                        'message': clean[5] if len(clean) > 5 else (clean[-1] if clean else ''),
                    })
        except Exception as e:
            print(f"[TIMES] ⚠️ Scrape error: {e}")
        return msgs

    # ─── جلب الرسائل ───
    def fetch_messages(self, records=100, hours_back=1):
        all_messages = []
        try:
            need_login = (
                not self.session or
                not self.last_login or
                (datetime.now() - self.last_login).seconds > 3600
            )
            if need_login:
                if not self.login():
                    return []

            today     = datetime.now().strftime("%Y-%m-%d")
            today_alt = datetime.now().strftime("%d/%m/%Y")
            start_dt  = f"{today} 00:00:00"
            end_dt    = f"{today} 23:59:59"

            # الـ endpoints الصحيحة من timesms.org بناءً على الصفحة المرئية
            endpoints = [
                f"{self.base_url}/agent/SMS",
                f"{self.base_url}/agent/SMSIncoming",
                f"{self.base_url}/agent/sms",
                f"{self.base_url}/agent/sms/incoming",
                f"{self.base_url}/agent/inbox",
                f"{self.base_url}/agent/reports",
            ]

            params_list = [
                {'token': self.token, 'limit': records, 'date': today,
                 'date_from': start_dt, 'date_to': end_dt, 'format': 'json'},
                {'token': self.token, 'limit': records, 'format': 'json'},
                {'token': self.token, 'records': records},
                {'limit': records, 'date': today},
                {'date_from': start_dt, 'date_to': end_dt},
                {},
            ]

            for url in endpoints:
                for params in params_list:
                    try:
                        resp = self.session.get(
                            url, params=params, timeout=15,
                            headers={
                                'Accept': 'application/json, text/html, */*',
                                'X-Requested-With': 'XMLHttpRequest',
                                'Referer': f"{self.base_url}/agent/SMS",
                            }
                        )
                        print(f"[TIMES] 📡 {url} params={list(params.keys())} → {resp.status_code}")

                        if resp.status_code != 200 or not resp.text.strip():
                            continue

                        # محاولة JSON أولاً
                        try:
                            data = resp.json()
                            msgs_raw = []
                            if isinstance(data, list) and len(data) > 0:
                                msgs_raw = data
                            elif isinstance(data, dict):
                                for key in ['data', 'messages', 'records', 'otp_messages',
                                            'sms', 'smsList', 'result', 'items', 'list', 'rows']:
                                    val = data.get(key)
                                    if isinstance(val, list) and len(val) > 0:
                                        msgs_raw = val
                                        print(f"[TIMES] ✅ JSON key='{key}' count={len(msgs_raw)}")
                                        break

                            if msgs_raw:
                                for msg in msgs_raw:
                                    if not isinstance(msg, dict):
                                        continue
                                    all_messages.append({
                                        'dt': (msg.get('date') or msg.get('dt') or
                                               msg.get('created_at') or msg.get('time') or
                                               msg.get('datetime') or msg.get('timestamp') or
                                               datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                        'num': (msg.get('number') or msg.get('num') or
                                                msg.get('phone') or msg.get('phone_number') or
                                                msg.get('to') or msg.get('mobile') or
                                                msg.get('receiver') or msg.get('destination') or ''),
                                        'cli': (msg.get('sender') or msg.get('cli') or
                                                msg.get('from') or msg.get('service') or
                                                msg.get('source') or msg.get('app') or
                                                msg.get('originator') or ''),
                                        'message': (msg.get('message') or msg.get('text') or
                                                    msg.get('body') or msg.get('otp_message') or
                                                    msg.get('content') or msg.get('sms') or
                                                    msg.get('msg') or ''),
                                    })
                                print(f"[TIMES] ✅ {len(all_messages)} رسالة (JSON) من {url}")
                                return all_messages
                        except:
                            pass

                        # محاولة HTML scraping
                        if '<table' in resp.text.lower() or '<tr' in resp.text.lower():
                            scraped = self._scrape_table(resp.text)
                            if scraped:
                                print(f"[TIMES] 🕸️ {len(scraped)} رسالة (HTML) من {url}")
                                return scraped

                    except Exception as e:
                        print(f"[TIMES] ⚠️ {url}: {e}")
                        continue

            print("[TIMES] ❌ لم ينجح أي endpoint")

        except Exception as e:
            print(f"[TIMES] ❌ خطأ عام: {e}")
            traceback.print_exc()

        return all_messages

    # ─── التحقق من الاتصال ───
    def check_token_valid(self):
        try:
            if not self.session or not self.last_login:
                return self.login()
            resp = self.session.get(
                f"{self.base_url}/agent/SMS",
                params={'token': self.token, 'limit': 1},
                timeout=10
            )
            return resp.status_code == 200
        except:
            return False

crapi = CRAPI()

def send_to_telegram_group(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    keyboard = {
        "inline_keyboard": [[
            {"text": "👨‍💻 Owner", "url": OWNER_1_LINK},
            {"text": "📢 Channel", "url": get_setting('channel_1', CHANNEL_1_URL)}
        ]]
    }
    success = 0
    for chat_id in CHAT_IDS:
        try:
            payload = {"chat_id": chat_id, "text": text,
                       "parse_mode": "HTML", "reply_markup": json.dumps(keyboard)}
            resp = requests.post(url, data=payload, timeout=10)
            if resp.status_code == 200:
                success += 1
        except Exception as e:
            print(f"[!] خطأ Telegram لـ {chat_id}: {e}")
    return success > 0

def process_and_send_message(msg_data):
    try:
        formatted_msg, otp, country, service = format_otp_message(msg_data)
        if is_otp_already_sent(msg_data.get('message', '')):
            return False

        group_sent = send_to_telegram_group(formatted_msg)
        num = msg_data.get('num', '')
        user_id = get_user_by_number(num)
        user_sent = 0

        if user_id:
            try:
                user_msg = f"""📱 Your OTP Code 🦂 — من <b>{service}</b>:

🔑 <code>{otp}</code>
📞 الرقم: <code>{num}</code>
🌍 الدولة: {country}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""
                markup = types.InlineKeyboardMarkup()
                markup.row(
                    types.InlineKeyboardButton("👨‍💻 Owner", url=OWNER_1_LINK),
                    types.InlineKeyboardButton("📢 Channel", url=get_setting('channel_1', CHANNEL_1_URL))
                )
                bot.send_message(user_id, user_msg, reply_markup=markup, parse_mode="HTML")
                user_sent = 1
            except Exception as e:
                print(f"[!] فشل إرسال OTP للمستخدم {user_id}: {e}")

        log_otp_to_db(dt=msg_data.get('dt'), num=num, cli=msg_data.get('cli', ''),
                      message=msg_data.get('message', ''), otp=otp, country=country,
                      service=service, sent_to_user=user_sent,
                      sent_to_group=1 if group_sent else 0)
        print(f"[API] ✅ تم إرسال: {country} | {otp} | {service}")
        return True
    except Exception as e:
        print(f"[API] ❌ خطأ: {e}")
        traceback.print_exc()
        return False

# ======================
# 🛠️ أمر التشخيص /debug (للأدمن فقط)
# ======================
@bot.message_handler(commands=['debug'])
def debug_api(message):
    if not is_admin(message.from_user.id):
        return
    bot.reply_to(message, "🔍 جاري تسجيل الدخول واختبار الـ API... انتظر")

    result_text = "🛠️ <b>نتائج تشخيص timesms.org:</b>\n\n"

    try:
        import requests as req
        session = req.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0'})

        login_page = session.get(f"{TIMESMS_URL}/login", timeout=15)
        result_text += f"📌 Login Page: <code>{login_page.status_code}</code>\n"

        csrf = ""
        for pattern in [
            r'name=["\']_token["\'][^>]*value=["\']([^"\']+)["\']',
            r'value=["\']([^"\']+)["\'][^>]*name=["\']_token["\']',
        ]:
            m = re.search(pattern, login_page.text)
            if m:
                csrf = m.group(1)
                break
        result_text += f"🔑 CSRF: <code>{'found' if csrf else 'not found'}</code>\n"

        login_data = {
            'username': TIMESMS_USERNAME, 'password': TIMESMS_PASSWORD,
            'user': TIMESMS_USERNAME, 'pass': TIMESMS_PASSWORD,
            'email': TIMESMS_USERNAME,
        }
        if csrf:
            login_data['_token'] = csrf

        lr = session.post(f"{TIMESMS_URL}/login", data=login_data, timeout=15, allow_redirects=True)
        result_text += f"🔐 Login: <code>{lr.status_code}</code> → <code>{lr.url}</code>\n\n"

        test_urls = [
            f"{TIMESMS_URL}/agent/SMS",
            f"{TIMESMS_URL}/agent/SMSIncoming",
            f"{TIMESMS_URL}/agent/sms",
            f"{TIMESMS_URL}/agent/inbox",
            f"{TIMESMS_URL}/agent/reports",
        ]

        for url in test_urls:
            try:
                r = session.get(url, params={'token': TIMESMS_TOKEN, 'limit': 3,
                                              'format': 'json'}, timeout=10,
                                headers={'Accept': 'application/json, text/html, */*',
                                         'X-Requested-With': 'XMLHttpRequest'})
                short = url.replace(TIMESMS_URL, '')
                raw = r.text[:500].replace('<', '&lt;').replace('>', '&gt;')
                result_text += f"📡 <b>{short}</b> → <code>{r.status_code}</code>\n<code>{raw}</code>\n\n"
            except Exception as e:
                short = url.replace(TIMESMS_URL, '')
                result_text += f"❌ <b>{short}</b>: {e}\n\n"

    except Exception as e:
        result_text += f"\n❌ خطأ عام: {e}"

    for i in range(0, len(result_text), 4000):
        try:
            bot.send_message(message.chat.id, result_text[i:i+4000], parse_mode="HTML")
        except:
            bot.send_message(message.chat.id, result_text[i:i+4000])

# ======================
# 🏠 واجهة المستخدم الرئيسية
# ======================
def build_user_main_menu(user_id):
    """بناء القائمة الرئيسية للمستخدم"""
    lang = get_lang(user_id)
    markup = types.InlineKeyboardMarkup()

    countries = get_all_combos()
    for code in countries:
        if code in COUNTRY_CODES:
            name = get_combo_name(code)
            flag = COUNTRY_CODES.get(code, ("", "🌍"))[1]
            markup.add(types.InlineKeyboardButton(f"{flag} {name}", callback_data=f"country_{code}"))

    # أزرار واجهة المستخدم العادي
    markup.row(
        types.InlineKeyboardButton("📜 التعليمات", callback_data="user_instructions"),
        types.InlineKeyboardButton("🌍 المنصات المتاحة", callback_data="user_platforms")
    )
    markup.row(
        types.InlineKeyboardButton("🌐 تغيير اللغة", callback_data="user_change_lang"),
        types.InlineKeyboardButton("📜 الشروط", callback_data="user_terms")
    )
    markup.row(
        types.InlineKeyboardButton("💰 الإحالات", callback_data="user_referrals"),
        types.InlineKeyboardButton("🧾 حسابي", callback_data="user_account")
    )

    if is_admin(user_id):
        markup.add(types.InlineKeyboardButton("🔐 لوحة الأدمن", callback_data="admin_panel"))

    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id

    # فحص وضع الصيانة
    if is_maintenance() and not is_admin(user_id):
        bot.reply_to(message, "🔧 البوت في وضع الصيانة حالياً. تابع قناتنا للإشعارات.\n\n👨‍💻 <b>AL ASKRY</b>", parse_mode="HTML")
        return

    # فحص الاشتراك الإجباري
    if is_force_sub_enabled() and not check_user_joined(user_id):
        send_force_sub(message)
        return

    if is_banned(user_id):
        lang = get_lang(user_id)
        bot.reply_to(message, lang['banned'])
        return

    # فحص الإحالة
    referral_by = None
    if len(message.text.split()) > 1:
        ref_part = message.text.split()[1]
        if ref_part.startswith("ref_"):
            try:
                referral_by = int(ref_part.split("_")[1])
                if referral_by == user_id:
                    referral_by = None
            except:
                referral_by = None

    # إشعار الأدمن بمستخدم جديد
    is_new = not get_user(user_id)
    if is_new:
        for admin in get_all_admins():
            try:
                caption = (f"🆕 مستخدم جديد!\n"
                           f"🆔: `{user_id}`\n"
                           f"👤: @{message.from_user.username or 'None'}\n"
                           f"الاسم: {message.from_user.first_name or ''} {message.from_user.last_name or ''}")
                bot.send_message(admin, caption, parse_mode="Markdown")
            except:
                pass

        # زيادة عداد الإحالات
        if referral_by:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("UPDATE users SET referral_count=referral_count+1, referral_balance=referral_balance+10 WHERE user_id=?", (referral_by,))
            conn.commit()
            conn.close()
            try:
                bot.send_message(referral_by, f"🎉 مستخدم جديد انضم عن طريق رابطك!\n💰 ربحت 10 نقاط إضافية!")
            except:
                pass

    save_user(user_id,
              username=message.from_user.username or "",
              first_name=message.from_user.first_name or "",
              last_name=message.from_user.last_name or "",
              referral_by=referral_by)

    lang = get_lang(user_id)
    countries = get_all_combos()

    if not countries:
        markup = types.InlineKeyboardMarkup()
        markup.row(
            types.InlineKeyboardButton("📜 التعليمات", callback_data="user_instructions"),
            types.InlineKeyboardButton("🌍 المنصات المتاحة", callback_data="user_platforms")
        )
        markup.row(
            types.InlineKeyboardButton("🌐 تغيير اللغة", callback_data="user_change_lang"),
            types.InlineKeyboardButton("📜 الشروط", callback_data="user_terms")
        )
        markup.row(
            types.InlineKeyboardButton("💰 الإحالات", callback_data="user_referrals"),
            types.InlineKeyboardButton("🧾 حسابي", callback_data="user_account")
        )
        if is_admin(user_id):
            markup.add(types.InlineKeyboardButton("🔐 لوحة الأدمن", callback_data="admin_panel"))
        bot.send_message(message.chat.id, lang['no_countries'], reply_markup=markup)
        return

    welcome_text = f"""🦂 <b>{lang['welcome']}</b>

{lang['choose_country']}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    # إرسال صورة البداية إن وجدت
    start_img = get_setting('bot_start_image', '')
    markup = build_user_main_menu(user_id)

    try:
        if start_img:
            bot.send_photo(message.chat.id, start_img, caption=welcome_text,
                           reply_markup=markup, parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="HTML")

# ======================
# 📜 أزرار المستخدم الجديدة
# ======================
@bot.callback_query_handler(func=lambda call: call.data == "user_instructions")
def user_instructions(call):
    lang = get_lang(call.from_user.id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(lang['instructions'], call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, lang['instructions'], reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "user_platforms")
def user_platforms(call):
    lang = get_lang(call.from_user.id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(lang['platforms'], call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, lang['platforms'], reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "user_terms")
def user_terms(call):
    lang = get_lang(call.from_user.id)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(lang['terms'], call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, lang['terms'], reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "user_change_lang")
def user_change_lang(call):
    lang = get_lang(call.from_user.id)
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🇸🇦 العربية", callback_data="setlang_ar"),
        types.InlineKeyboardButton("🇬🇧 English", callback_data="setlang_en"),
        types.InlineKeyboardButton("🇫🇷 Français", callback_data="setlang_fr")
    )
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(lang['change_lang'], call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, lang['change_lang'], reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("setlang_"))
def set_language(call):
    lang_code = call.data.split("_")[1]
    set_user_language(call.from_user.id, lang_code)
    lang = LANGUAGES.get(lang_code, LANGUAGES['ar'])
    bot.answer_callback_query(call.id, "✅ تم تغيير اللغة!")
    markup = build_user_main_menu(call.from_user.id)
    try:
        bot.edit_message_text(f"🦂 <b>{lang['welcome']}</b>\n\n{lang['choose_country']}\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>",
                              call.message.chat.id, call.message.message_id,
                              reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, lang['welcome'], reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "user_referrals")
def user_referrals(call):
    user_id = call.from_user.id
    lang = get_lang(user_id)
    try:
        bot_info = bot.get_me()
        bot_username = bot_info.username
    except:
        bot_username = "bot"
    refs = get_user_referral_count(user_id)
    user = get_user(user_id)
    bal = user[11] if user and len(user) > 11 else 0

    text = lang['referrals'].format(
        bot_user=bot_username, uid=user_id, refs=refs, bal=bal
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(text, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "user_account")
def user_account(call):
    user_id = call.from_user.id
    lang = get_lang(user_id)
    user = get_user(user_id)
    if not user:
        bot.answer_callback_query(call.id, "❌ لا توجد بيانات!")
        return

    country_code = user[4] or ""
    country_name = ""
    if country_code and country_code in COUNTRY_CODES:
        country_name = f"{COUNTRY_CODES[country_code][1]} {COUNTRY_CODES[country_code][0]}"

    name = f"{user[2] or ''} {user[3] or ''}".strip()
    num = user[5] or "لا يوجد"
    refs = get_user_referral_count(user_id)
    bal = user[11] if len(user) > 11 else 0

    text = lang['my_account'].format(
        uid=user_id, name=name, num=num,
        country=country_name or "غير محددة", refs=refs, bal=bal
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_to_main"))
    try:
        bot.edit_message_text(text, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "back_to_main")
def back_to_main(call):
    lang = get_lang(call.from_user.id)
    markup = build_user_main_menu(call.from_user.id)
    welcome_text = f"""🦂 <b>{lang['welcome']}</b>

{lang['choose_country']}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""
    try:
        bot.edit_message_text(welcome_text, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, welcome_text, reply_markup=markup, parse_mode="HTML")

# ======================
# 🌍 اختيار الدولة والرقم
# ======================
@bot.callback_query_handler(func=lambda call: call.data.startswith("country_"))
def handle_country_selection(call):
    if is_banned(call.from_user.id):
        bot.answer_callback_query(call.id, "🚫 You are banned.", show_alert=True)
        return

    country_code = call.data.split("_", 1)[1]
    country_name, flag = COUNTRY_CODES.get(country_code, ("Unknown", "🌍"))
    available_numbers = get_available_numbers(country_code)

    if not available_numbers:
        bot.answer_callback_query(call.id, "❌ All numbers are currently in use.", show_alert=True)
        return

    selected_number = random.choice(available_numbers)
    user_data = get_user(call.from_user.id)
    if user_data and user_data[5]:
        release_number(user_data[5])

    assign_number_to_user(call.from_user.id, selected_number)
    save_user(call.from_user.id, country_code=country_code, assigned_number=selected_number)

    otp_group_link = get_setting('otp_group_link', 'https://t.me/Alaskey9')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👥 OTP GROUP", url=otp_group_link))
    markup.row(
        types.InlineKeyboardButton("🔄 Change Number", callback_data=f"change_num_{country_code}"),
        types.InlineKeyboardButton("🌍 Change Country", callback_data="back_to_countries")
    )
    markup.add(types.InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_to_main"))

    lang = get_lang(call.from_user.id)
    message_text = f"""
{lang['number']}: <code>{selected_number}</code>
{lang['country']}: {flag} {country_name}
{lang['waiting_otp']}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    try:
        bot.edit_message_text(message_text, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data.startswith("change_num_"))
def change_number(call):
    if is_banned(call.from_user.id):
        return
    country_code = call.data.split("_", 2)[2]
    country_name, flag = COUNTRY_CODES.get(country_code, ("Unknown", "🌍"))
    available_numbers = get_available_numbers(country_code)

    if not available_numbers:
        bot.answer_callback_query(call.id, "❌ All numbers are currently in use.", show_alert=True)
        return

    user_data = get_user(call.from_user.id)
    if user_data and user_data[5]:
        release_number(user_data[5])

    selected_number = random.choice(available_numbers)
    assign_number_to_user(call.from_user.id, selected_number)
    save_user(call.from_user.id, assigned_number=selected_number)

    otp_group_link = get_setting('otp_group_link', 'https://t.me/Alaskey9')
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👥 OTP GROUP", url=otp_group_link))
    markup.row(
        types.InlineKeyboardButton("🔄 Change Number", callback_data=f"change_num_{country_code}"),
        types.InlineKeyboardButton("🌍 Change Country", callback_data="back_to_countries")
    )
    markup.add(types.InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_to_main"))

    lang = get_lang(call.from_user.id)
    message_text = f"""
{lang['number']}: <code>{selected_number}</code>
{lang['country']}: {flag} {country_name}
{lang['waiting_otp']}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    try:
        bot.edit_message_text(message_text, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, message_text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "back_to_countries")
def back_to_countries(call):
    countries = get_all_combos()
    lang = get_lang(call.from_user.id)
    markup = build_user_main_menu(call.from_user.id)
    welcome_text = f"🦂 <b>{lang['choose_country']}</b>\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
    try:
        bot.edit_message_text(welcome_text, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, welcome_text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_subscription(call):
    if check_user_joined(call.from_user.id):
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
        lang = get_lang(call.from_user.id)
        bot.answer_callback_query(call.id, lang['sub_confirmed'])
        send_welcome(call.message)
    else:
        lang = get_lang(call.from_user.id)
        bot.answer_callback_query(call.id, lang['not_subbed'], show_alert=True)

# ============================================================
# 🔐 لوحة تحكم الأدمن الخارقة
# ============================================================
def btn_red(text, cb):
    """زر أحمر - للعمليات الخطيرة"""
    return types.InlineKeyboardButton(f"🔴 {text}", callback_data=cb)

def btn_green(text, cb):
    """زر أخضر - للعمليات الإيجابية"""
    return types.InlineKeyboardButton(f"🟢 {text}", callback_data=cb)

def btn_blue(text, cb):
    """زر أزرق - للمعلومات والإعدادات"""
    return types.InlineKeyboardButton(f"🔵 {text}", callback_data=cb)

def btn_url(text, url):
    return types.InlineKeyboardButton(text, url=url)

def admin_main_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)

    # ─── قسم المستخدمين ───
    markup.add(types.InlineKeyboardButton("👥 ━━ قسم المستخدمين ━━ 👥", callback_data="ignore"))
    markup.row(
        btn_red("حظر مستخدم 🚫", "admin_ban"),
        btn_green("فك حظر ✅", "admin_unban")
    )
    markup.row(
        btn_blue("معلومات مستخدم 👤", "admin_user_info"),
        btn_blue("كومبو برايفت 👤", "admin_private_combo")
    )
    markup.row(
        btn_green("إضافة أدمن ➕", "admin_add_admin"),
        btn_red("إزالة أدمن ➖", "admin_remove_admin")
    )

    # ─── قسم الإذاعات ───
    markup.add(types.InlineKeyboardButton("📢 ━━ قسم الإذاعات ━━ 📢", callback_data="ignore"))
    markup.row(
        btn_blue("إذاعة لمستخدم 📩", "admin_broadcast_user"),
        btn_blue("إذاعة للجميع 📢", "admin_broadcast_all")
    )
    markup.add(btn_blue("إذاعة للجروبات 📡", "admin_broadcast_groups"))

    # ─── قسم القنوات ───
    markup.add(types.InlineKeyboardButton("🔗 ━━ قسم القنوات والاشتراك ━━ 🔗", callback_data="ignore"))
    markup.add(btn_blue("إدارة الاشتراك الإجباري 🔒", "admin_force_sub"))
    markup.row(
        btn_green("إضافة مجموعة ➕", "admin_add_group"),
        btn_red("إزالة مجموعة ➖", "admin_remove_group")
    )

    # ─── قسم الأقسام ───
    markup.add(types.InlineKeyboardButton("📂 ━━ قسم الأقسام والأزرار ━━ 📂", callback_data="ignore"))
    markup.row(
        btn_green("إضافة قسم 📂", "admin_add_combo"),
        btn_red("حذف قسم 🗑️", "admin_del_combo")
    )
    markup.row(
        btn_blue("إدارة الأزرار المخصصة 🔘", "admin_custom_buttons"),
        btn_blue("التحكم باللوحات 🎮", "admin_manage_panels_ui")
    )
    markup.add(btn_blue("إعادة تسمية رينج ✏️", "admin_rename_range"))

    # ─── قسم النظام ───
    markup.add(types.InlineKeyboardButton("⚙️ ━━ قسم النظام ━━ ⚙️", callback_data="ignore"))
    markup.row(
        btn_red("وضع الصيانة 🔧", "admin_toggle_maintenance"),
        btn_red("إعادة تشغيل 🔄", "admin_restart")
    )
    markup.row(
        btn_blue("قياس السرعة ⚡", "admin_speed_test"),
        btn_blue("الإحصائيات 📊", "admin_stats")
    )
    markup.row(
        btn_blue("تعديل زمن التحديث 🔄", "admin_set_refresh"),
        btn_blue("تعديل زمن الكاش ⏰", "admin_set_cache")
    )

    # ─── قسم الصور ───
    markup.add(types.InlineKeyboardButton("🖼️ ━━ قسم الصور والهوية ━━ 🖼️", callback_data="ignore"))
    markup.add(btn_blue("تعيين صور البوت 🖼️", "admin_set_images"))

    # ─── قسم اللوحات و API ───
    markup.add(types.InlineKeyboardButton("🔑 ━━ قسم اللوحات و API ━━ 🔑", callback_data="ignore"))
    markup.row(
        btn_blue("إدارة API Panels 🔑", "admin_api_panels"),
        btn_blue("اللوحات اليدوية 📋", "admin_manual_panels")
    )
    markup.add(btn_green("فحص اللوحات 🖥️", "admin_check_panels"))

    # ─── تقرير ورجوع ───
    markup.add(types.InlineKeyboardButton("━━━━━━━━━━━━━━━━━━━━━━━━", callback_data="ignore"))
    markup.row(
        btn_blue("تقرير شامل 📄", "admin_full_report"),
        btn_green("القائمة الرئيسية 🔙", "back_to_main")
    )

    return markup

@bot.callback_query_handler(func=lambda call: call.data == "ignore")
def ignore_click(call):
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel")
def admin_panel(call):
    if not is_admin(call.from_user.id):
        bot.answer_callback_query(call.id, "🚫 ليس لديك صلاحية!", show_alert=True)
        return

    admin_text = f"""🔐 <b>لوحة تحكم الأدمن</b>

👑 <b>المطور:</b> عسكري
🆔 <b>الأدمن:</b> <code>{call.from_user.id}</code>
👥 <b>إجمالي الأدمنز:</b> {len(get_all_admins())}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    try:
        bot.edit_message_text(admin_text, call.message.chat.id,
                              call.message.message_id,
                              reply_markup=admin_main_menu(), parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, admin_text,
                         reply_markup=admin_main_menu(), parse_mode="HTML")

# ─── قسم المستخدمين ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_ban")
def admin_ban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "ban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("🚫 أدخل ID المستخدم لحظره:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "🚫 أدخل ID المستخدم لحظره:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "ban_user")
def admin_ban_step2(message):
    try:
        uid = int(message.text.strip())
        ban_user(uid)
        bot.reply_to(message, f"✅ تم حظر المستخدم: `{uid}`\n\n👨‍💻 <b>AL ASKRY</b>", parse_mode="HTML")
        try:
            bot.send_message(uid, "🚫 تم حظرك من البوت. تواصل مع الأدمن.")
        except:
            pass
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_unban")
def admin_unban_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "unban_user"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("✅ أدخل ID المستخدم لفك حظره:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "✅ أدخل ID المستخدم لفك حظره:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "unban_user")
def admin_unban_step2(message):
    try:
        uid = int(message.text.strip())
        unban_user(uid)
        bot.reply_to(message, f"✅ تم فك حظر المستخدم: `{uid}`", parse_mode="Markdown")
        try:
            bot.send_message(uid, "✅ تم رفع الحظر عنك. يمكنك استخدام البوت الآن!")
        except:
            pass
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_user_info")
def admin_user_info_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "get_user_info"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("👤 أدخل ID المستخدم:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "👤 أدخل ID المستخدم:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "get_user_info")
def admin_user_info_step2(message):
    try:
        uid = int(message.text.strip())
        user = get_user(uid)
        if not user:
            bot.reply_to(message, "❌ المستخدم غير موجود!")
        else:
            status = "🚫 محظور" if user[6] else "✅ نشط"
            refs = get_user_referral_count(uid)
            info = f"""👤 <b>معلومات المستخدم:</b>

🆔 ID: <code>{user[0]}</code>
👤 يوزر: @{user[1] or 'N/A'}
📛 الاسم: {user[2] or ''} {user[3] or ''}
📞 رقمه الحالي: <code>{user[5] or 'لا يوجد'}</code>
🌍 كود الدولة: {user[4] or 'N/A'}
🔒 الحالة: {status}
🔗 إحالاته: {refs}
🗓️ تاريخ الانضمام: {user[12] if len(user) > 12 else 'N/A'}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b>"""
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton("🚫 حظر", callback_data=f"quick_ban_{uid}"),
                types.InlineKeyboardButton("✅ فك حظر", callback_data=f"quick_unban_{uid}")
            )
            bot.reply_to(message, info, parse_mode="HTML", reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {e}")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data.startswith("quick_ban_"))
def quick_ban(call):
    if not is_admin(call.from_user.id): return
    uid = int(call.data.split("_")[2])
    ban_user(uid)
    bot.answer_callback_query(call.id, f"✅ تم حظر {uid}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("quick_unban_"))
def quick_unban(call):
    if not is_admin(call.from_user.id): return
    uid = int(call.data.split("_")[2])
    unban_user(uid)
    bot.answer_callback_query(call.id, f"✅ تم فك حظر {uid}")

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_admin")
def admin_add_admin_step1(call):
    if not is_owner(call.from_user.id):
        bot.answer_callback_query(call.id, "🚫 فقط المالك يمكنه إضافة أدمن!", show_alert=True)
        return
    user_states[call.from_user.id] = "add_admin"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("➕ أدخل ID المستخدم لترقيته أدمن:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "➕ أدخل ID المستخدم لترقيته أدمن:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_admin")
def admin_add_admin_step2(message):
    try:
        uid = int(message.text.strip())
        add_admin(uid, message.from_user.id)
        bot.reply_to(message, f"✅ تم إضافة `{uid}` كأدمن!", parse_mode="Markdown")
        try:
            bot.send_message(uid, "🎉 تهانينا! تمت ترقيتك أدمن في البوت.\n\n👨‍💻 <b>AL ASKRY</b>", parse_mode="HTML")
        except:
            pass
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_admin")
def admin_remove_admin_step1(call):
    if not is_owner(call.from_user.id):
        bot.answer_callback_query(call.id, "🚫 فقط المالك!", show_alert=True)
        return
    admins = get_all_admins()
    markup = types.InlineKeyboardMarkup()
    for adm in admins:
        if adm != OWNER_ID:
            markup.add(types.InlineKeyboardButton(f"➖ {adm}", callback_data=f"remove_adm_{adm}"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("➖ اختر الأدمن لإزالته:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "➖ اختر الأدمن لإزالته:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("remove_adm_"))
def remove_admin_confirm(call):
    if not is_owner(call.from_user.id): return
    uid = int(call.data.split("_")[2])
    remove_admin(uid)
    bot.answer_callback_query(call.id, f"✅ تم إزالة {uid} من الأدمنز")

# ─── قسم الإذاعات ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_all")
def admin_broadcast_all_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_all"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("📢 أرسل الرسالة للإذاعة لجميع المستخدمين:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "📢 أرسل الرسالة:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_all")
def admin_broadcast_all_step2(message):
    users = get_all_users()
    success = 0
    broadcast_text = message.text + f"\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
    for uid in users:
        try:
            bot.send_message(uid, broadcast_text, parse_mode="HTML")
            success += 1
        except:
            pass
    bot.reply_to(message, f"✅ تم الإرسال: {success}/{len(users)} مستخدم")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_user")
def admin_broadcast_user_step1(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_user_id"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("📩 أدخل ID المستخدم:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "📩 أدخل ID المستخدم:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_user_id")
def admin_broadcast_user_step2(message):
    try:
        uid = int(message.text.strip())
        user_states[message.from_user.id] = f"broadcast_msg_{uid}"
        bot.reply_to(message, "📝 أرسل الرسالة الآن:")
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")
        if message.from_user.id in user_states:
            del user_states[message.from_user.id]

@bot.message_handler(func=lambda msg: str(user_states.get(msg.from_user.id, "")).startswith("broadcast_msg_"))
def admin_broadcast_user_step3(message):
    uid = int(user_states[message.from_user.id].split("_")[2])
    try:
        send_text = message.text + f"\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
        bot.send_message(uid, send_text, parse_mode="HTML")
        bot.reply_to(message, f"✅ تم الإرسال للمستخدم {uid}")
    except Exception as e:
        bot.reply_to(message, f"❌ فشل: {e}")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_broadcast_groups")
def admin_broadcast_groups(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "broadcast_groups"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("📡 أرسل الرسالة للإذاعة للجروبات:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "📡 أرسل الرسالة:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "broadcast_groups")
def admin_broadcast_groups_step2(message):
    success = 0
    for chat_id in CHAT_IDS:
        try:
            send_text = message.text + f"\n\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
            bot.send_message(chat_id, send_text, parse_mode="HTML")
            success += 1
        except:
            pass
    bot.reply_to(message, f"✅ تم الإرسال لـ {success} جروب")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

# ─── قسم القنوات والاشتراك ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_force_sub")
def admin_force_sub(call):
    if not is_admin(call.from_user.id): return
    current = is_force_sub_enabled()
    if current:
        set_setting("force_sub", "off")
        bot.answer_callback_query(call.id, "❌ تم تعطيل الاشتراك الإجباري")
        status = "❌ معطل"
    else:
        set_setting("force_sub", "on")
        bot.answer_callback_query(call.id, "✅ تم تفعيل الاشتراك الإجباري")
        status = "✅ مفعل"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text(f"🔒 حالة الاشتراك الإجباري: {status}", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "admin_add_group")
def admin_add_group(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_group"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("➕ أرسل ID الجروب (مثال: -1001234567890):", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "➕ أرسل ID الجروب:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_group")
def admin_add_group_step2(message):
    group_id = message.text.strip()
    if group_id not in CHAT_IDS:
        CHAT_IDS.append(group_id)
        bot.reply_to(message, f"✅ تم إضافة الجروب: `{group_id}`\n⚠️ ملاحظة: يُحفظ مؤقتاً في الجلسة الحالية.", parse_mode="Markdown")
    else:
        bot.reply_to(message, "⚠️ الجروب موجود بالفعل!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_remove_group")
def admin_remove_group(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    for gid in CHAT_IDS:
        markup.add(types.InlineKeyboardButton(f"➖ {gid}", callback_data=f"rm_group_{gid}"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("➖ اختر الجروب لإزالته:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "➖ اختر الجروب:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_group_"))
def remove_group_confirm(call):
    if not is_admin(call.from_user.id): return
    gid = call.data[9:]
    if gid in CHAT_IDS:
        CHAT_IDS.remove(gid)
    bot.answer_callback_query(call.id, f"✅ تم إزالة الجروب {gid}")

# ─── قسم النظام ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_toggle_maintenance")
def admin_toggle_maintenance(call):
    if not is_admin(call.from_user.id): return
    current = is_maintenance()
    if current:
        set_setting("maintenance", "off")
        bot.answer_callback_query(call.id, "✅ تم إيقاف وضع الصيانة")
        status = "✅ إيقاف"
    else:
        set_setting("maintenance", "on")
        bot.answer_callback_query(call.id, "🔧 تم تفعيل وضع الصيانة")
        status = "🔧 مفعل"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text(f"🔧 وضع الصيانة: {status}", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        pass

@bot.callback_query_handler(func=lambda call: call.data == "admin_restart")
def admin_restart(call):
    if not is_admin(call.from_user.id): return
    bot.answer_callback_query(call.id, "🔄 جاري إعادة التشغيل...")
    bot.send_message(call.message.chat.id, "🔄 <b>إعادة تشغيل البوت...</b>\n\n👨‍💻 <b>AL ASKRY</b>", parse_mode="HTML")
    os.execv(__file__, ['python'] + [__file__])

@bot.callback_query_handler(func=lambda call: call.data == "admin_speed_test")
def admin_speed_test(call):
    if not is_admin(call.from_user.id): return
    start = time.time()
    try:
        requests.get("https://api.telegram.org", timeout=5)
        ping = round((time.time() - start) * 1000)
        result = f"⚡ <b>اختبار السرعة:</b>\n\n📡 Ping: {ping}ms\n✅ الاتصال: جيد\n\n👨‍💻 <b>AL ASKRY</b>"
    except:
        result = "❌ فشل اختبار الاتصال"

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text(result, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, result, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_refresh")
def admin_set_refresh(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "set_refresh"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    current = get_setting('refresh_interval', str(REFRESH_INTERVAL))
    try:
        bot.edit_message_text(f"🔄 زمن التحديث الحالي: {current} ثانية\nأدخل الزمن الجديد (بالثواني):", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "🔄 أدخل زمن التحديث:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "set_refresh")
def admin_set_refresh_step2(message):
    try:
        val = int(message.text.strip())
        if val < 1: val = 1
        set_setting('refresh_interval', str(val))
        global REFRESH_INTERVAL
        REFRESH_INTERVAL = val
        bot.reply_to(message, f"✅ تم تعديل زمن التحديث إلى {val} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صحيحة!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_set_cache")
def admin_set_cache(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "set_cache"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    current = get_setting('cache_time', '60')
    try:
        bot.edit_message_text(f"⏰ زمن الكاش الحالي: {current} ثانية\nأدخل الزمن الجديد:", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "⏰ أدخل زمن الكاش:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "set_cache")
def admin_set_cache_step2(message):
    try:
        val = int(message.text.strip())
        set_setting('cache_time', str(val))
        bot.reply_to(message, f"✅ تم تعديل زمن الكاش إلى {val} ثانية")
    except:
        bot.reply_to(message, "❌ قيمة غير صحيحة!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

# ─── قسم الأقسام والأزرار ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_add_combo")
def admin_add_combo(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "waiting_combo_file"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("📤 أرسل ملف الكومبو بصيغة TXT أو أرسل الأرقام مباشرة:", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "📤 أرسل ملف الكومبو:", reply_markup=markup)

@bot.message_handler(content_types=['document'])
def handle_combo_file(message):
    if not is_admin(message.from_user.id): return
    if user_states.get(message.from_user.id) != "waiting_combo_file": return

    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        content = downloaded_file.decode('utf-8', errors='ignore')

        all_phone_numbers = []
        for line in content.splitlines():
            line = line.strip()
            if not line: continue
            # إزالة كل ما ليس أرقام أو +
            clean_line = re.sub(r'[^\d\+]', '', line)
            # إذا كان يبدأ بـ + نحذف علامة + فقط ونحتفظ بالأرقام
            if clean_line.startswith('+'):
                clean_line = clean_line[1:]
            # نبحث عن أرقام بطول 7 إلى 15
            numbers = re.findall(r'\d{7,15}', clean_line)
            for phone in numbers:
                # نحذف الصفر فقط إذا كان الرقم يبدأ بصفر واحد وليس برمز دولة
                # (أي إذا كان رقماً محلياً مثل 0512345678)
                if phone.startswith('00'):
                    phone = phone[2:]  # حذف 00 من بداية الأرقام الدولية
                elif phone.startswith('0') and len(phone) <= 11:
                    phone = phone[1:]  # حذف الصفر المحلي فقط للأرقام القصيرة
                # إذا كان الرقم طويلاً (12+ رقم) يبدأ بصفر، نحتفظ به كما هو
                if len(phone) >= 7:
                    all_phone_numbers.append(phone)

        if not all_phone_numbers:
            bot.reply_to(message, "❌ لم أعثر على أرقام هواتف في الملف!")
            if message.from_user.id in user_states:
                del user_states[message.from_user.id]
            return

        country_code = None
        country_name = "غير معروف"
        country_flag = "🌍"

        sample_numbers = all_phone_numbers[:20]
        sorted_codes = sorted(COUNTRY_CODES.keys(), key=len, reverse=True)
        code_counts = {}

        for phone in sample_numbers:
            for code in sorted_codes:
                if phone.startswith(code):
                    code_counts[code] = code_counts.get(code, 0) + 1
                    break

        if code_counts:
            sorted_counts = sorted(code_counts.items(), key=lambda x: x[1], reverse=True)
            winning_code, win_count = sorted_counts[0]
            if win_count >= len(sample_numbers) * 0.3:
                country_code = winning_code
                country_name, country_flag = COUNTRY_CODES.get(winning_code, ("غير معروف", "🌍"))

        if not country_code:
            bot.reply_to(message, "❌ فشل تحديد الدولة! تأكد أن الأرقام تحتوي على كود دولة.")
            if message.from_user.id in user_states:
                del user_states[message.from_user.id]
            return

        save_combo(country_code, all_phone_numbers)

        success_msg = f"""✅ <b>تم حفظ الكومبو بنجاح!</b>

{country_flag} <b>الدولة:</b> {country_name}
📞 <b>كود الدولة:</b> +{country_code}
🔢 <b>عدد الأرقام:</b> {len(all_phone_numbers)}
🕒 <b>الوقت:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b>"""
        bot.reply_to(message, success_msg, parse_mode="HTML")
        if message.from_user.id in user_states:
            del user_states[message.from_user.id]

    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {str(e)}")
        if message.from_user.id in user_states:
            del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_del_combo")
def admin_del_combo(call):
    if not is_admin(call.from_user.id): return
    combos = get_all_combos()
    if not combos:
        bot.answer_callback_query(call.id, "❌ لا توجد كومبوهات!", show_alert=True)
        return

    markup = types.InlineKeyboardMarkup()
    for code in combos:
        if code in COUNTRY_CODES:
            name, flag = COUNTRY_CODES[code]
            markup.add(types.InlineKeyboardButton(f"{flag} {name}", callback_data=f"del_combo_{code}"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))

    try:
        bot.edit_message_text("🗑️ اختر الكومبو لحذفه:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "🗑️ اختر الكومبو:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("del_combo_"))
def confirm_del_combo(call):
    if not is_admin(call.from_user.id): return
    code = call.data.split("_", 2)[2]
    delete_combo(code)
    if code in COUNTRY_CODES:
        name, flag = COUNTRY_CODES[code]
        msg = f"✅ تم حذف: {flag} {name}"
    else:
        msg = f"✅ تم حذف: {code}"
    bot.answer_callback_query(call.id, msg)

@bot.callback_query_handler(func=lambda call: call.data == "admin_rename_range")
def admin_rename_range(call):
    if not is_admin(call.from_user.id): return
    combos = get_all_combos()
    markup = types.InlineKeyboardMarkup()
    for code in combos:
        name = get_combo_name(code)
        markup.add(types.InlineKeyboardButton(name, callback_data=f"rename_{code}"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("✏️ اختر الرينج لتغيير اسمه:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "✏️ اختر الرينج:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rename_"))
def rename_range(call):
    if not is_admin(call.from_user.id): return
    code = call.data.split("_", 1)[1]
    user_states[call.from_user.id] = f"rename_range_{code}"
    bot.send_message(call.from_user.id, "✏️ أرسل الاسم الجديد للرينج:")

@bot.message_handler(func=lambda m: str(user_states.get(m.from_user.id, "")).startswith("rename_range_"))
def rename_range_save(message):
    code = user_states[message.from_user.id].split("_", 2)[2]
    new_name = message.text.strip()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE combos SET custom_name=? WHERE country_code=?", (new_name, code))
    conn.commit()
    conn.close()
    bot.reply_to(message, f"✅ تم تغيير اسم الرينج إلى: <b>{new_name}</b>", parse_mode="HTML")
    del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_custom_buttons")
def admin_custom_buttons(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("➕ إضافة زر", callback_data="add_custom_btn"),
        types.InlineKeyboardButton("🗑️ حذف زر", callback_data="del_custom_btn")
    )
    markup.add(types.InlineKeyboardButton("📋 عرض الأزرار", callback_data="list_custom_btn"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("🔘 <b>إدارة الأزرار المخصصة:</b>", call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, "🔘 إدارة الأزرار:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "add_custom_btn")
def add_custom_btn(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_custom_btn"
    bot.send_message(call.from_user.id, "🔘 أرسل بيانات الزر بالشكل:\nالنص | الرابط\n\nمثال: 📢 قناتنا | https://t.me/channel")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_custom_btn")
def add_custom_btn_step2(message):
    try:
        parts = message.text.split("|")
        if len(parts) != 2:
            bot.reply_to(message, "❌ الشكل خاطئ! المطلوب: النص | الرابط")
            return
        label = parts[0].strip()
        url = parts[1].strip()
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO custom_buttons (label, url) VALUES (?, ?)", (label, url))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"✅ تم إضافة الزر: <b>{label}</b>", parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {e}")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "list_custom_btn")
def list_custom_btn(call):
    if not is_admin(call.from_user.id): return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, label, url FROM custom_buttons")
    btns = c.fetchall()
    conn.close()
    if not btns:
        bot.answer_callback_query(call.id, "لا توجد أزرار مخصصة!")
        return
    text = "📋 <b>الأزرار المخصصة:</b>\n\n"
    for btn in btns:
        text += f"🔘 ID:{btn[0]} | {btn[1]} → {btn[2]}\n"
    text += "\n👨‍💻 <b>AL ASKRY</b>"
    bot.send_message(call.message.chat.id, text, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "del_custom_btn")
def del_custom_btn(call):
    if not is_admin(call.from_user.id): return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, label FROM custom_buttons")
    btns = c.fetchall()
    conn.close()
    markup = types.InlineKeyboardMarkup()
    for btn in btns:
        markup.add(types.InlineKeyboardButton(f"🗑️ {btn[1]}", callback_data=f"rm_btn_{btn[0]}"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="admin_custom_buttons"))
    try:
        bot.edit_message_text("🗑️ اختر الزر لحذفه:", call.message.chat.id,
                              call.message.message_id, reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, "🗑️ اختر الزر:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("rm_btn_"))
def rm_btn(call):
    if not is_admin(call.from_user.id): return
    bid = int(call.data.split("_")[2])
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM custom_buttons WHERE id=?", (bid,))
    conn.commit()
    conn.close()
    bot.answer_callback_query(call.id, "✅ تم حذف الزر!")

@bot.callback_query_handler(func=lambda call: call.data == "admin_manage_panels_ui")
def admin_manage_panels_ui(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📊 الإحصائيات", callback_data="admin_stats"),
        types.InlineKeyboardButton("📄 تقرير شامل", callback_data="admin_full_report")
    )
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("🎮 <b>التحكم باللوحات:</b>", call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, "🎮 التحكم باللوحات", reply_markup=markup)

# ─── قسم الصور والهوية ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_set_images")
def admin_set_images(call):
    if not is_admin(call.from_user.id): return
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🖼️ صورة Start", callback_data="set_img_start"))
    markup.add(types.InlineKeyboardButton("🖼️ صورة الأقسام", callback_data="set_img_sections"))
    markup.add(types.InlineKeyboardButton("🖼️ صورة القنوات", callback_data="set_img_channels"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("🖼️ <b>تعيين صور البوت:</b>", call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, "🖼️ تعيين الصور:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("set_img_"))
def set_img(call):
    if not is_admin(call.from_user.id): return
    img_type = call.data.split("_", 2)[2]
    user_states[call.from_user.id] = f"set_image_{img_type}"
    bot.send_message(call.from_user.id, f"📸 أرسل الصورة الخاصة بـ {img_type} (كـ file_id أو رابط URL):")

@bot.message_handler(func=lambda msg: str(user_states.get(msg.from_user.id, "")).startswith("set_image_"))
def set_img_step2(message):
    img_type = user_states[message.from_user.id].split("_", 2)[2]
    img_value = message.text.strip()
    set_setting(f"bot_{img_type}_image", img_value)
    bot.reply_to(message, f"✅ تم تعيين صورة {img_type} بنجاح!")
    del user_states[message.from_user.id]

# ─── قسم اللوحات والـ API ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_api_panels")
def admin_api_panels(call):
    if not is_admin(call.from_user.id): return
    panels_text = "🔑 <b>API Panels الحالية:</b>\n\n"
    for i, panel in enumerate(API_PANELS, 1):
        panels_text += f"{i}. {panel['url'][:50]}...\n"
    panels_text += f"\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("➕ إضافة Panel", callback_data="add_api_panel"))
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text(panels_text, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, panels_text, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "add_api_panel")
def add_api_panel(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_api_panel"
    bot.send_message(call.from_user.id, "🔑 أرسل بيانات الـ API Panel بالشكل:\nURL | TOKEN")

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_api_panel")
def add_api_panel_step2(message):
    try:
        parts = message.text.split("|")
        if len(parts) != 2:
            bot.reply_to(message, "❌ الشكل خاطئ! URL | TOKEN")
            return
        url = parts[0].strip()
        token = parts[1].strip()
        API_PANELS.append({"url": url, "token": token})
        bot.reply_to(message, f"✅ تم إضافة API Panel:\n{url}")
    except Exception as e:
        bot.reply_to(message, f"❌ خطأ: {e}")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_manual_panels")
def admin_manual_panels(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "add_manual_panel"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("📋 <b>اللوحات اليدوية:</b>\nأرسل الأرقام يدوياً (سطر لكل رقم):", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, "📋 أرسل الأرقام:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "add_manual_panel")
def add_manual_panel_step2(message):
    numbers = [line.strip() for line in message.text.splitlines() if line.strip()]
    if not numbers:
        bot.reply_to(message, "❌ لا توجد أرقام!")
        return
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO manual_panels (name, numbers) VALUES (?, ?)",
              (f"Panel_{datetime.now().strftime('%H%M')}", json.dumps(numbers)))
    conn.commit()
    conn.close()
    bot.reply_to(message, f"✅ تم إضافة {len(numbers)} رقم يدوياً!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

@bot.callback_query_handler(func=lambda call: call.data == "admin_check_panels")
def admin_check_panels(call):
    if not is_admin(call.from_user.id): return
    bot.answer_callback_query(call.id, "⏳ جاري الفحص...")
    results = "🖥️ <b>فحص اللوحات:</b>\n\n"
    for i, panel in enumerate(API_PANELS, 1):
        try:
            start = time.time()
            params = {'token': panel['token'], 'records': 1}
            resp = requests.get(panel['url'], params=params, timeout=10)
            ping = round((time.time() - start) * 1000)
            data = resp.json()
            status = "🟢 يعمل" if data.get('status') != 'error' else "🔴 خطأ"
            results += f"{i}. {status} | Ping: {ping}ms\n"
        except:
            results += f"{i}. 🔴 لا يستجيب\n"
    results += f"\n━━━━━━━━━━━━━━━\n👨‍💻 <b>AL ASKRY</b>"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text(results, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, results, reply_markup=markup, parse_mode="HTML")

# ─── كومبو برايفت ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_private_combo")
def admin_private_combo(call):
    if not is_admin(call.from_user.id): return
    user_states[call.from_user.id] = "private_combo_uid"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))
    try:
        bot.edit_message_text("👤 <b>كومبو برايفت:</b>\nأدخل ID المستخدم لتعيين كومبو خاص له:", 
                              call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, "👤 أدخل ID:", reply_markup=markup)

@bot.message_handler(func=lambda msg: user_states.get(msg.from_user.id) == "private_combo_uid")
def private_combo_uid(message):
    try:
        uid = int(message.text.strip())
        user_states[message.from_user.id] = f"private_combo_nums_{uid}"
        bot.reply_to(message, f"📞 الآن أرسل الأرقام الخاصة بالمستخدم {uid} (سطر لكل رقم):")
    except:
        bot.reply_to(message, "❌ ID غير صحيح!")
        if message.from_user.id in user_states:
            del user_states[message.from_user.id]

@bot.message_handler(func=lambda msg: str(user_states.get(msg.from_user.id, "")).startswith("private_combo_nums_"))
def private_combo_nums(message):
    uid = int(user_states[message.from_user.id].split("_")[3])
    numbers = [line.strip() for line in message.text.splitlines() if line.strip()]
    if numbers:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("UPDATE users SET private_combo_country=? WHERE user_id=?",
                  (json.dumps(numbers), uid))
        conn.commit()
        conn.close()
        bot.reply_to(message, f"✅ تم تعيين {len(numbers)} رقم كومبو برايفت للمستخدم {uid}!")
        try:
            bot.send_message(uid, "🎉 تم تعيين أرقام خاصة لك في البوت!\n\n👨‍💻 <b>AL ASKRY</b>", parse_mode="HTML")
        except:
            pass
    else:
        bot.reply_to(message, "❌ لا توجد أرقام!")
    if message.from_user.id in user_states:
        del user_states[message.from_user.id]

# ─── الإحصائيات والتقارير ───
@bot.callback_query_handler(func=lambda call: call.data == "admin_stats")
def admin_stats(call):
    if not is_admin(call.from_user.id): return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users WHERE is_banned=0")
    active_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM users WHERE is_banned=1")
    banned_users = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM otp_logs")
    total_otp = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM otp_logs WHERE date(timestamp) = date('now')")
    today_otp = c.fetchone()[0]
    conn.close()

    combos = get_all_combos()
    total_numbers = sum(len(get_combo(code)) for code in combos)
    token_valid = crapi.check_token_valid()
    api_status = "🟢 نشط" if token_valid else "🔴 غير نشط"
    maintenance = "🔧 مفعل" if is_maintenance() else "✅ إيقاف"
    force_sub = "✅ مفعل" if is_force_sub_enabled() else "❌ معطل"

    stats_msg = f"""📊 <b>إحصائيات البوت الكاملة:</b>

👥 <b>المستخدمون:</b>
  • نشطون: {active_users}
  • محظورون: {banned_users}
  • الإجمالي: {active_users + banned_users}

🌐 <b>الكومبوهات:</b>
  • الدول المضافة: {len(combos)}
  • إجمالي الأرقام: {total_numbers}

🔑 <b>OTP:</b>
  • الإجمالي: {total_otp}
  • اليوم: {today_otp}

⚙️ <b>النظام:</b>
  • حالة API: {api_status}
  • الصيانة: {maintenance}
  • الاشتراك الإجباري: {force_sub}
  • الأدمنز: {len(get_all_admins())}

━━━━━━━━━━━━━━━
👨‍💻 <b>AL ASKRY</b> | <a href='https://t.me/askry47'>@askry47</a>"""

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 لوحة الأدمن", callback_data="admin_panel"))

    try:
        bot.edit_message_text(stats_msg, call.message.chat.id,
                              call.message.message_id, reply_markup=markup, parse_mode="HTML")
    except:
        bot.send_message(call.message.chat.id, stats_msg, reply_markup=markup, parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: call.data == "admin_full_report")
def admin_full_report(call):
    if not is_admin(call.from_user.id): return
    try:
        report = "📊 تقرير شامل - AL ASKRY Bot\n" + "="*50 + "\n\n"
        report += f"⏰ التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()

        report += f"👥 المستخدمون ({len(users)}):\n"
        for u in users:
            status = "محظور" if u[6] else "نشط"
            report += f"ID:{u[0]} | @{u[1] or 'N/A'} | {u[2] or ''} {u[3] or ''} | رقم:{u[5] or 'N/A'} | {status}\n"

        report += "\n" + "="*50 + "\n\n"
        c.execute("SELECT * FROM otp_logs ORDER BY id DESC LIMIT 100")
        logs = c.fetchall()
        report += f"🔑 سجل OTP ({len(logs)} آخر):\n"
        for log in logs:
            report += f"رقم:{log[2]} | OTP:{log[5]} | خدمة:{log[7]} | وقت:{log[10]}\n"

        conn.close()
        report += "\n" + "="*50 + "\n👨‍💻 AL ASKRY - @askry47"

        with open("bot_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        with open("bot_report.txt", "rb") as f:
            bot.send_document(call.from_user.id, f, caption="📊 التقرير الشامل\n\n👨‍💻 AL ASKRY")
        os.remove("bot_report.txt")
        bot.answer_callback_query(call.id, "✅ تم إرسال التقرير!")
    except Exception as e:
        bot.answer_callback_query(call.id, f"❌ خطأ: {e}")

# ======================
# 🔄 الحلقة الرئيسية
# ======================
def api_main_loop():
    print("=" * 60)
    print("🚀 بدء تشغيل بوت AL ASKRY OTP V2")
    print(f"👑 المالك: {OWNER_ID}")
    print(f"👥 الأدمنز: {len(get_all_admins())}")
    print(f"📢 القناة: {CHAT_IDS[0]}")
    print(f"🔗 API: {API_URL}")
    print(f"👨‍💻 المطور: عسكري | @askry47")
    print("=" * 60)

    processed_messages = set()
    error_count = 0

    while True:
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            interval = int(get_setting('refresh_interval', str(REFRESH_INTERVAL)))

            if error_count > 10:
                print("⚠️ عدد الأخطاء تجاوز الحد، انتظار دقيقة...")
                time.sleep(60)
                error_count = 0
                continue

            if is_maintenance():
                time.sleep(interval)
                continue

            print(f"[{current_time}] 🔍 جلب الرسائل...")
            messages = crapi.fetch_messages(records=100, hours_back=1)

            if isinstance(messages, list):
                new_count = 0
                for msg in messages:
                    if not isinstance(msg, dict): continue
                    msg_key = f"{msg.get('dt')}_{msg.get('num')}_{hash(msg.get('message', ''))}"
                    if msg_key not in processed_messages:
                        try:
                            if process_and_send_message(msg):
                                new_count += 1
                            processed_messages.add(msg_key)
                        except Exception as e:
                            print(f"❌ خطأ في معالجة رسالة: {e}")
                if new_count > 0:
                    print(f"✅ تم إرسال {new_count} رسالة جديدة")
                else:
                    print(f"[{current_time}] ⏭️ لا جديد")
                error_count = 0
            else:
                error_count += 1

            if len(processed_messages) > 1000:
                processed_messages = set(list(processed_messages)[-500:])

        except KeyboardInterrupt:
            print("\n⛔ إيقاف...")
            break
        except requests.exceptions.RequestException as e:
            print(f"❌ خطأ شبكة: {e}")
            error_count += 1
            time.sleep(30)
        except Exception as e:
            print(f"❌ خطأ: {e}")
            traceback.print_exc()
            error_count += 1

        time.sleep(interval)

# ======================
# ▶️ تشغيل البوت
# ======================
def run_bot():
    print("[🤖] تشغيل بوت التليجرام...")
    while True:
        try:
            bot.polling(none_stop=True, timeout=60)
        except KeyboardInterrupt:
            print("\n⛔ إيقاف...")
            break
        except Exception as e:
            print(f"❌ خطأ في البوت: {e}")
            time.sleep(10)

def keep_alive_ping():
    while True:
        try:
            bot.get_me()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ♻️ Ping OK")
        except Exception as e:
            print(f"⚠️ Ping فشل: {e}")
        time.sleep(300)

# ======================
# 🚀 التشغيل الرئيسي
# ======================
if __name__ == "__main__":
    print("=" * 60)
    print("📋 AL ASKRY OTP Bot V2 - إعداد التشغيل")
    print(f"👑 المالك: {OWNER_ID}")
    print(f"📢 القناة: {CHAT_IDS[0]}")
    print(f"📢 القناة 1: {CHANNEL_1_URL}")
    print(f"📢 القناة 2: {CHANNEL_2_URL}")
    print(f"👨‍💻 المطور: عسكري | @askry47")
    print("=" * 60)

    try:
        bot_thread = threading.Thread(target=run_bot, daemon=True, name="TelegramBot")
        bot_thread.start()
        print("✅ ثريد البوت بدأ")
        time.sleep(5)

        ping_thread = threading.Thread(target=keep_alive_ping, daemon=True, name="KeepAlivePing")
        ping_thread.start()
        print("✅ ثريد Ping بدأ")

        api_main_loop()

    except KeyboardInterrupt:
        print("\n\n⛔ تم الإيقاف")
    except Exception as e:
        print(f"\n\n💥 خطأ رئيسي: {e}")
        traceback.print_exc()
    finally:
        print("🔄 إنهاء...")
