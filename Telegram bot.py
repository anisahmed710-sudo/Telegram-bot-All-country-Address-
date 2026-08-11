import requests
import random
import time
import json
import html
import urllib.parse

# ==============================
# SETTINGS
# ==============================

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"
REST_COUNTRIES_KEY = "Rc_live_317037a7db864904b9a3695f31b68e57"

TELEGRAM_API = (
    "https://api.telegram.org/bot"
    + BOT_TOKEN + "/"
)

COUNTRIES_API = (
    "https://api.restcountries.com/countries/v5"
)

CITIES_API = (
    "https://countriesnow.space/api/v0.1/countries/cities"
)


# ==============================
# COUNTRY ALIASES
# ==============================

COUNTRY_ALIASES = {
    "bd": "Bangladesh",
    "bangladesh": "Bangladesh",
    "in": "India",
    "india": "India",
    "pk": "Pakistan",
    "pakistan": "Pakistan",
    "usa": "United States",
    "us": "United States",
    "america": "United States",
    "united states": "United States",
    "uk": "United Kingdom",
    "united kingdom": "United Kingdom",
    "uae": "United Arab Emirates",
    "dubai": "United Arab Emirates",
    "united arab emirates": "United Arab Emirates",
    "oman": "Oman",
    "om": "Oman",
    "qatar": "Qatar",
    "qa": "Qatar",
    "saudi arabia": "Saudi Arabia",
    "spain": "Spain",
    "france": "France",
    "germany": "Germany",
    "italy": "Italy",
    "portugal": "Portugal",
    "japan": "Japan",
    "china": "China",
    "south korea": "South Korea",
    "malaysia": "Malaysia",
    "singapore": "Singapore",
    "indonesia": "Indonesia",
    "australia": "Australia",
    "canada": "Canada",
    "brazil": "Brazil",
    "mexico": "Mexico",
    "turkey": "Turkey",
    "nepal": "Nepal",
    "sri lanka": "Sri Lanka"
}


# ==============================
# DEMO NAMES
# ==============================

NAMES = [
    "মাহমুদুল হাসান",
    "সাইফুল ইসলাম",
    "রাকিব হাসান",
    "নুসরাত জাহান",
    "সুমাইয়া আক্তার",
    "Aarav Sharma",
    "Priya Singh",
    "Rahul Verma",
    "Ananya Patel",
    "James Williams",
    "Emily Wilson",
    "Daniel Brown",
    "Olivia Davis",
    "Lucía Martínez",
    "Sofia García",
    "Ahmed Hassan",
    "Fatima Ali",
    "Yuki Tanaka",
    "Haruto Sato",
    "Mehmet Kaya",
    "Anna Weber",
    "Marco Rossi"
]


# ==============================
# STREET
# ==============================

STREETS = [
    "Fictional Main Street",
    "Fictional Central Road",
    "Fictional Market Road",
    "Fictional Garden Street",
    "Fictional Park Avenue",
    "Fictional Station Road",
    "Fictional Riverside Road"
]


def make_street():
    number = random.randint(100, 999)
    street = random.choice(STREETS)
    block = random.choice(["A", "B", "C", "D"])
    return f"{number} {street}, Block {block}"


# ==============================
# CITY FAMOUS
# ==============================

CITY_FAMOUS = {
    "Dhaka": "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Chattogram": "সমুদ্রবন্দর, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Rajshahi": "আম, রেশম ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Khulna": "সুন্দরবন ও শিল্পাঞ্চলের জন্য বিখ্যাত",
    "Barishal": "নদী, খাল ও পেয়ারা বাগানের জন্য বিখ্যাত",
    "Sylhet": "চা-বাগান, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Rangpur": "কৃষি ও ঐতিহ্যের জন্য বিখ্যাত",
    "Mumbai": "Bollywood, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
    "Delhi": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Kolkata": "সাহিত্য, সংস্কৃতি ও ঐতিহ্যের জন্য বিখ্যাত",
    "Bengaluru": "প্রযুক্তি ও IT industry-এর জন্য বিখ্যাত",
    "Chennai": "শিল্প, প্রযুক্তি ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Hyderabad": "প্রযুক্তি, খাবার ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Pune": "শিক্ষা, প্রযুক্তি ও শিল্পের জন্য বিখ্যাত",
    "Madrid": "রাজধানী, শিল্প, সংস্কৃতি ও ফুটবলের জন্য বিখ্যাত",
    "Barcelona": "Gaudí স্থাপত্য, সমুদ্রসৈকত ও ফুটবলের জন্য বিখ্যাত",
    "Valencia": "সমুদ্রসৈকত, Paella ও City of Arts-এর জন্য বিখ্যাত",
    "Seville": "Flamenco, ইতিহাস ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",
    "New York": "Times Square, Wall Street ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Los Angeles": "Hollywood ও চলচ্চিত্র শিল্পের জন্য বিখ্যাত",
    "Chicago": "স্থাপত্য, ব্যবসা ও Lake Michigan-এর জন্য বিখ্যাত",
    "Houston": "Space Center, energy industry ও ব্যবসার জন্য বিখ্যাত",
    "Miami": "সমুদ্রসৈকত, পর্যটন ও nightlife-এর জন্য বিখ্যাত",
    "Boston": "শিক্ষা, ইতিহাস ও গবেষণার জন্য বিখ্যাত",
    "Seattle": "Technology ও সমুদ্রের জন্য বিখ্যাত",
    "Muscat": "রাজধানী, সমুদ্র, পাহাড় ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",
    "Salalah": "খারিফ মৌসুম, সবুজ পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Sohar": "বন্দর, শিল্প ও ঐতিহাসিক ঐতিহ্যের জন্য বিখ্যাত",
    "Nizwa": "দুর্গ, বাজার ও ঐতিহ্যের জন্য বিখ্যাত",
    "Sur": "নৌকা নির্মাণ ও সমুদ্রের জন্য বিখ্যাত",
    "Khasab": "Musandam-এর পাহাড় ও সমুদ্রের জন্য বিখ্যাত",
    "Rustaq": "ঐতিহাসিক দুর্গ ও উষ্ণ প্রস্রবণের জন্য বিখ্যাত",
    "Dubai": "আকাশচুম্বী ভবন, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Abu Dhabi": "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Sharjah": "সংস্কৃতি, জাদুঘর ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Ajman": "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",
    "Al Ain": "ওয়েসিস, সবুজ পরিবেশ ও ঐতিহ্যের জন্য বিখ্যাত",
    "Fujairah": "পাহাড়, সমুদ্র ও diving-এর জন্য বিখ্যাত",
    "Ras Al Khaimah": "পাহাড়, adventure tourism ও সমুদ্রের জন্য বিখ্যাত",
    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Osaka": "ব্যবসা, খাবার ও বিনোদনের জন্য বিখ্যাত",
    "Kyoto": "প্রাচীন মন্দির, ঐতিহ্য ও সংস্কৃতির জন্য বিখ্যাত",
    "Yokohama": "বন্দর, সমুদ্র ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Nagoya": "Automobile industry ও শিল্পের জন্য বিখ্যাত",
    "Sapporo": "তুষার, শীতকালীন ক্রীড়া ও খাবারের জন্য বিখ্যাত",
    "Fukuoka": "খাবার, বন্দর ও ব্যবসার জন্য বিখ্যাত",
    "London": "রাজধানী, ইতিহাস, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Manchester": "ফুটবল, শিল্প ও সঙ্গীতের জন্য বিখ্যাত",
    "Birmingham": "শিল্প, ব্যবসা ও সংস্কৃতির জন্য বিখ্যাত",
    "Liverpool": "The Beatles, football ও বন্দরনগরী হিসেবে বিখ্যাত",
    "Paris": "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
    "Berlin": "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",
    "Munich": "Bavarian culture, industry ও Oktoberfest-এর জন্য বিখ্যাত",
    "Hamburg": "বন্দর ও বাণিজ্যের জন্য বিখ্যাত",
    "Frankfurt": "Finance ও ব্যবসার জন্য বিখ্যাত",
    "Rome": "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",
    "Milan": "Fashion, design ও ব্যবসার জন্য বিখ্যাত",
    "Naples": "Pizza, ইতিহাস ও সমুদ্রের জন্য বিখ্যাত",
    "Florence": "Renaissance art ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Venice": "খাল, gondola ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Beijing": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Shanghai": "Finance, বন্দর ও আধুনিক skyline-এর জন্য বিখ্যাত",
    "Guangzhou": "বাণিজ্য, শিল্প ও Canton Fair-এর জন্য বিখ্যাত",
    "Shenzhen": "Technology, innovation ও manufacturing-এর জন্য বিখ্যাত",
    "Chengdu": "Panda, খাবার ও প্রযুক্তির জন্য বিখ্যাত",
    "Wuhan": "শিক্ষা, শিল্প ও Yangtze River-এর জন্য বিখ্যাত",
    "Xi'an": "Terracotta Army ও প্রাচীন ইতিহাসের জন্য বিখ্যাত",
    "Toronto": "ব্যবসা, সংস্কৃতি ও CN Tower-এর জন্য বিখ্যাত",
    "Vancouver": "পাহাড়, সমুদ্র ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Montreal": "সংস্কৃতি, খাবার ও French heritage-এর জন্য বিখ্যাত",
    "Calgary": "Energy industry ও Rocky Mountains-এর জন্য বিখ্যাত",
    "Ottawa": "কানাডার রাজধানী ও Parliament-এর জন্য বিখ্যাত",
    "Sydney": "Opera House, Harbour ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Melbourne": "সংস্কৃতি, ক্রীড়া ও খাবারের জন্য বিখ্যাত"
}


# ==============================
# COUNTRY FOOD
# ==============================

COUNTRY_FOOD = {
    "Bangladesh": "ভাত, মাছ, ডাল ও ভর্তা",
    "India": "ভাত, রুটি, ডাল ও বিভিন্ন আঞ্চলিক খাবার",
    "Pakistan": "বিরিয়ানি, নিহারি ও বিভিন্ন স্থানীয় খাবার",
    "Spain": "Paella, Tapas ও Tortilla Española",
    "United States": "Burger, Barbecue, Steak ও আঞ্চলিক খাবার",
    "United Kingdom": "Fish and Chips, Roast ও Pie",
    "Oman": "Shuwa, Majboos ও সামুদ্রিক খাবার",
    "United Arab Emirates": "Machboos, Hummus ও Shawarma",
    "Qatar": "Machboos, Harees ও Dates",
    "Japan": "Sushi, Ramen ও Tempura",
    "China": "Rice, Noodles ও বিভিন্ন আঞ্চলিক খাবার",
    "Malaysia": "Nasi Lemak, Satay ও Laksa",
    "France": "Baguette, Cheese ও বিভিন্ন আঞ্চলিক খাবার",
    "Germany": "Bratwurst, Bread ও Schnitzel",
    "Italy": "Pizza, Pasta ও Risotto",
    "Turkey": "Kebab, Pide ও Baklava",
    "Canada": "Poutine, Salmon ও বিভিন্ন আঞ্চলিক খাবার",
    "Australia": "Meat Pie, Seafood ও Barbecue"
}


# ==============================
# COUNTRY JOBS
# ==============================

COUNTRY_JOBS = {
    "Bangladesh": "Garments / Agriculture / Business / Services",
    "India": "IT / Business / Manufacturing / Services",
    "Pakistan": "Textile / Agriculture / Services",
    "Spain": "Tourism / Services / Industry",
    "United States": "Technology / Finance / Services / Manufacturing",
    "United Kingdom": "Finance / Services / Technology",
    "Oman": "Energy / Tourism / Services",
    "United Arab Emirates": "Business / Tourism / Finance",
    "Qatar": "Energy / Construction / Business",
    "Japan": "Technology / Automobile / Industry",
    "China": "Manufacturing / Technology / Trade",
    "Malaysia": "Manufacturing / Services / Business",
    "France": "Tourism / Services / Industry",
    "Germany": "Engineering / Manufacturing / Services",
    "Italy": "Manufacturing / Fashion / Tourism",
    "Turkey": "Manufacturing / Tourism / Services",
    "Canada": "Services / Energy / Technology",
    "Australia": "Mining / Services / Agriculture"
}


# ==============================
# FALLBACK CITIES
# ==============================

FALLBACK_CITIES = {
    "Bangladesh": ["Dhaka", "Chattogram", "Rajshahi", "Khulna", "Barishal", "Sylhet", "Rangpur"],
    "India": ["Mumbai", "Delhi", "Kolkata", "Bengaluru", "Chennai", "Hyderabad", "Pune"],
    "United States": ["New York", "Los Angeles", "Chicago", "Houston", "Miami", "Boston", "Seattle"],
    "Oman": ["Muscat", "Salalah", "Sohar", "Nizwa", "Sur", "Khasab", "Rustaq"],
    "United Arab Emirates": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", "Al Ain", "Fujairah", "Ras Al Khaimah"],
    "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Málaga", "Bilbao", "Alicante"],
    "Japan": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo", "Fukuoka"],
    "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Wuhan", "Xi'an"],
    "United Kingdom": ["London", "Manchester", "Birmingham", "Liverpool", "Leeds", "Bristol", "Edinburgh"],
    "France": ["Paris", "Lyon", "Marseille", "Toulouse", "Nice", "Bordeaux", "Lille"],
    "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart", "Dresden"],
    "Italy": ["Rome", "Milan", "Naples", "Turin", "Florence", "Bologna", "Venice"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton", "Quebec City"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra", "Hobart"],
    "Pakistan": ["Islamabad", "Karachi", "Lahore", "Peshawar", "Quetta", "Multan", "Faisalabad"],
    "Qatar": ["Doha", "Al Rayyan", "Al Wakrah", "Umm Salal", "Al Khor", "Dukhan", "Mesaieed"]
}

# ==============================
# VERIFIED POLITICAL DATA
# ==============================

POLITICAL_DATA = {
    "BD": {
        "head_title": "Prime Minister",
        "head_name": "তারেক রহমান",
        "rep_title": "Running MP",
        "locations": {
            "Dhaka": {"seat": "ঢাকা-১৭ আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Chattogram": {"seat": "চট্টগ্রাম-XX আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Rajshahi": {"seat": "রাজশাহী-১ আসন", "name": "মোঃ মুজিবুর রহমান"},
            "Khulna": {"seat": "খুলনা-XX আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Barishal": {"seat": "বরিশাল-XX আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Sylhet": {"seat": "সিলেট-XX আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Rangpur": {"seat": "রংপুর-XX আসন", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"}
        }
    },
    "IN": {
        "head_title": "Prime Minister",
        "head_name": "নরেন্দ্র মোদি",
        "rep_title": "Running Lok Sabha MP",
        "locations": {
            "Mumbai": {"seat": "Mumbai North-West Lok Sabha আসন", "name": "রবীন্দ্র দত্তারাম ওয়াইকর"},
            "Delhi": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Kolkata": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Bengaluru": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Chennai": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Hyderabad": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"},
            "Pune": {"seat": "Lok Sabha constituency", "name": "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"}
        }
    },
    "US": {
        "head_title": "President",
        "head_name": "Donald J. Trump",
        "rep_title": "Running U.S. Representative",
        "locations": {
            "New York": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Los Angeles": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Chicago": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Houston": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Miami": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Boston": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"},
            "Seattle": {"seat": "Congressional District", "name": "District অনুযায়ী বর্তমান Representative"}
        }
    },
    "OM": {
        "head_title": "Sultan",
        "head_name": "হাইথাম বিন তারিক",
        "rep_title": "Running Shura Council Member",
        "locations": {
            "Muscat": {"seat": "Muscat Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Salalah": {"seat": "Salalah Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Sohar": {"seat": "Sohar Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Nizwa": {"seat": "Nizwa Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Sur": {"seat": "Sur Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Khasab": {"seat": "Khasab Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"},
            "Rustaq": {"seat": "Rustaq Wilayat", "name": "বর্তমান সদস্য যাচাই প্রয়োজন"}
        }
    }
}


# ==============================
# TELEGRAM REQUEST
# ==============================

def tg_request(method, data=None):
    try:
        response = requests.post(
            TELEGRAM_API + method,
            data=data or {},
            timeout=60
        )
        return response.json()
    except Exception as e:
        print("Telegram Error:", e)
        return None


# ==============================
# REST COUNTRIES
# ==============================

def get_country(country):
    url = (
        COUNTRIES_API
        + "/names.common/"
        + urllib.parse.quote(country, safe="")
    )
    headers = {
        "Authorization": "Bearer " + REST_COUNTRIES_KEY.strip()
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code != 200:
            print("REST Countries ERROR:", response.status_code)
            print(response.text)
            return None

        result = response.json()
        if "_demo" in result.get("data", {}):
            print("❌ DEMO API KEY")
            return None

        objects = result.get("data", {}).get("objects", [])
        if not objects:
            return None

        return objects[0]

    except Exception as e:
        print("Country API Error:", e)
        return None


# ==============================
# CITIES API
# ==============================

def get_api_cities(country):
    try:
        response = requests.post(
            CITIES_API,
            json={"country": country},
            timeout=30
        )
        if response.status_code != 200:
            return []

        result = response.json()
        if result.get("error", True):
            return []

        cities = result.get("data", [])
        final = []
        for city in cities:
            city = str(city).strip()
            if city and city not in final:
                final.append(city)

        return final

    except Exception as e:
        print("City API Error:", e)
        return []


# ==============================
# LOCATIONS
# ==============================

def get_locations(country, capital):
    locations = []
    if country in FALLBACK_CITIES:
        locations.extend(FALLBACK_CITIES[country])

    if len(locations) < 7:
        api_cities = get_api_cities(country)
        for city in api_cities:
            if city not in locations:
                locations.append(city)
            if len(locations) >= 7:
                break

    if capital != "N/A" and capital not in locations:
        locations.insert(0, capital)

    final = []
    for city in locations:
        if city not in final:
            final.append(city)

    return final[:7]


# ==============================
# POSTAL
# ==============================

POSTAL_EXAMPLES = {
    "Bangladesh": "1000",
    "India": "400001",
    "United States": "10001",
    "United Kingdom": "SW1A 1AA",
    "Oman": "100",
    "United Arab Emirates": "00000",
    "Spain": "28001",
    "Japan": "100-0001",
    "China": "100000",
    "France": "75001",
    "Germany": "10115",
    "Italy": "00100",
    "Canada": "K1A 0A1",
    "Australia": "2000",
    "Pakistan": "44000",
    "Qatar": "00000"
}


def get_postal(country, api_data):
    if country in POSTAL_EXAMPLES:
        return POSTAL_EXAMPLES[country]

    postal = api_data.get("postal_code", {})
    if postal.get("format"):
        return postal["format"]

    return "N/A"


# ==============================
# POLITICAL
# ==============================

def get_political(country_code, city):
    data = POLITICAL_DATA.get(country_code)
    if not data:
        return {
            "head": "Current leader data unavailable",
            "rep_title": "Running Representative",
            "rep_name": "Verified current representative unavailable",
            "seat": "N/A"
        }

    head = data["head_title"] + ": " + data["head_name"]
    locations = data.get("locations", {})

    if city in locations:
        item = locations[city]
        return {
            "head": head,
            "rep_title": data["rep_title"],
            "rep_name": item["name"],
            "seat": item["seat"]
        }

    return {
        "head": head,
        "rep_title": data["rep_title"],
        "rep_name": "Verified current representative unavailable",
        "seat": "N/A"
    }


# ==============================
# FORMAT NUMBERS
# ==============================

def population(data):
    value = data.get("population")
    if value is None:
        return "N/A"
    try:
        return f"{int(value):,}"
    except:
        return str(value)


def area(data):
    value = data.get("area", {}).get("kilometers")
    if value is None:
        return "N/A"
    try:
        return f"{int(value):,} km²"
    except:
        return str(value) + " km²"


# ==============================
# GENERATE RECORD
# ==============================

def generate_record(country, old_city=""):
    data = get_country(country)
    if not data:
        return None

    names = data.get("names", {})
    real_country = names.get("common", country)
    flag = data.get("flag", {}).get("emoji", "")
    codes = data.get("codes", {})
    country_code = codes.get("alpha_2", "")

    capitals = data.get("capitals", [])
    if capitals:
        capital = capitals[0].get("name", "N/A")
    else:
        capital = "N/A"

    locations = get_locations(real_country, capital)
    if not locations:
        locations = [capital]

    choices = [city for city in locations if city != old_city]
    if not choices:
        choices = locations

    city = random.choice(choices)

    if real_country == "Bangladesh":
        state = city + " Division"
        division = city
    else:
        state = data.get("subregion", data.get("region", "Regional area"))
        division = city

    political = get_political(country_code, city)

    return {
        "country": real_country,
        "flag": flag,
        "head": political["head"],
        "name": random.choice(NAMES),
        "street": make_street(),
        "city": city,
        "famous": CITY_FAMOUS.get(city, "স্থানীয় ইতিহাস, সংস্কৃতি, ব্যবসা ও পর্যটনের জন্য পরিচিত"),
        "state": state,
        "postal": get_postal(real_country, data),
        "population": population(data),
        "division": division,
        "rep_title": political["rep_title"],
        "rep_name": political["rep_name"],
        "seat": political["seat"],
        "area": area(data),
        "food": COUNTRY_FOOD.get(real_country, "স্থানীয় খাবার"),
        "jobs": COUNTRY_JOBS.get(real_country, "Business / Services / Industry"),
        "duty": random.choice(["সাধারণত ৮ ঘণ্টা", "সাধারণত ৮–৯ ঘণ্টা", "সাধারণত ৮–১০ ঘণ্টা"])
    }


# ==============================
# MESSAGE FORMAT (WITH MONO TAGS `<code>...</code>`)
# ==============================

def format_message(d):
    return (
        f"<b>{html.escape(d['country'])} {d['flag']} ({html.escape(d['head'])})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{html.escape(d['name'])}</code>\n"
        f"– <b>Street:</b> <code>{html.escape(d['street'])}</code>\n"
        f"– <b>City:</b> <code>{html.escape(d['city'])}</code>\n"
        f"  ↳ <b>বিখ্যাত:</b> {html.escape(d['famous'])}\n"
        f"– <b>State/Region:</b> <code>{html.escape(d['state'])}</code>\n"
        f"– <b>Postal Code:</b> <code>{html.escape(str(d['postal']))}</code>\n"
        f"– <b>Country Population:</b> {html.escape(str(d['population']))}\n"
        f"– <b>Division/Constituency:</b> <code>{html.escape(d['division'])}</code>\n"
        f"  ↳ <b>{html.escape(d['rep_title'])}:</b> {html.escape(d['rep_name'])} — {html.escape(d['seat'])}\n"
        f"– <b>Country Area:</b> {html.escape(d['area'])}\n"
        f"– <b>প্রধান খাদ্য:</b> {html.escape(d['food'])}\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> {html.escape(d['jobs'])}\n"
        f"– <b>Job Duty Hour:</b> {html.escape(d['duty'])}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )


# ==============================
# COPY ADDRESS TEXT
# ==============================

def copy_text(d):
    return (
        f"Name: {d['name']}\n"
        f"Street: {d['street']}\n"
        f"City: {d['city']}\n"
        f"State/Region: {d['state']}\n"
        f"Postal Code: {d['postal']}\n"
        f"Country: {d['country']}"
    )


# ==============================
# KEYBOARD (GENERATE & COPY BUTTON)
# ==============================

def make_keyboard(country, record):
    c = urllib.parse.quote(country, safe="")
    old = urllib.parse.quote(record["city"], safe="")
    callback = "GEN|" + c + "|" + old

    copied = copy_text(record)

    return json.dumps({
        "inline_keyboard": [
            [
                {
                    "text": "📋 Copy Address",
                    "copy_text": {
                        "text": copied[:256]
                    }
                }
            ],
            [
                {
                    "text": "🔄 Generate",
                    "callback_data": callback
                }
            ]
        ]
    }, ensure_ascii=False)


# ==============================
# SEND & EDIT MESSAGES
# ==============================

def send_message(chat_id, text, keyboard=None):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    if keyboard:
        payload["reply_markup"] = keyboard

    return tg_request("sendMessage", payload)


def edit_message(chat_id, message_id, text, keyboard):
    return tg_request(
        "editMessageText",
        {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
            "reply_markup": keyboard
        }
    )


def answer_callback(callback_id):
    return tg_request(
        "answerCallbackQuery",
        {"callback_query_id": callback_id}
    )


# ==============================
# HANDLERS
# ==============================

def handle_start(message):
    chat_id = message.get("chat", {}).get("id")
    text = (
        "<b>🌍 LIVE COUNTRY GENERATOR</b>\n\n"
        "Country লিখে Generate করুন।\n\n"
        "<code>/fake Bangladesh</code>\n"
        "<code>/fake India</code>\n"
        "<code>/fake USA</code>\n"
        "<code>/fake Oman</code>\n"
        "<code>/fake Spain</code>\n"
        "<code>/fake Japan</code>\n"
        "<code>/fake Malaysia</code>\n"
        "<code>/fake Qatar</code>\n\n"
        "📋 টেক্সটের ওপর ট্যাপ করলে বা 'Copy Address' চাপলে সরাসরি কপি হবে।"
    )
    send_message(chat_id, text)


def handle_fake(message):
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip()

    parts = text.split(None, 1)
    if len(parts) < 2:
        send_message(chat_id, "❌ Country লিখুন।\n\n<code>/fake Bangladesh</code>")
        return

    raw = parts[1].strip().lower()
    country = COUNTRY_ALIASES.get(raw, parts[1].strip())

    record = generate_record(country)
    if not record:
        send_message(chat_id, "❌ Country data পাওয়া যায়নি।")
        return

    msg_text = format_message(record)
    keyboard = make_keyboard(country, record)

    send_message(chat_id, msg_text, keyboard)


def handle_callback(callback):
    answer_callback(callback.get("id"))
    data = callback.get("data", "")

    if not data.startswith("GEN|"):
        return

    parts = data.split("|", 2)
    country = urllib.parse.unquote(parts[1])
    old_city = urllib.parse.unquote(parts[2]) if len(parts) > 2 else ""

    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    new_record = generate_record(country, old_city)
    if not new_record:
        return

    msg_text = format_message(new_record)
    keyboard = make_keyboard(country, new_record)

    edit_message(chat_id, message_id, msg_text, keyboard)


# ==============================
# BOT LOOP
# ==============================

def run_bot():
    print("================================")
    print("🌍 LIVE COUNTRY GENERATOR")
    print("================================")
    print("REST Countries API: CONNECTED")
    print("Telegram Bot: STARTING...\n")

    offset = 0

    while True:
        try:
            result = tg_request("getUpdates", {"timeout": 50, "offset": offset})

            if not result:
                time.sleep(2)
                continue

            if not result.get("ok", False):
                print("Telegram ERROR:", result)
                time.sleep(5)
                continue

            updates = result.get("result", [])
            for update in updates:
                offset = update["update_id"] + 1

                if "message" in update:
                    message = update["message"]
                    text = message.get("text", "")

                    try:
                        if text.startswith("/start"):
                            handle_start(message)
                        elif text.lower().startswith("/fake"):
                            handle_fake(message)
                    except Exception as e:
                        print("Message ERROR:", e)

                elif "callback_query" in update:
                    try:
                        handle_callback(update["callback_query"])
                    except Exception as e:
                        print("Callback ERROR:", e)

        except KeyboardInterrupt:
            print("BOT STOPPED")
            break
        except Exception as e:
            print("MAIN LOOP ERROR:", e)
            time.sleep(5)


# ==============================
# START PROGRAM
# ==============================

if __name__ == "__main__":
    if BOT_TOKEN.startswith("PASTE_") or REST_COUNTRIES_KEY.startswith("PASTE_"):
        print("\n❌ BOT_TOKEN এবং REST_COUNTRIES_KEY বসাও।\n")
    else:
        run_bot()
