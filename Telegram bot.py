# -*- coding: utf-8 -*-

import requests
import json
import random
import time
import html
import urllib.parse

# =========================================================
# QPYTHON TELEGRAM COUNTRY BOT
# FULL SINGLE-FILE SCRIPT WITH MONO & COPY BUTTON
# =========================================================

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"
REST_COUNTRIES_KEY = "Rc_live_317037a7db864904b9a3695f31b68e57"

TG = "https://api.telegram.org/bot" + BOT_TOKEN + "/"
RC = "https://api.restcountries.com/countries/v5"


COUNTRY_ALIASES = {
    "bd": "Bangladesh",
    "bangladesh": "Bangladesh",
    "in": "India",
    "india": "India",
    "us": "United States",
    "usa": "United States",
    "america": "United States",
    "united states": "United States",
    "ae": "United Arab Emirates",
    "uae": "United Arab Emirates",
    "dubai": "United Arab Emirates",
    "united arab emirates": "United Arab Emirates",
    "om": "Oman",
    "oman": "Oman",
    "qa": "Qatar",
    "qatar": "Qatar",
    "my": "Malaysia",
    "malaysia": "Malaysia",
    "jp": "Japan",
    "japan": "Japan",
    "cn": "China",
    "china": "China",
    "pk": "Pakistan",
    "pakistan": "Pakistan",
    "es": "Spain",
    "spain": "Spain",
    "pt": "Portugal",
    "portugal": "Portugal",
    "fr": "France",
    "france": "France",
    "de": "Germany",
    "germany": "Germany",
    "it": "Italy",
    "italy": "Italy",
    "uk": "United Kingdom",
    "united kingdom": "United Kingdom",
    "ca": "Canada",
    "canada": "Canada",
    "au": "Australia",
    "australia": "Australia",
    "tr": "Turkey",
    "turkey": "Turkey",
    "np": "Nepal",
    "nepal": "Nepal",
    "lk": "Sri Lanka",
    "sri lanka": "Sri Lanka",
    "sg": "Singapore",
    "singapore": "Singapore",
    "br": "Brazil",
    "brazil": "Brazil",
    "mx": "Mexico",
    "mexico": "Mexico"
}


NAMES = {
    "Bangladesh": [
        "মাহমুদুল হাসান",
        "সাইফুল ইসলাম",
        "রাকিব হাসান",
        "নুসরাত জাহান",
        "সুমাইয়া আক্তার",
        "তানভীর আহমেদ",
        "আরিফ হোসেন"
    ],

    "India": [
        "Aarav Sharma",
        "Priya Singh",
        "Rahul Verma",
        "Ananya Patel",
        "Arjun Mehta",
        "Neha Gupta",
        "Rohan Kumar"
    ],

    "United States": [
        "James Williams",
        "Emily Wilson",
        "Daniel Brown",
        "Olivia Davis",
        "Michael Johnson",
        "Sophia Miller",
        "Ethan Anderson"
    ],

    "Oman": [
        "Ahmed Al Balushi",
        "Salim Al Harthy",
        "Fatma Al Hinai",
        "Said Al Rashdi",
        "Maryam Al Lawati"
    ],

    "United Arab Emirates": [
        "Ahmed Hassan",
        "Omar Abdullah",
        "Fatima Ali",
        "Sara Mohammed",
        "Khalid Ahmed"
    ],

    "Qatar": [
        "Mohammed Al Thani",
        "Ahmed Al Kuwari",
        "Fatima Al Sulaiti",
        "Noura Al Ali"
    ],

    "Japan": [
        "Yuki Tanaka",
        "Haruto Sato",
        "Aoi Suzuki",
        "Hana Watanabe"
    ]
}


DEFAULT_NAMES = [
    "James Williams",
    "Michael Davis",
    "Emma Anderson",
    "Daniel Wilson",
    "Sophia Martin",
    "Alexander Thomas",
    "Olivia Taylor"
]


STREET_NAMES = [
    "Central Road",
    "Market Road",
    "Garden Street",
    "Station Road",
    "Park Avenue",
    "Riverside Road",
    "Main Street"
]


COUNTRY_FOOD = {
    "Bangladesh": "ভাত, মাছ, ডাল ও ভর্তা",
    "India": "ভাত, রুটি, ডাল ও বিভিন্ন আঞ্চলিক খাবার",
    "United States": "Burger, Barbecue, Steak ও বিভিন্ন আঞ্চলিক খাবার",
    "Oman": "Shuwa, Majboos ও সামুদ্রিক খাবার",
    "United Arab Emirates": "Machboos, Hummus ও Shawarma",
    "Qatar": "Machboos, Harees ও খেজুর",
    "Japan": "Sushi, Ramen ও Tempura",
    "China": "Rice, Noodles ও বিভিন্ন আঞ্চলিক খাবার",
    "Malaysia": "Nasi Lemak, Satay ও Laksa",
    "Spain": "Paella, Tapas ও Tortilla Española",
    "Portugal": "Bacalhau, Pastel de Nata ও সামুদ্রিক খাবার",
    "France": "Baguette, Cheese ও বিভিন্ন স্থানীয় খাবার",
    "Germany": "Bratwurst, Bread ও Schnitzel",
    "Italy": "Pizza, Pasta ও Risotto",
    "Pakistan": "Biryani, Nihari ও বিভিন্ন স্থানীয় খাবার",
    "United Kingdom": "Fish and Chips, Roast ও Pie",
    "Canada": "Poutine, Salmon ও বিভিন্ন স্থানীয় খাবার",
    "Australia": "Meat Pie, Seafood ও Barbecue",
    "Turkey": "Kebab, Pide ও Baklava",
    "Singapore": "Hainanese Chicken Rice, Laksa ও Satay"
}


COUNTRY_JOBS = {
    "Bangladesh": "Garments / Agriculture / Business / Services",
    "India": "IT / Business / Manufacturing / Services",
    "United States": "Technology / Finance / Services / Manufacturing",
    "Oman": "Energy / Tourism / Services",
    "United Arab Emirates": "Business / Tourism / Finance",
    "Qatar": "Energy / Construction / Business",
    "Japan": "Technology / Automobile / Industry",
    "China": "Manufacturing / Technology / Trade",
    "Malaysia": "Manufacturing / Services / Business",
    "Spain": "Tourism / Services / Industry",
    "France": "Tourism / Services / Industry",
    "Germany": "Engineering / Manufacturing / Services",
    "Italy": "Manufacturing / Fashion / Tourism",
    "Pakistan": "Textile / Agriculture / Services",
    "United Kingdom": "Finance / Services / Technology",
    "Canada": "Services / Energy / Technology",
    "Australia": "Mining / Services / Agriculture",
    "Turkey": "Manufacturing / Tourism / Services",
    "Singapore": "Finance / Technology / Services"
}


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

    "New York": "Times Square, Wall Street ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Los Angeles": "Hollywood ও চলচ্চিত্র শিল্পের জন্য বিখ্যাত",
    "Chicago": "স্থাপত্য, ব্যবসা ও Lake Michigan-এর জন্য বিখ্যাত",
    "Houston": "Space Center, energy industry ও ব্যবসার জন্য বিখ্যাত",
    "Miami": "সমুদ্রসৈকত, পর্যটন ও nightlife-এর জন্য বিখ্যাত",
    "Boston": "শিক্ষা, ইতিহাস ও গবেষণার জন্য বিখ্যাত",
    "Seattle": "Technology ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",

    "Muscat": "রাজধানী, সমুদ্র, পাহাড় ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",
    "Salalah": "খারিফ মৌসুম, সবুজ পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Sohar": "বন্দর, শিল্প ও ঐতিহাসিক ঐতিহ্যের জন্য বিখ্যাত",
    "Nizwa": "দুর্গ, বাজার ও ঐতিহ্যের জন্য বিখ্যাত",
    "Sur": "নৌকা নির্মাণ ও সমুদ্রের জন্য বিখ্যাত",

    "Dubai": "আকাশচুম্বী ভবন, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Abu Dhabi": "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Sharjah": "সংস্কৃতি, জাদুঘর ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Ajman": "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",

    "Doha": "আধুনিক স্থাপত্য, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Al Rayyan": "শিক্ষা, ক্রীড়া ও আবাসিক এলাকার জন্য বিখ্যাত",

    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Osaka": "ব্যবসা, খাবার ও বিনোদনের জন্য বিখ্যাত",
    "Kyoto": "প্রাচীন মন্দির, ঐতিহ্য ও সংস্কৃতির জন্য বিখ্যাত",

    "Madrid": "রাজধানী, শিল্প, সংস্কৃতি ও ফুটবলের জন্য বিখ্যাত",
    "Barcelona": "Gaudí স্থাপত্য, সমুদ্রসৈকত ও ফুটবলের জন্য বিখ্যাত",
    "Valencia": "সমুদ্রসৈকত, Paella ও City of Arts-এর জন্য বিখ্যাত",

    "London": "রাজধানী, ইতিহাস, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",
    "Manchester": "ফুটবল, শিল্প ও সঙ্গীতের জন্য বিখ্যাত",
    "Liverpool": "The Beatles, football ও বন্দরনগরী হিসেবে বিখ্যাত",

    "Paris": "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
    "Berlin": "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",
    "Munich": "Bavarian culture, industry ও Oktoberfest-এর জন্য বিখ্যাত",

    "Rome": "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",
    "Milan": "Fashion, design ও ব্যবসার জন্য বিখ্যাত",
    "Venice": "খাল, gondola ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Toronto": "ব্যবসা, সংস্কৃতি ও CN Tower-এর জন্য বিখ্যাত",
    "Vancouver": "পাহাড়, সমুদ্র ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Ottawa": "কানাডার রাজধানী ও Parliament-এর জন্য বিখ্যাত",

    "Sydney": "Opera House, Harbour ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Melbourne": "সংস্কৃতি, ক্রীড়া ও খাবারের জন্য বিখ্যাত"
}


FALLBACK_CITIES = {
    "Bangladesh": [
        "Dhaka", "Chattogram", "Rajshahi",
        "Khulna", "Barishal", "Sylhet", "Rangpur"
    ],

    "India": [
        "Mumbai", "Delhi", "Kolkata",
        "Bengaluru", "Chennai", "Hyderabad", "Pune"
    ],

    "United States": [
        "New York", "Los Angeles", "Chicago",
        "Houston", "Miami", "Boston", "Seattle"
    ],

    "Oman": [
        "Muscat", "Salalah", "Sohar",
        "Nizwa", "Sur", "Khasab", "Rustaq"
    ],

    "United Arab Emirates": [
        "Dubai", "Abu Dhabi", "Sharjah",
        "Ajman", "Al Ain", "Fujairah",
        "Ras Al Khaimah"
    ],

    "Qatar": [
        "Doha", "Al Rayyan", "Al Wakrah",
        "Umm Salal", "Al Khor", "Dukhan", "Mesaieed"
    ],

    "Spain": [
        "Madrid", "Barcelona", "Valencia",
        "Seville", "Málaga", "Bilbao", "Alicante"
    ],

    "Japan": [
        "Tokyo", "Osaka", "Kyoto",
        "Yokohama", "Nagoya", "Sapporo", "Fukuoka"
    ],

    "China": [
        "Beijing", "Shanghai", "Guangzhou",
        "Shenzhen", "Chengdu", "Wuhan", "Xi'an"
    ],

    "United Kingdom": [
        "London", "Manchester", "Birmingham",
        "Liverpool", "Leeds", "Bristol", "Edinburgh"
    ],

    "France": [
        "Paris", "Lyon", "Marseille",
        "Toulouse", "Nice", "Bordeaux", "Lille"
    ],

    "Germany": [
        "Berlin", "Munich", "Hamburg",
        "Frankfurt", "Cologne", "Stuttgart", "Dresden"
    ],

    "Italy": [
        "Rome", "Milan", "Naples",
        "Turin", "Florence", "Bologna", "Venice"
    ],

    "Canada": [
        "Toronto", "Vancouver", "Montreal",
        "Calgary", "Ottawa", "Edmonton", "Quebec City"
    ],

    "Australia": [
        "Sydney", "Melbourne", "Brisbane",
        "Perth", "Adelaide", "Canberra", "Hobart"
    ]
}


# =========================================================
# API & DATA ENGINE
# =========================================================

def tg(method, data=None):
    try:
        r = requests.post(
            TG + method,
            data=data or {},
            timeout=60
        )
        try:
            return r.json()
        except:
            return {"ok": False, "error": r.text}
    except Exception as e:
        print("Telegram error:", e)
        return None


def country_api(country):
    url = (
        RC +
        "/names.common/" +
        urllib.parse.quote(country, safe="")
    )

    headers = {
        "Authorization": "Bearer " + REST_COUNTRIES_KEY.strip()
    }

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            return None

        data = r.json()
        objects = data.get("data", {}).get("objects", [])
        if not objects:
            return None

        return objects[0]
    except Exception as e:
        print("Country API error:", e)
        return None


def get_cities(country):
    if country in FALLBACK_CITIES:
        return FALLBACK_CITIES[country][:]
    return ["Capital City", "Central City", "North City", "South City"]


def get_flag(data):
    if not data:
        return "🌍"
    return data.get("flag", {}).get("emoji", "🌍")


def get_population(data):
    if not data:
        return "তথ্য উপলভ্য নয়"
    value = data.get("population")
    if value is None:
        return "N/A"
    try:
        return f"{int(value):,}"
    except:
        return str(value)


def get_area(data):
    if not data:
        return "তথ্য উপলভ্য নয়"
    value = data.get("area", {}).get("kilometers")
    if value is None:
        return "N/A"
    try:
        return f"{int(value):,} km²"
    except:
        return str(value) + " km²"


POSTAL = {
    "Bangladesh": "1000",
    "India": "400001",
    "United States": "10001",
    "United Kingdom": "SW1A 1AA",
    "Oman": "100",
    "United Arab Emirates": "00000",
    "Qatar": "00000",
    "Spain": "28001",
    "Japan": "100-0001",
    "China": "100000",
    "France": "75001",
    "Germany": "10115",
    "Italy": "00100",
    "Canada": "K1A 0A1",
    "Australia": "2000",
    "Pakistan": "44000",
    "Malaysia": "50000",
    "Singapore": "018956",
    "Portugal": "1000-001",
    "Turkey": "06000"
}


LEADERS = {
    "Bangladesh": "প্রধানমন্ত্রী: তারেক রহমান",
    "India": "প্রধানমন্ত্রী: নরেন্দ্র মোদি",
    "United States": "President: Donald J. Trump",
    "Oman": "সুলতান: হাইথাম বিন তারিক",
    "United Arab Emirates": "President: মোহাম্মদ বিন জায়েদ আল নাহিয়ান",
    "Qatar": "আমির: তামিম বিন হামাদ আল থানি",
    "Spain": "রাজা: ষষ্ঠ ফিলিপ",
    "Japan": "সম্রাট: নারুহিতো",
    "China": "President: শি জিনপিং",
    "France": "President: Emmanuel Macron",
    "Germany": "Chancellor: Friedrich Merz",
    "Italy": "President: Sergio Mattarella",
    "United Kingdom": "রাজা: তৃতীয় চার্লস",
    "Canada": "প্রধানমন্ত্রী: Mark Carney",
    "Australia": "প্রধানমন্ত্রী: Anthony Albanese",
    "Pakistan": "President: Asif Ali Zardari",
    "Malaysia": "Yang di-Pertuan Agong: Sultan Ibrahim",
    "Singapore": "President: Tharman Shanmugaratnam",
    "Portugal": "President: António José Seguro",
    "Turkey": "President: Recep Tayyip Erdoğan"
}


def get_leader(country):
    return LEADERS.get(country, "বর্তমান রাষ্ট্রপ্রধানের তথ্য")


DIVISION_DATA = {
    "Bangladesh": {
        "Dhaka": ("ঢাকা বিভাগ", "ঢাকা-১৭ আসনের বর্তমান প্রতিনিধি"),
        "Chattogram": ("চট্টগ্রাম বিভাগ", "চট্টগ্রাম অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি"),
        "Rajshahi": ("রাজশাহী বিভাগ", "রাজশাহী অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি"),
        "Khulna": ("খুলনা বিভাগ", "খুলনা অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি"),
        "Barishal": ("বরিশাল বিভাগ", "বরিশাল অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি"),
        "Sylhet": ("সিলেট বিভাগ", "সিলেট অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি"),
        "Rangpur": ("রংপুর বিভাগ", "রংপুর অঞ্চলের সংশ্লিষ্ট আসনের প্রতিনিধি")
    }
}


def division_info(country, city):
    if country == "Bangladesh":
        item = DIVISION_DATA.get(country, {}).get(city)
        if item:
            return item[0], item[1]
        return (city + " বিভাগ", "সংশ্লিষ্ট নির্বাচনী আসনের প্রতিনিধি")
    return (city + " অঞ্চল", "সংশ্লিষ্ট স্থানীয় প্রতিনিধি")


def generate(country_input, old_city=""):
    real_country = COUNTRY_ALIASES.get(country_input.lower(), country_input.title())
    data = country_api(real_country)

    flag = get_flag(data)
    cities = get_cities(real_country)

    available = [x for x in cities if x != old_city]
    city = random.choice(available if available else cities)

    famous = CITY_FAMOUS.get(city, "স্থানীয় সংস্কৃতি, ব্যবসা ও পর্যটনের জন্য পরিচিত")
    division, representative = division_info(real_country, city)

    names = NAMES.get(real_country, DEFAULT_NAMES)
    name = random.choice(names)

    street_number = random.randint(10, 999)
    street = f"{street_number} {random.choice(STREET_NAMES)}, Block {random.choice(['A', 'B', 'C', 'D'])}"

    postal = POSTAL.get(
        real_country,
        data.get("postal_code", {}).get("format", "N/A") if data else "N/A"
    )

    food = COUNTRY_FOOD.get(real_country, "স্থানীয় খাবার")
    jobs = COUNTRY_JOBS.get(real_country, "Business / Services / Industry")
    duty = random.choice(["সাধারণত ৮ ঘণ্টা", "সাধারণত ৮–৯ ঘণ্টা", "সাধারণত ৮–১০ ঘণ্টা"])

    return {
        "country": real_country,
        "flag": flag,
        "leader": get_leader(real_country),
        "name": name,
        "street": street,
        "city": city,
        "famous": famous,
        "state": division,
        "postal": postal,
        "population": get_population(data),
        "division": division,
        "representative": representative,
        "area": get_area(data),
        "food": food,
        "jobs": jobs,
        "duty": duty
    }


def format_record(d):
    return (
        f"<b>{html.escape(d['country'])} {d['flag']} ({html.escape(d['leader'])})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{html.escape(d['name'])}</code>\n"
        f"– <b>Street:</b> <code>{html.escape(d['street'])}</code>\n"
        f"– <b>City:</b> <code>{html.escape(d['city'])}</code>\n"
        f"  ↳ <b>বিখ্যাত:</b> {html.escape(d['famous'])}\n"
        f"– <b>State/Region:</b> <code>{html.escape(d['state'])}</code>\n"
        f"– <b>Postal Code:</b> <code>{html.escape(str(d['postal']))}</code>\n"
        f"– <b>Country Population:</b> {html.escape(str(d['population']))}\n"
        f"– <b>Division:</b> <code>{html.escape(d['division'])}</code>\n"
        f"  ↳ <b>Representative:</b> {html.escape(d['representative'])}\n"
        f"– <b>Country Area:</b> {html.escape(d['area'])}\n"
        f"– <b>প্রধান খাদ্য:</b> {html.escape(d['food'])}\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> {html.escape(d['jobs'])}\n"
        f"– <b>Job Duty Hour:</b> {html.escape(d['duty'])}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )


def copy_text(d):
    return (
        f"Name: {d['name']}\n"
        f"Street: {d['street']}\n"
        f"City: {d['city']}\n"
        f"State/Region: {d['state']}\n"
        f"Postal Code: {d['postal']}\n"
        f"Country: {d['country']}"
    )


def keyboard(country, record):
    a = urllib.parse.quote(country, safe="")
    b = urllib.parse.quote(record["city"], safe="")
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
                    "callback_data": f"GEN|{a}|{b}"
                }
            ]
        ]
    }, ensure_ascii=False)


# =========================================================
# TELEGRAM QPYTHON BOT HANDLERS
# =========================================================

def send(chat_id, text, markup=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    if markup:
        data["reply_markup"] = markup
    return tg("sendMessage", data)


def edit(chat_id, message_id, text, markup):
    return tg(
        "editMessageText",
        {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
            "reply_markup": markup
        }
    )


def answer(callback_id):
    return tg("answerCallbackQuery", {"callback_query_id": callback_id})


def command_fake(message):
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip()

    parts = text.split(None, 1)
    if len(parts) < 2:
        send(chat_id, "❌ Country লিখুন।\n\n<code>/fake bd</code>")
        return

    raw = parts[1].strip()
    record = generate(raw)

    send(
        chat_id,
        format_record(record),
        keyboard(raw, record)
    )


def callback_generate(callback):
    callback_id = callback.get("id")
    answer(callback_id)

    raw = callback.get("data", "")
    if not raw.startswith("GEN|"):
        return

    parts = raw.split("|", 2)
    if len(parts) < 3:
        return

    country = urllib.parse.unquote(parts[1])
    old_city = urllib.parse.unquote(parts[2])

    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    record = generate(country, old_city)
    edit(
        chat_id,
        message_id,
        format_record(record),
        keyboard(country, record)
    )


def start_bot():
    print("==================================")
    print("🌍 COUNTRY DETAILS BOT")
    print("QPython 3")
    print("==================================")

    me = tg("getMe")
    if not me or not me.get("ok", False):
        print("\n❌ Telegram Bot Token ভুল।")
        print(me)
        return

    print("\n✅ Telegram Bot Connected")
    print("Bot:", me["result"].get("username", ""))
    print("\n🚀 BOT RUNNING...")

    offset = 0

    while True:
        try:
            result = tg(
                "getUpdates",
                {
                    "offset": offset,
                    "timeout": 30,
                    "allowed_updates": json.dumps(["message", "callback_query"])
                }
            )

            if not result or not result.get("ok", False):
                time.sleep(3)
                continue

            updates = result.get("result", [])
            for update in updates:
                offset = update["update_id"] + 1

                if "message" in update:
                    message = update["message"]
                    text = message.get("text", "").strip()

                    try:
                        if text.startswith("/start"):
                            chat_id = message.get("chat", {}).get("id")
                            send(
                                chat_id,
                                "<b>🌍 Country Details Bot</b>\n\n"
                                "ব্যবহার করুন:\n"
                                "<code>/fake bd</code>\n"
                                "<code>/fake india</code>\n"
                                "<code>/fake usa</code>\n"
                                "<code>/fake ae</code>\n"
                                "<code>/fake oman</code>\n"
                                "<code>/fake qatar</code>\n\n"
                                "📋 মানগুলোর ওপর আলতো চাপলেই স্বয়ংক্রিয়ভাবে কপি হয়ে যাবে।"
                            )
                        elif text.lower().startswith("/fake"):
                            command_fake(message)
                    except Exception as e:
                        print("Message Error:", e)

                elif "callback_query" in update:
                    try:
                        callback_generate(update["callback_query"])
                    except Exception as e:
                        print("Generate Error:", e)

        except KeyboardInterrupt:
            print("\n🛑 BOT STOPPED")
            break
        except Exception as e:
            print("\nMAIN ERROR:", e)
            time.sleep(3)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    start_bot()
