1# -*- coding: utf-8 -*-

# ==============================
# PART 1/3
# RAVEN FAKE ADDRESS BOT
# 121 COUNTRY DATABASE
# ==============================

import random
import time
import json
import urllib.request
import urllib.parse
import ssl

# QPython SSL Fix
ssl_context = ssl._create_unverified_context()

# ==============================
# BOT TOKEN
# ==============================
BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"

# ==============================
# 121 COUNTRIES
# code : (country, flag, cities)
# ==============================

COUNTRIES = {
    "af": ("Afghanistan", "🇦🇫", ["Kabul", "Kandahar", "Herat"]),
    "al": ("Albania", "🇦🇱", ["Tirana", "Durrës", "Vlorë"]),
    "dz": ("Algeria", "🇩🇿", ["Algiers", "Oran", "Constantine"]),
    "ao": ("Angola", "🇦🇴", ["Luanda", "Huambo", "Lobito"]),
    "ar": ("Argentina", "🇦🇷", ["Buenos Aires", "Córdoba", "Rosario"]),
    "am": ("Armenia", "🇦🇲", ["Yerevan", "Gyumri", "Vanadzor"]),
    "au": ("Australia", "🇦🇺", ["Sydney", "Melbourne", "Brisbane"]),
    "at": ("Austria", "🇦🇹", ["Vienna", "Graz", "Salzburg"]),
    "az": ("Azerbaijan", "🇦🇿", ["Baku", "Ganja", "Sumqayit"]),
    "bs": ("Bahamas", "🇧🇸", ["Nassau", "Freeport", "West End"]),
    "bh": ("Bahrain", "🇧🇭", ["Manama", "Riffa", "Muharraq"]),
    "bd": ("Bangladesh", "🇧🇩", ["Dhaka", "Chattogram", "Rajshahi", "Khulna", "Barishal", "Sylhet"]),
    "bb": ("Barbados", "🇧🇧", ["Bridgetown", "Speightstown", "Oistins"]),
    "by": ("Belarus", "🇧🇾", ["Minsk", "Gomel", "Brest"]),
    "be": ("Belgium", "🇧🇪", ["Brussels", "Antwerp", "Ghent"]),
    "bz": ("Belize", "🇧🇿", ["Belmopan", "Belize City", "San Ignacio"]),
    "bj": ("Benin", "🇧🇯", ["Porto-Novo", "Cotonou", "Abomey-Calavi"]),
    "bt": ("Bhutan", "🇧🇹", ["Thimphu", "Phuntsholing", "Punakha"]),
    "bo": ("Bolivia", "🇧🇴", ["Sucre", "La Paz", "Santa Cruz"]),
    "ba": ("Bosnia and Herzegovina", "🇧🇦", ["Sarajevo", "Banja Luka", "Mostar"]),
    "bw": ("Botswana", "🇧🇼", ["Gaborone", "Francistown", "Maun"]),
    "br": ("Brazil", "🇧🇷", ["Brasília", "São Paulo", "Rio de Janeiro"]),
    "bn": ("Brunei", "🇧🇳", ["Bandar Seri Begawan", "Kuala Belait", "Seria"]),
    "bg": ("Bulgaria", "🇧🇬", ["Sofia", "Plovdiv", "Varna"]),
    "bf": ("Burkina Faso", "🇧🇫", ["Ouagadougou", "Bobo-Dioulasso", "Koudougou"]),
    "bi": ("Burundi", "🇧🇮", ["Gitega", "Bujumbura", "Ngozi"]),
    "cv": ("Cabo Verde", "🇨🇻", ["Praia", "Mindelo", "Santa Maria"]),
    "kh": ("Cambodia", "🇰🇭", ["Phnom Penh", "Siem Reap", "Battambang"]),
    "cm": ("Cameroon", "🇨🇲", ["Yaoundé", "Douala", "Bamenda"]),
    "ca": ("Canada", "🇨🇦", ["Toronto", "Vancouver", "Montreal"]),
    "cf": ("Central African Republic", "🇨🇫", ["Bangui", "Bimbo", "Berbérati"]),
    "td": ("Chad", "🇹🇩", ["N'Djamena", "Moundou", "Sarh"]),
    "cl": ("Chile", "🇨🇱", ["Santiago", "Valparaíso", "Concepción"]),
    "cn": ("China", "🇨🇳", ["Beijing", "Shanghai", "Guangzhou"]),
    "co": ("Colombia", "🇨🇴", ["Bogotá", "Medellín", "Cali"]),
    "km": ("Comoros", "🇰🇲", ["Moroni", "Mutsamudu", "Fomboni"]),
    "cg": ("Republic of the Congo", "🇨🇬", ["Brazzaville", "Pointe-Noire", "Dolisie"]),
    "cr": ("Costa Rica", "🇨🇷", ["San José", "Alajuela", "Cartago"]),
    "ci": ("Côte d'Ivoire", "🇨🇮", ["Yamoussoukro", "Abidjan", "Bouaké"]),
    "hr": ("Croatia", "🇭🇷", ["Zagreb", "Split", "Rijeka"]),
    "cu": ("Cuba", "🇨🇺", ["Havana", "Santiago de Cuba", "Camagüey"]),
    "cy": ("Cyprus", "🇨🇾", ["Nicosia", "Limassol", "Larnaca"]),
    "cz": ("Czechia", "🇨🇿", ["Prague", "Brno", "Ostrava"]),
    "cd": ("DR Congo", "🇨🇩", ["Kinshasa", "Lubumbashi", "Goma"]),
    "dk": ("Denmark", "🇩🇰", ["Copenhagen", "Aarhus", "Odense"]),
    "dj": ("Djibouti", "🇩🇯", ["Djibouti City", "Ali Sabieh", "Tadjoura"]),
    "dm": ("Dominica", "🇩🇲", ["Roseau", "Portsmouth", "Marigot"]),
    "do": ("Dominican Republic", "🇩🇴", ["Santo Domingo", "Santiago de los Caballeros", "La Romana"]),
    "ec": ("Ecuador", "🇪🇨", ["Quito", "Guayaquil", "Cuenca"]),
    "eg": ("Egypt", "🇪🇬", ["Cairo", "Alexandria", "Giza"]),
    "sv": ("El Salvador", "🇸🇻", ["San Salvador", "Santa Ana", "San Miguel"]),
    "gq": ("Equatorial Guinea", "🇬🇶", ["Malabo", "Bata", "Ebebiyin"]),
    "er": ("Eritrea", "🇪🇷", ["Asmara", "Keren", "Massawa"]),
    "ee": ("Estonia", "🇪🇪", ["Tallinn", "Tartu", "Narva"]),
    "sz": ("Eswatini", "🇸🇿", ["Mbabane", "Manzini", "Lobamba"]),
    "et": ("Ethiopia", "🇪🇹", ["Addis Ababa", "Dire Dawa", "Mekelle"]),
    "fj": ("Fiji", "🇫🇯", ["Suva", "Nadi", "Lautoka"]),
    "fi": ("Finland", "🇫🇮", ["Helsinki", "Espoo", "Tampere"]),
    "fr": ("France", "🇫🇷", ["Paris", "Marseille", "Lyon"]),
    "ga": ("Gabon", "🇬🇦", ["Libreville", "Port-Gentil", "Franceville"]),
    "gm": ("Gambia", "🇬🇲", ["Banjul", "Serekunda", "Brikama"]),
    "ge": ("Georgia", "🇬🇪", ["Tbilisi", "Batumi", "Kutaisi"]),
    "de": ("Germany", "🇩🇪", ["Berlin", "Hamburg", "Munich"]),
    "gh": ("Ghana", "🇬🇭", ["Accra", "Kumasi", "Tamale"]),
    "gr": ("Greece", "🇬🇷", ["Athens", "Thessaloniki", "Patras"]),
    "gd": ("Grenada", "🇬🇩", ["St. George's", "Gouyave", "Grenville"]),
    "gt": ("Guatemala", "🇬🇹", ["Guatemala City", "Quetzaltenango", "Escuintla"]),
    "gn": ("Guinea", "🇬🇳", ["Conakry", "Nzérékoré", "Kankan"]),
    "gw": ("Guinea-Bissau", "🇬🇼", ["Bissau", "Bafatá", "Gabú"]),
    "gy": ("Guyana", "🇬🇾", ["Georgetown", "Linden", "New Amsterdam"]),
    "ht": ("Haiti", "🇭🇹", ["Port-au-Prince", "Cap-Haïtien", "Gonaïves"]),
    "hn": ("Honduras", "🇭🇳", ["Tegucigalpa", "San Pedro Sula", "La Ceiba"]),
    "hu": ("Hungary", "🇭🇺", ["Budapest", "Debrecen", "Szeged"]),
    "is": ("Iceland", "🇮🇸", ["Reykjavík", "Kópavogur", "Hafnarfjörður"]),
    "in": ("India", "🇮🇳", ["New Delhi", "Mumbai", "Kolkata"]),
    "id": ("Indonesia", "🇮🇩", ["Jakarta", "Surabaya", "Bandung"]),
    "ir": ("Iran", "🇮🇷", ["Tehran", "Mashhad", "Isfahan"]),
    "iq": ("Iraq", "🇮🇶", ["Baghdad", "Basra", "Mosul"]),
    "ie": ("Ireland", "🇮🇪", ["Dublin", "Cork", "Limerick"]),
    "il": ("Israel", "🇮🇱", ["Jerusalem", "Tel Aviv", "Haifa"]),
    "it": ("Italy", "🇮🇹", ["Rome", "Milan", "Naples"]),
    "jm": ("Jamaica", "🇯🇲", ["Kingston", "Montego Bay", "Spanish Town"]),
    "jp": ("Japan", "🇯🇵", ["Tokyo", "Osaka", "Kyoto"]),
    "jo": ("Jordan", "🇯🇴", ["Amman", "Zarqa", "Irbid"]),
    "kz": ("Kazakhstan", "🇰🇿", ["Astana", "Almaty", "Shymkent"]),
    "ke": ("Kenya", "🇰🇪", ["Nairobi", "Mombasa", "Kisumu"]),
    "kw": ("Kuwait", "🇰🇼", ["Kuwait City", "Hawalli", "Salmiya"]),
    "kg": ("Kyrgyzstan", "🇰🇬", ["Bishkek", "Osh", "Jalal-Abad"]),
    "la": ("Laos", "🇱🇦", ["Vientiane", "Luang Prabang", "Savannakhet"]),
    "lv": ("Latvia", "🇱🇻", ["Riga", "Daugavpils", "Liepāja"]),
    "lb": ("Lebanon", "🇱🇧", ["Beirut", "Tripoli", "Sidon"]),
    "ls": ("Lesotho", "🇱🇸", ["Maseru", "Mafeteng", "Hlotse"]),
    "lr": ("Liberia", "🇱🇷", ["Monrovia", "Gbarnga", "Buchanan"]),
    "ly": ("Libya", "🇱🇾", ["Tripoli", "Benghazi", "Misrata"]),
    "li": ("Liechtenstein", "🇱🇮", ["Vaduz", "Schaan", "Balzers"]),
    "lt": ("Lithuania", "🇱🇹", ["Vilnius", "Kaunas", "Klaipėda"]),
    "lu": ("Luxembourg", "🇱🇺", ["Luxembourg City", "Esch-sur-Alzette", "Differdange"]),
    "mg": ("Madagascar", "🇲🇬", ["Antananarivo", "Toamasina", "Antsirabe"]),
    "mw": ("Malawi", "🇲🇼", ["Lilongwe", "Blantyre", "Mzuzu"]),
    "my": ("Malaysia", "🇲🇾", ["Kuala Lumpur", "George Town", "Johor Bahru"]),
    "mv": ("Maldives", "🇲🇻", ["Malé", "Addu City", "Fuvahmulah"]),
    "ml": ("Mali", "🇲🇱", ["Bamako", "Sikasso", "Mopti"]),
    "mt": ("Malta", "🇲🇹", ["Valletta", "Birkirkara", "Mosta"]),
    "mr": ("Mauritania", "🇲🇷", ["Nouakchott", "Nouadhibou", "Rosso"]),
    "mu": ("Mauritius", "🇲🇺", ["Port Louis", "Beau Bassin-Rose Hill", "Vacoas-Phoenix"]),
    "mx": ("Mexico", "🇲🇽", ["Mexico City", "Guadalajara", "Monterrey"]),
    "md": ("Moldova", "🇲🇩", ["Chișinău", "Bălți", "Tiraspol"]),
    "mc": ("Monaco", "🇲🇨", ["Monaco", "Monte Carlo", "Fontvieille"]),
    "mn": ("Mongolia", "🇲🇳", ["Ulaanbaatar", "Erdenet", "Darkhan"]),
    "me": ("Montenegro", "🇲🇪", ["Podgorica", "Nikšić", "Budva"]),
    "ma": ("Morocco", "🇲🇦", ["Rabat", "Casablanca", "Marrakesh"]),
    "mz": ("Mozambique", "🇲🇿", ["Maputo", "Matola", "Nampula"]),
    "mm": ("Myanmar", "🇲🇲", ["Naypyidaw", "Yangon", "Mandalay"]),
    "na": ("Namibia", "🇳🇦", ["Windhoek", "Walvis Bay", "Swakopmund"]),
    "np": ("Nepal", "🇳🇵", ["Kathmandu", "Pokhara", "Lalitpur"]),
    "nl": ("Netherlands", "🇳🇱", ["Amsterdam", "Rotterdam", "The Hague"]),
    "nz": ("New Zealand", "🇳🇿", ["Wellington", "Auckland", "Christchurch"]),
    "ni": ("Nicaragua", "🇳🇮", ["Managua", "León", "Granada"]),
    "ae": ("United Arab Emirates", "🇦🇪", ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]),
    "gb": ("United Kingdom", "🇬🇧", ["London", "Manchester", "Birmingham"]),
    "us": ("United States", "🇺🇸", ["New York", "Los Angeles", "Chicago"]),
}

print("Country database loaded:", len(COUNTRIES))

# ==============================
# PART 2/3
# GENERATOR FUNCTIONS
# ==============================

BD_NAMES = [
    "মাহমুদুল হাসান", "শাহানা বেগম", "মোঃ রাকিব হাসান", "সুমাইয়া আক্তার",
    "আব্দুল্লাহ আল মামুন", "নুসরাত জাহান", "সাইফুল ইসলাম", "তানজিলা আক্তার",
    "আরিফ হোসেন", "মারুফা ইয়াসমিন", "রিফাত আহমেদ", "সাদিয়া রহমান"
]

FIRST_NAMES = [
    "Alex", "Daniel", "Michael", "James", "David",
    "Robert", "John", "William", "Thomas", "Andrew",
    "Sarah", "Emma", "Sophia", "Olivia", "Emily"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Miller", "Davis", "Wilson", "Taylor", "Anderson"
]

BD_REAL_PLACES = {
    "Dhaka": {"state": "ঢাকা বিভাগ", "postcode": "১২০৭", "streets": ["মোহাম্মদপুর বাস স্ট্যান্ড", "মিরপুর রোড", "ধানমন্ডি ২৭", "গ্রীন রোড"]},
    "Chattogram": {"state": "চট্টগ্রাম বিভাগ", "postcode": "৪০০০", "streets": ["জিইসি মোড়", "সিডিএ এভিনিউ", "আগ্রাবাদ বা/এ", "স্টেশন রোড"]},
    "Rajshahi": {"state": "রাজশাহী বিভাগ", "postcode": "৬০০০", "streets": ["কাজলা মেইন রোড", "নিউ মার্কেট রোড", "গ্রেটার রোড"]},
    "Khulna": {"state": "খুলনা বিভাগ", "postcode": "৯০০০", "streets": ["খান এ সবুর রোড", "কেডিএ এভিনিউ", "যশোর রোড"]},
    "Barishal": {"state": "বরিশাল বিভাগ", "postcode": "৮২০০", "streets": ["বরিশাল সদর", "সদর রোড", "সিএন্ডবি রোড"]},
    "Sylhet": {"state": "সিলেট বিভাগ", "postcode": "৩১০০", "streets": ["জিন্দাবাজার রোড", "দরগাহ গেট", "আম্বারখানা"]}
}


def random_name(code):
    if code == "bd":
        return random.choice(BD_NAMES)
    return random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)


def generate_address(code):
    if code not in COUNTRIES:
        return None

    country, flag, cities = COUNTRIES[code]
    city = random.choice(cities)
    name = random_name(code)

    if code == "bd" and city in BD_REAL_PLACES:
        place_info = BD_REAL_PLACES[city]
        road_no = random.randint(10, 120)
        bangla_nums = {'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'}
        road_no_bn = "".join(bangla_nums.get(c, c) for c in str(road_no))
        
        street = f"{road_no_bn} {random.choice(place_info['streets'])}"
        state = place_info["state"]
        postal = place_info["postcode"]
        city_display = "ঢাকা" if city == "Dhaka" else ("চট্টগ্রাম" if city == "Chattogram" else ("বরিশাল" if city == "Barishal" else city))
    else:
        street = f"{random.randint(10, 150)} Main Street, Block {random.choice(['A','B','C'])}"
        state = f"{city} Division" if code == "bd" else f"{city} State"
        postal = str(random.randint(10000, 99999))
        city_display = city

    return {
        "name": name,
        "street": street,
        "city": city_display,
        "state": state,
        "postal": postal,
        "country": country,
        "flag": flag
    }


def format_address(data):
    return (
        f"<b>{data['country']} {data['flag']} Address</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"– <b>Name:</b> <code>{data['name']}</code>\n"
        f"– <b>Street:</b> <code>{data['street']}</code>\n"
        f"– <b>City:</b> <code>{data['city']}</code>\n"
        f"– <b>State:</b> <code>{data['state']}</code>\n"
        f"– <b>Postal Code:</b> <code>{data['postal']}</code>\n"
        f"– <b>Country:</b> <code>{data['country']}</code>\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )


def format_multiple(code, amount=5):
    country, flag, cities = COUNTRIES[code]
    text = (
        f"<b>{country} {flag} — {amount} Locations</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
    )

    for i in range(amount):
        data = generate_address(code)
        text += (
            f"\n<b>#{i + 1}</b>\n"
            f"Name: <code>{data['name']}</code>\n"
            f"Street: <code>{data['street']}</code>\n"
            f"City: <code>{data['city']}</code>\n"
            f"State: <code>{data['state']}</code>\n"
            f"Postal: <code>{data['postal']}</code>\n"
        )

    text += "\n━━━━━━━━━━━━━━━━━━━━\n"
    return text


def make_keyboard(code):
    return {
        "inline_keyboard": [
            [{"text": "🔄 Regenerate", "callback_data": "gen:" + code}],
            [{"text": "📍 5 Locations", "callback_data": "multi:" + code}]
        ]
    }


def make_multiple_keyboard(code):
    return {
        "inline_keyboard": [
            [{"text": "🔄 Generate Again", "callback_data": "multi:" + code}],
            [{"text": "📍 Single Address", "callback_data": "gen:" + code}]
        ]
    }


# ==============================
# TELEGRAM API
# ==============================

def api(method, data=None):
    url = API + method
    if data is None:
        data = {}

    encoded = urllib.parse.urlencode(data).encode("utf-8")

    try:
        request = urllib.request.Request(
            url, data=encoded,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        with urllib.request.urlopen(request, timeout=60, context=ssl_context) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print("API ERROR:", e)
        return None


def send_message(chat_id, text, keyboard=None):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard, ensure_ascii=False)
    return api("sendMessage", data)


def edit_message(chat_id, message_id, text, keyboard=None):
    data = {"chat_id": chat_id, "message_id": message_id, "text": text, "parse_mode": "HTML"}
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard, ensure_ascii=False)
    return api("editMessageText", data)


def answer_callback(callback_id):
    api("answerCallbackQuery", {"callback_query_id": callback_id})


# ==============================
# PART 3/3
# BOT HANDLER
# ==============================

def normalize_code(value):
    value = value.strip().lower()
    if value in COUNTRIES:
        return value

    for code, info in COUNTRIES.items():
        if value == info[0].lower():
            return code

    aliases = {
        "bangladesh": "bd", "বাংলাদেশ": "bd", "uae": "ae", "dubai": "ae",
        "america": "us", "usa": "us", "uk": "gb", "england": "gb",
        "india": "in", "germany": "de", "france": "fr", "italy": "it",
        "japan": "jp", "china": "cn", "canada": "ca", "australia": "au"
    }
    return aliases.get(value)


def handle_message(message):
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    if not chat_id:
        return

    if text.startswith("/start"):
        msg = (
            "<b>🟣 RAVEN ADDRESS GENERATOR</b>\n\n"
            "121 countries supported with Tap-to-Copy.\n\n"
            "Example:\n"
            "<code>/fake bd</code>\n"
            "<code>/fake ae</code>\n"
            "<code>/fake us</code>"
        )
        send_message(chat_id, msg)
        return

    if text.lower().startswith("/fake"):
        parts = text.split()
        if len(parts) < 2:
            send_message(chat_id, "<b>❌ Country code দাও</b>\nExample: <code>/fake bd</code>")
            return

        code = normalize_code(parts[1])
        if not code:
            send_message(chat_id, "❌ Country পাওয়া যায়নি।\nExample: <code>/fake bd</code>")
            return

        data = generate_address(code)
        if not data:
            return

        text_out = format_address(data)
        keyboard = make_keyboard(code)
        send_message(chat_id, text_out, keyboard)


def handle_callback(callback):
    callback_id = callback.get("id")
    data = callback.get("data", "")
    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    answer_callback(callback_id)

    if data.startswith("gen:"):
        code = data.split(":", 1)[1]
        if code not in COUNTRIES:
            return

        new_address = generate_address(code)
        new_text = format_address(new_address)
        keyboard = make_keyboard(code)
        edit_message(chat_id, message_id, new_text, keyboard)

    elif data.startswith("multi:"):
        code = data.split(":", 1)[1]
        if code not in COUNTRIES:
            return

        new_text = format_multiple(code, 5)
        keyboard = make_multiple_keyboard(code)
        edit_message(chat_id, message_id, new_text, keyboard)


def run_bot():
    print("\n===================================")
    print(" RAVEN ADDRESS GENERATOR")
    print(" 121 COUNTRY SYSTEM")
    print("===================================")
    
    # 409 Conflict সমাধান করার জন্য পুরোনো ওয়েব হুক রিমুভ করা
    api("deleteWebhook", {"drop_pending_updates": True})
    
    print("Bot starting...")

    offset = 0
    while True:
        try:
            result = api("getUpdates", {"timeout": 30, "offset": offset})
            if not result or not result.get("ok"):
                time.sleep(3)
                continue

            updates = result.get("result", [])
            for update in updates:
                offset = update["update_id"] + 1

                if "message" in update:
                    handle_message(update["message"])
                elif "callback_query" in update:
                    handle_callback(update["callback_query"])

        except KeyboardInterrupt:
            print("\nBot stopped.")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            time.sleep(5)


if __name__ == "__main__":
    run_bot()
