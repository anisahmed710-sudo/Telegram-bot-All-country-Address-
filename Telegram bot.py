# ==========================================
# GLOBAL COUNTRY ADDRESS GENERATOR (FULL CODE)
# ==========================================

import random
import time
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

# ==========================================
# SSL FIX FOR QPYTHON
# ==========================================
ssl_context = ssl._create_unverified_context()

# ==========================================
# BOT TOKEN
# ==========================================
BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"

# ==========================================
# COUNTRY DATABASE
# ==========================================
COUNTRIES = {

    "bd": {
        "name": "Bangladesh",
        "flag": "🇧🇩",
        "leader": "বর্তমান রাষ্ট্রপ্রধান",
        "cities": {
            "Dhaka": {
                "famous": "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
                "state": "Dhaka Division",
                "admin": "বিভাগীয় প্রশাসন"
            },
            "Chattogram": {
                "famous": "সমুদ্রবন্দর, পাহাড় ও বাণিজ্যের জন্য বিখ্যাত",
                "state": "Chattogram Division",
                "admin": "বিভাগীয় প্রশাসন"
            },
            "Rajshahi": {
                "famous": "আম, রেশম ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
                "state": "Rajshahi Division",
                "admin": "বিভাগীয় প্রশাসন"
            },
            "Khulna": {
                "famous": "সুন্দরবনের নিকটবর্তী অঞ্চল ও শিল্পের জন্য বিখ্যাত",
                "state": "Khulna Division",
                "admin": "বিভাগীয় প্রশাসন"
            },
            "Sylhet": {
                "famous": "চা-বাগান ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
                "state": "Sylhet Division",
                "admin": "বিভাগীয় প্রশাসন"
            }
        },
        "population": "প্রায় ১৭ কোটি",
        "area": "প্রায় ১,৪৭,৫৭০ বর্গকিলোমিটার",
        "food": "ভাত, মাছ, ডাল, ভর্তা ও বিরিয়ানি",
        "work": "গার্মেন্টস, কৃষি, ব্যবসা ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "in": {
        "name": "India",
        "flag": "🇮🇳",
        "leader": "নরেন্দ্র মোদি",
        "cities": {
            "Mumbai": {
                "famous": "বলিউড, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
                "state": "Maharashtra",
                "admin": "দেবেন্দ্র ফড়নবিশ"
            },
            "New Delhi": {
                "famous": "দেশের রাজধানী ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
                "state": "Delhi",
                "admin": "রেখা গুপ্ত"
            },
            "Kolkata": {
                "famous": "সংস্কৃতি, সাহিত্য ও মিষ্টির জন্য বিখ্যাত",
                "state": "West Bengal",
                "admin": "মমতা বন্দ্যোপাধ্যায়"
            },
            "Bengaluru": {
                "famous": "প্রযুক্তি ও IT শিল্পের জন্য বিখ্যাত",
                "state": "Karnataka",
                "admin": "সিদ্ধারামাইয়া"
            },
            "Chennai": {
                "famous": "তামিল সংস্কৃতি, গাড়ি শিল্প ও সমুদ্রতটের জন্য বিখ্যাত",
                "state": "Tamil Nadu",
                "admin": "এম. কে. স্ট্যালিন"
            }
        },
        "population": "প্রায় ১৪৬ কোটি",
        "area": "৩২,৮৭,২৬৩ বর্গকিলোমিটার",
        "food": "ভাত, রুটি, ডাল, বিরিয়ানি ও বিভিন্ন আঞ্চলিক খাবার",
        "work": "IT, ব্যবসা, কৃষি, শিল্প ও সেবা",
        "duty": "সাধারণত ৮–১০ ঘণ্টা"
    },

    "ae": {
        "name": "United Arab Emirates",
        "flag": "🇦🇪",
        "leader": "শেখ মোহাম্মদ বিন জায়েদ আল নাহিয়ান",
        "cities": {
            "Dubai": {
                "famous": "আকাশচুম্বী ভবন, ব্যবসা, পর্যটন ও বিলাসবহুল শপিংয়ের জন্য বিখ্যাত",
                "state": "Dubai Emirate",
                "admin": "শেখ হামদান বিন মোহাম্মদ"
            },
            "Abu Dhabi": {
                "famous": "রাজধানী, তেল-গ্যাস ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
                "state": "Abu Dhabi Emirate",
                "admin": "শেখ খালেদ বিন মোহাম্মদ"
            },
            "Sharjah": {
                "famous": "সংস্কৃতি, জাদুঘর ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
                "state": "Sharjah Emirate",
                "admin": "শেখ সুলতান আল কাসিমি"
            }
        },
        "population": "প্রায় ১ কোটি",
        "area": "প্রায় ৮৩,৬০০ বর্গকিলোমিটার",
        "food": "মাচবুস, হুমুস, শাওয়ারমা ও খেজুর",
        "work": "ব্যবসা, তেল-গ্যাস, নির্মাণ, পর্যটন ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "us": {
        "name": "United States",
        "flag": "🇺🇸",
        "leader": "ডোনাল্ড ট্রাম্প",
        "cities": {
            "New York": {
                "famous": "আর্থিক কেন্দ্র, Times Square ও Statue of Liberty-এর জন্য বিখ্যাত",
                "state": "New York",
                "admin": "Kathy Hochul"
            },
            "Los Angeles": {
                "famous": "Hollywood ও বিনোদন শিল্পের জন্য বিখ্যাত",
                "state": "California",
                "admin": "Gavin Newsom"
            },
            "Chicago": {
                "famous": "স্থাপত্য, ব্যবসা ও শিল্পের জন্য বিখ্যাত",
                "state": "Illinois",
                "admin": "JB Pritzker"
            },
            "Miami": {
                "famous": "সমুদ্রসৈকত, পর্যটন ও বিনোদনের জন্য বিখ্যাত",
                "state": "Florida",
                "admin": "Ron DeSantis"
            }
        },
        "population": "প্রায় ৩৪ কোটি",
        "area": "প্রায় ৯৮,৩৩,৫১৭ বর্গকিলোমিটার",
        "food": "বার্গার, স্টেক, পিজা ও স্যান্ডউইচ",
        "work": "প্রযুক্তি, ব্যবসা, শিল্প, স্বাস্থ্যসেবা ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "gb": {
        "name": "United Kingdom",
        "flag": "🇬🇧",
        "leader": "রাজা তৃতীয় চার্লস",
        "cities": {
            "London": {
                "famous": "রাজধানী, আর্থিক কেন্দ্র ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
                "state": "England",
                "admin": "Sadiq Khan"
            },
            "Manchester": {
                "famous": "ফুটবল, সঙ্গীত ও শিল্পের জন্য বিখ্যাত",
                "state": "England",
                "admin": "Andy Burnham"
            },
            "Birmingham": {
                "famous": "শিল্প ও বাণিজ্যের জন্য বিখ্যাত",
                "state": "England",
                "admin": "Richard Parker"
            }
        },
        "population": "প্রায় ৬ কোটি ৯০ লাখ",
        "area": "প্রায় ২,৪৩,৬১০ বর্গকিলোমিটার",
        "food": "Fish and Chips, Roast ও Pie",
        "work": "সেবা, অর্থনীতি, প্রযুক্তি, ব্যবসা ও শিল্প",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "ca": {
        "name": "Canada",
        "flag": "🇨🇦",
        "leader": "রাজা তৃতীয় চার্লস",
        "cities": {
            "Toronto": {
                "famous": "ব্যবসা, CN Tower ও বহুসাংস্কৃতিক পরিবেশের জন্য বিখ্যাত",
                "state": "Ontario",
                "admin": "Doug Ford"
            },
            "Vancouver": {
                "famous": "পাহাড়, সমুদ্র ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
                "state": "British Columbia",
                "admin": "David Eby"
            },
            "Montreal": {
                "famous": "ফরাসি সংস্কৃতি, খাবার ও উৎসবের জন্য বিখ্যাত",
                "state": "Quebec",
                "admin": "François Legault"
            }
        },
        "population": "প্রায় ৪ কোটি ১০ লাখ",
        "area": "প্রায় ৯৯,৮৪,৬৭০ বর্গকিলোমিটার",
        "food": "Poutine, Salmon ও Maple-based খাবার",
        "work": "সেবা, প্রাকৃতিক সম্পদ, প্রযুক্তি ও ব্যবসা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "au": {
        "name": "Australia",
        "flag": "🇦🇺",
        "leader": "রাজা তৃতীয় চার্লস",
        "cities": {
            "Sydney": {
                "famous": "Opera House, Harbour Bridge ও সমুদ্রসৈকতের জন্য বিখ্যাত",
                "state": "New South Wales",
                "admin": "Chris Minns"
            },
            "Melbourne": {
                "famous": "ক্রীড়া, শিল্প ও কফি সংস্কৃতির জন্য বিখ্যাত",
                "state": "Victoria",
                "admin": "Jacinta Allan"
            },
            "Brisbane": {
                "famous": "উষ্ণ আবহাওয়া ও নদীঘেরা শহরের জন্য বিখ্যাত",
                "state": "Queensland",
                "admin": "David Crisafulli"
            }
        },
        "population": "প্রায় ২ কোটি ৭০ লাখ",
        "area": "প্রায় ৭৬,৯২,০২৪ বর্গকিলোমিটার",
        "food": "Meat Pie, Seafood ও Barbecue",
        "work": "খনি, কৃষি, শিক্ষা, স্বাস্থ্য ও সেবা",
        "duty": "সাধারণত ৭.৬ ঘণ্টা"
    },

    "de": {
        "name": "Germany",
        "flag": "🇩🇪",
        "leader": "ফ্রিডরিখ মের্ৎস",
        "cities": {
            "Berlin": {
                "famous": "রাজধানী, ইতিহাস ও সংস্কৃতির জন্য বিখ্যাত",
                "state": "Berlin",
                "admin": "Kai Wegner"
            },
            "Munich": {
                "famous": "Bavarian সংস্কৃতি, BMW ও Oktoberfest-এর জন্য বিখ্যাত",
                "state": "Bavaria",
                "admin": "Markus Söder"
            },
            "Hamburg": {
                "famous": "বন্দর ও বাণিজ্যের জন্য বিখ্যাত",
                "state": "Hamburg",
                "admin": "Peter Tschentscher"
            }
        },
        "population": "প্রায় ৮ কোটি ৪০ লাখ",
        "area": "প্রায় ৩,৫৭,৫৮৮ বর্গকিলোমিটার",
        "food": "Bratwurst, Pretzel ও বিভিন্ন Bread",
        "work": "অটোমোবাইল, প্রকৌশল, শিল্প ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "fr": {
        "name": "France",
        "flag": "🇫🇷",
        "leader": "ইমানুয়েল ম্যাক্রোঁ",
        "cities": {
            "Paris": {
                "famous": "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
                "state": "Île-de-France",
                "admin": "Valérie Pécresse"
            },
            "Lyon": {
                "famous": "খাবার, ইতিহাস ও শিল্পের জন্য বিখ্যাত",
                "state": "Auvergne-Rhône-Alpes",
                "admin": "Laurent Wauquiez"
            },
            "Marseille": {
                "famous": "ভূমধ্যসাগরীয় বন্দর ও সামুদ্রিক খাবারের জন্য বিখ্যাত",
                "state": "Provence-Alpes-Côte d'Azur",
                "admin": "Renaud Muselier"
            }
        },
        "population": "প্রায় ৬ কোটি ৮০ লাখ",
        "area": "প্রায় ৫,৫১,৬৯৫ বর্গকিলোমিটার",
        "food": "Baguette, Cheese, Croissant ও বিভিন্ন French cuisine",
        "work": "পর্যটন, শিল্প, বিমান, প্রযুক্তি ও সেবা",
        "duty": "সাধারণত ৭ ঘণ্টা"
    },

    "jp": {
        "name": "Japan",
        "flag": "🇯🇵",
        "leader": "সানায়ে তাকাইচি",
        "cities": {
            "Tokyo": {
                "famous": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
                "state": "Tokyo",
                "admin": "Yuriko Koike"
            },
            "Osaka": {
                "famous": "খাবার, ব্যবসা ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
                "state": "Osaka",
                "admin": "Hirofumi Yoshimura"
            },
            "Kyoto": {
                "famous": "মন্দির, ঐতিহ্য ও জাপানি সংস্কৃতির জন্য বিখ্যাত",
                "state": "Kyoto",
                "admin": "Takatoshi Nishiwaki"
            }
        },
        "population": "প্রায় ১২ কোটি ৩০ লাখ",
        "area": "প্রায় ৩,৭৭,৯৭৫ বর্গকিলোমিটার",
        "food": "Sushi, Ramen, Tempura ও Rice",
        "work": "প্রযুক্তি, অটোমোবাইল, ইলেকট্রনিক্স ও শিল্প",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "cn": {
        "name": "China",
        "flag": "🇨🇳",
        "leader": "শি জিনপিং",
        "cities": {
            "Beijing": {
                "famous": "রাজধানী, ঐতিহাসিক স্থাপনা ও রাজনীতি",
                "state": "Beijing",
                "admin": "Yin Li"
            },
            "Shanghai": {
                "famous": "আর্থিক কেন্দ্র ও বাণিজ্যের জন্য বিখ্যাত",
                "state": "Shanghai",
                "admin": "Gong Zheng"
            },
            "Guangzhou": {
                "famous": "ব্যবসা, শিল্প ও Cantonese খাবারের জন্য বিখ্যাত",
                "state": "Guangdong",
                "admin": "Wang Weizhong"
            }
        },
        "population": "প্রায় ১৪১ কোটি",
        "area": "প্রায় ৯৫,৯৬,৯৬০ বর্গকিলোমিটার",
        "food": "Rice, Noodles, Dumplings ও বিভিন্ন আঞ্চলিক খাবার",
        "work": "উৎপাদন, প্রযুক্তি, ব্যবসা ও শিল্প",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "sa": {
        "name": "Saudi Arabia",
        "flag": "🇸🇦",
        "leader": "বাদশাহ সালমান বিন আবদুলআজিজ",
        "cities": {
            "Riyadh": {
                "famous": "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
                "state": "Riyadh Province",
                "admin": "Prince Faisal bin Bandar"
            },
            "Jeddah": {
                "famous": "লাল সাগরের বন্দর ও ব্যবসার জন্য বিখ্যাত",
                "state": "Makkah Province",
                "admin": "Prince Khalid Al-Faisal"
            },
            "Dammam": {
                "famous": "তেল শিল্প ও উপসাগরীয় উপকূলের জন্য বিখ্যাত",
                "state": "Eastern Province",
                "admin": "Prince Saud bin Bandar"
            }
        },
        "population": "প্রায় ৩ কোটি ৫০ লাখ",
        "area": "প্রায় ২১,৪৯,৬৯০ বর্গকিলোমিটার",
        "food": "Kabsa, Mandi, Dates ও Arabic bread",
        "work": "তেল-গ্যাস, নির্মাণ, ব্যবসা ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "tr": {
        "name": "Turkey",
        "flag": "🇹🇷",
        "leader": "রেজেপ তাইয়েপ এরদোয়ান",
        "cities": {
            "Istanbul": {
                "famous": "ইউরোপ-এশিয়ার সংযোগ, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
                "state": "Istanbul Province",
                "admin": "Ekrem İmamoğlu"
            },
            "Ankara": {
                "famous": "রাজধানী ও সরকারি প্রতিষ্ঠানের জন্য বিখ্যাত",
                "state": "Ankara Province",
                "admin": "Vasip Şahin"
            },
            "Izmir": {
                "famous": "সমুদ্রতট, পর্যটন ও বাণিজ্যের জন্য বিখ্যাত",
                "state": "Izmir Province",
                "admin": "Süleyman Elban"
            }
        },
        "population": "প্রায় ৮ কোটি ৭০ লাখ",
        "area": "প্রায় ৭,৮৩,৫৬২ বর্গকিলোমিটার",
        "food": "Kebab, Pide, Baklava ও Meze",
        "work": "শিল্প, পর্যটন, কৃষি ও ব্যবসা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "it": {
        "name": "Italy",
        "flag": "🇮🇹",
        "leader": "সেরজিও মাত্তারেল্লা",
        "cities": {
            "Rome": {
                "famous": "প্রাচীন ইতিহাস, Colosseum ও Vatican-এর জন্য বিখ্যাত",
                "state": "Lazio",
                "admin": "Francesco Rocca"
            },
            "Milan": {
                "famous": "Fashion, ব্যবসা ও শিল্পের জন্য বিখ্যাত",
                "state": "Lombardy",
                "admin": "Attilio Fontana"
            },
            "Naples": {
                "famous": "Pizza, ইতিহাস ও সমুদ্রতটের জন্য বিখ্যাত",
                "state": "Campania",
                "admin": "Vincenzo De Luca"
            }
        },
        "population": "প্রায় ৫ কোটি ৯০ লাখ",
        "area": "প্রায় ৩,০১,৩৪০ বর্গকিলোমিটার",
        "food": "Pizza, Pasta, Risotto ও Gelato",
        "work": "শিল্প, Fashion, পর্যটন ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "br": {
        "name": "Brazil",
        "flag": "🇧🇷",
        "leader": "লুইজ ইনাসিও লুলা দা সিলভা",
        "cities": {
            "Sao Paulo": {
                "famous": "ব্যবসা, শিল্প ও আর্থিক কর্মকাণ্ডের জন্য বিখ্যাত",
                "state": "São Paulo",
                "admin": "Tarcísio de Freitas"
            },
            "Rio de Janeiro": {
                "famous": "Copacabana Beach, Carnival ও Christ the Redeemer-এর জন্য বিখ্যাত",
                "state": "Rio de Janeiro",
                "admin": "Cláudio Castro"
            },
            "Brasilia": {
                "famous": "দেশের রাজধানী ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
                "state": "Federal District",
                "admin": "Ibaneis Rocha"
            }
        },
        "population": "প্রায় ২১ কোটি ৩০ লাখ",
        "area": "প্রায় ৮৫,১৫,৭৬৭ বর্গকিলোমিটার",
        "food": "Feijoada, Rice, Beans ও Churrasco",
        "work": "কৃষি, খনি, শিল্প, ব্যবসা ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "mx": {
        "name": "Mexico",
        "flag": "🇲🇽",
        "leader": "ক্লাউদিয়া শেইনবাউম",
        "cities": {
            "Mexico City": {
                "famous": "রাজধানী, ইতিহাস ও সংস্কৃতির জন্য বিখ্যাত",
                "state": "Mexico City",
                "admin": "Clara Brugada"
            },
            "Guadalajara": {
                "famous": "Tequila, Mariachi ও প্রযুক্তির জন্য বিখ্যাত",
                "state": "Jalisco",
                "admin": "Pablo Lemus"
            },
            "Monterrey": {
                "famous": "শিল্প, ব্যবসা ও পাহাড়ের জন্য বিখ্যাত",
                "state": "Nuevo Leon",
                "admin": "Samuel García"
            }
        },
        "population": "প্রায় ১৩ কোটি ২০ লাখ",
        "area": "প্রায় ১৯,৬৪,৩৭৫ বর্গকিলোমিটার",
        "food": "Tacos, Tamales, Mole ও Enchiladas",
        "work": "শিল্প, উৎপাদন, কৃষি, ব্যবসা ও পর্যটন",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "eg": {
        "name": "Egypt",
        "flag": "🇪🇬",
        "leader": "আবদেল ফাত্তাহ এল-সিসি",
        "cities": {
            "Cairo": {
                "famous": "রাজধানী, পিরামিড ও নীলনদের জন্য বিখ্যাত",
                "state": "Cairo Governorate",
                "admin": "Ibrahim Saber"
            },
            "Alexandria": {
                "famous": "ভূমধ্যসাগরীয় বন্দর ও ইতিহাসের জন্য বিখ্যাত",
                "state": "Alexandria Governorate",
                "admin": "Ahmed Khaled Hassan"
            },
            "Giza": {
                "famous": "Great Pyramid ও Sphinx-এর জন্য বিখ্যাত",
                "state": "Giza Governorate",
                "admin": "Adel El-Gabbar"
            }
        },
        "population": "প্রায় ১১ কোটি",
        "area": "প্রায় ১০,০১,৪৫০ বর্গকিলোমিটার",
        "food": "Koshari, Ful, Falafel ও Molokhia",
        "work": "কৃষি, পর্যটন, শিল্প, ব্যবসা ও সেবা",
        "duty": "সাধারণত ৮ ঘণ্টা"
    },

    "za": {
        "name": "South Africa",
        "flag": "🇿🇦",
        "leader": "সিরিল রামাফোসা",
        "cities": {
            "Cape Town": {
                "famous": "Table Mountain, সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",
                "state": "Western Cape",
                "admin": "Alan Winde"
            },
            "Johannesburg": {
                "famous": "ব্যবসা, খনি ও অর্থনীতির জন্য বিখ্যাত",
                "state": "Gauteng",
                "admin": "Panyaza Lesufi"
            },
            "Durban": {
                "famous": "সমুদ্রসৈকত, বন্দর ও পর্যটনের জন্য বিখ্যাত",
                "state": "KwaZulu-Natal",
                "admin": "Thami Ntuli"
            }
        },
        "population": "প্রায় ৬ কোটি ৪০ লাখ",
        "area": "প্রায় ১২,২১,০৩৭ বর্গকিলোমিটার",
        "food": "Braai, Bobotie, Pap ও বিভিন্ন মাংসের খাবার",
        "work": "খনি, শিল্প, কৃষি, ব্যবসা ও পর্যটন",
        "duty": "সাধারণত ৮ ঘণ্টা"
    }

}

# ==========================================
# COUNTRY-SPECIFIC NAMES
# ==========================================
NAMES = {
    "bd": [
        "মোঃ রাকিব হাসান", "সুমাইয়া আক্তার", "মাহমুদুল হাসান",
        "নুসরাত জাহান", "সাইফুল ইসলাম", "তানজিলা আক্তার", "আরিফ হোসেন"
    ],
    "in": [
        "Aarav Sharma", "Arjun Patel", "Rahul Mehta",
        "Priya Singh", "Ananya Gupta", "Rohan Verma"
    ],
    "ae": [
        "Omar Al Mansouri", "Ahmed Al Nuaimi", "Fatima Al Mazrouei",
        "Maryam Al Hashimi", "Khalid Al Mansoori"
    ],
    "us": [
        "James Williams", "Michael Johnson", "William Davis",
        "Daniel Brown", "Emily Wilson", "Sarah Miller"
    ],
    "gb": [
        "Oliver Smith", "George Williams", "Harry Taylor",
        "Emily Brown", "Sophie Wilson"
    ],
    "de": [
        "Lukas Müller", "Thomas Schneider", "Anna Weber", "Sophie Fischer"
    ],
    "fr": [
        "Jean Martin", "Pierre Bernard", "Claire Dubois", "Marie Laurent"
    ],
    "it": [
        "Marco Rossi", "Luca Romano", "Giulia Bianchi", "Sofia Conti"
    ],
    "jp": [
        "Haruto Sato", "Yuki Tanaka", "Ren Suzuki", "Aoi Yamamoto"
    ],
    "cn": [
        "Wei Zhang", "Li Wang", "Chen Liu", "Mei Zhang"
    ],
    "sa": [
        "Ahmed Al-Qahtani", "Mohammed Al-Harbi", "Fatimah Al-Shehri", "Noura Al-Otaibi"
    ],
    "tr": [
        "Mehmet Yilmaz", "Ahmet Kaya", "Elif Demir", "Zeynep Aydin"
    ],
    "br": [
        "João Silva", "Carlos Santos", "Lucas Oliveira", "Ana Souza"
    ],
    "mx": [
        "Carlos Hernández", "Luis García", "Diego Martínez", "Sofía López"
    ],
    "eg": [
        "Ahmed Hassan", "Mohamed Ali", "Omar Mahmoud", "Mariam Ahmed"
    ],
    "za": [
        "Thabo Mokoena", "Sipho Dlamini", "Lerato Molefe", "Nomsa Ndlovu"
    ]
}

DEFAULT_NAMES = [
    "Alexander Martin", "Daniel Thomas", "Michael Anderson",
    "James Wilson", "Emma Taylor", "Sarah Johnson"
]

# ==========================================
# GENERATOR FUNCTIONS
# ==========================================
def get_country_code(value):
    value = value.strip().lower()

    if value in COUNTRIES:
        return value

    aliases = {
        "bangladesh": "bd", "বাংলাদেশ": "bd",
        "india": "in", "uae": "ae", "dubai": "ae",
        "america": "us", "usa": "us", "united states": "us",
        "uk": "gb", "united kingdom": "gb",
        "germany": "de", "france": "fr", "italy": "it",
        "japan": "jp", "china": "cn", "saudi": "sa",
        "saudi arabia": "sa", "turkey": "tr", "brazil": "br",
        "mexico": "mx", "egypt": "eg", "south africa": "za",
        "canada": "ca", "australia": "au"
    }

    return aliases.get(value)

def generate_name(code):
    names = NAMES.get(code, DEFAULT_NAMES)
    return random.choice(names)

def generate_postal(code, city):
    if code == "bd":
        postcodes = {
            "Dhaka": ["1000", "1100", "1205", "1212", "1216"],
            "Chattogram": ["4000", "4100", "4203"],
            "Rajshahi": ["6000", "6201"],
            "Khulna": ["9000", "9100"],
            "Sylhet": ["3100", "3101"]
        }
        return random.choice(postcodes.get(city, ["1000"]))

    if code == "in":
        pins = {
            "Mumbai": ["400001", "400050", "400070"],
            "New Delhi": ["110001", "110002", "110003"],
            "Kolkata": ["700001", "700020", "700029"],
            "Bengaluru": ["560001", "560034", "560038"],
            "Chennai": ["600001", "600018", "600034"]
        }
        return random.choice(pins.get(city, ["110001"]))

    if code == "us":
        zips = {
            "New York": ["10001", "10011", "10018", "10019"],
            "Los Angeles": ["90001", "90012", "90015", "90028"],
            "Chicago": ["60601", "60602", "60611", "60614"],
            "Miami": ["33101", "33125", "33130"]
        }
        return random.choice(zips.get(city, ["10001"]))

    if code == "gb":
        postcodes = {
            "London": ["SW1A 1AA", "EC1A 1BB", "W1A 0AX"],
            "Manchester": ["M1 1AE", "M2 3AA", "M4 1HQ"],
            "Birmingham": ["B1 1AA", "B2 4QA"]
        }
        return random.choice(postcodes.get(city, ["SW1A 1AA"]))

    if code == "ca":
        return random.choice(["M5V 2T6", "V6B 1A1", "H2X 1Y4"])

    if code == "au":
        return random.choice(["2000", "3000", "4000", "6000"])

    if code == "ae":
        return "N/A"

    if code == "de":
        return random.choice(["10115", "20095", "80331", "50667"])

    if code == "fr":
        return random.choice(["75001", "69001", "13001"])

    if code == "it":
        return random.choice(["00118", "20121", "80100"])

    if code == "jp":
        return random.choice(["100-0001", "530-0001", "600-8001"])

    if code == "cn":
        return random.choice(["100000", "200000", "510000"])

    if code == "sa":
        return random.choice(["11564", "21442", "12211"])

    if code == "tr":
        return random.choice(["34000", "06000", "35000"])

    if code == "br":
        return random.choice(["01000-000", "20000-000", "30100-000"])

    if code == "mx":
        return random.choice(["06000", "44100", "64000"])

    if code == "eg":
        return random.choice(["11511", "21500", "12511"])

    if code == "za":
        return random.choice(["8001", "2001", "4001"])

    return str(random.randint(10000, 999999))

def generate_street():
    number = random.randint(10, 999)
    street = random.choice([
        "Main Street", "Central Road", "Market Road",
        "Station Road", "Park Avenue", "King Street",
        "High Street", "River Road"
    ])
    block = random.choice(["A", "B", "C", "D"])
    return f"{number} {street}, Block {block}"

def generate_address(code):
    info = COUNTRIES[code]
    city = random.choice(list(info["cities"].keys()))
    city_info = info["cities"][city]

    return {
        "country": info["name"],
        "flag": info["flag"],
        "leader": info["leader"],
        "name": generate_name(code),
        "street": generate_street(),
        "city": city,
        "famous": city_info["famous"],
        "state": city_info["state"],
        "admin": city_info["admin"],
        "postal": generate_postal(code, city),
        "population": info["population"],
        "area": info["area"],
        "food": info["food"],
        "work": info["work"],
        "duty": info["duty"]
    }

# ==========================================
# TAP-TO-COPY FORMATTING (HTML MODE)
# ==========================================
def format_address(data):
    return (
        f"<b>{data['country']} {data['flag']} ({data['leader']})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{data['name']}</code>\n"
        f"– <b>Street:</b> <code>{data['street']}</code>\n"
        f"– <b>City:</b> <code>{data['city']}</code>\n"
        f"  ↳ <b>বিখ্যাত:</b> <code>{data['famous']}</code>\n"
        f"– <b>State/Province:</b> <code>{data['state']}</code>\n"
        f"  ↳ <b>প্রশাসনিক প্রধান:</b> <code>{data['admin']}</code>\n"
        f"– <b>Postal Code:</b> <code>{data['postal']}</code>\n"
        f"– <b>Country Population:</b> <code>{data['population']}</code>\n"
        f"– <b>Country Area:</b> <code>{data['area']}</code>\n"
        f"– <b>প্রধান খাদ্য:</b> <code>{data['food']}</code>\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> <code>{data['work']}</code>\n"
        f"– <b>Job Duty Hour:</b> <code>{data['duty']}</code>\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

def make_keyboard(code):
    return {
        "inline_keyboard": [
            [
                {
                    "text": "🔄 Generate",
                    "callback_data": "generate:" + code
                }
            ]
        ]
    }

# ==========================================
# TELEGRAM API FUNCTIONS
# ==========================================
def api(method, data=None):
    if data is None:
        data = {}
    url = API + method
    encoded = urllib.parse.urlencode(data).encode("utf-8")

    try:
        request = urllib.request.Request(url, data=encoded)
        with urllib.request.urlopen(request, timeout=60, context=ssl_context) as response:
            raw = response.read().decode("utf-8")
            return json.loads(raw)
    except Exception as e:
        print("API ERROR:", e)
        return None

def send_message(chat_id, text, keyboard=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard, ensure_ascii=False)
    return api("sendMessage", data)

def edit_message(chat_id, message_id, text, keyboard=None):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML"
    }
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
            "<b>🌍 GLOBAL ADDRESS GENERATOR</b>\n\n"
            "Country code দিয়ে Generate করো।\n\n"
            "<code>/fake bd</code>\n"
            "<code>/fake in</code>\n"
            "<code>/fake ae</code>\n"
            "<code>/fake us</code>\n"
            "<code>/fake gb</code>\n\n"
            "🔄 Generate চাপলে একই message-এ নতুন তথ্য আসবে।"
        )
        return

    if text.startswith("/countries"):
        country_list = []
        for code, info in COUNTRIES.items():
            country_list.append(f"{info['flag']} {info['name']} — <code>{code}</code>")

        send_message(
            chat_id,
            "<b>🌍 Available Countries</b>\n\n" + "\n".join(country_list)
        )
        return

    if text.lower().startswith("/fake"):
        parts = text.split()
        if len(parts) < 2:
            send_message(
                chat_id,
                "❌ Country code দিন।\n\nExample:\n<code>/fake bd</code>\n<code>/fake in</code>\n<code>/fake ae</code>\n<code>/fake us</code>"
            )
            return

        code = get_country_code(parts[1])
        if not code:
            send_message(chat_id, "❌ Country পাওয়া যায়নি।\n\nউদাহরণ:\n<code>/fake bd</code>")
            return

        address = generate_address(code)
        output = format_address(address)
        keyboard = make_keyboard(code)
        send_message(chat_id, output, keyboard)

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
        new_output = format_address(new_address)
        new_keyboard = make_keyboard(code)
        edit_message(chat_id, message_id, new_output, new_keyboard)

# ==========================================
# MAIN LOOP
# ==========================================
def run_bot():
    print("================================")
    print(" GLOBAL ADDRESS GENERATOR")
    print("================================")
    print("Countries loaded:", len(COUNTRIES))

    # Drop Pending Updates to Fix HTTP 409 Conflict
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

# ==========================================
# START BOT
# ==========================================
if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❌ BOT TOKEN বসানো হয়নি।")
    else:
        run_bot()
