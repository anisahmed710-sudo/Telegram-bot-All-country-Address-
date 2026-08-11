# -*- coding: utf-8 -*-

import json
import time
import random
import urllib.parse
import urllib.request
import ssl

# =========================================================
# SSL CERTIFICATE FIX FOR QPYTHON
# =========================================================
# QPython-এর SSL ভেরিফিকেশন ফেইলিউর বাইপাস করার জন্য
ssl_context = ssl._create_unverified_context()


# =========================================================
# BOT TOKEN
# =========================================================
BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

API = "https://api.telegram.org/bot" + BOT_TOKEN

NOMINATIM_API = (
    "https://nominatim.openstreetmap.org/search"
)


# =========================================================
# COUNTRY DATABASE
# =========================================================

COUNTRIES = {
    "bd": ("Bangladesh 🇧🇩", "Dhaka"),
    "in": ("India 🇮🇳", "New Delhi"),
    "pk": ("Pakistan 🇵🇰", "Islamabad"),
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
        