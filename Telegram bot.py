# ==========================================
# RAVEN ADDRESS GENERATOR (FULL WORKING CODE)
# ==========================================

import random
import time
import json
import urllib.request
import urllib.parse
import ssl

# ==========================================
# SSL FIX FOR QPYTHON
# ==========================================
ssl_context = ssl._create_unverified_context()

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"
API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"

# ==========================================
# 121 COUNTRIES DATABASE
# ==========================================
COUNTRIES = {
    "bd": ("Bangladesh", "🇧🇩", ["Dhaka", "Chattogram", "Rajshahi", "Khulna", "Barishal", "Sylhet"]),
    "ae": ("United Arab Emirates", "🇦🇪", ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]),
    "in": ("India", "🇮🇳", ["New Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"]),
    "us": ("United States", "🇺🇸", ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]),
    "gb": ("United Kingdom", "🇬🇧", ["London", "Manchester", "Birmingham", "Liverpool"]),
    "ca": ("Canada", "🇨🇦", ["Toronto", "Vancouver", "Montreal", "Calgary"]),
    "au": ("Australia", "🇦🇺", ["Sydney", "Melbourne", "Brisbane", "Perth"]),
    "de": ("Germany", "🇩🇪", ["Berlin", "Hamburg", "Munich", "Frankfurt"]),
    "fr": ("France", "🇫🇷", ["Paris", "Marseille", "Lyon", "Toulouse"]),
    "it": ("Italy", "🇮🇹", ["Rome", "Milan", "Naples", "Turin"]),
    "es": ("Spain", "🇪🇸", ["Madrid", "Barcelona", "Valencia", "Seville"]),
    "nl": ("Netherlands", "🇳🇱", ["Amsterdam", "Rotterdam", "The Hague"]),
    "be": ("Belgium", "🇧🇪", ["Brussels", "Antwerp", "Ghent"]),
    "ch": ("Switzerland", "🇨🇭", ["Zurich", "Geneva", "Basel"]),
    "at": ("Austria", "🇦🇹", ["Vienna", "Graz", "Salzburg"]),
    "se": ("Sweden", "🇸🇪", ["Stockholm", "Gothenburg", "Malmö"]),
    "no": ("Norway", "🇳🇴", ["Oslo", "Bergen", "Trondheim"]),
    "dk": ("Denmark", "🇩🇰", ["Copenhagen", "Aarhus", "Odense"]),
    "fi": ("Finland", "🇫🇮", ["Helsinki", "Espoo", "Tampere"]),
    "ie": ("Ireland", "🇮🇪", ["Dublin", "Cork", "Limerick"]),
    "pt": ("Portugal", "🇵🇹", ["Lisbon", "Porto", "Braga"]),
    "gr": ("Greece", "🇬🇷", ["Athens", "Thessaloniki", "Patras"]),
    "tr": ("Turkey", "🇹🇷", ["Istanbul", "Ankara", "Izmir"]),
    "sa": ("Saudi Arabia", "🇸🇦", ["Riyadh", "Jeddah", "Mecca"]),
    "qa": ("Qatar", "🇶🇦", ["Doha", "Al Rayyan", "Al Wakrah"]),
    "kw": ("Kuwait", "🇰🇼", ["Kuwait City", "Hawalli", "Salmiya"]),
    "om": ("Oman", "🇴🇲", ["Muscat", "Salalah", "Sohar"]),
    "bh": ("Bahrain", "🇧🇭", ["Manama", "Riffa", "Muharraq"]),
    "my": ("Malaysia", "🇲🇾", ["Kuala Lumpur", "George Town", "Johor Bahru"]),
    "sg": ("Singapore", "🇸🇬", ["Singapore"]),
    "id": ("Indonesia", "🇮🇩", ["Jakarta", "Surabaya", "Bandung"]),
    "th": ("Thailand", "🇹🇭", ["Bangkok", "Chiang Mai", "Phuket"]),
    "vn": ("Vietnam", "🇻🇳", ["Hanoi", "Ho Chi Minh City", "Da Nang"]),
    "ph": ("Philippines", "🇵🇭", ["Manila", "Quezon City", "Cebu City"]),
    "jp": ("Japan", "🇯🇵", ["Tokyo", "Osaka", "Kyoto"]),
    "kr": ("South Korea", "🇰🇷", ["Seoul", "Busan", "Incheon"]),
    "cn": ("China", "🇨🇳", ["Beijing", "Shanghai", "Guangzhou"]),
    "nz": ("New Zealand", "🇳🇿", ["Auckland", "Wellington", "Christchurch"]),
    "za": ("South Africa", "🇿🇦", ["Johannesburg", "Cape Town", "Durban"]),
    "ng": ("Nigeria", "🇳🇬", ["Lagos", "Abuja", "Kano"]),
    "ke": ("Kenya", "🇰🇪", ["Nairobi", "Mombasa", "Kisumu"]),
    "gh": ("Ghana", "🇬🇭", ["Accra", "Kumasi", "Tamale"]),
    "eg": ("Egypt", "🇪🇬", ["Cairo", "Alexandria", "Giza"]),
    "ma": ("Morocco", "🇲🇦", ["Rabat", "Casablanca", "Marrakesh"]),
    "dz": ("Algeria", "🇩🇿", ["Algiers", "Oran", "Constantine"]),
    "tn": ("Tunisia", "🇹🇳", ["Tunis", "Sfax", "Sousse"]),
    "br": ("Brazil", "🇧🇷", ["São Paulo", "Rio de Janeiro", "Brasília"]),
    "ar": ("Argentina", "🇦🇷", ["Buenos Aires", "Córdoba", "Rosario"]),
    "cl": ("Chile", "🇨🇱", ["Santiago", "Valparaíso", "Concepción"]),
    "co": ("Colombia", "🇨🇴", ["Bogotá", "Medellín", "Cali"]),
    "mx": ("Mexico", "🇲🇽", ["Mexico City", "Guadalajara", "Monterrey"]),
    "pe": ("Peru", "🇵🇪", ["Lima", "Arequipa", "Cusco"]),
    "uy": ("Uruguay", "🇺🇾", ["Montevideo", "Salto", "Paysandú"]),
    "pa": ("Panama", "🇵🇦", ["Panama City", "Colón", "David"]),
    "cr": ("Costa Rica", "🇨🇷", ["San José", "Alajuela", "Cartago"]),
    "is": ("Iceland", "🇮🇸", ["Reykjavik", "Kopavogur", "Hafnarfjordur"]),
    "cz": ("Czechia", "🇨🇿", ["Prague", "Brno", "Ostrava"]),
    "pl": ("Poland", "🇵🇱", ["Warsaw", "Krakow", "Wroclaw"]),
    "hu": ("Hungary", "🇭🇺", ["Budapest", "Debrecen", "Szeged"]),
    "ro": ("Romania", "🇷🇴", ["Bucharest", "Cluj-Napoca", "Timisoara"]),
    "bg": ("Bulgaria", "🇧🇬", ["Sofia", "Plovdiv", "Varna"]),
    "rs": ("Serbia", "🇷🇸", ["Belgrade", "Novi Sad", "Nis"]),
    "hr": ("Croatia", "🇭🇷", ["Zagreb", "Split", "Rijeka"]),
    "si": ("Slovenia", "🇸🇮", ["Ljubljana", "Maribor", "Koper"]),
    "sk": ("Slovakia", "🇸🇰", ["Bratislava", "Kosice", "Presov"]),
    "ee": ("Estonia", "🇪🇪", ["Tallinn", "Tartu", "Narva"]),
    "lv": ("Latvia", "🇱🇻", ["Riga", "Daugavpils", "Liepaja"]),
    "lt": ("Lithuania", "🇱🇹", ["Vilnius", "Kaunas", "Klaipeda"]),
    "ua": ("Ukraine", "🇺🇦", ["Kyiv", "Lviv", "Odesa"]),
    "ge": ("Georgia", "🇬🇪", ["Tbilisi", "Batumi", "Kutaisi"]),
    "am": ("Armenia", "🇦🇲", ["Yerevan", "Gyumri", "Vanadzor"]),
    "az": ("Azerbaijan", "🇦🇿", ["Baku", "Ganja", "Sumqayit"]),
    "kz": ("Kazakhstan", "🇰🇿", ["Astana", "Almaty", "Shymkent"]),
    "uz": ("Uzbekistan", "🇺🇿", ["Tashkent", "Samarkand", "Bukhara"]),
    "np": ("Nepal", "🇳🇵", ["Kathmandu", "Pokhara", "Lalitpur"]),
    "lk": ("Sri Lanka", "🇱🇰", ["Colombo", "Kandy", "Galle"]),
    "mv": ("Maldives", "🇲🇻", ["Male", "Addu City", "Fuvahmulah"]),
    "bt": ("Bhutan", "🇧🇹", ["Thimphu", "Phuntsholing", "Punakha"]),
    "mm": ("Myanmar", "🇲🇲", ["Yangon", "Mandalay", "Naypyidaw"]),
    "kh": ("Cambodia", "🇰🇭", ["Phnom Penh", "Siem Reap", "Battambang"]),
    "la": ("Laos", "🇱🇦", ["Vientiane", "Luang Prabang", "Savannakhet"]),
    "mn": ("Mongolia", "🇲🇳", ["Ulaanbaatar", "Erdenet", "Darkhan"]),
    "fj": ("Fiji", "🇫🇯", ["Suva", "Nadi", "Lautoka"]),
    "pg": ("Papua New Guinea", "🇵🇬", ["Port Moresby", "Lae", "Madang"]),
    "jm": ("Jamaica", "🇯🇲", ["Kingston", "Montego Bay", "Spanish Town"]),
    "bs": ("Bahamas", "🇧🇸", ["Nassau", "Freeport", "West End"]),
    "bb": ("Barbados", "🇧🇧", ["Bridgetown", "Oistins", "Speightstown"]),
    "tt": ("Trinidad and Tobago", "🇹🇹", ["Port of Spain", "San Fernando", "Arima"]),
    "bz": ("Belize", "🇧🇿", ["Belmopan", "Belize City", "San Ignacio"]),
    "gt": ("Guatemala", "🇬🇹", ["Guatemala City", "Quetzaltenango"]),
    "hn": ("Honduras", "🇭🇳", ["Tegucigalpa", "San Pedro Sula", "La Ceiba"]),
    "sv": ("El Salvador", "🇸🇻", ["San Salvador", "Santa Ana", "San Miguel"]),
    "ni": ("Nicaragua", "🇳🇮", ["Managua", "Leon", "Granada"]),
    "do": ("Dominican Republic", "🇩🇴", ["Santo Domingo", "Santiago", "La Romana"]),
    "ht": ("Haiti", "🇭🇹", ["Port-au-Prince", "Cap-Haitien", "Gonaives"]),
    "bo": ("Bolivia", "🇧🇴", ["La Paz", "Sucre", "Santa Cruz"]),
    "ec": ("Ecuador", "🇪🇨", ["Quito", "Guayaquil", "Cuenca"]),
    "py": ("Paraguay", "🇵🇾", ["Asuncion", "Ciudad del Este", "Encarnacion"]),
    "gy": ("Guyana", "🇬🇾", ["Georgetown", "Linden", "New Amsterdam"]),
    "sr": ("Suriname", "🇸🇷", ["Paramaribo", "Lelydorp", "Nieuw Nickerie"]),
    "tz": ("Tanzania", "🇹🇿", ["Dodoma", "Dar es Salaam", "Arusha"]),
    "ug": ("Uganda", "🇺🇬", ["Kampala", "Entebbe", "Jinja"]),
    "rw": ("Rwanda", "🇷🇼", ["Kigali", "Butare", "Gisenyi"]),
    "zm": ("Zambia", "🇿🇲", ["Lusaka", "Kitwe", "Ndola"]),
    "zw": ("Zimbabwe", "🇿🇼", ["Harare", "Bulawayo", "Mutare"]),
    "bw": ("Botswana", "🇧🇼", ["Gaborone", "Francistown", "Maun"]),
    "na": ("Namibia", "🇳🇦", ["Windhoek", "Walvis Bay", "Swakopmund"]),
    "mz": ("Mozambique", "🇲🇿", ["Maputo", "Matola", "Nampula"]),
    "mg": ("Madagascar", "🇲🇬", ["Antananarivo", "Toamasina", "Antsirabe"]),
    "mu": ("Mauritius", "🇲🇺", ["Port Louis", "Curepipe", "Vacoas"]),
    "sc": ("Seychelles", "🇸🇨", ["Victoria", "Beau Vallon", "Anse Royale"]),
    "sn": ("Senegal", "🇸🇳", ["Dakar", "Touba", "Thiès"]),
    "ci": ("Côte d'Ivoire", "🇨🇮", ["Abidjan", "Yamoussoukro", "Bouake"]),
    "cm": ("Cameroon", "🇨🇲", ["Yaounde", "Douala", "Bamenda"]),
    "ao": ("Angola", "🇦🇴", ["Luanda", "Huambo", "Lobito"]),
    "ml": ("Mali", "🇲🇱", ["Bamako", "Sikasso", "Mopti"]),
    "bf": ("Burkina Faso", "🇧🇫", ["Ouagadougou", "Bobo-Dioulasso"]),
    "ne": ("Niger", "🇳🇪", ["Niamey", "Zinder", "Maradi"]),
    "td": ("Chad", "🇹🇩", ["N'Djamena", "Moundou", "Sarh"]),
    "so": ("Somalia", "🇸🇴", ["Mogadishu", "Hargeisa", "Kismayo"]),
    "sd": ("Sudan", "🇸🇩", ["Khartoum", "Omdurman", "Port Sudan"]),
    "ly": ("Libya", "🇱🇾", ["Tripoli", "Benghazi", "Misrata"]),
    "jo": ("Jordan", "🇯🇴", ["Amman", "Zarqa", "Irbid"]),
    "lb": ("Lebanon", "🇱🇧", ["Beirut", "Tripoli", "Sidon"]),
    "iq": ("Iraq", "🇮🇶", ["Baghdad", "Basra", "Mosul"]),
    "ir": ("Iran", "🇮🇷", ["Tehran", "Mashhad", "Isfahan"]),
    "il": ("Israel", "🇮🇱", ["Jerusalem", "Tel Aviv", "Haifa"]),
    "mc": ("Monaco", "🇲🇨", ["Monaco", "Monte Carlo"]),
    "li": ("Liechtenstein", "🇱🇮", ["Vaduz", "Schaan"]),
}

ALIASES = {
    "bangladesh": "bd", "বাংলাদেশ": "bd", "uae": "ae", "dubai": "ae",
    "india": "in", "usa": "us", "america": "us", "uk": "gb", "england": "gb",
    "germany": "de", "france": "fr", "italy": "it", "japan": "jp",
    "china": "cn", "canada": "ca", "australia": "au", "mexico": "mx"
}

# ==========================================
# LOCALIZED GENERATOR DATA
# ==========================================
BD_NAMES = [
    "মাহমুদুল হাসান", "শাহানা বেগম", "মোঃ রাকিব হাসান", "সুমাইয়া আক্তার",
    "আব্দুল্লাহ আল মামুন", "নুসরাত জাহান", "সাইফুল ইসলাম", "তানজিলা আক্তার",
    "আরিফ হোসেন", "ফারজানা আক্তার", "মেহেদী হাসান", "আয়েশা সিদ্দিকা"
]

BD_REAL_PLACES = {
    "Dhaka": {"city": "ঢাকা", "state": "ঢাকা বিভাগ", "postcode": "১২০৭", "streets": ["মোহাম্মদপুর বাস স্ট্যান্ড", "মিরপুর রোড", "ধানমন্ডি ২৭", "গ্রীন রোড"]},
    "Chattogram": {"city": "চট্টগ্রাম", "state": "চট্টগ্রাম বিভাগ", "postcode": "৪০০০", "streets": ["জিইসি মোড়", "সিডিএ এভিনিউ", "আগ্রাবাদ বা/এ", "স্টেশন রোড"]},
    "Rajshahi": {"city": "রাজশাহী", "state": "রাজশাহী বিভাগ", "postcode": "৬০০০", "streets": ["কাজলা মেইন রোড", "নিউ মার্কেট রোড", "গ্রেটার রোড"]},
    "Khulna": {"city": "খুলনা", "state": "খুলনা বিভাগ", "postcode": "৯০০০", "streets": ["খান এ সবুর রোড", "কেডিএ এভিনিউ", "যশোর রোড"]},
    "Barishal": {"city": "বরিশাল", "state": "বরিশাল বিভাগ", "postcode": "৮২০০", "streets": ["বরিশাল সদর", "সদর রোড", "সিএন্ডবি রোড"]},
    "Sylhet": {"city": "সিলেট", "state": "সিলেট বিভাগ", "postcode": "৩১০০", "streets": ["জিন্দাবাজার রোড", "দরগাহ গেট", "আম্বারখানা"]}
}

FIRST_NAMES = ["Michael", "James", "David", "Robert", "John", "William", "Daniel", "Alex", "Emma", "Sarah", "Sophia", "Olivia", "Emily"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Wilson", "Taylor", "Anderson"]

def get_code(value):
    value = value.strip().lower()
    if value in COUNTRIES:
        return value
    if value in ALIASES:
        return ALIASES[value]
    for code, info in COUNTRIES.items():
        if value == info[0].lower():
            return code
    return None

def generate_address(code):
    country, flag, cities = COUNTRIES[code]
    city = random.choice(cities)

    if code == "bd":
        name = random.choice(BD_NAMES)
        place = BD_REAL_PLACES.get(city, BD_REAL_PLACES["Dhaka"])
        road_no = random.randint(10, 150)
        bangla_nums = {'0':'০','1':'১','2':'২','3':'৩','4':'৪','5':'৫','6':'৬','7':'৭','8':'৮','9':'৯'}
        road_no_bn = "".join(bangla_nums.get(c, c) for c in str(road_no))
        street = f"{road_no_bn} {random.choice(place['streets'])}"
        city_disp = place["city"]
        state_disp = place["state"]
        postal_disp = place["postcode"]
    else:
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        number = random.randint(10, 999)
        block = random.choice(["A", "B", "C", "D", "E"])
        street = f"{number} Main Street, Block {block}"
        city_disp = city
        state_disp = f"{city} Emirate" if code == "ae" else (f"{city} State" if code != "gb" else "England")
        postal_disp = "N/A" if code == "ae" else str(random.randint(10000, 99999))

    return {
        "name": name,
        "street": street,
        "city": city_disp,
        "state": state_disp,
        "postal": postal_disp,
        "country": country,
        "flag": flag
    }

# ==========================================
# TAP-TO-COPY FORMATTING
# ==========================================
def format_address(data):
    return (
        f"<b>{data['country']} {data['flag']} Address</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{data['name']}</code>\n"
        f"– <b>Street:</b> <code>{data['street']}</code>\n"
        f"– <b>City:</b> <code>{data['city']}</code>\n"
        f"– <b>State:</b> <code>{data['state']}</code>\n"
        f"– <b>Postal Code:</b> <code>{data['postal']}</code>\n"
        f"– <b>Country:</b> <code>{data['country']}</code>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"<i>⚠ Synthetic/Test Address</i>"
    )

def generate_button(code):
    return {
        "inline_keyboard": [
            [{"text": "🔄 Generate", "callback_data": "generate:" + code}]
        ]
    }

# ==========================================
# TELEGRAM API REQUESTS
# ==========================================
def api(method, data=None):
    if data is None:
        data = {}
    url = API + method
    encoded = urllib.parse.urlencode(data).encode("utf-8")

    try:
        request = urllib.request.Request(url, data=encoded)
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
    return api("answerCallbackQuery", {"callback_query_id": callback_id})

# ==========================================
# BOT HANDLERS
# ==========================================
def handle_message(message):
    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if text.startswith("/start"):
        send_message(
            chat_id,
            "<b>🟣 RAVEN ADDRESS GENERATOR</b>\n\n"
            "Country code দিয়ে address generate করো।\n\n"
            "<code>/fake bd</code>\n"
            "<code>/fake ae</code>\n"
            "<code>/fake us</code>\n\n"
            "🔄 Generate চাপলে একই message-এ নতুন address আসবে।"
        )
        return

    if text.startswith("/countries"):
        send_message(chat_id, "<b>🌍 121 COUNTRIES SUPPORTED</b>\n\nExample:\n<code>/fake bd</code>\n<code>/fake us</code>")
        return

    if text.lower().startswith("/fake"):
        parts = text.split()
        if len(parts) < 2:
            send_message(chat_id, "❌ Country code দিন।\n\nExample:\n<code>/fake bd</code>")
            return

        code = get_code(parts[1])
        if not code:
            send_message(chat_id, "❌ Country পাওয়া যায়নি।")
            return

        address = generate_address(code)
        text_out = format_address(address)
        keyboard = generate_button(code)
        send_message(chat_id, text_out, keyboard)

def handle_callback(callback):
    callback_id = callback["id"]
    data = callback.get("data", "")
    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    answer_callback(callback_id)

    if data.startswith("generate:"):
        code = data.split(":", 1)[1]
        if code not in COUNTRIES:
            return

        new_address = generate_address(code)
        new_text = format_address(new_address)
        keyboard = generate_button(code)
        edit_message(chat_id, message_id, new_text, keyboard)

# ==========================================
# MAIN LOOP
# ==========================================
def run_bot():
    print("==============================")
    print(" RAVEN ADDRESS GENERATOR")
    print("==============================")
    print("Countries:", len(COUNTRIES))
    
    # Drop pending updates to fix 409 Conflict Error
    api("deleteWebhook", {"drop_pending_updates": True})
    
    print("Bot is running...")
    print("")

    offset = 0
    while True:
        try:
            result = api("getUpdates", {"timeout": 50, "offset": offset})
            if not result or not result.get("ok"):
                time.sleep(3)
                continue

            updates = result.get("result", [])
            for update in updates:
                offset = update["update_id"] + 1

                if "message" in update:
                    try:
                        handle_message(update["message"])
                    except Exception as e:
                        print("MESSAGE ERROR:", e)

                elif "callback_query" in update:
                    try:
                        handle_callback(update["callback_query"])
                    except Exception as e:
                        print("CALLBACK ERROR:", e)

        except KeyboardInterrupt:
            print("\nBot stopped.")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
