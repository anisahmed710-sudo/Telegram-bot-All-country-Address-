import requests
import random
import time
import json
import html
import urllib.parse


# ============================================================
# 1. YOUR SETTINGS
# ============================================================

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

REST_COUNTRIES_KEY = "rc_live_317037a7db864904b9a3695f31b68e57"


# ============================================================
# 2. API URLS
# ============================================================

TELEGRAM_API = (
    "https://api.telegram.org/bot"
    + BOT_TOKEN
    + "/"
)

COUNTRIES_API = (
    "https://api.restcountries.com/countries/v5"
)

# CountriesNow public city API
CITIES_API = (
    "https://countriesnow.space/api/v0.1/countries/cities"
)


# ============================================================
# 3. COUNTRY ALIASES
# ============================================================

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
    "emirates": "United Arab Emirates",
    "dubai": "United Arab Emirates",
    "united arab emirates":
        "United Arab Emirates",

    "oman": "Oman",
    "om": "Oman",

    "qatar": "Qatar",
    "qa": "Qatar",

    "saudi": "Saudi Arabia",
    "saudi arabia": "Saudi Arabia",

    "spain": "Spain",
    "es": "Spain",

    "france": "France",
    "germany": "Germany",
    "italy": "Italy",
    "portugal": "Portugal",

    "japan": "Japan",
    "china": "China",
    "south korea": "South Korea",
    "korea": "South Korea",

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


# ============================================================
# 4. DEMO / FICTIONAL NAMES
# ============================================================

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


# ============================================================
# 5. FICTIONAL STREET GENERATOR
# ============================================================

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

    number = random.randint(
        100,
        999
    )

    street = random.choice(
        STREETS
    )

    block = random.choice(
        ["A", "B", "C", "D"]
    )

    return (
        f"{number} {street}, "
        f"Block {block}"
    )


# ============================================================
# 6. CITY FAMOUS INFORMATION
# ============================================================

CITY_FAMOUS = {

    # Bangladesh
    "Dhaka":
        "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Chattogram":
        "সমুদ্রবন্দর, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",

    "Rajshahi":
        "আম, রেশম ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",

    "Khulna":
        "সুন্দরবন ও শিল্পাঞ্চলের জন্য বিখ্যাত",

    "Barishal":
        "নদী, খাল ও পেয়ারা বাগানের জন্য বিখ্যাত",

    "Sylhet":
        "চা-বাগান, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",

    "Rangpur":
        "কৃষি ও ঐতিহ্যের জন্য বিখ্যাত",

    # India
    "Mumbai":
        "Bollywood, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",

    "Delhi":
        "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Kolkata":
        "সাহিত্য, সংস্কৃতি ও ঐতিহ্যের জন্য বিখ্যাত",

    "Bengaluru":
        "প্রযুক্তি ও IT industry-এর জন্য বিখ্যাত",

    "Chennai":
        "শিল্প, প্রযুক্তি ও সমুদ্রসৈকতের জন্য বিখ্যাত",

    "Hyderabad":
        "প্রযুক্তি, খাবার ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Pune":
        "শিক্ষা, প্রযুক্তি ও শিল্পের জন্য বিখ্যাত",

    # Spain
    "Madrid":
        "রাজধানী, শিল্প, সংস্কৃতি ও ফুটবলের জন্য বিখ্যাত",

    "Barcelona":
        "Gaudí স্থাপত্য, সমুদ্রসৈকত ও ফুটবলের জন্য বিখ্যাত",

    "Valencia":
        "সমুদ্রসৈকত, Paella ও City of Arts-এর জন্য বিখ্যাত",

    "Seville":
        "Flamenco, ইতিহাস ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",

    "Málaga":
        "সমুদ্রসৈকত, পর্যটন ও সংস্কৃতির জন্য বিখ্যাত",

    "Bilbao":
        "Guggenheim Museum ও সংস্কৃতির জন্য বিখ্যাত",

    "Alicante":
        "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",

    # USA
    "New York":
        "Times Square, Wall Street ও Statue of Liberty-এর জন্য বিখ্যাত",

    "Los Angeles":
        "Hollywood ও চলচ্চিত্র শিল্পের জন্য বিখ্যাত",

    "Chicago":
        "স্থাপত্য, ব্যবসা ও Lake Michigan-এর জন্য বিখ্যাত",

    "Houston":
        "Space Center, energy industry ও ব্যবসার জন্য বিখ্যাত",

    "Miami":
        "সমুদ্রসৈকত, পর্যটন ও nightlife-এর জন্য বিখ্যাত",

    "Boston":
        "শিক্ষা, ইতিহাস ও গবেষণার জন্য বিখ্যাত",

    "Seattle":
        "Technology, Microsoft/Amazon অঞ্চল ও সমুদ্রের জন্য বিখ্যাত",

    # Oman
    "Muscat":
        "রাজধানী, সমুদ্র, পাহাড় ও ঐতিহ্যবাহী স্থাপত্যের জন্য বিখ্যাত",

    "Salalah":
        "খারিফ মৌসুম, সবুজ পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",

    "Sohar":
        "বন্দর, শিল্প ও ঐতিহাসিক ঐতিহ্যের জন্য বিখ্যাত",

    "Nizwa":
        "দুর্গ, বাজার ও ঐতিহ্যের জন্য বিখ্যাত",

    "Sur":
        "নৌকা নির্মাণ ও সমুদ্রের জন্য বিখ্যাত",

    "Khasab":
        "Musandam-এর পাহাড় ও সমুদ্রের জন্য বিখ্যাত",

    "Rustaq":
        "ঐতিহাসিক দুর্গ ও উষ্ণ প্রস্রবণের জন্য বিখ্যাত",

    # UAE
    "Dubai":
        "আকাশচুম্বী ভবন, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",

    "Abu Dhabi":
        "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",

    "Sharjah":
        "সংস্কৃতি, জাদুঘর ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",

    "Ajman":
        "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",

    "Al Ain":
        "ওয়েসিস, সবুজ পরিবেশ ও ঐতিহ্যের জন্য বিখ্যাত",

    "Fujairah":
        "পাহাড়, সমুদ্র ও diving-এর জন্য বিখ্যাত",

    "Ras Al Khaimah":
        "পাহাড়, adventure tourism ও সমুদ্রের জন্য বিখ্যাত",

    # Japan
    "Tokyo":
        "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",

    "Osaka":
        "ব্যবসা, খাবার ও বিনোদনের জন্য বিখ্যাত",

    "Kyoto":
        "প্রাচীন মন্দির, ঐতিহ্য ও সংস্কৃতির জন্য বিখ্যাত",

    "Yokohama":
        "বন্দর, সমুদ্র ও আধুনিক নগরজীবনের জন্য বিখ্যাত",

    "Nagoya":
        "Automobile industry ও শিল্পের জন্য বিখ্যাত",

    "Sapporo":
        "তুষার, শীতকালীন ক্রীড়া ও খাবারের জন্য বিখ্যাত",

    "Fukuoka":
        "খাবার, বন্দর ও ব্যবসার জন্য বিখ্যাত",

    # UK
    "London":
        "রাজধানী, ইতিহাস, ব্যবসা ও পর্যটনের জন্য বিখ্যাত",

    "Manchester":
        "ফুটবল, শিল্প ও সঙ্গীতের জন্য বিখ্যাত",

    "Birmingham":
        "শিল্প, ব্যবসা ও সংস্কৃতির জন্য বিখ্যাত",

    "Liverpool":
        "The Beatles, football ও বন্দরনগরী হিসেবে বিখ্যাত",

    "Leeds":
        "ব্যবসা, শিক্ষা ও সংস্কৃতির জন্য বিখ্যাত",

    "Bristol":
        "বন্দর, aerospace ও সংস্কৃতির জন্য বিখ্যাত",

    "Edinburgh":
        "ঐতিহাসিক স্থাপনা, Castle ও festival-এর জন্য বিখ্যাত",

    # France
    "Paris":
        "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",

    "Lyon":
        "খাবার, ইতিহাস ও ব্যবসার জন্য বিখ্যাত",

    "Marseille":
        "বন্দর, সমুদ্র ও Mediterranean সংস্কৃতির জন্য বিখ্যাত",

    "Toulouse":
        "Aerospace industry ও বিশ্ববিদ্যালয়ের জন্য বিখ্যাত",

    "Nice":
        "French Riviera ও সমুদ্রসৈকতের জন্য বিখ্যাত",

    "Bordeaux":
        "Wine, ইতিহাস ও স্থাপত্যের জন্য বিখ্যাত",

    "Lille":
        "সংস্কৃতি, ব্যবসা ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    # Germany
    "Berlin":
        "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",

    "Munich":
        "Bavarian culture, industry ও Oktoberfest-এর জন্য বিখ্যাত",

    "Hamburg":
        "বন্দর ও বাণিজ্যের জন্য বিখ্যাত",

    "Frankfurt":
        "Finance ও ব্যবসার জন্য বিখ্যাত",

    "Cologne":
        "Cologne Cathedral ও সংস্কৃতির জন্য বিখ্যাত",

    "Stuttgart":
        "Automobile industry-এর জন্য বিখ্যাত",

    "Dresden":
        "শিল্প, সংস্কৃতি ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    # Italy
    "Rome":
        "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",

    "Milan":
        "Fashion, design ও ব্যবসার জন্য বিখ্যাত",

    "Naples":
        "Pizza, ইতিহাস ও সমুদ্রের জন্য বিখ্যাত",

    "Turin":
        "Automobile, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",

    "Florence":
        "Renaissance art ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Bologna":
        "বিশ্ববিদ্যালয়, খাবার ও ইতিহাসের জন্য বিখ্যাত",

    "Venice":
        "খাল, gondola ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    # China
    "Beijing":
        "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",

    "Shanghai":
        "Finance, বন্দর ও আধুনিক skyline-এর জন্য বিখ্যাত",

    "Guangzhou":
        "বাণিজ্য, শিল্প ও Canton Fair-এর জন্য বিখ্যাত",

    "Shenzhen":
        "Technology, innovation ও manufacturing-এর জন্য বিখ্যাত",

    "Chengdu":
        "Panda, খাবার ও প্রযুক্তির জন্য বিখ্যাত",

    "Wuhan":
        "শিক্ষা, শিল্প ও Yangtze River-এর জন্য বিখ্যাত",

    "Xi'an":
        "Terracotta Army ও প্রাচীন ইতিহাসের জন্য বিখ্যাত",

    # Canada
    "Toronto":
        "ব্যবসা, সংস্কৃতি ও CN Tower-এর জন্য বিখ্যাত",

    "Vancouver":
        "পাহাড়, সমুদ্র ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",

    "Montreal":
        "সংস্কৃতি, খাবার ও French heritage-এর জন্য বিখ্যাত",

    "Calgary":
        "Energy industry ও Rocky Mountains-এর জন্য বিখ্যাত",

    "Ottawa":
        "কানাডার রাজধানী ও Parliament-এর জন্য বিখ্যাত",

    "Edmonton":
        "Government, shopping ও festivals-এর জন্য বিখ্যাত",

    "Quebec City":
        "ঐতিহাসিক স্থাপনা ও French culture-এর জন্য বিখ্যাত"
}


# ============================================================
# 7. COUNTRY FOOD
# ============================================================

COUNTRY_FOOD = {

    "Bangladesh":
        "ভাত, মাছ, ডাল ও ভর্তা",

    "India":
        "ভাত, রুটি, ডাল ও বিভিন্ন আঞ্চলিক খাবার",

    "Pakistan":
        "বিরিয়ানি, নিহারি ও বিভিন্ন স্থানীয় খাবার",

    "Spain":
        "Paella, Tapas ও Tortilla Española",

    "United States":
        "Burger, Barbecue, Steak ও আঞ্চলিক খাবার",

    "United Kingdom":
        "Fish and Chips, Roast ও Pie",

    "Oman":
        "Shuwa, Majboos ও সামুদ্রিক খাবার",

    "United Arab Emirates":
        "Machboos, Hummus ও Shawarma",

    "Qatar":
        "Machboos, Harees ও Dates",

    "Japan":
        "Sushi, Ramen ও Tempura",

    "China":
        "Rice, Noodles ও বিভিন্ন আঞ্চলিক খাবার",

    "Malaysia":
        "Nasi Lemak, Satay ও Laksa",

    "Indonesia":
        "Nasi Goreng, Satay ও Rendang",

    "France":
        "Baguette, Cheese ও বিভিন্ন আঞ্চলিক খাবার",

    "Germany":
        "Bratwurst, Bread ও Schnitzel",

    "Italy":
        "Pizza, Pasta ও Risotto",

    "Turkey":
        "Kebab, Pide ও Baklava",

    "Canada":
        "Poutine, Salmon ও বিভিন্ন আঞ্চলিক খাবার",

    "Australia":
        "Meat Pie, Seafood ও Barbecue"
}


# ============================================================
# 8. COUNTRY JOBS
# ============================================================

COUNTRY_JOBS = {

    "Bangladesh":
        "Garments / Agriculture / Business / Services",

    "India":
        "IT / Business / Manufacturing / Services",

    "Pakistan":
        "Textile / Agriculture / Services",

    "Spain":
        "Tourism / Services / Industry",

    "United States":
        "Technology / Finance / Services / Manufacturing",

    "United Kingdom":
        "Finance / Services / Technology",

    "Oman":
        "Energy / Tourism / Services",

    "United Arab Emirates":
        "Business / Tourism / Finance",

    "Qatar":
        "Energy / Construction / Business",

    "Japan":
        "Technology / Automobile / Industry",

    "China":
        "Manufacturing / Technology / Trade",

    "Malaysia":
        "Manufacturing / Services / Business",

    "France":
        "Tourism / Services / Industry",

    "Germany":
        "Engineering / Manufacturing / Services",

    "Italy":
        "Manufacturing / Fashion / Tourism",

    "Turkey":
        "Manufacturing / Tourism / Services",

    "Canada":
        "Services / Energy / Technology",

    "Australia":
        "Mining / Services / Agriculture"
}


# ============================================================
# 9. VERIFIED POLITICAL DATA
# ============================================================
#
# IMPORTANT:
# এখানে শুধু verified data রাখবে।
#
# 121 দেশের সব constituency/representative
# এক জায়গায় নির্ভরযোগ্যভাবে পাওয়া যায় না।
#
# তাই data না থাকলে bot বানানো নাম দেখাবে না।
# ============================================================

POLITICAL_DATA = {

    # --------------------------------------------------------
    # BANGLADESH
    # --------------------------------------------------------

    "BD": {

        "head_title":
            "Prime Minister",

        "head_bn":
            "প্রধানমন্ত্রী",

        "head_name":
            "তারেক রহমান",

        "rep_title":
            "MP",

        "rep_bn":
            "সংসদ সদস্য",

        "locations": {

            "Dhaka": {
                "seat":
                    "ঢাকা-১৭",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Chattogram": {
                "seat":
                    "চট্টগ্রাম-XX",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Rajshahi": {
                "seat":
                    "রাজশাহী-১",
                "name":
                    "মোঃ মুজিবুর রহমান"
            },

            "Khulna": {
                "seat":
                    "খুলনা-XX",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Barishal": {
                "seat":
                    "বরিশাল-XX",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Sylhet": {
                "seat":
                    "সিলেট-XX",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Rangpur": {
                "seat":
                    "রংপুর-XX",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            }
        }
    },


    # --------------------------------------------------------
    # INDIA
    # --------------------------------------------------------

    "IN": {

        "head_title":
            "Prime Minister",

        "head_bn":
            "প্রধানমন্ত্রী",

        "head_name":
            "নরেন্দ্র মোদি",

        "rep_title":
            "Lok Sabha MP",

        "rep_bn":
            "লোকসভা সংসদ সদস্য",

        "locations": {

            "Mumbai": {
                "seat":
                    "Mumbai North-West",
                "name":
                    "রবীন্দ্র দত্তারাম ওয়াইকর"
            },

            "Delhi": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Kolkata": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Bengaluru": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Chennai": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Hyderabad": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            },

            "Pune": {
                "seat":
                    "Lok Sabha constituency",
                "name":
                    "বর্তমান প্রতিনিধি যাচাই প্রয়োজন"
            }
        }
    },


    # --------------------------------------------------------
    # USA
    # --------------------------------------------------------

    "US": {

        "head_title":
            "President",

        "head_bn":
            "রাষ্ট্রপতি",

        "head_name":
            "Donald J. Trump",

        "rep_title":
            "U.S. Representative",

        "rep_bn":
            "প্রতিনিধি",

        "locations": {

            "New York": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Los Angeles": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Chicago": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Houston": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Miami": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Boston": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            },

            "Seattle": {
                "seat":
                    "Congressional District",
                "name":
                    "Current representative varies by district"
            }
        }
    },


    # --------------------------------------------------------
    # OMAN
    # --------------------------------------------------------

    "OM": {

        "head_title":
            "Sultan",

        "head_bn":
            "সুলতান",

        "head_name":
            "হাইথাম বিন তারিক",

        "rep_title":
            "Shura Council Member",

        "rep_bn":
            "শূরা কাউন্সিল সদস্য",

        "locations": {

            "Muscat": {
                "seat":
                    "Muscat Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Salalah": {
                "seat":
                    "Salalah Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Sohar": {
                "seat":
                    "Sohar Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Nizwa": {
                "seat":
                    "Nizwa Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Sur": {
                "seat":
                    "Sur Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Khasab": {
                "seat":
                    "Khasab Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            },

            "Rustaq": {
                "seat":
                    "Rustaq Wilayat",
                "name":
                    "বর্তমান সদস্য যাচাই প্রয়োজন"
            }
        }
    }
}


# ============================================================
# 10. GENERIC POLITICAL TITLE
# ============================================================

def representative_title(
    country_code
):

    titles = {

        "BD":
            "Running MP",

        "IN":
            "Running Lok Sabha MP",

        "US":
            "Running U.S. Representative",

        "OM":
            "Running Shura Council Member",

        "GB":
            "Running MP",

        "CA":
            "Running MP",

        "AU":
            "Running MP",

        "NZ":
            "Running MP",

        "PK":
            "Running MNA",

        "JP":
            "Running Diet Member",

        "CN":
            "Running NPC Deputy",

        "ES":
            "Running Diputado/Diputada",

        "FR":
            "Running Député/Députée",

        "DE":
            "Running Bundestag Member",

        "IT":
            "Running Deputato/Deputata",

        "BR":
            "Running Federal Deputy",

        "QA":
            "Running Shura Council Member",

        "AE":
            "Running Federal National Council Member"
    }

    return titles.get(
        country_code,
        "Running Representative"
)

# ============================================================
# 11. TELEGRAM REQUEST
# ============================================================

def tg_request(
    method,
    data=None
):

    url = (
        TELEGRAM_API
        + method
    )

    try:

        r = requests.post(

            url,

            data=data or {},

            timeout=60
        )

        return r.json()

    except Exception as e:

        print(
            "Telegram Error:",
            e
        )

        return None


# ============================================================
# 12. REST COUNTRIES REQUEST
# ============================================================

def get_country(
    country
):

    url = (
        COUNTRIES_API
        + "/names.common/"
        + urllib.parse.quote(
            country,
            safe=""
        )
    )

    headers = {

        "Authorization":
            "Bearer "
            + REST_COUNTRIES_KEY.strip()
    }

    try:

        r = requests.get(

            url,

            headers=headers,

            timeout=30
        )

        if r.status_code != 200:

            print(
                "Country API ERROR:",
                r.status_code
            )

            print(
                r.text
            )

            return None


        result = r.json()


        if "_demo" in result.get(
            "data",
            {}
        ):

            print(
                "❌ DEMO API KEY"
            )

            return None


        objects = (
            result
            .get("data", {})
            .get("objects", [])
        )


        if not objects:

            return None


        return objects[0]


    except Exception as e:

        print(
            "Country API Error:",
            e
        )

        return None


# ============================================================
# 13. GET CITIES
# ============================================================

def get_cities(
    country
):

    try:

        response = requests.post(

            CITIES_API,

            json={
                "country":
                    country
            },

            timeout=30
        )


        if response.status_code != 200:

            return []


        data = response.json()


        if data.get(
            "error",
            True
        ):

            return []


        cities = data.get(
            "data",
            []
        )


        cleaned = []

        for city in cities:

            if not city:
                continue

            city = str(city).strip()

            if city not in cleaned:

                cleaned.append(city)


        return cleaned


    except Exception as e:

        print(
            "Cities API:",
            e
        )

        return []


# ============================================================
# 14. COUNTRY FALLBACK CITIES
# ============================================================

FALLBACK_CITIES = {

    "Bangladesh": [
        "Dhaka",
        "Chattogram",
        "Rajshahi",
        "Khulna",
        "Barishal",
        "Sylhet",
        "Rangpur"
    ],

    "India": [
        "Mumbai",
        "Delhi",
        "Kolkata",
        "Bengaluru",
        "Chennai",
        "Hyderabad",
        "Pune"
    ],

    "United States": [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Miami",
        "Boston",
        "Seattle"
    ],

    "Oman": [
        "Muscat",
        "Salalah",
        "Sohar",
        "Nizwa",
        "Sur",
        "Khasab",
        "Rustaq"
    ],

    "United Arab Emirates": [
        "Dubai",
        "Abu Dhabi",
        "Sharjah",
        "Ajman",
        "Al Ain",
        "Fujairah",
        "Ras Al Khaimah"
    ],

    "Spain": [
        "Madrid",
        "Barcelona",
        "Valencia",
        "Seville",
        "Málaga",
        "Bilbao",
        "Alicante"
    ],

    "Japan": [
        "Tokyo",
        "Osaka",
        "Kyoto",
        "Yokohama",
        "Nagoya",
        "Sapporo",
        "Fukuoka"
    ],

    "China": [
        "Beijing",
        "Shanghai",
        "Guangzhou",
        "Shenzhen",
        "Chengdu",
        "Wuhan",
        "Xi'an"
    ],

    "United Kingdom": [
        "London",
        "Manchester",
        "Birmingham",
        "Liverpool",
        "Leeds",
        "Bristol",
        "Edinburgh"
    ],

    "France": [
        "Paris",
        "Lyon",
        "Marseille",
        "Toulouse",
        "Nice",
        "Bordeaux",
        "Lille"
    ],

    "Germany": [
        "Berlin",
        "Munich",
        "Hamburg",
        "Frankfurt",
        "Cologne",
        "Stuttgart",
        "Dresden"
    ],

    "Italy": [
        "Rome",
        "Milan",
        "Naples",
        "Turin",
        "Florence",
        "Bologna",
        "Venice"
    ],

    "Canada": [
        "Toronto",
        "Vancouver",
        "Montreal",
        "Calgary",
        "Ottawa",
        "Edmonton",
        "Quebec City"
    ],

    "Australia": [
        "Sydney",
        "Melbourne",
        "Brisbane",
        "Perth",
        "Adelaide",
        "Canberra",
        "Hobart"
    ],

    "Pakistan": [
        "Islamabad",
        "Karachi",
        "Lahore",
        "Peshawar",
        "Quetta",
        "Multan",
        "Faisalabad"
    ],

    "Qatar": [
        "Doha",
        "Al Rayyan",
        "Al Wakrah",
        "Umm Salal",
        "Al Khor",
        "Dukhan",
        "Mesaieed"
    ]
}

# ============================================================
# 15. GET 7 LOCATIONS
# ============================================================

def get_locations(
    country,
    capital
):

    locations = []


    # First priority:
    # manually selected country cities

    if country in FALLBACK_CITIES:

        locations = list(
            FALLBACK_CITIES[
                country
            ]
        )


    # Second:
    # API city data

    if len(locations) < 7:

        api_cities = get_cities(
            country
        )

        for city in api_cities:

            if city not in locations:

                locations.append(
                    city
                )

            if len(locations) >= 7:

                break


    # Third:
    # capital

    if (
        capital
        and capital != "N/A"
        and capital not in locations
    ):

        locations.insert(
            0,
            capital
        )


    # Remove duplicates

    final = []

    for city in locations:

        if city not in final:

            final.append(city)


    # Exactly 7 where possible

    return final[:7]


# ============================================================
# 16. POSTAL CODE
# ============================================================

POSTAL_EXAMPLES = {

    "Bangladesh":
        "1000",

    "India":
        "400001",

    "United States":
        "10001",

    "United Kingdom":
        "SW1A 1AA",

    "Oman":
        "100",

    "United Arab Emirates":
        "00000",

    "Spain":
        "28001",

    "Japan":
        "100-0001",

    "China":
        "100000",

    "France":
        "75001",

    "Germany":
        "10115",

    "Italy":
        "00100",

    "Canada":
        "K1A 0A1",

    "Australia":
        "2000",

    "Pakistan":
        "44000",

    "Qatar":
        "00000"
}


def postal_code(
    country,
    api_data
):

    if country in POSTAL_EXAMPLES:

        return POSTAL_EXAMPLES[
            country
        ]


    postal = api_data.get(
        "postal_code",
        {}
    )


    fmt = postal.get(
        "format"
    )


    if fmt:

        return fmt


    return "N/A"


# ============================================================
# 17. AREA
# ============================================================

def format_area(
    api_data
):

    area = (
        api_data
        .get("area", {})
        .get(
            "kilometers"
        )
    )

    if area is None:

        return "N/A"


    try:

        return (
            f"{int(area):,} km²"
        )

    except:

        return str(area) + " km²"


# ============================================================
# 18. POPULATION
# ============================================================

def format_population(
    api_data
):

    pop = api_data.get(
        "population"
    )


    if pop is None:

        return "N/A"


    try:

        return f"{int(pop):,}"

    except:

        return str(pop)


# ============================================================
# 19. POLITICAL INFO
# ============================================================

def political_info(
    country_code,
    city
):

    data = POLITICAL_DATA.get(
        country_code
    )


    # No political mapping

    if not data:

        return {

            "head":
                "Current leader data unavailable",

            "rep_title":
                representative_title(
                    country_code
                ),

            "rep_name":
                "Verified current representative unavailable",

            "seat":
                "N/A"
        }


    head = (

        data[
            "head_title"
        ]
        + ": "
        + data[
            "head_name"
        ]
    )


    location = data.get(
        "locations",
        {}
    ).get(
        city
    )


    if location:

        return {

            "head":
                head,

            "rep_title":
                data[
                    "rep_title"
                ],

            "rep_name":
                location[
                    "name"
                ],

            "seat":
                location[
                    "seat"
                ]
        }


    return {

        "head":
            head,

        "rep_title":
            data[
                "rep_title"
            ],

        "rep_name":
            "Verified current representative unavailable",

        "seat":
            "N/A"
    }


# ============================================================
# 20. GENERATE ONE RECORD
# ============================================================

def generate_record(
    country,
    old_city=""
):

    api_data = get_country(
        country
    )


    if not api_data:

        return None


    real_country = (
        api_data
        .get("names", {})
        .get(
            "common",
            country
        )
    )


    flag = (
        api_data
        .get("flag", {})
        .get(
            "emoji",
            ""
        )
    )


    codes = (
        api_data
        .get("codes", {})
    )


    country_code = codes.get(
        "alpha_2",
        ""
    )


    capitals = api_data.get(
        "capitals",
        []
    )


    if capitals:

        capital = capitals[0].get(
            "name",
            "N/A"
        )

    else:

        capital = "N/A"


    locations = get_locations(
        real_country,
        capital
    )


    if not locations:

        locations = [
            capital
        ]


    # Try not to repeat city

    available = [

        city

        for city in locations

        if city != old_city
    ]


    if not available:

        available = locations


    city = random.choice(
        available
    )


    famous = CITY_FAMOUS.get(

        city,

        "স্থানীয় ইতিহাস, সংস্কৃতি, ব্যবসা ও পর্যটনের জন্য পরিচিত"
    )


    # State / Region

    if real_country == "Bangladesh":

        state = (
            city
            + " Division"
        )

        division = city


    else:

        state = api_data.get(
            "subregion",
            api_data.get(
                "region",
                "Regional area"
            )
        )

        division = city


    political = political_info(
        country_code,
        city
    )


    name = random.choice(
        NAMES
    )


    food = COUNTRY_FOOD.get(

        real_country,

        "স্থানীয় খাবার"
    )


    jobs = COUNTRY_JOBS.get(

        real_country,

        "Business / Services / Industry"
    )


    duty = random.choice([

        "সাধারণত ৮ ঘণ্টা",

        "সাধারণত ৮–৯ ঘণ্টা",

        "সাধারণত ৮–১০ ঘণ্টা"

    ])


    return {

        "country":
            real_country,

        "flag":
            flag,

        "head":
            political[
                "head"
            ],

        "name":
            name,

        "street":
            make_street(),

        "city":
            city,

        "famous":
            famous,

        "state":
            state,

        "postal":
            postal_code(
                real_country,
                api_data
            ),

        "population":
            format_population(
                api_data
            ),

        "division":
            division,

        "rep_title":
            political[
                "rep_title"
            ],

        "rep_name":
            political[
                "rep_name"
            ],

        "seat":
            political[
                "seat"
            ],

        "area":
            format_area(
                api_data
            ),

        "food":
            food,

        "jobs":
            jobs,

        "duty":
            duty
        }

# ============================================================
# 21. FORMAT TELEGRAM MESSAGE
# ============================================================

def make_message(
    data
):

    return (

        f"<b>{html.escape(data['country'])} "
        f"{data['flag']} "
        f"({html.escape(data['head'])})</b>\n"

        f"━━━━━━━━━━━━━━━━━━━━\n\n"

        f"– <b>Name:</b> "
        f"{html.escape(data['name'])}\n"

        f"– <b>Street:</b> "
        f"{html.escape(data['street'])}\n"

        f"– <b>City:</b> "
        f"{html.escape(data['city'])}\n"

        f"  ↳ <b>বিখ্যাত:</b> "
        f"{html.escape(data['famous'])}\n"

        f"– <b>State/Region:</b> "
        f"{html.escape(data['state'])}\n"

        f"– <b>Postal Code:</b> "
        f"{html.escape(str(data['postal']))}\n"

        f"– <b>Country Population:</b> "
        f"{html.escape(str(data['population']))}\n"

        f"– <b>Division/Constituency:</b> "
        f"{html.escape(data['division'])}\n"

        f"  ↳ <b>"
        f"{html.escape(data['rep_title'])}:"
        f"</b> "

        f"{html.escape(data['rep_name'])}"

        f" — "

        f"{html.escape(data['seat'])}\n"

        f"– <b>Country Area:</b> "
        f"{html.escape(data['area'])}\n"

        f"– <b>প্রধান খাদ্য:</b> "
        f"{html.escape(data['food'])}\n"

        f"– <b>প্রধান কর্মক্ষেত্র:</b> "
        f"{html.escape(data['jobs'])}\n"

        f"– <b>Job Duty Hour:</b> "
        f"{html.escape(data['duty'])}\n\n"

        f"━━━━━━━━━━━━━━━━━━━━"
    )


# ============================================================
# 22. GENERATE BUTTON
# ============================================================

def generate_keyboard(
    country,
    old_city
):

    country_encoded = urllib.parse.quote(
        country,
        safe=""
    )

    city_encoded = urllib.parse.quote(
        old_city,
        safe=""
    )


    callback = (
        "GEN|"
        + country_encoded
        + "|"
        + city_encoded
    )


    # Telegram callback_data max ~64 bytes
    # Country names are short enough here.

    if len(callback.encode("utf-8")) > 60:

        callback = (
            "GEN|"
            + country_encoded[:25]
        )


    return json.dumps({

        "inline_keyboard": [

            [

                {
                    "text":
                        "🔄 Generate",

                    "callback_data":
                        callback
                }

            ]

        ]

    }, ensure_ascii=False)


# ============================================================
# 23. SEND MESSAGE
# ============================================================

def send_message(
    chat_id,
    text,
    keyboard=None
):

    payload = {

        "chat_id":
            chat_id,

        "text":
            text,

        "parse_mode":
            "HTML",

        "disable_web_page_preview":
            True
    }


    if keyboard:

        payload[
            "reply_markup"
        ] = keyboard


    return tg_request(
        "sendMessage",
        payload
    )


# ============================================================
# 24. EDIT MESSAGE
# ============================================================

def edit_message(
    chat_id,
    message_id,
    text,
    keyboard
):

    return tg_request(

        "editMessageText",

        {

            "chat_id":
                chat_id,

            "message_id":
                message_id,

            "text":
                text,

            "parse_mode":
                "HTML",

            "disable_web_page_preview":
                True,

            "reply_markup":
                keyboard
        }
    )


# ============================================================
# 25. ANSWER CALLBACK
# ============================================================

def answer_callback(
    callback_id
):

    return tg_request(

        "answerCallbackQuery",

        {

            "callback_query_id":
                callback_id
        }
    )

# ============================================================
# 26. /START
# ============================================================

def handle_start(
    message
):

    chat_id = (
        message
        .get("chat", {})
        .get("id")
    )


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

        "Population, Area, Capital ও Country "
        "information live API থেকে নেওয়া হবে।"
    )


    send_message(
        chat_id,
        text
    )


# ============================================================
# 27. /FAKE
# ============================================================

def handle_fake(
    message
):

    chat_id = (
        message
        .get("chat", {})
        .get("id")
    )


    text = message.get(
        "text",
        ""
    ).strip()


    parts = text.split(
        None,
        1
    )


    if len(parts) < 2:

        send_message(

            chat_id,

            "❌ Country লিখুন।\n\n"
            "<code>/fake Bangladesh</code>"
        )

        return


    raw_country = (
        parts[1]
        .strip()
        .lower()
    )


    country = COUNTRY_ALIASES.get(

        raw_country,

        parts[1].strip()
    )


    print(
        "Generating:",
        country
    )


    record = generate_record(
        country
    )


    if not record:

        send_message(

            chat_id,

            "❌ Country data পাওয়া যায়নি।\n\n"
            "Country-এর English নাম দিয়ে "
            "আবার চেষ্টা করুন।"
        )

        return


    text = make_message(
        record
    )


    keyboard = generate_keyboard(

        country,

        record["city"]
    )


    send_message(

        chat_id,

        text,

        keyboard
    )


# ============================================================
# 28. GENERATE CALLBACK
# ============================================================

def handle_generate(
    callback
):

    callback_id = callback.get(
        "id"
    )


    answer_callback(
        callback_id
    )


    callback_data = callback.get(
        "data",
        ""
    )


    if not callback_data.startswith(
        "GEN|"
    ):

        return


    parts = callback_data.split(
        "|",
        2
    )


    if len(parts) < 2:

        return


    country = urllib.parse.unquote(
        parts[1]
    )


    old_city = ""


    if len(parts) >= 3:

        old_city = urllib.parse.unquote(
            parts[2]
        )


    message = callback.get(
        "message",
        {}
    )


    chat_id = (
        message
        .get("chat", {})
        .get("id")
    )


    message_id = message.get(
        "message_id"
    )


    new_record = generate_record(

        country,

        old_city
    )


    if not new_record:

        return


    text = make_message(
        new_record
    )


    keyboard = generate_keyboard(

        country,

        new_record["city"]
    )


    edit_message(

        chat_id,

        message_id,

        text,

        keyboard
    )


    print(
        "GENERATED:",
        new_record["country"],
        "|",
        new_record["city"],
        "|",
        new_record["division"]
    )


# ============================================================
# 29. TELEGRAM POLLING
# ============================================================

def run_bot():

    print(
        "======================================"
    )

    print(
        "🌍 LIVE COUNTRY GENERATOR BOT"
    )

    print(
        "======================================"
    )

    print(
        "REST Countries API: CONNECTED"
    )

    print(
        "Telegram Bot: STARTING..."
    )


    offset = 0


    while True:

        try:

            result = tg_request(

                "getUpdates",

                {

                    "timeout":
                        50,

                    "offset":
                        offset
                }
            )


            if not result:

                time.sleep(2)

                continue


            if not result.get(
                "ok",
                False
            ):

                print(
                    "Telegram error:",
                    result
                )

                time.sleep(5)

                continue


            updates = result.get(
                "result",
                []
            )


            for update in updates:

                offset = (
                    update[
                        "update_id"
                    ]
                    + 1
                )


                # --------------------------------------
                # Normal Message
                # --------------------------------------

                if "message" in update:

                    message = update[
                        "message"
                    ]

                    text = message.get(
                        "text",
                        ""
                    )


                    try:

                        if text.startswith(
                            "/start"
                        ):

                            handle_start(
                                message
                            )


                        elif text.lower().startswith(
                            "/fake"
                        ):

                            handle_fake(
                                message
                            )


                    except Exception as e:

                        print(
                            "Message error:",
                            e
                        )


                # --------------------------------------
                # Callback
                # --------------------------------------

                elif (
                    "callback_query"
                    in update
                ):

                    try:

                        handle_generate(

                            update[
                                "callback_query"
                            ]
                        )


                    except Exception as e:

                        print(
                            "Callback error:",
                            e
                        )


        except KeyboardInterrupt:

            print(
                "\nBOT STOPPED"
            )

            break


        except Exception as e:

            print(
                "Main loop error:",
                e
            )

            time.sleep(5)


# ============================================================
# 30. START
# ============================================================

if __name__ == "__main__":

    if (
        BOT_TOKEN.startswith(
            "PASTE_"
        )
        or
        REST_COUNTRIES_KEY.startswith(
            "PASTE_"
        )
    ):

        print()
        print(
            "❌ প্রথমে BOT_TOKEN এবং "
            "REST_COUNTRIES_KEY বসাও।"
        )
        print()

    else:

        run_bot()
