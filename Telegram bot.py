# ==========================================
# RAVEN GLOBAL COUNTRY GENERATOR
# 121 COUNTRIES (FULL SINGLE-FILE BOT CODE)
# ==========================================

import random
import time
import json
import urllib.request
import urllib.parse

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"

# code | country | flag | capital
COUNTRY_LIST = """
af|Afghanistan|🇦🇫|Kabul
al|Albania|🇦🇱|Tirana
dz|Algeria|🇩🇿|Algiers
ao|Angola|🇦🇴|Luanda
ar|Argentina|🇦🇷|Buenos Aires
am|Armenia|🇦🇲|Yerevan
au|Australia|🇦🇺|Canberra
at|Austria|🇦🇹|Vienna
az|Azerbaijan|🇦🇿|Baku
bh|Bahrain|🇧🇭|Manama
bd|Bangladesh|🇧🇩|Dhaka
bb|Barbados|🇧🇧|Bridgetown
by|Belarus|🇧🇾|Minsk
be|Belgium|🇧🇪|Brussels
bz|Belize|🇧🇿|Belmopan
bj|Benin|🇧🇯|Porto-Novo
bt|Bhutan|🇧🇹|Thimphu
bo|Bolivia|🇧🇴|Sucre
ba|Bosnia and Herzegovina|🇧🇦|Sarajevo
bw|Botswana|🇧🇼|Gaborone
br|Brazil|🇧🇷|Brasilia
bn|Brunei|🇧🇳|Bandar Seri Begawan
bg|Bulgaria|🇧🇬|Sofia
bf|Burkina Faso|🇧🇫|Ouagadougou
bi|Burundi|🇧🇮|Gitega
cv|Cabo Verde|🇨🇻|Praia
kh|Cambodia|🇰🇭|Phnom Penh
cm|Cameroon|🇨🇲|Yaounde
ca|Canada|🇨🇦|Ottawa
cf|Central African Republic|🇨🇫|Bangui
td|Chad|🇹🇩|N'Djamena
cl|Chile|🇨🇱|Santiago
cn|China|🇨🇳|Beijing
co|Colombia|🇨🇴|Bogota
km|Comoros|🇰🇲|Moroni
cg|Republic of the Congo|🇨🇬|Brazzaville
cr|Costa Rica|🇨🇷|San Jose
ci|Cote d'Ivoire|🇨🇮|Yamoussoukro
hr|Croatia|🇭🇷|Zagreb
cu|Cuba|🇨🇺|Havana
cy|Cyprus|🇨🇾|Nicosia
cz|Czechia|🇨🇿|Prague
cd|DR Congo|🇨🇩|Kinshasa
dk|Denmark|🇩🇰|Copenhagen
dj|Djibouti|🇩🇯|Djibouti
dm|Dominica|🇩🇲|Roseau
do|Dominican Republic|🇩🇴|Santo Domingo
ec|Ecuador|🇪🇨|Quito
eg|Egypt|🇪🇬|Cairo
sv|El Salvador|🇸🇻|San Salvador
gq|Equatorial Guinea|🇬🇶|Malabo
er|Eritrea|🇪🇷|Asmara
ee|Estonia|🇪🇪|Tallinn
sz|Eswatini|🇸🇿|Mbabane
et|Ethiopia|🇪🇹|Addis Ababa
fj|Fiji|🇫🇯|Suva
fi|Finland|🇫🇮|Helsinki
fr|France|🇫🇷|Paris
ga|Gabon|🇬🇦|Libreville
gm|Gambia|🇬🇲|Banjul
ge|Georgia|🇬🇪|Tbilisi
de|Germany|🇩🇪|Berlin
gh|Ghana|🇬🇭|Accra
gr|Greece|🇬🇷|Athens
gd|Grenada|🇬🇩|St. George's
gt|Guatemala|🇬🇹|Guatemala City
gn|Guinea|🇬🇳|Conakry
gw|Guinea-Bissau|🇬🇼|Bissau
gy|Guyana|🇬🇾|Georgetown
ht|Haiti|🇭🇹|Port-au-Prince
hn|Honduras|🇭🇳|Tegucigalpa
hu|Hungary|🇭🇺|Budapest
is|Iceland|🇮🇸|Reykjavik
in|India|🇮🇳|New Delhi
id|Indonesia|🇮🇩|Jakarta
ir|Iran|🇮🇷|Tehran
iq|Iraq|🇮🇶|Baghdad
ie|Ireland|🇮🇪|Dublin
il|Israel|🇮🇱|Jerusalem
it|Italy|🇮🇹|Rome
jm|Jamaica|🇯🇲|Kingston
jp|Japan|🇯🇵|Tokyo
jo|Jordan|🇯🇴|Amman
kz|Kazakhstan|🇰🇿|Astana
ke|Kenya|🇰🇪|Nairobi
kw|Kuwait|🇰🇼|Kuwait City
kg|Kyrgyzstan|🇰🇬|Bishkek
la|Laos|🇱🇦|Vientiane
lv|Latvia|🇱🇻|Riga
lb|Lebanon|🇱🇧|Beirut
ls|Lesotho|🇱🇸|Maseru
lr|Liberia|🇱🇷|Monrovia
ly|Libya|🇱🇾|Tripoli
li|Liechtenstein|🇱🇮|Vaduz
lt|Lithuania|🇱🇹|Vilnius
lu|Luxembourg|🇱🇺|Luxembourg
mg|Madagascar|🇲🇬|Antananarivo
mw|Malawi|🇲🇼|Lilongwe
my|Malaysia|🇲🇾|Kuala Lumpur
mv|Maldives|🇲🇻|Male
ml|Mali|🇲🇱|Bamako
mt|Malta|🇲🇹|Valletta
mr|Mauritania|🇲🇷|Nouakchott
mu|Mauritius|🇲🇺|Port Louis
mx|Mexico|🇲🇽|Mexico City
md|Moldova|🇲🇩|Chisinau
mc|Monaco|🇲🇨|Monaco
mn|Mongolia|🇲🇳|Ulaanbaatar
me|Montenegro|🇲🇪|Podgorica
ma|Morocco|🇲🇦|Rabat
mz|Mozambique|🇲🇿|Maputo
mm|Myanmar|🇲🇲|Naypyidaw
na|Namibia|🇳🇦|Windhoek
np|Nepal|🇳🇵|Kathmandu
nl|Netherlands|🇳🇱|Amsterdam
nz|New Zealand|🇳🇿|Wellington
ni|Nicaragua|🇳🇮|Managua
ne|Niger|🇳🇪|Niamey
ng|Nigeria|🇳🇬|Abuja
mk|North Macedonia|🇲🇰|Skopje
no|Norway|🇳🇴|Oslo
om|Oman|🇴🇲|Muscat
pk|Pakistan|🇵🇰|Islamabad
pa|Panama|🇵🇦|Panama City
pg|Papua New Guinea|🇵🇬|Port Moresby
py|Paraguay|🇵🇾|Asuncion
pe|Peru|🇵🇪|Lima
ph|Philippines|🇵🇭|Manila
pl|Poland|🇵🇱|Warsaw
pt|Portugal|🇵🇹|Lisbon
qa|Qatar|🇶🇦|Doha
ro|Romania|🇷🇴|Bucharest
ru|Russia|🇷🇺|Moscow
rw|Rwanda|🇷🇼|Kigali
sa|Saudi Arabia|🇸🇦|Riyadh
sn|Senegal|🇸🇳|Dakar
rs|Serbia|🇷🇸|Belgrade
sc|Seychelles|🇸🇨|Victoria
sl|Sierra Leone|🇸🇱|Freetown
sg|Singapore|🇸🇬|Singapore
sk|Slovakia|🇸🇰|Bratislava
si|Slovenia|🇸🇮|Ljubljana
so|Somalia|🇸🇴|Mogadishu
za|South Africa|🇿🇦|Pretoria
kr|South Korea|🇰🇷|Seoul
es|Spain|🇪🇸|Madrid
lk|Sri Lanka|🇱🇰|Sri Jayawardenepura Kotte
sd|Sudan|🇸🇩|Khartoum
sr|Suriname|🇸🇷|Paramaribo
se|Sweden|🇸🇪|Stockholm
ch|Switzerland|🇨🇭|Bern
sy|Syria|🇸🇾|Damascus
tj|Tajikistan|🇹🇯|Dushanbe
tz|Tanzania|🇹ℤ|Dodoma
th|Thailand|🇹🇭|Bangkok
tg|Togo|🇹🇬|Lome
tt|Trinidad and Tobago|🇹🇹|Port of Spain
tn|Tunisia|🇹🇳|Tunis
tr|Turkey|🇹🇷|Ankara
tm|Turkmenistan|🇹🇲|Ashgabat
ug|Uganda|🇺🇬|Kampala
ua|Ukraine|🇺🇦|Kyiv
ae|United Arab Emirates|🇦🇪|Abu Dhabi
gb|United Kingdom|🇬🇧|London
us|United States|🇺🇸|Washington
uy|Uruguay|🇺🇾|Montevideo
uz|Uzbekistan|🇺🇿|Tashkent
ve|Venezuela|🇻🇪|Caracas
vn|Vietnam|🇻🇳|Hanoi
ye|Yemen|🇾🇪|Sanaa
zm|Zambia|🇿🇲|Lusaka
zw|Zimbabwe|🇿🇼|Harare
""".strip()

COUNTRIES = {}
for line in COUNTRY_LIST.splitlines():
    parts = line.split("|")
    code = parts[0]
    name = parts[1]
    flag = parts[2]
    capital = parts[3]
    COUNTRIES[code] = {
        "name": name,
        "flag": flag,
        "capital": capital
    }

ALIASES = {}
for code, info in COUNTRIES.items():
    ALIASES[info["name"].lower()] = code

ALIASES.update({
    "bangladesh": "bd",
    "india": "in",
    "malaysia": "my",
    "qatar": "qa",
    "oman": "om",
    "portugal": "pt",
    "japan": "jp",
    "uae": "ae",
    "dubai": "ae",
    "america": "us",
    "usa": "us",
    "uk": "gb",
    "england": "gb",
    "south korea": "kr",
    "korea": "kr",
    "saudi": "sa",
    "saudi arabia": "sa",
    "turkey": "tr",
    "germany": "de",
    "france": "fr",
    "italy": "it",
    "spain": "es",
    "canada": "ca",
    "australia": "au",
    "china": "cn"
})

NAMES = {
    "bd": ["মাহমুদুল হাসান", "সুমাইয়া আক্তার", "রাকিব হাসান", "নুসরাত জাহান", "সাইফুল ইসলাম"],
    "in": ["Aarav Sharma", "Arjun Patel", "Rahul Mehta", "Priya Singh", "Ananya Gupta"],
    "my": ["Muhammad Faris", "Ahmad Hakim", "Nur Aisyah", "Siti Aminah", "Hafiz Rahman"],
    "qa": ["Mohammed Al-Kuwari", "Ahmed Al-Thani", "Fatima Al-Mansoori", "Mariam Al-Hajri"],
    "om": ["Ahmed Al-Harthy", "Mohammed Al-Balushi", "Fatma Al-Rawahi", "Aisha Al-Hinai"],
    "ae": ["Omar Al Mansouri", "Ahmed Al Nuaimi", "Fatima Al Mazrouei", "Maryam Al Hashimi"],
    "jp": ["Haruto Sato", "Yuki Tanaka", "Ren Suzuki", "Aoi Yamamoto"],
    "cn": ["Wei Zhang", "Li Wang", "Chen Liu", "Mei Zhang"],
    "de": ["Lukas Müller", "Thomas Schneider", "Anna Weber", "Sophie Fischer"],
    "fr": ["Jean Martin", "Pierre Bernard", "Claire Dubois", "Marie Laurent"],
    "it": ["Marco Rossi", "Luca Romano", "Giulia Bianchi", "Sofia Conti"],
    "es": ["Carlos García", "Miguel Fernández", "Lucía Martínez", "Sofía López"],
    "pt": ["João Silva", "Miguel Santos", "Tiago Pereira", "Ana Ferreira"],
    "us": ["James Williams", "Michael Johnson", "William Davis", "Daniel Brown", "Emily Wilson"],
    "gb": ["Oliver Smith", "George Williams", "Harry Taylor", "Emily Brown"],
    "ca": ["Liam Martin", "Noah Wilson", "Emma Thompson", "Olivia Brown"],
    "au": ["Jack Smith", "William Jones", "Charlotte Brown", "Amelia Wilson"],
    "br": ["João Silva", "Carlos Santos", "Lucas Oliveira", "Ana Souza"],
    "mx": ["Carlos Hernández", "Luis García", "Diego Martínez", "Sofía López"],
    "tr": ["Mehmet Yılmaz", "Ahmet Kaya", "Elif Demir", "Zeynep Aydın"],
    "sa": ["Ahmed Al-Qahtani", "Mohammed Al-Harbi", "Fatimah Al-Shehri", "Noura Al-Otaibi"],
    "eg": ["Ahmed Hassan", "Mohamed Ali", "Omar Mahmoud", "Mariam Ahmed"],
    "za": ["Thabo Mokoena", "Sipho Dlamini", "Lerato Molefe", "Nomsa Ndlovu"]
}

DEFAULT_NAMES = [
    "Alexander Martin",
    "Daniel Thomas",
    "Michael Anderson",
    "James Wilson",
    "Emma Taylor",
    "Sarah Johnson"
]

CITY_INFO = {
    "Dhaka": "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Mumbai": "বলিউড, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
    "Kuala Lumpur": "Petronas Twin Towers, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Doha": "আধুনিক স্থাপত্য, ব্যবসা ও বিশ্বকাপ আয়োজনের জন্য বিখ্যাত",
    "Muscat": "সমুদ্র, পাহাড় ও ঐতিহ্যবাহী আরব স্থাপত্যের জন্য বিখ্যাত",
    "Dubai": "আকাশচুম্বী ভবন, পর্যটন, ব্যবসা ও শপিংয়ের জন্য বিখ্যাত",
    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Beijing": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Berlin": "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",
    "Paris": "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
    "Rome": "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",
    "Madrid": "ফুটবল, শিল্প, সংস্কৃতি ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Lisbon": "ঐতিহাসিক স্থাপনা, সমুদ্র ও Portuguese culture-এর জন্য বিখ্যাত",
    "London": "রাজধানী, ব্যবসা, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
    "New York": "আর্থিক কেন্দ্র, Times Square ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Toronto": "ব্যবসা, CN Tower ও বহুসাংস্কৃতিক পরিবেশের জন্য বিখ্যাত",
    "Sydney": "Opera House, Harbour Bridge ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Sao Paulo": "ব্যবসা, শিল্প ও আর্থিক কর্মকাণ্ডের জন্য বিখ্যাত",
    "Mexico City": "রাজধানী, ইতিহাস ও সংস্কৃতির জন্য বিখ্যাত",
    "Istanbul": "ইউরোপ-এশিয়ার সংযোগ, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
    "Riyadh": "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Cairo": "পিরামিড, নীলনদ ও প্রাচীন ইতিহাসের জন্য বিখ্যাত",
    "Johannesburg": "ব্যবসা, খনি ও অর্থনীতির জন্য বিখ্যাত"
}

FACTS = {
    "bd": {"population": "প্রায় ১৭.৫ কোটি", "area": "প্রায় ১,৪৭,৫৭০ বর্গকিলোমিটার", "food": "ভাত, মাছ, ডাল ও ভর্তা", "work": "গার্মেন্টস, কৃষি, ব্যবসা ও সেবা", "duty": "সাধারণত ৮ ঘণ্টা"},
    "in": {"population": "প্রায় ১৪৬ কোটি", "area": "প্রায় ৩২,৮৭,২৬৩ বর্গকিলোমিটার", "food": "ভাত, রুটি, ডাল ও বিরিয়ানি", "work": "IT, ব্যবসা, কৃষি, শিল্প ও সেবা", "duty": "সাধারণত ৮–১০ ঘণ্টা"},
    "my": {"population": "প্রায় ৩.৫ কোটি", "area": "প্রায় ৩,৩০,৮০৩ বর্গকিলোমিটার", "food": "Nasi Lemak, Satay ও Laksa", "work": "Manufacturing, ব্যবসা, প্রযুক্তি ও সেবা", "duty": "সাধারণত ৮ ঘণ্টা"},
    "qa": {"population": "প্রায় ৩০ লাখ", "area": "প্রায় ১১,৫৮৬ বর্গকিলোমিটার", "food": "Machboos, Harees ও Dates", "work": "তেল-গ্যাস, ব্যবসা, নির্মাণ ও সেবা", "duty": "সাধারণত ৮ ঘণ্টা"},
    "om": {"population": "প্রায় ৫৫ লাখ", "area": "প্রায় ৩,০৯,৫০০ বর্গকিলোমিটার", "food": "Shuwa, Majboos ও Dates", "work": "তেল-গ্যাস, বাণিজ্য, পর্যটন ও সেবা", "duty": "সাধারণত ৮ ঘণ্টা"},
    "ae": {"population": "প্রায় ১ কোটি", "area": "প্রায় ৮৩,৬০০ বর্গকিলোমিটার", "food": "Machboos, Hummus, Shawarma ও Dates", "work": "ব্যবসা, তেল-গ্যাস, নির্মাণ ও পর্যটন", "duty": "সাধারণত ৮ ঘণ্টা"},
    "jp": {"population": "প্রায় ১২.৩ কোটি", "area": "প্রায় ৩,৭৭,৯৭৫ বর্গকিলোমিটার", "food": "Sushi, Ramen ও Tempura", "work": "প্রযুক্তি, অটোমোবাইল ও শিল্প", "duty": "সাধারণত ৮ ঘণ্টা"},
    "us": {"population": "প্রায় ৩৪ কোটি", "area": "প্রায় ৯৮,৩৩,৫১৭ বর্গকিলোমিটার", "food": "Burger, Steak, Pizza", "work": "Technology, Business, Industry ও Services", "duty": "সাধারণত ৮ ঘণ্টা"},
    "gb": {"population": "প্রায় ৬.৯ কোটি", "area": "প্রায় ২,৪৩,৬১০ বর্গকিলোমিটার", "food": "Fish and Chips, Roast ও Pie", "work": "Finance, Services, Technology ও Business", "duty": "সাধারণত ৮ ঘণ্টা"}
}

LEADERS = {
    "bd": "রাষ্ট্রপ্রধান",
    "in": "নরেন্দ্র মোদি",
    "us": "ডোনাল্ড ট্রাম্প",
    "cn": "শি জিনপিং",
    "jp": "সানায়ে তাকাইচি",
    "my": "আনোয়ার ইব্রাহিম",
    "qa": "শেখ মোহাম্মদ বিন আবদুর রহমান",
    "om": "হাইথাম বিন তারিক",
    "ae": "শেখ মোহাম্মদ বিন জায়েদ আল নাহিয়ান",
    "gb": "রাজা তৃতীয় চার্লস",
    "ca": "রাজা তৃতীয় চার্লস",
    "au": "রাজা তৃতীয় চার্লস",
    "de": "ফ্রিডরিখ মের্ৎস",
    "fr": "ইমানুয়েল ম্যাক্রোঁ",
    "it": "সেরজিও মাত্তারেল্লা",
    "es": "রাজা ষষ্ঠ ফিলিপ",
    "pt": "মার্সেলো রেবেলো দে সুজা",
    "sa": "বাদশাহ সালমান বিন আবদুলআজিজ",
    "tr": "রেজেপ তাইয়েপ এরদোয়ান",
    "br": "লুইজ ইনাসিও লুলা দা সিলভা",
    "mx": "ক্লাউদিয়া শেইনবাউম",
    "eg": "আবদেল ফাত্তাহ এল-সিসি",
    "za": "সিরিল রামাফোসা"
}

def generate_name(code):
    return random.choice(NAMES.get(code, DEFAULT_NAMES))

def generate_postal(code):
    formats = {
        "bd": lambda: random.choice(["1000", "1100", "1205", "4000", "6000", "3100"]),
        "in": lambda: str(random.randint(110000, 999999)),
        "us": lambda: str(random.randint(10000, 99999)),
        "gb": lambda: random.choice(["SW1A 1AA", "EC1A 1BB", "M1 1AE"]),
        "ca": lambda: random.choice(["M5V 2T6", "V6B 1A1", "H2X 1Y4"]),
        "au": lambda: random.choice(["2000", "3000", "4000", "6000"]),
        "de": lambda: random.choice(["10115", "20095", "80331", "50667"]),
        "fr": lambda: random.choice(["75001", "69001", "13001"]),
        "it": lambda: random.choice(["00118", "20121", "80100"]),
        "jp": lambda: random.choice(["100-0001", "530-0001", "600-8001"]),
        "cn": lambda: random.choice(["100000", "200000", "510000"]),
        "my": lambda: random.choice(["50000", "50100", "50450"]),
        "qa": lambda: "N/A",
        "om": lambda: "N/A",
        "ae": lambda: "N/A",
        "pt": lambda: random.choice(["1000-001", "4000-001"]),
        "es": lambda: random.choice(["28001", "08001", "41001"]),
        "tr": lambda: random.choice(["06000", "34000", "35000"])
    }
    if code in formats:
        return formats[code]()
    return str(random.randint(10000, 999999))

def generate_address(code):
    info = COUNTRIES[code]
    city = info["capital"]
    street = (
        str(random.randint(10, 999))
        + " "
        + random.choice(["Main Street", "Central Road", "Market Road", "Station Road", "Park Avenue"])
        + ", Block "
        + random.choice(["A", "B", "C", "D"])
    )
    facts = FACTS.get(code, {
        "population": "তথ্য দেখুন",
        "area": "তথ্য দেখুন",
        "food": "স্থানীয় খাবার",
        "work": "Business / Job / Services",
        "duty": "সাধারণত ৮ ঘণ্টা"
    })

    return {
        "country": info["name"],
        "flag": info["flag"],
        "leader": LEADERS.get(code, "রাষ্ট্রপ্রধান / সরকারপ্রধান"),
        "name": generate_name(code),
        "street": street,
        "city": city,
        "famous": CITY_INFO.get(city, "ঐতিহাসিক, সাংস্কৃতিক ও অর্থনৈতিক গুরুত্বের জন্য পরিচিত"),
        "state": info["capital"] + " Region",
        "postal": generate_postal(code),
        "population": facts["population"],
        "area": facts["area"],
        "food": facts["food"],
        "work": facts["work"],
        "duty": facts["duty"]
    }

def format_address(data):
    return (
        f"<b>{data['country']} {data['flag']} ({data['leader']})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> {data['name']}\n"
        f"– <b>Street:</b> {data['street']}\n"
        f"– <b>City:</b> {data['city']}\n"
        f"  ↳ <b>বিখ্যাত:</b> {data['famous']}\n"
        f"– <b>State/Region:</b> {data['state']}\n"
        f"– <b>Postal Code:</b> {data['postal']}\n"
        f"– <b>Country Population:</b> {data['population']}\n"
        f"– <b>Country Area:</b> {data['area']}\n"
        f"– <b>প্রধান খাদ্য:</b> {data['food']}\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> {data['work']}\n"
        f"– <b>Job Duty Hour:</b> {data['duty']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

def api(method, data=None):
    if data is None:
        data = {}
    encoded = urllib.parse.urlencode(data).encode("utf-8")
    try:
        request = urllib.request.Request(API + method, data=encoded)
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
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

def handle_message(message):
    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if text.startswith("/start"):
        send_message(
            chat_id,
            "<b>🌍 COUNTRY DETAILS 🚀</b>\n\n"
            "121 Country Generator Ready.\n\n"
            "Example:\n"
            "<code>/fake bd</code>\n"
            "<code>/fake malaysia</code>\n"
            "<code>/fake qatar</code>\n"
            "<code>/fake oman</code>\n"
            "<code>/fake portugal</code>\n"
            "<code>/fake japan</code>\n\n"
            "🔄 Generate চাপলে একই card পরিবর্তন হবে।"
        )
        return

    if text.lower().startswith("/countries"):
        lines = []
        for code, info in COUNTRIES.items():
            lines.append(f"{info['flag']} {info['name']} — <code>{code}</code>")
        send_message(
            chat_id,
            "<b>🌍 121 COUNTRIES</b>\n\n" + "\n".join(lines)
        )
        return

    if text.lower().startswith("/fake"):
        parts = text.split(None, 1)
        if len(parts) < 2:
            send_message(
                chat_id,
                "❌ Country দিন।\n\n"
                "Example:\n"
                "<code>/fake malaysia</code>\n"
                "<code>/fake qatar</code>\n"
                "<code>/fake oman</code>"
            )
            return

        country_input = parts[1].strip().lower()
        code = ALIASES.get(country_input)

        if not code and country_input in COUNTRIES:
            code = country_input

        if not code:
            send_message(
                chat_id,
                "❌ Country পাওয়া যায়নি।\n\n"
                "Try:\n"
                "<code>/fake malaysia</code>\n"
                "<code>/fake qatar</code>\n"
                "<code>/fake oman</code>\n"
                "<code>/fake portugal</code>\n"
                "<code>/fake japan</code>"
            )
            return

        address = generate_address(code)
        output = format_address(address)
        keyboard = make_keyboard(code)

        send_message(chat_id, output, keyboard)
        return

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
        keyboard = make_keyboard(code)

        edit_message(chat_id, message_id, new_output, keyboard)


def run_bot():
    print("================================")
    print(" RAVEN COUNTRY DETAILS BOT")
    print("================================")
    print("Countries loaded:", len(COUNTRIES))
    print("Bot is running...\n")

    offset = 0

    while True:
        try:
            result = api("getUpdates", {"timeout": 50, "offset": offset})
            if not result or not result.get("ok"):
                time.sleep(2)
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
            print("Bot stopped.")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            time.sleep(5)

if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❌ BOT TOKEN বসাও।")
    else:
        run_bot()

