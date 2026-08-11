# -*- coding: utf-8 -*-

import requests
import json
import random
import time
import html
import urllib.parse
import traceback

# ============================================================
# COUNTRY DETAILS TELEGRAM BOT
# FULL SINGLE-FILE CODE (EXACT FORMAT MATCH)
# ============================================================

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"
REST_COUNTRIES_KEY = "rc_live_317037a7db864904b9a3695f31b68e57"

TELEGRAM_API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"
COUNTRIES_API = "https://api.restcountries.com/countries/v5"

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "CountryDetailsBot/5.0"})

USER_STATE = {}

# ------------------------------------------------------------
# BENGALI NUMBER CONVERTER
# ------------------------------------------------------------

def to_bn_digits(number_str):
    en_to_bn = {
        '0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪',
        '5': '৫', '6': '৬', '7': '৭', '8': '৮', '9': '৯'
    }
    return "".join(en_to_bn.get(ch, ch) for ch in str(number_str))

# ------------------------------------------------------------
# TELEGRAM & API REQUESTS
# ------------------------------------------------------------

def telegram_request(method, data=None):
    try:
        response = SESSION.post(TELEGRAM_API + method, data=data or {}, timeout=60)
        try:
            return response.json()
        except Exception:
            return {"ok": False, "status": response.status_code, "text": response.text}
    except Exception as e:
        print("Telegram error:", e)
        return None

def country_request(country):
    try:
        encoded_country = urllib.parse.quote(country, safe="")
        url = COUNTRIES_API + "/names.common/" + encoded_country
        headers = {"Authorization": "Bearer " + REST_COUNTRIES_KEY.strip()}
        response = SESSION.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        result = response.json()
        objects = result.get("data", {}).get("objects", [])
        if not objects:
            return None
        return objects[0]
    except Exception as e:
        print("Country API error:", e)
        return None

def send_message(chat_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id, 
        "text": text, 
        "parse_mode": "HTML", 
        "disable_web_page_preview": True
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    else:
        payload["reply_markup"] = json.dumps({"remove_keyboard": True})
    return telegram_request("sendMessage", payload)

def edit_message(chat_id, message_id, text, reply_markup=None):
    payload = {
        "chat_id": chat_id, 
        "message_id": message_id, 
        "text": text, 
        "parse_mode": "HTML", 
        "disable_web_page_preview": True
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup
    return telegram_request("editMessageText", payload)

def answer_callback(callback_id):
    return telegram_request("answerCallbackQuery", {"callback_query_id": callback_id})

def safe_text(value):
    if value is None:
        return ""
    return html.escape(str(value), quote=False)

# ------------------------------------------------------------
# DATABASE & DATA BANKS
# ------------------------------------------------------------

COUNTRY_ALIASES = {
    "bd": "Bangladesh", "bangladesh": "Bangladesh",
    "in": "India", "india": "India",
    "us": "United States", "usa": "United States", "america": "United States", "united states": "United States",
    "ae": "United Arab Emirates", "uae": "United Arab Emirates", "dubai": "United Arab Emirates",
    "oman": "Oman", "om": "Oman",
    "qatar": "Qatar", "qa": "Qatar",
    "iran": "Iran", "ir": "Iran",
    "spain": "Spain", "es": "Spain",
    "japan": "Japan", "jp": "Japan",
    "china": "China", "cn": "China",
    "pakistan": "Pakistan", "pakistan": "Pakistan",
    "malaysia": "Malaysia", "my": "Malaysia",
    "singapore": "Singapore", "sg": "Singapore",
    "canada": "Canada", "ca": "Canada",
    "australia": "Australia", "au": "Australia",
    "germany": "Germany", "de": "Germany",
    "france": "France", "fr": "France",
    "italy": "Italy", "it": "Italy",
    "portugal": "Portugal", "pt": "Portugal",
    "turkey": "Turkey", "tr": "Turkey",
    "nepal": "Nepal", "np": "Nepal",
    "sri lanka": "Sri Lanka", "lk": "Sri Lanka",
    "brazil": "Brazil", "br": "Brazil",
    "mexico": "Mexico", "mx": "Mexico",
    "south africa": "South Africa", "za": "South Africa",
    "saudi arabia": "Saudi Arabia", "sa": "Saudi Arabia",
    "kuwait": "Kuwait", "kw": "Kuwait",
    "bahrain": "Bahrain", "bh": "Bahrain",
    "indonesia": "Indonesia", "id": "Indonesia",
    "thailand": "Thailand", "th": "Thailand",
    "south korea": "South Korea", "kr": "South Korea",
    "new zealand": "New Zealand", "nz": "New Zealand",
    "russia": "Russia", "ru": "Russia",
    "netherlands": "Netherlands", "nl": "Netherlands",
    "belgium": "Belgium", "be": "Belgium",
    "switzerland": "Switzerland", "ch": "Switzerland",
    "sweden": "Sweden", "se": "Sweden",
    "norway": "Norway", "no": "Norway",
    "denmark": "Denmark", "dk": "Denmark",
    "finland": "Finland", "fi": "Finland",
    "ireland": "Ireland", "ie": "Ireland",
    "greece": "Greece", "gr": "Greece",
    "egypt": "Egypt", "eg": "Egypt",
    "morocco": "Morocco", "ma": "Morocco"
}

COUNTRY_FLAGS = {
    "Bangladesh": "🇧🇩", "India": "🇮🇳", "United States": "🇺🇸", "Oman": "🇴🇲",
    "United Arab Emirates": "🇦🇪", "Qatar": "🇶🇦", "Iran": "🇮🇷", "Spain": "🇪🇸",
    "Japan": "🇯🇵", "China": "🇨🇳", "Pakistan": "🇵🇰", "Malaysia": "🇲🇾",
    "Singapore": "🇸🇬", "Canada": "🇨🇦", "Australia": "🇦🇺", "Germany": "🇩🇪",
    "France": "🇫🇷", "Italy": "🇮🇹", "Portugal": "🇵🇹", "Turkey": "🇹🇷",
    "Nepal": "🇳🇵", "Sri Lanka": "🇱🇰", "Brazil": "🇧🇷", "Mexico": "🇲🇽",
    "South Africa": "🇿🇦", "Saudi Arabia": "🇸🇦", "Kuwait": "🇰🇼", "Bahrain": "🇧🇭",
    "Indonesia": "🇮🇩", "Thailand": "🇹🇭", "South Korea": "🇰🇷", "New Zealand": "🇳🇿",
    "Russia": "🇷🇺", "Netherlands": "🇳🇱", "Belgium": "🇧🇪", "Switzerland": "🇨🇭",
    "Sweden": "🇸🇪", "Norway": "🇳🇴", "Denmark": "🇩🇰", "Finland": "🇫🇮",
    "Ireland": "🇮🇪", "Greece": "🇬🇷", "Egypt": "🇪🇬", "Morocco": "🇲🇦"
}

LEADERS = {
    "Bangladesh": "(President: মোহাম্মদ সাহাবুদ্দিন)\n(Prime Minister: তারেক রহমান)",
    "India": "(President: দ্রৌপদী মুর্মু)\n(Prime Minister: নরেন্দ্র মোদি)",
    "United States": "(President: Donald J. Trump)",
    "Oman": "(Sultan: হাইথাম বিন তারিক)",
    "United Arab Emirates": "(President: মোহাম্মদ বিন জায়েদ আল নাহিয়ান)",
    "Qatar": "(Amir: তামিম বিন হামাদ আল থানি)",
    "Iran": "(Supreme Leader: আলী খামেনেয়ী)\n(President: মাসউদ পেজেশকিয়ান)",
    "Spain": "(King: ষষ্ঠ ফিলিপ)\n(Prime Minister: Pedro Sánchez)",
    "Japan": "(Emperor: নারুহিতো)\n(Prime Minister: Shigeru Ishiba)",
    "China": "(President: শি জিনপিং)",
    "Pakistan": "(President: আসিফ আলী জারদারি)\n(Prime Minister: শেহবাজ শরীফ)",
    "Malaysia": "(King: সুলতান ইব্রাহিম)\n(Prime Minister: আনোয়ার ইব্রাহিম)",
    "Singapore": "(President: থারমান শানমুগারত্নম)",
    "Canada": "(Prime Minister: Justin Trudeau)",
    "Australia": "(Prime Minister: Anthony Albanese)",
    "Germany": "(President: Frank-Walter Steinmeier)\n(Chancellor: Friedrich Merz)",
    "France": "(President: Emmanuel Macron)",
    "Italy": "(President: Sergio Mattarella)\n(Prime Minister: Giorgia Meloni)",
    "Portugal": "(President: Marcelo Rebelo de Sousa)",
    "Turkey": "(President: Recep Tayyip Erdoğan)"
}

COUNTRY_NAMES = {
    "Bangladesh": ["আরিফ হোসেন", "মাহমুদুল হাসান", "সাইফুল ইসলাম", "রাকিব হাসান", "তানভীর আহমেদ", "নুসরাত জাহান", "সুমাইয়া আক্তার"],
    "India": ["Rohan Kumar", "Aarav Sharma", "Rahul Verma", "Arjun Mehta", "Priya Singh", "Ananya Patel", "Neha Gupta"],
    "United States": ["James Williams", "Michael Davis", "Daniel Brown", "William Wilson", "Emily Johnson", "Olivia Miller"],
    "Oman": ["Ahmed Al Balushi", "Salim Al Harthy", "Said Al Rashdi", "Fatma Al Hinai"],
    "United Arab Emirates": ["Ahmed Hassan", "Omar Abdullah", "Khalid Mohammed", "Fatima Ali"],
    "Qatar": ["Mohammed Al Thani", "Ahmed Al Kuwari", "Noura Al Ali"],
    "Iran": ["Mohammad Reza Ahmadi", "Ali Hosseini", "Reza Karimi", "Sara Mohammadi", "Maryam Rahimi"],
    "Japan": ["Haruto Sato", "Yuki Tanaka", "Ren Suzuki", "Aoi Watanabe"]
}

DEFAULT_NAMES = ["James Williams", "Michael Davis", "Daniel Brown", "William Wilson", "Emma Anderson"]

STREET_NAMES = ["Riverside Road", "Central Road", "Market Road", "Station Road", "Garden Street", "Park Road", "Main Street"]

CITY_FAMOUS = {
    "Dhaka": "বাংলাদেশের রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Chattogram": "সমুদ্রবন্দর, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Rajshahi": "আম, রেশম ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Khulna": "সুন্দরবন ও শিল্পাঞ্চলের জন্য বিখ্যাত",
    "Barishal": "নদী, খাল ও পেয়ারা বাগানের জন্য বিখ্যাত",
    "Sylhet": "চা-বাগান, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Rangpur": "কৃষি ও ঐতিহ্যের জন্য বিখ্যাত",
    "Mumbai": "Bollywood, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
    "Delhi": "ভারতের রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Kolkata": "সাহিত্য, সংস্কৃতি ও ঐতিহ্যের জন্য বিখ্যাত",
    "Bengaluru": "Technology ও IT industry-এর জন্য বিখ্যাত",
    "Chennai": "শিল্প, প্রযুক্তি ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Hyderabad": "Technology, খাবার ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "New York": "Times Square, Wall Street ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Los Angeles": "Hollywood ও চলচ্চিত্র শিল্পের জন্য বিখ্যাত",
    "Muscat": "ওমানের রাজধানী, সমুদ্র, পাহাড় ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",
    "Dubai": "আকাশচুম্বী ভবন, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Abu Dhabi": "UAE-এর রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Doha": "কাতারের রাজধানী, আধুনিক স্থাপত্য, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Tehran": "ইরানের রাজধানী, ব্যবসা, সংস্কৃতি ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Mashhad": "ধর্মীয় পর্যটন ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Isfahan": "ঐতিহাসিক স্থাপত্য, সেতু ও শিল্পকলার জন্য বিখ্যাত",
    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "London": "যুক্তরাজ্যের রাজধানী, ইতিহাস, ব্যবসা ও পর্যটনের জন্য বিখ্যাত"
}

COUNTRY_BASIC = {
    "Bangladesh": {"pop": "১৬৯,৮২৮,৯১১", "area": "১৪৭,৫৭০ km²", "food": "ভাত, মাছ, ডাল ও ভর্তা", "jobs": "Garments / Agriculture / Business / Services"},
    "India": {"pop": "১,৪২৯,৪০৪,০০০", "area": "৩,২৮৭,৫৯০ km²", "food": "ভাত, রুটি, ডাল ও বিরিয়ানি", "jobs": "IT / Business / Manufacturing / Services"},
    "United States": {"pop": "৩৩১,০০২,৬৫১", "area": "৯,৮৩৩,৫১৭ km²", "food": "Burger, Barbecue, Steak ও খাবার", "jobs": "Technology / Finance / Services / Manufacturing"},
    "United Arab Emirates": {"pop": "৯,৮৯০,৪৫৩", "area": "৮৩,৬০০ km²", "food": "Machboos, Hummus ও Shawarma", "jobs": "Business / Tourism / Finance / Construction"},
    "Oman": {"pop": "৫,১০৯,০৬০", "area": "৩০৯,৫০০ km²", "food": "Shuwa, Majboos ও সামুদ্রিক খাবার", "jobs": "Oil & Gas / Logistics / Tourism / Services"},
    "Qatar": {"pop": "২,৮৮১,০৫৪", "area": "১১,৫৮৬ km²", "food": "Machboos, Harees ও খেজুর", "jobs": "Energy / Construction / Business / Services"},
    "Iran": {"pop": "৮৭,১৩৪,০০০", "area": "১,৬৪৮,১৯৫ km²", "food": "Chelo Kebab, Ghormeh Sabzi ও Fesenjan", "jobs": "Oil & Gas / Manufacturing / Agriculture / Services"}
}

CITIES_DB = {
    "Bangladesh": {
        "Khulna": {"postal": "9000", "region": "খুলনা বিভাগ"},
        "Dhaka": {"postal": "1000", "region": "ঢাকা বিভাগ"},
        "Chattogram": {"postal": "4000", "region": "চট্টগ্রাম বিভাগ"},
        "Rajshahi": {"postal": "6000", "region": "রাজশাহী বিভাগ"},
        "Rangpur": {"postal": "5400", "region": "রংপুর বিভাগ"},
        "Sylhet": {"postal": "3100", "region": "সিলেট বিভাগ"}
    },
    "India": {
        "Bengaluru": {"postal": "560001", "region": "Karnataka"},
        "Mumbai": {"postal": "400001", "region": "Maharashtra"},
        "Delhi": {"postal": "110001", "region": "Delhi (NCT)"},
        "Kolkata": {"postal": "700001", "region": "West Bengal"}
    },
    "United States": {
        "New York": {"postal": "10001", "region": "New York"},
        "Los Angeles": {"postal": "90001", "region": "California"}
    },
    "Iran": {
        "Tehran": {"postal": "11369", "region": "Tehran Province"},
        "Mashhad": {"postal": "91336", "region": "Razavi Khorasan Province"},
        "Isfahan": {"postal": "81386", "region": "Isfahan Province"}
    }
}

# ------------------------------------------------------------
# LOGIC & GENERATOR
# ------------------------------------------------------------

def generate_country_record(country_key, previous=None):
    country_name = COUNTRY_ALIASES.get(country_key.lower(), country_key.title())
    api_data = country_request(country_name)
    
    basic = COUNTRY_BASIC.get(country_name, {
        "pop": "৮৭,১৩৪,০০০", "area": "১,৬৪৮,১৯৫ km²", "food": "স্থানীয় খাবার", "jobs": "Business / Services / Job"
    })
    
    cities_dict = CITIES_DB.get(country_name, {
        "Capital City": {"postal": "10000", "region": "Central Region"}
    })
    
    old_city = previous.get("city") if previous else None
    available_cities = [c for c in cities_dict.keys() if c != old_city]
    city = random.choice(available_cities if available_cities else list(cities_dict.keys()))
    
    c_info = cities_dict[city]
    
    names_list = COUNTRY_NAMES.get(country_name, DEFAULT_NAMES)
    name = random.choice(names_list)
    
    street = f"{random.randint(10, 999)} {random.choice(STREET_NAMES)}, Block {random.choice(['A', 'B', 'C', 'D'])}"
    duty = random.choice(["সাধারণত ৮–৯ ঘণ্টা", "সাধারণত ৮ ঘণ্টা", "সাধারণত ৮–১০ ঘণ্টা"])
    
    flag = COUNTRY_FLAGS.get(country_name, "🌍")
    leader = LEADERS.get(country_name, "(রাষ্ট্রপ্রধান ও সরকারপ্রধানের তথ্য)")
    famous = CITY_FAMOUS.get(city, "স্থানীয় ঐতিহাসিক, সাংস্কৃতিক ও অর্থনৈতিক গুরুত্বের জন্য পরিচিত")

    pop_val = basic["pop"]
    area_val = basic["area"]

    if api_data:
        if api_data.get("population"):
            pop_val = f"{int(api_data['population']):,}"
        if api_data.get("area"):
            if isinstance(api_data["area"], dict):
                area_val = f"{int(api_data['area'].get('kilometers', 0)):,} km²"
            else:
                area_val = f"{int(api_data['area']):,} km²"

    return {
        "country": country_name,
        "country_key": country_key,
        "flag": flag,
        "leader": leader,
        "name": name,
        "street": street,
        "city": city,
        "famous": famous,
        "state": c_info["region"],
        "postal": c_info["postal"],
        "population": to_bn_digits(pop_val),
        "area": to_bn_digits(area_val),
        "food": basic["food"],
        "jobs": basic["jobs"],
        "duty": duty
    }

def build_country_message(record):
    country = safe_text(record["country"])
    flag = safe_text(record["flag"])
    leader = safe_text(record["leader"])

    return (
        f"<b>{country} {flag}</b>\n"
        f"{leader}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{safe_text(record['name'])}</code>\n"
        f"– <b>Street:</b> <code>{safe_text(record['street'])}</code>\n\n"
        f"– <b>City:</b> <code>{safe_text(record['city'])}</code>\n"
        f"  ↳ <b>বিখ্যাত:</b> {safe_text(record['famous'])}\n\n"
        f"– <b>State/Region:</b> <code>{safe_text(record['state'])}</code>\n"
        f"– <b>Postal Code:</b> <code>{safe_text(record['postal'])}</code>\n"
        f"– <b>Country Population:</b> <code>{safe_text(record['population'])}</code>\n"
        f"– <b>Country Area:</b> <code>{safe_text(record['area'])}</code>\n"
        f"– <b>প্রধান খাদ্য:</b> {safe_text(record['food'])}\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> {safe_text(record['jobs'])}\n"
        f"– <b>Job Duty Hour:</b> {safe_text(record['duty'])}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

def make_reply_markup():
    keyboard = {
        "inline_keyboard": [
            [
                {
                    "text": "🔄 Generate",
                    "callback_data": "GENERATE"
                }
            ]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)

# ------------------------------------------------------------
# BOT LOGIC HANDLERS
# ------------------------------------------------------------

def generate_for_user(chat_id, country):
    previous = USER_STATE.get(chat_id, {}).get("record")
    record = generate_country_record(country, previous)
    if record:
        USER_STATE[chat_id] = {"country": country, "record": record}
    return record

def handle_start(chat_id):
    text = (
        "<b>🌍 Country Information Generator Bot</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "টাইপ করুন:\n"
        "• <code>/fake bd</code>\n"
        "• <code>/fake india</code>\n"
        "• <code>/fake usa</code>\n"
        "• <code>/fake iran</code>\n\n"
        "📋 কোড টেক্সটে ট্যাপ করলেই সরাসরি কপি হবে।"
    )
    send_message(chat_id, text)

def handle_country(chat_id, text):
    raw = text.replace("/fake", "").strip()
    country_key = COUNTRY_ALIASES.get(raw.lower(), raw)
    
    record = generate_for_user(chat_id, country_key)
    if not record:
        send_message(chat_id, "❌ এই Country-এর তথ্য পাওয়া যায়নি। সঠিক নাম বা কোড দিন।")
        return
        
    text_output = build_country_message(record)
    send_message(chat_id, text_output, make_reply_markup())

def handle_generate_callback(callback):
    callback_id = callback.get("id")
    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")
    
    answer_callback(callback_id)
    if not chat_id:
        return
        
    country = USER_STATE.get(chat_id, {}).get("country", "Bangladesh")
    record = generate_for_user(chat_id, country)
    
    if record:
        text_output = build_country_message(record)
        edit_message(chat_id, message_id, text_output, make_reply_markup())

def handle_update(update):
    if "message" in update:
        message = update["message"]
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "").strip()
        
        if not chat_id or not text:
            return
            
        if text.lower() == "/start":
            handle_start(chat_id)
        elif text.lower().startswith("/fake"):
            handle_country(chat_id, text)
        elif text.lower() in COUNTRY_ALIASES or text in COUNTRY_FLAGS:
            handle_country(chat_id, text)

    elif "callback_query" in update:
        callback = update["callback_query"]
        if callback.get("data") == "GENERATE":
            handle_generate_callback(callback)

# ------------------------------------------------------------
# MAIN POLLING LOOP
# ------------------------------------------------------------

def main():
    print("==========================================")
    print(" COUNTRY INFORMATION GENERATOR BOT READY")
    print("==========================================")
    
    telegram_request("deleteWebhook", {"drop_pending_updates": False})
    
    offset = None
    while True:
        try:
            payload = {"timeout": 30, "allowed_updates": json.dumps(["message", "callback_query"])}
            if offset is not None:
                payload["offset"] = offset
                
            response = telegram_request("getUpdates", payload)
            if not response or not response.get("ok", False):
                time.sleep(3)
                continue
                
            updates = response.get("result", [])
            for update in updates:
                offset = update.get("update_id", 0) + 1
                handle_update(update)
                
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped.")
            break
        except Exception as e:
            print("\n❌ Main loop error:", e)
            time.sleep(3)

if __name__ == "__main__":
    main()
