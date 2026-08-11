# -*- coding: utf-8 -*-

import json
import time
import random
import urllib.parse
import urllib.request
import ssl

# =========================================================
# SSL & BOT TOKEN
# =========================================================
ssl_context = ssl._create_unverified_context()
BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"
API = "https://api.telegram.org/bot" + BOT_TOKEN

# =========================================================
# 121+ ACCURATE COUNTRY DATABASE
# =========================================================
ACCURATE_ADDRESS_DB = {
    "bd": {
        "country": "Bangladesh 🇧🇩",
        "first_names": ["মাহমুদুল", "শাহানা", "তানভীর", "সাব্বির", "নুসরাত", "আনিকা", "মেহেদী", "ফাহিম", "আয়েশা", "রহিম", "রাফি", "কামরুল"],
        "last_names": ["হাসান", "বেগম", "চৌধুরী", "ইসলাম", "রহমান", "খান", "সদ্দিকী", "হোসেন", "আহমেদ"],
        "places": [
            {"city": "বরিশাল", "state": "বরিশাল বিভাগ", "postcode": "৮২০০", "streets": ["বরিশাল সদর", "সদর রোড", "সিএন্ডবি রোড", "বান্দ রোড"]},
            {"city": "ঢাকা", "state": "ঢাকা বিভাগ", "postcode": "১২০৭", "streets": ["মোহাম্মদপুর বাস স্ট্যান্ড", "মিরপুর রোড", "আসাদ এভিনিউ", "রিং রোড"]},
            {"city": "ঢাকা", "state": "ঢাকা বিভাগ", "postcode": "১২০৫", "streets": ["গ্রীন রোড", "এলিফ্যান্ট রোড", "ধানমন্ডি ২৭"]},
            {"city": "চট্টগ্রাম", "state": "চট্টগ্রাম বিভাগ", "postcode": "৪০০০", "streets": ["জিইসি মোড়", "সিডিএ এভিনিউ", "আগ্রাবাদ বা/এ", "স্টেশন রোড"]},
            {"city": "রাজশাহী", "state": "রাজশাহী বিভাগ", "postcode": "৬০০০", "streets": ["কাজলা মেইন রোড", "নিউ মার্কেট রোড", "গ্রেটার রোড"]},
            {"city": "খুলনা", "state": "খুলনা বিভাগ", "postcode": "৯০০০", "streets": ["খান এ সবুর রোড", "কেডিএ এভিনিউ", "যশোর রোড"]},
            {"city": "সিলেট", "state": "সিলেট বিভাগ", "postcode": "৩১০০", "streets": ["জিন্দাবাজার রোড", "দরগাহ গেট", "আম্বারখানা"]}
        ]
    },
    "mx": {
        "country": "Mexico 🇲🇽",
        "first_names": ["Carlos", "Luis", "Mateo", "Sofia", "Valentina", "Camila", "Alejandro"],
        "last_names": ["Hernández", "García", "López", "González", "Pérez", "Rodríguez"],
        "places": [
            {"city": "Villahermosa", "state": "Tabasco", "postcode": "86000", "streets": ["Paseo Tabasco", "Gregorio Méndez Magaña", "Avenida Juárez"]},
            {"city": "Mexico City", "state": "CDMX", "postcode": "06600", "streets": ["Paseo de la Reforma", "Avenida Insurgentes Sur"]},
            {"city": "Guadalajara", "state": "Jalisco", "postcode": "44100", "streets": ["Avenida Vallarta", "Avenida Juárez"]}
        ]
    },
    "ca": {
        "country": "Canada 🇨🇦",
        "first_names": ["James", "John", "Robert", "Emily", "Sarah", "Michael", "David"],
        "last_names": ["Smith", "Brown", "Wilson", "Taylor", "Anderson", "Thomas"],
        "places": [
            {"city": "Toronto", "state": "Ontario", "postcode": "M5H 2N2", "streets": ["Yonge Street", "Bay Street", "Queen Street West"]},
            {"city": "Vancouver", "state": "British Columbia", "postcode": "V6B 1A1", "streets": ["Robson Street", "Granville Street"]},
            {"city": "Montreal", "state": "Quebec", "postcode": "H3B 1A1", "streets": ["Sainte-Catherine St", "Saint-Denis St"]}
        ]
    },
    "us": {
        "country": "United States 🇺🇸",
        "first_names": ["David", "Chris", "Jessica", "Daniel", "Matthew", "Ashley", "Joshua"],
        "last_names": ["Johnson", "Williams", "Jones", "Miller", "Davis", "Garcia"],
        "places": [
            {"city": "New York", "state": "New York", "postcode": "10001", "streets": ["5th Avenue", "Broadway", "Madison Avenue"]},
            {"city": "Miami", "state": "Florida", "postcode": "33101", "streets": ["Ocean Drive", "Biscayne Blvd", "Collins Ave"]},
            {"city": "Los Angeles", "state": "California", "postcode": "90001", "streets": ["Sunset Blvd", "Hollywood Blvd"]}
        ]
    },
    "in": {
        "country": "India 🇮🇳",
        "first_names": ["Aarav", "Priya", "Rahul", "Ananya", "Rohan", "Siddharth"],
        "last_names": ["Sharma", "Verma", "Sen", "Patel", "Das", "Mukherjee"],
        "places": [
            {"city": "Kolkata", "state": "West Bengal", "postcode": "700001", "streets": ["Park Street", "Camac Street", "Strand Road"]},
            {"city": "Mumbai", "state": "Maharashtra", "postcode": "400001", "streets": ["Marine Drive", "Linking Road"]},
            {"city": "Bhubaneswar", "state": "Odisha", "postcode": "751001", "streets": ["Janpath Road", "Lewis Road"]}
        ]
    }
}

ALIASES = {
    "bd": "bd", "bangladesh": "bd", "বাংলাদেশ": "bd",
    "mx": "mx", "mexico": "mx",
    "ca": "ca", "canada": "ca",
    "us": "us", "usa": "us", "america": "us",
    "in": "in", "india": "in"
}

# =========================================================
# TELEGRAM API REQUEST FUNCTION
# =========================================================
def telegram_request(method, data=None):
    if data is None:
        data = {}
    url = API + "/" + method
    try:
        encoded = urllib.parse.urlencode(data).encode("utf-8")
        request = urllib.request.Request(url, data=encoded, headers={"User-Agent": "Bot/1.0"})
        with urllib.request.urlopen(request, timeout=45, context=ssl_context) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print("API Error:", e)
        return None

# =========================================================
# ADDRESS GENERATOR & BUTTON BUILDER
# =========================================================
def generate_address_text(code):
    db = ACCURATE_ADDRESS_DB.get(code, ACCURATE_ADDRESS_DB["bd"])
    full_name = f"{random.choice(db['first_names'])} {random.choice(db['last_names'])}"
    place = random.choice(db["places"])
    street_no = random.randint(10, 150)
    
    # বাংলা সংখ্যা কনভার্টার (বাংলাদেশের ক্ষেত্রে)
    if code == "bd":
        bangla_nums = {'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'}
        street_no_str = "".join(bangla_nums.get(c, c) for c in str(street_no))
    else:
        street_no_str = str(street_no)

    street_address = f"{street_no_str} {random.choice(place['streets'])}"

    text = (
        f"<b>{db['country']} Address</b>\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"- <b>Name:</b> <code>{full_name}</code>\n"
        f"- <b>Street:</b> <code>{street_address}</code>\n"
        f"- <b>City:</b> <code>{place['city']}</code>\n"
        f"- <b>State:</b> <code>{place['state']}</code>\n"
        f"- <b>Postal Code:</b> <code>{place['postcode']}</code>\n"
        f"- <b>Country:</b> <code>{db['country'].split()[0]}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━"
    )
    return text

def get_regenerate_keyboard(code):
    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "Regenerate 🔄", "callback_data": f"regen_{code}"}
            ]
        ]
    }
    return json.dumps(reply_markup)

# =========================================================
# MESSAGE & CALLBACK PROCESSOR
# =========================================================
def process_update(update):
    # text message handle
    if "message" in update:
        message = update["message"]
        chat_id = message.get("chat", {}).get("id")
        text = message.get("text", "").strip()

        if text.startswith("/start"):
            msg = "<b>🤖 Address Bot</b>\n\nউদাহরণ:\n<code>/fake bd</code>\n<code>/fake mexico</code>"
            telegram_request("sendMessage", {"chat_id": chat_id, "text": msg, "parse_mode": "HTML"})

        elif text.startswith("/fake"):
            parts = text.split(" ", 1)
            raw_code = parts[1].strip().lower() if len(parts) > 1 else "bd"
            code = ALIASES.get(raw_code, "bd")
            
            response_text = generate_address_text(code)
            keyboard = get_regenerate_keyboard(code)
            telegram_request("sendMessage", {
                "chat_id": chat_id,
                "text": response_text,
                "parse_mode": "HTML",
                "reply_markup": keyboard
            })

    # button click (Callback Query) handle
    elif "callback_query" in update:
        query = update["callback_query"]
        query_id = query["id"]
        chat_id = query["message"]["chat"]["id"]
        message_id = query["message"]["message_id"]
        data = query.get("data", "")

        if data.startswith("regen_"):
            code = data.replace("regen_", "")
            new_text = generate_address_text(code)
            keyboard = get_regenerate_keyboard(code)

            # এডিট মেসেজ
            telegram_request("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": new_text,
                "parse_mode": "HTML",
                "reply_markup": keyboard
            })
            # অ্যানসার কলব্যাক পপআপ বন্ধ করা
            telegram_request("answerCallbackQuery", {"callback_query_id": query_id})

# =========================================================
# MAIN BOT LOOP
# =========================================================
def run_bot():
    print("\n🤖 Bot Starting with Inline Regenerate Button...\n")
    offset = None

    while True:
        try:
            data = {"timeout": 30, "allowed_updates": json.dumps(["message", "callback_query"])}
            if offset is not None:
                data["offset"] = offset

            result = telegram_request("getUpdates", data)
            if result and result.get("ok"):
                for update in result.get("result", []):
                    offset = update.get("update_id", 0) + 1
                    process_update(update)
        except Exception as e:
            print("Main Loop Exception:", e)
            time.sleep(3)

if __name__ == "__main__":
    run_bot()
    "ca": ("Canada 🇨🇦", "Ottawa"),
    "us": ("United States 🇺🇸", "Washington"),
    "mx": ("Mexico 🇲🇽", "Mexico City"),
    "jp": ("Japan 🇯🇵", "Tokyo"),
    "cn": ("China 🇨🇳", "Beijing"),
    "kr": ("South Korea 🇰🇷", "Seoul"),
    "au": ("Australia 🇦🇺", "Canberra"),
    "nz": ("New Zealand 🇳🇿", "Wellington"),

    "uk": ("United Kingdom 🇬🇧", "London"),
    "ie": ("Ireland 🇮🇪", "Dublin"),
    "fr": ("France 🇫🇷", "Paris"),
    "de": ("Germany 🇩🇪", "Berlin"),
    "es": ("Spain 🇪🇸", "Madrid"),
    "pt": ("Portugal 🇵🇹", "Lisbon"),
    "it": ("Italy 🇮🇹", "Rome"),
    "nl": ("Netherlands 🇳🇱", "Amsterdam"),
    "be": ("Belgium 🇧🇪", "Brussels"),
    "ch": ("Switzerland 🇨🇭", "Bern"),
    "at": ("Austria 🇦🇹", "Vienna"),
    "se": ("Sweden 🇸🇪", "Stockholm"),
    "no": ("Norway 🇳🇴", "Oslo"),
    "dk": ("Denmark 🇩🇰", "Copenhagen"),
    "fi": ("Finland 🇫🇮", "Helsinki"),
    "pl": ("Poland 🇵🇱", "Warsaw"),
    "cz": ("Czechia 🇨🇿", "Prague"),
    "gr": ("Greece 🇬🇷", "Athens"),
    "ro": ("Romania 🇷🇴", "Bucharest"),
    "hu": ("Hungary 🇭🇺", "Budapest"),
    "hr": ("Croatia 🇭🇷", "Zagreb"),
    "rs": ("Serbia 🇷🇸", "Belgrade"),
    "ua": ("Ukraine 🇺🇦", "Kyiv"),
    "tr": ("Turkey 🇹🇷", "Ankara"),

    "br": ("Brazil 🇧🇷", "Brasilia"),
    "ar": ("Argentina 🇦🇷", "Buenos Aires"),
    "cl": ("Chile 🇨🇱", "Santiago"),
    "co": ("Colombia 🇨🇴", "Bogota"),
    "pe": ("Peru 🇵🇪", "Lima"),
    "ec": ("Ecuador 🇪🇨", "Quito"),
    "uy": ("Uruguay 🇺🇾", "Montevideo"),

    "th": ("Thailand 🇹🇭", "Bangkok"),
    "my": ("Malaysia 🇲🇾", "Kuala Lumpur"),
    "sg": ("Singapore 🇸🇬", "Singapore"),
    "id": ("Indonesia 🇮🇩", "Jakarta"),
    "ph": ("Philippines 🇵🇭", "Manila"),
    "vn": ("Vietnam 🇻🇳", "Hanoi"),
    "kh": ("Cambodia 🇰🇭", "Phnom Penh"),
    "la": ("Laos 🇱🇦", "Vientiane"),
    "mm": ("Myanmar 🇲🇲", "Naypyidaw"),
    "np": ("Nepal 🇳🇵", "Kathmandu"),
    "lk": ("Sri Lanka 🇱🇰", "Colombo"),
    "mv": ("Maldives 🇲🇻", "Male"),

    "sa": ("Saudi Arabia 🇸🇦", "Riyadh"),
    "ae": ("United Arab Emirates 🇦🇪", "Abu Dhabi"),
    "qa": ("Qatar 🇶🇦", "Doha"),
    "kw": ("Kuwait 🇰🇼", "Kuwait City"),
    "bh": ("Bahrain 🇧🇭", "Manama"),
    "om": ("Oman 🇴🇲", "Muscat"),
    "jo": ("Jordan 🇯🇴", "Amman"),
    "lb": ("Lebanon 🇱🇧", "Beirut"),
    "iq": ("Iraq 🇮🇶", "Baghdad"),
    "ir": ("Iran 🇮🇷", "Tehran"),

    "eg": ("Egypt 🇪🇬", "Cairo"),
    "ma": ("Morocco 🇲🇦", "Rabat"),
    "dz": ("Algeria 🇩🇿", "Algiers"),
    "tn": ("Tunisia 🇹🇳", "Tunis"),
    "ke": ("Kenya 🇰🇪", "Nairobi"),
    "ng": ("Nigeria 🇳🇬", "Abuja"),
    "gh": ("Ghana 🇬🇭", "Accra"),
    "et": ("Ethiopia 🇪🇹", "Addis Ababa"),
    "ug": ("Uganda 🇺🇬", "Kampala"),
    "tz": ("Tanzania 🇹🇿", "Dodoma"),
    "rw": ("Rwanda 🇷🇼", "Kigali"),
    "za": ("South Africa 🇿🇦", "Pretoria"),

    "ru": ("Russia 🇷🇺", "Moscow"),
    "kz": ("Kazakhstan 🇰🇿", "Astana"),
    "uz": ("Uzbekistan 🇺🇿", "Tashkent"),
    "ge": ("Georgia 🇬🇪", "Tbilisi"),
    "am": ("Armenia 🇦🇲", "Yerevan"),
    "az": ("Azerbaijan 🇦🇿", "Baku"),

    "is": ("Iceland 🇮🇸", "Reykjavik"),
    "lu": ("Luxembourg 🇱🇺", "Luxembourg"),
    "mt": ("Malta 🇲🇹", "Valletta"),
    "cy": ("Cyprus 🇨🇾", "Nicosia"),
    "bg": ("Bulgaria 🇧🇬", "Sofia"),
    "sk": ("Slovakia 🇸🇰", "Bratislava"),
    "si": ("Slovenia 🇸🇮", "Ljubljana"),
    "ba": ("Bosnia and Herzegovina 🇧🇦", "Sarajevo"),
    "al": ("Albania 🇦🇱", "Tirana"),
    "me": ("Montenegro 🇲🇪", "Podgorica"),
    "mk": ("North Macedonia 🇲🇰", "Skopje"),

    "cr": ("Costa Rica 🇨🇷", "San Jose"),
    "pa": ("Panama 🇵🇦", "Panama City"),
    "gt": ("Guatemala 🇬🇹", "Guatemala City"),
    "hn": ("Honduras 🇭🇳", "Tegucigalpa"),
    "sv": ("El Salvador 🇸🇻", "San Salvador"),
    "ni": ("Nicaragua 🇳🇮", "Managua"),
    "cu": ("Cuba 🇨🇺", "Havana"),
    "jm": ("Jamaica 🇯🇲", "Kingston"),
    "do": ("Dominican Republic 🇩🇴", "Santo Domingo"),

    "fj": ("Fiji 🇫🇯", "Suva"),
    "pg": ("Papua New Guinea 🇵🇬", "Port Moresby"),
    "ws": ("Samoa 🇼🇸", "Apia"),
    "to": ("Tonga 🇹🇴", "Nuku'alofa"),
    "vu": ("Vanuatu 🇻🇺", "Port Vila"),
}

# =========================================================
# COUNTRY ALIASES
# =========================================================

ALIASES = {
    "bangladesh": "bd",
    "বাংলাদেশ": "bd",

    "india": "in",
    "pakistan": "pk",
    "nepal": "np",
    "srilanka": "lk",
    "maldives": "mv",

    "canada": "ca",
    "can": "ca",

    "usa": "us",
    "america": "us",
    "unitedstates": "us",

    "mexico": "mx",

    "japan": "jp",
    "china": "cn",
    "korea": "kr",
    "southkorea": "kr",

    "australia": "au",
    "newzealand": "nz",

    "uk": "uk",
    "england": "uk",
    "britain": "uk",
    "unitedkingdom": "uk",

    "germany": "de",
    "france": "fr",
    "italy": "it",
    "spain": "es",
    "portugal": "pt",
    "netherlands": "nl",
    "belgium": "be",
    "switzerland": "ch",
    "austria": "at",
    "sweden": "se",
    "norway": "no",
    "denmark": "dk",
    "finland": "fi",
    "poland": "pl",
    "czechia": "cz",
    "czech": "cz",
    "greece": "gr",
    "romania": "ro",
    "hungary": "hu",
    "croatia": "hr",
    "serbia": "rs",
    "ukraine": "ua",
    "turkey": "tr",
    "türkiye": "tr",

    "brazil": "br",
    "argentina": "ar",
    "chile": "cl",
    "colombia": "co",
    "peru": "pe",
    "ecuador": "ec",
    "uruguay": "uy",

    "thailand": "th",
    "malaysia": "my",
    "singapore": "sg",
    "indonesia": "id",
    "philippines": "ph",
    "vietnam": "vn",
    "cambodia": "kh",
    "laos": "la",
    "myanmar": "mm",

    "saudiarabia": "sa",
    "ksa": "sa",
    "uae": "ae",
    "emirates": "ae",
    "qatar": "qa",
    "kuwait": "kw",
    "bahrain": "bh",
    "oman": "om",
    "jordan": "jo",
    "lebanon": "lb",
    "iraq": "iq",
    "iran": "ir",

    "egypt": "eg",
    "morocco": "ma",
    "algeria": "dz",
    "tunisia": "tn",
    "kenya": "ke",
    "nigeria": "ng",
    "ghana": "gh",
    "ethiopia": "et",
    "uganda": "ug",
    "tanzania": "tz",
    "rwanda": "rw",
    "southafrica": "za",

    "russia": "ru",
    "kazakhstan": "kz",
    "uzbekistan": "uz",
    "georgia": "ge",
    "armenia": "am",
    "azerbaijan": "az",

    "iceland": "is",
    "luxembourg": "lu",
    "malta": "mt",
    "cyprus": "cy",
    "bulgaria": "bg",
    "slovakia": "sk",
    "slovenia": "si",
    "bosnia": "ba",
    "albania": "al",
    "montenegro": "me",
    "northmacedonia": "mk",

    "costarica": "cr",
    "panama": "pa",
    "guatemala": "gt",
    "honduras": "hn",
    "elsalvador": "sv",
    "nicaragua": "ni",
    "cuba": "cu",
    "jamaica": "jm",
    "dominicanrepublic": "do",

    "fiji": "fj",
    "papuanewguinea": "pg",
    "samoa": "ws",
    "tonga": "to",
    "vanuatu": "vu",
}

for code in COUNTRIES:
    ALIASES[code] = code


FIRST_NAMES = ["Alex", "Daniel", "Michael", "David", "James", "Robert", "John", "William", "Thomas", "Charles", "Emily", "Sarah", "Amanda", "Jessica", "Maria"]
LAST_NAMES = ["Smith", "Brown", "Wilson", "Taylor", "Martin", "Anderson", "Thomas", "White", "Harris", "Clark", "Miller", "Davis"]

def make_display_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return first + " " + last

def get_country_code(user_input):
    value = user_input.lower().strip().replace("-", "").replace("_", "").replace(" ", "")
    return ALIASES.get(value)


# =========================================================
# TELEGRAM API REQUEST (WITH SSL FIX)
# =========================================================

def telegram_request(method, data=None):
    if data is None:
        data = {}

    url = API + "/" + method

    try:
        encoded = urllib.parse.urlencode(data).encode("utf-8")
        request = urllib.request.Request(
            url,
            data=encoded,
            headers={"User-Agent": "QPython-Telegram-Bot/1.0"}
        )

        # context=ssl_context যোগ করে SSL এরর সমাধান করা হয়েছে
        with urllib.request.urlopen(request, timeout=45, context=ssl_context) as response:
            result = response.read().decode("utf-8")
            return json.loads(result)

    except Exception as error:
        print("Telegram API Error:", error)
        return None


def send_message(chat_id, text):
    return telegram_request(
        "sendMessage",
        {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
    )


# =========================================================
# PUBLIC ADDRESS SEARCH
# =========================================================

def search_public_address(country, capital):
    queries = [
        "Central Post Office, " + capital + ", " + country,
        "Main Post Office, " + capital + ", " + country,
        "City Hall, " + capital + ", " + country,
        "Public Library, " + capital + ", " + country
    ]

    headers = {"User-Agent": "QPython-Public-Address-Bot/1.0"}

    for query in queries:
        try:
            params = urllib.parse.urlencode({
                "q": query,
                "format": "jsonv2",
                "addressdetails": 1,
                "limit": 5
            })

            url = NOMINATIM_API + "?" + params
            request = urllib.request.Request(url, headers=headers)

            # SSL context পাস করা হচ্ছে
            with urllib.request.urlopen(request, timeout=30, context=ssl_context) as response:
                raw = response.read().decode("utf-8")
                results = json.loads(raw)

            if not results:
                time.sleep(1)
                continue

            for item in results:
                address = item.get("address", {})
                road = address.get("road") or address.get("pedestrian") or address.get("street") or ""
                house_number = address.get("house_number", "")
                city = address.get("city") or address.get("town") or address.get("municipality") or address.get("village") or capital
                state = address.get("state") or address.get("state_district", "") or ""
                postcode = address.get("postcode", "")

                if road or house_number or postcode:
                    if house_number and road:
                        street = house_number + " " + road
                    elif road:
                        street = road
                    else:
                        street = item.get("display_name", "")

                    return {
                        "street": street,
                        "city": city,
                        "state": state,
                        "postcode": postcode
                    }

        except Exception as error:
            print("Address Search Error:", error)

        time.sleep(1)

    return None


def handle_start(chat_id):
    text = (
        "<b>🌍 PUBLIC ADDRESS BOT</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "বাস্তব public location থেকে address lookup করা হবে।\n\n"
        "<b>ব্যবহার:</b>\n"
        "<code>/fake bd</code>\n"
        "<code>/fake canada</code>\n"
        "<code>/fake mexico</code>\n"
        "<code>/fake usa</code>\n\n"
        "━━━━━━━━━━━━━━━━━━━"
    )
    send_message(chat_id, text)


def handle_fake(chat_id, argument):
    code = get_country_code(argument)

    if not code:
        send_message(
            chat_id,
            "❌ <b>Country পাওয়া যায়নি।</b>\n\n"
            "উদাহরণ:\n"
            "<code>/fake bd</code>\n"
            "<code>/fake ca</code>\n"
            "<code>/fake mx</code>"
        )
        return

    country_name, capital = COUNTRIES[code]

    send_message(
        chat_id,
        "🔎 <b>Public address খোঁজা হচ্ছে...</b>\n\n🌍 " + country_name
    )

    address = search_public_address(country_name, capital)

    if not address:
        send_message(
            chat_id,
            "⚠️ <b>Address পাওয়া যায়নি।</b>\n\n"
            "এই মুহূর্তে নির্ভরযোগ্য public address পাওয়া যায়নি।"
        )
        return

    name = make_display_name()
    street = address.get("street", "N/A")
    city = address.get("city", capital)
    state = address.get("state", "N/A")
    postcode = address.get("postcode", "N/A")

    response = (
        "<b>" + country_name + " Public Address</b>\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        "- <b>Name:</b> <code>" + name + "</code>\n"
        "- <b>Street:</b> <code>" + str(street) + "</code>\n"
        "- <b>City:</b> <code>" + str(city) + "</code>\n"
        "- <b>State:</b> <code>" + str(state) + "</code>\n"
        "- <b>Postal Code:</b> <code>" + str(postcode) + "</code>\n"
        "- <b>Country:</b> <code>" + country_name + "</code>\n"
        "━━━━━━━━━━━━━━━━━━━\n\n"
        "ℹ️ <i>এটি public location-এর geocoded address।</i>"
    )

    send_message(chat_id, response)


def process_message(message):
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "").strip()

    if not text:
        return

    if text.startswith("/start"):
        handle_start(chat_id)
        return

    if text.startswith("/fake"):
        parts = text.split(" ", 1)
        argument = "bd" if len(parts) == 1 else parts[1].strip()
        handle_fake(chat_id, argument)


def run_bot():
    print("")
    print("======================================")
    print("       QPYTHON TELEGRAM BOT")
    print("======================================")
    print("BOT চালু হচ্ছে...")
    print("Telegram server-এর সাথে connecting...")
    print("")

    offset = None

    while True:
        try:
            data = {
                "timeout": 30,
                "allowed_updates": json.dumps(["message"])
            }

            if offset is not None:
                data["offset"] = offset

            result = telegram_request("getUpdates", data)

            if result is None:
                print("Telegram response পাওয়া যায়নি। Retry করা হচ্ছে...")
                time.sleep(5)
                continue

            if not result.get("ok"):
                print("Telegram API Error:", result)
                time.sleep(5)
                continue

            updates = result.get("result", [])

            for update in updates:
                offset = update.get("update_id", 0) + 1
                message = update.get("message")
                if message:
                    try:
                        process_message(message)
                    except Exception as error:
                        print("Message Error:", error)

        except KeyboardInterrupt:
            print("\nBOT বন্ধ করা হয়েছে।")
            break
        except Exception as error:
            print("\nMain Loop Error:", error)
            time.sleep(5)


if __name__ == "__main__":
    if not BOT_TOKEN:
        print("\nERROR: BOT TOKEN দেওয়া হয়নি!\n")
    else:
        print("\nBOT TOKEN পাওয়া গেছে।\nBOT starting...\n")
        run_bot()
        
