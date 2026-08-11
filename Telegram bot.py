# ==========================================
# GLOBAL COUNTRY ADDRESS BOT
# 121 COUNTRIES (FULL SINGLE-FILE BOT CODE WITH MONO/COPY FORMAT)
# ==========================================

import random
import time
import json
import urllib.request
import urllib.parse

BOT_TOKEN = "7633364572:AAHoxt4ER_KUBoA6sfxkFKXtlTT3t529Zg4"

API = "https://api.telegram.org/bot" + BOT_TOKEN + "/"


# ==========================================
# 121 COUNTRIES
# code | country | flag | cities
# ==========================================

RAW_COUNTRIES = """
bd|Bangladesh|🇧🇩|Dhaka,Chattogram,Rajshahi,Khulna,Sylhet
in|India|🇮🇳|Mumbai,Delhi,Kolkata,Bengaluru,Chennai,Hyderabad
my|Malaysia|🇲🇾|Kuala Lumpur,George Town,Johor Bahru,Malacca,Kota Kinabalu
qa|Qatar|🇶🇦|Doha,Al Rayyan,Al Wakrah,Umm Salal
om|Oman|🇴🇲|Muscat,Salalah,Sohar,Nizwa,Sur
pt|Portugal|🇵🇹|Lisbon,Porto,Braga,Coimbra,Faro
jp|Japan|🇯🇵|Tokyo,Osaka,Kyoto,Yokohama,Nagoya
ae|United Arab Emirates|🇦🇪|Dubai,Abu Dhabi,Sharjah,Ajman,Al Ain
us|United States|🇺🇸|New York,Los Angeles,Chicago,Miami,Houston
gb|United Kingdom|🇬🇧|London,Manchester,Birmingham,Liverpool,Leeds
ca|Canada|🇨🇦|Toronto,Vancouver,Montreal,Calgary,Ottawa
au|Australia|🇦🇺|Sydney,Melbourne,Brisbane,Perth,Adelaide
de|Germany|🇩🇪|Berlin,Munich,Hamburg,Frankfurt,Cologne
fr|France|🇫🇷|Paris,Lyon,Marseille,Toulouse,Nice
it|Italy|🇮🇹|Rome,Milan,Naples,Turin,Florence
es|Spain|🇪🇸|Madrid,Barcelona,Valencia,Seville,Bilbao
tr|Turkey|🇹🇷|Istanbul,Ankara,Izmir,Bursa,Antalya
sa|Saudi Arabia|🇸🇦|Riyadh,Jeddah,Dammam,Mecca,Medina
cn|China|🇨🇳|Beijing,Shanghai,Guangzhou,Shenzhen,Chengdu
kr|South Korea|🇰🇷|Seoul,Busan,Incheon,Daegu,Daejeon
id|Indonesia|🇮🇩|Jakarta,Surabaya,Bandung,Medan,Semarang
th|Thailand|🇹🇭|Bangkok,Chiang Mai,Pattaya,Phuket,Ayutthaya
vn|Vietnam|🇻🇳|Hanoi,Ho Chi Minh City,Da Nang,Haiphong,Hue
ph|Philippines|🇵🇭|Manila,Cebu City,Davao City,Quezon City,Taguig
pk|Pakistan|🇵🇰|Islamabad,Karachi,Lahore,Rawalpindi,Peshawar
np|Nepal|🇳🇵|Kathmandu,Pokhara,Lalitpur,Bharatpur,Biratnagar
lk|Sri Lanka|🇱🇰|Colombo,Kandy,Galle,Jaffna,Negombo
mv|Maldives|🇲🇻|Male,Addu City,Fuvahmulah,Hulhumale
sg|Singapore|🇸🇬|Singapore
bn|Brunei|🇧🇳|Bandar Seri Begawan,Kuala Belait,Seria,Tutong
kh|Cambodia|🇰🇭|Phnom Penh,Siem Reap,Battambang,Sihanoukville
la|Laos|🇱🇦|Vientiane,Luang Prabang,Pakse,Savannakhet
mm|Myanmar|🇲🇲|Yangon,Mandalay,Naypyidaw,Bago,Mawlamyine
mn|Mongolia|🇲🇳|Ulaanbaatar,Erdenet,Darkhan,Choibalsan
kz|Kazakhstan|🇰🇿|Almaty,Astana,Shymkent,Karaganda,Atyrau
uz|Uzbekistan|🇺🇿|Tashkent,Samarkand,Bukhara,Andijan,Namangan
kg|Kyrgyzstan|🇰🇬|Bishkek,Osh,Jalal-Abad,Tokmok,Karakol
tj|Tajikistan|🇹🇯|Dushanbe,Khujand,Kulob,Istaravshan,Tursunzoda
tm|Turkmenistan|🇹🇲|Ashgabat,Turkmenabat,Mary,Dashoguz,Balkanabat
af|Afghanistan|🇦🇫|Kabul,Herat,Kandahar,Mazar-i-Sharif,Jalalabad
ir|Iran|🇮🇷|Tehran,Isfahan,Shiraz,Tabriz,Mashhad
iq|Iraq|🇮🇶|Baghdad,Basra,Erbil,Mosul,Najaf
jo|Jordan|🇯🇴|Amman,Zarqa,Irbid,Aqaba,Madaba
lb|Lebanon|🇱🇧|Beirut,Tripoli,Byblos,Zahle,Sidon
il|Israel|🇮🇱|Jerusalem,Tel Aviv,Haifa,Eilat,Nazareth
kw|Kuwait|🇰🇼|Kuwait City,Hawally,Salmiya,Farwaniya,Ahmadi
bh|Bahrain|🇧🇭|Manama,Riffa,Muharraq,Hamad Town,Isa Town
sy|Syria|🇸🇾|Damascus,Aleppo,Homs,Latakia,Hama
ye|Yemen|🇾🇪|Sanaa,Aden,Taiz,Hodeidah,Ibb
eg|Egypt|🇪🇬|Cairo,Alexandria,Giza,Luxor,Aswan
ma|Morocco|🇲🇦|Rabat,Casablanca,Marrakesh,Fes,Tangier
dz|Algeria|🇩🇿|Algiers,Oran,Constantine,Annaba,Blida
tn|Tunisia|🇹🇳|Tunis,Sfax,Sousse,Bizerte,Gabes
ly|Libya|🇱🇾|Tripoli,Benghazi,Misrata,Derna,Sabha
sd|Sudan|🇸🇩|Khartoum,Omdurman,Port Sudan,Nyala,El Obeid
et|Ethiopia|🇪🇹|Addis Ababa,Gondar,Mekelle,Dire Dawa,Bahir Dar
ke|Kenya|🇰🇪|Nairobi,Mombasa,Kisumu,Nakuru,Eldoret
tz|Tanzania|🇹🇿|Dodoma,Dar es Salaam,Arusha,Mwanza,Zanzibar City
ug|Uganda|🇺🇬|Kampala,Entebbe,Jinja,Mbarara,Gulu
rw|Rwanda|🇷🇼|Kigali,Butare,Gisenyi,Ruhengeri,Byumba
gh|Ghana|🇬🇭|Accra,Kumasi,Tamale,Takoradi,Cape Coast
ng|Nigeria|🇳🇬|Abuja,Lagos,Kano,Ibadan,Port Harcourt
za|South Africa|🇿🇦|Johannesburg,Cape Town,Durban,Pretoria,Port Elizabeth
zm|Zambia|🇿🇲|Lusaka,Kitwe,Ndola,Livingstone,Kabwe
zw|Zimbabwe|🇿🇼|Harare,Bulawayo,Mutare,Gweru,Kwekwe
bw|Botswana|🇧🇼|Gaborone,Francistown,Maun,Molepolole,Kasane
na|Namibia|🇳🇦|Windhoek,Swakopmund,Walfish Bay,Otjiwarongo,Rundu
ao|Angola|🇦🇴|Luanda,Huambo,Lubango,Benguela,Malanje
mz|Mozambique|🇲🇿|Maputo,Matola,Nampula,Beira,Chimoio
mg|Madagascar|🇲🇬|Antananarivo,Toamasina,Antsirabe,Fianarantsoa,Mahajanga
mu|Mauritius|🇲🇺|Port Louis,Beau Bassin,Curepipe,Quatre Bornes,Vacoas
sn|Senegal|🇸🇳|Dakar,Thies,Saint-Louis,Touba,Kaolack
ci|Cote d'Ivoire|🇨🇮|Abidjan,Yamoussoukro,Bouake,San-Pedro,Korhogo
cm|Cameroon|🇨🇲|Yaounde,Douala,Garoua,Bafoussam,Limbé
bf|Burkina Faso|🇧🇫|Ouagadougou,Bobo-Dioulasso,Koudougou,Ouahigouya,Banfora
ml|Mali|🇲🇱|Bamako,Sikasso,Mopti,Segou,Koutiala
ne|Niger|🇳🇪|Niamey,Maradi,Zinder,Agadez,Tahoua
gn|Guinea|🇬🇳|Conakry,Kankan,Labe,Nzerekore,Kindia
sl|Sierra Leone|🇸🇱|Freetown,Bo,Koidu,Makeni,Kenema
lr|Liberia|🇱🇷|Monrovia,Gbarnga,Buchanan,Ganta,Harper
gm|Gambia|🇬🇲|Banjul,Serekunda,Brikama,Bakau,Fara
bj|Benin|🇧🇯|Porto-Novo,Cotonou,Parakou,Abomey,Natitingou
tg|Togo|🇹🇬|Lome,Sokode,Kara,Atakpame,Kpalime
ga|Gabon|🇬🇦|Libreville,Port-Gentil,Franceville,Oyem,Moanda
cg|Republic of the Congo|🇨🇬|Brazzaville,Pointe-Noire,Dolisie,Ouesso,Owando
cd|DR Congo|🇨🇩|Kinshasa,Lubumbashi,Goma,Kisangani,Mbuji-Mayi
cf|Central African Republic|🇨🇫|Bangui,Berberati,Bambari,Bouar,Bossangoa
td|Chad|🇹🇩|N'Djamena,Moundou,Sarh,Abeche,Kelo
so|Somalia|🇸🇴|Mogadishu,Hargeisa,Kismayo,Bosaso,Garowe
dj|Djibouti|🇩🇯|Djibouti City,Ali Sabieh,Tadjourah,Dikhil,Obock
er|Eritrea|🇪🇷|Asmara,Keren,Massawa,Agordat,Assab
ss|South Sudan|🇸🇸|Juba,Wau,Malakal,Yei,Bor
mr|Mauritania|🇲🇷|Nouakchott,Nouadhibou,Kiffa,Rosso,Atar
cv|Cabo Verde|🇨🇻|Praia,Mindelo,Assomada,Espargos,Sal Rei
ru|Russia|🇷🇺|Moscow,St Petersburg,Kazan,Novosibirsk,Yekaterinburg
ua|Ukraine|🇺🇦|Kyiv,Lviv,Kharkiv,Odesa,Dnipro
pl|Poland|🇵🇱|Warsaw,Krakow,Wroclaw,Gdansk,Poznan
cz|Czechia|🇨🇿|Prague,Brno,Ostrava,Plzen,Liberec
sk|Slovakia|🇸🇰|Bratislava,Kosice,Presov,Nitra,Zilina
hu|Hungary|🇭🇺|Budapest,Debrecen,Szeged,Miskolc,Pecs
at|Austria|🇦🇹|Vienna,Graz,Linz,Salzburg,Innsbruck
ch|Switzerland|🇨🇭|Zurich,Geneva,Basel,Bern,Lausanne
nl|Netherlands|🇳🇱|Amsterdam,Rotterdam,The Hague,Utrecht,Eindhoven
be|Belgium|🇧🇪|Brussels,Antwerp,Ghent,Bruges,Liege
lu|Luxembourg|🇱🇺|Luxembourg City,Esch-sur-Alzette,Dudelange
ie|Ireland|🇮🇪|Dublin,Cork,Limerick,Galway,Waterford
is|Iceland|🇮🇸|Reykjavik,Kopavogur,Hafnarfjordur,Akureyri,Reykjanesbaer
no|Norway|🇳🇴|Oslo,Bergen,Trondheim,Stavanger,Tromso
se|Sweden|🇸🇪|Stockholm,Gothenburg,Malmo,Uppsala,Vasteras
fi|Finland|🇫🇮|Helsinki,Espoo,Tampere,Turku,Oulu
dk|Denmark|🇩🇰|Copenhagen,Aarhus,Odense,Aalborg,Esbjerg
ee|Estonia|🇪🇪|Tallinn,Tartu,Narva,Pärnu,Kohtla-Jarve
lv|Latvia|🇱🇻|Riga,Daugavpils,Liepaja,Jelgava,Jurmala
lt|Lithuania|🇱🇹|Vilnius,Kaunas,Klaipeda,Siauliai,Panevezys
gr|Greece|🇬🇷|Athens,Thessaloniki,Patras,Heraklion,Larissa
ro|Romania|🇷🇴|Bucharest,Cluj-Napoca,Timisoara,Iasi,Constanta
bg|Bulgaria|🇧🇬|Sofia,Plovdiv,Varna,Burgas,Ruse
rs|Serbia|🇷🇸|Belgrade,Novi Sad,Nis,Kragujevac,Subotica
hr|Croatia|🇭🇷|Zagreb,Split,Rijeka,Osijek,Zadar
si|Slovenia|🇸🇮|Ljubljana,Maribor,Celje,Kranj,Koper
ba|Bosnia and Herzegovina|🇧🇦|Sarajevo,Banja Luka,Mostar,Tuzla,Zenica
me|Montenegro|🇲🇪|Podgorica,Niksic,Budva,Cetinje,Bar
mk|North Macedonia|🇲🇰|Skopje,Bitola,Kumanovo,Ohrid,Prilep
al|Albania|🇦🇱|Tirana,Durrës,Vlore,Shkoder,Elbasan
ge|Georgia|🇬🇪|Tbilisi,Batumi,Kutaisi,Rustavi,Gori
am|Armenia|🇦🇲|Yerevan,Gyumri,Vagharshapat,Vanadzor,Hrazdan
az|Azerbaijan|🇦🇿|Baku,Ganja,Sumqayit,Lankaran,Shaki
by|Belarus|🇧🇾|Minsk,Gomel,Mogilev,Vitebsk,Grodno
md|Moldova|🇲🇩|Chisinau,Balti,Bender,Cahul,Orhei
mt|Malta|🇲🇹|Valletta,Birkirkara,Mosta,Qormi,Sliema
cy|Cyprus|🇨🇾|Nicosia,Limasol,Larnaca,Paphos,Famagusta
il|Israel|🇮🇱|Jerusalem,Tel Aviv,Haifa,Eilat,Nazareth
ar|Argentina|🇦🇷|Buenos Aires,Cordoba,Rosario,Mendoza,La Plata
br|Brazil|🇧🇷|Sao Paulo,Rio de Janeiro,Brasilia,Salvador,Recife
cl|Chile|🇨🇱|Santiago,Valparaiso,Concepcion,Antofagasta,Temuco
pe|Peru|🇵🇪|Lima,Arequipa,Cusco,Trujillo,Chiclayo
co|Colombia|🇨🇴|Bogota,Medellin,Cali,Cartagena,Barranquilla
ec|Ecuador|🇪🇨|Quito,Guayaquil,Cuenca,Manta,Loja
bo|Bolivia|🇧🇴|La Paz,Santa Cruz,Cochabamba,Sucre,Oruro
py|Paraguay|🇵🇾|Asuncion,Ciudad del Este,San Lorenzo,Luque,Encarnacion
uy|Uruguay|🇺🇾|Montevideo,Salto,Paysandu,Las Piedras,Rivera
ve|Venezuela|🇻🇪|Caracas,Maracaibo,Valencia,Barquisimeto,Maracay
mx|Mexico|🇲🇽|Mexico City,Guadalajara,Monterrey,Puebla,Cancun
cr|Costa Rica|🇨🇷|San Jose,Alajuela,Cartago,Heredia,Liberia
pa|Panama|🇵🇦|Panama City,Colon,David,La Chorrera,Santiago
gt|Guatemala|🇬🇹|Guatemala City,Antigua,Quetzaltenango,Escuintla,Petapa
cu|Cuba|🇨🇺|Havana,Santiago de Cuba,Camaguey,Holguin,Varadero
do|Dominican Republic|🇩🇴|Santo Domingo,Santiago,La Romana,Punta Cana,Puerto Plata
jm|Jamaica|🇯🇲|Kingston,Montego Bay,Spanish Town,Portmore,Mandeville
tt|Trinidad and Tobago|🇹🇹|Port of Spain,San Fernando,Chaguanas,Arima,Scarborough
ht|Haiti|🇭🇹|Port-au-Prince,Cap-Haitien,Gonaives,Jacmel,Les Cayes
us|United States|🇺🇸|New York,Los Angeles,Chicago,Houston,Miami
ca|Canada|🇨🇦|Toronto,Vancouver,Montreal,Calgary,Ottawa
au|Australia|🇦🇺|Sydney,Melbourne,Brisbane,Perth,Adelaide
nz|New Zealand|🇳🇿|Auckland,Wellington,Christchurch,Hamilton,Dunedin
fj|Fiji|🇫🇯|Suva,Nadi,Lautoka,Nausori,Ba
pg|Papua New Guinea|🇵🇬|Port Moresby,Lae,Mount Hagen,Madang,Goroka
"""

COUNTRIES = {}

for line in RAW_COUNTRIES.strip().splitlines():
    parts = line.strip().split("|")
    if len(parts) != 4:
        continue
    code = parts[0].strip()
    COUNTRIES[code] = {
        "name": parts[1].strip(),
        "flag": parts[2].strip(),
        "cities": [x.strip() for x in parts[3].split(",") if x.strip()]
    }

ALIASES = {}
for code, info in COUNTRIES.items():
    ALIASES[info["name"].lower()] = code

ALIASES.update({
    "bd": "bd",
    "in": "in",
    "malaysia": "my",
    "my": "my",
    "qatar": "qa",
    "qa": "qa",
    "oman": "om",
    "om": "om",
    "portugal": "pt",
    "pt": "pt",
    "japan": "jp",
    "jp": "jp",
    "dubai": "ae",
    "uae": "ae",
    "america": "us",
    "usa": "us",
    "uk": "gb",
    "england": "gb",
    "korea": "kr",
    "south korea": "kr",
    "saudi": "sa",
    "turkey": "tr"
})


# ==========================================
# DATA BANKS & MAPS
# ==========================================

FAMOUS = {
    "Dhaka": "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Chattogram": "সমুদ্রবন্দর, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Rajshahi": "আম, রেশম ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Khulna": "সুন্দরবন ও শিল্পাঞ্চলের জন্য বিখ্যাত",
    "Sylhet": "চা-বাগান, পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Mumbai": "বলিউড, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
    "Delhi": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Kolkata": "সাহিত্য, সংস্কৃতি ও ঐতিহ্যের জন্য বিখ্যাত",
    "Bengaluru": "প্রযুক্তি ও IT industry-এর জন্য বিখ্যাত",
    "Chennai": "শিল্প, প্রযুক্তি ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Hyderabad": "IT industry, চারমিনার ও খাবারের জন্য বিখ্যাত",
    "Kuala Lumpur": "Petronas Twin Towers, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "George Town": "ঐতিহ্যবাহী স্থাপনা, খাবার ও সংস্কৃতির জন্য বিখ্যাত",
    "Johor Bahru": "ব্যবসা, পর্যটন ও Singapore-এর কাছাকাছি অবস্থানের জন্য বিখ্যাত",
    "Malacca": "ঐতিহাসিক স্থাপনা ও Portuguese heritage-এর জন্য বিখ্যাত",
    "Kota Kinabalu": "সমুদ্র, দ্বীপ ও Mount Kinabalu-এর জন্য বিখ্যাত",
    "Doha": "আধুনিক স্থাপত্য, ব্যবসা ও আন্তর্জাতিক ক্রীড়ার জন্য বিখ্যাত",
    "Al Rayyan": "শিক্ষা, ক্রীড়া ও আধুনিক স্থাপনার জন্য বিখ্যাত",
    "Al Wakrah": "ঐতিহ্যবাহী বাজার, সমুদ্র ও মাছ ধরার জন্য বিখ্যাত",
    "Muscat": "সমুদ্র, পাহাড় ও ঐতিহ্যবাহী আরব স্থাপত্যের জন্য বিখ্যাত",
    "Salalah": "খরিফ মৌসুম, সবুজ পাহাড় ও প্রাকৃতিক সৌন্দর্যের জন্য বিখ্যাত",
    "Sohar": "বন্দর, শিল্প ও ঐতিহাসিক ঐতিহ্যের জন্য বিখ্যাত",
    "Nizwa": "ঐতিহাসিক দুর্গ, বাজার ও সংস্কৃতির জন্য বিখ্যাত",
    "Dubai": "আকাশচুম্বী ভবন, ব্যবসা, পর্যটন ও শপিংয়ের জন্য বিখ্যাত",
    "Abu Dhabi": "রাজধানী, তেল-গ্যাস ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Sharjah": "সংস্কৃতি, জাদুঘর ও শিল্পের জন্য বিখ্যাত",
    "Ajman": "সমুদ্রসৈকত, বন্দর ও পর্যটনের জন্য বিখ্যাত",
    "Al Ain": "সবুজ বাগান, মরূদ্যান ও ঐতিহাসিক স্থানের জন্য বিখ্যাত",
    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Osaka": "ব্যবসা, খাবার ও বিনোদনের জন্য বিখ্যাত",
    "Kyoto": "প্রাচীন মন্দির, ঐতিহ্য ও সংস্কৃতির জন্য বিখ্যাত",
    "Yokohama": "বন্দর, সমুদ্র ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Nagoya": "অটোমোবাইল ও শিল্পের জন্য বিখ্যাত",
    "New York": "আর্থিক কেন্দ্র, Times Square ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Los Angeles": "Hollywood, চলচ্চিত্র ও বিনোদনের জন্য বিখ্যাত",
    "Chicago": "স্থাপত্য, ব্যবসা ও শিল্পের জন্য বিখ্যাত",
    "Houston": "Space Center, energy industry ও ব্যবসার জন্য বিখ্যাত",
    "Miami": "সমুদ্রসৈকত, পর্যটন ও nightlife-এর জন্য বিখ্যাত",
    "London": "রাজধানী, ব্যবসা, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
    "Manchester": "ফুটবল, শিল্প ও সঙ্গীতের জন্য বিখ্যাত",
    "Birmingham": "শিল্প, ব্যবসা ও শিক্ষা প্রতিষ্ঠানের জন্য বিখ্যাত",
    "Liverpool": "সঙ্গীত, বন্দর ও ফুটবলের জন্য বিখ্যাত",
    "Leeds": "ব্যবসা, শিক্ষা ও shopping-এর জন্য বিখ্যাত",
    "Paris": "Eiffel Tower, fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
    "Lyon": "খাবার, ইতিহাস ও silk industry-এর জন্য বিখ্যাত",
    "Marseille": "সমুদ্রবন্দর, Mediterranean coast ও খাবারের জন্য বিখ্যাত",
    "Toulouse": "Aerospace industry ও গোলাপি স্থাপত্যের জন্য বিখ্যাত",
    "Nice": "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",
    "Berlin": "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",
    "Munich": "BMW, শিল্প ও Oktoberfest-এর জন্য বিখ্যাত",
    "Hamburg": "বন্দর, ব্যবসা ও সঙ্গীতের জন্য বিখ্যাত",
    "Frankfurt": "ব্যাংকিং, Finance ও আন্তর্জাতিক ব্যবসার জন্য বিখ্যাত",
    "Cologne": "Cologne Cathedral ও সংস্কৃতির জন্য বিখ্যাত",
    "Rome": "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",
    "Milan": "Fashion, design ও ব্যবসার জন্য বিখ্যাত",
    "Naples": "Pizza, সমুদ্র ও ঐতিহাসিক স্থানের জন্য বিখ্যাত",
    "Turin": "Automobile industry ও ইতিহাসের জন্য বিখ্যাত",
    "Florence": "Renaissance art ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Madrid": "ফুটবল, শিল্প, সংস্কৃতি ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Barcelona": "Gaudi architecture, সমুদ্রসৈকত ও ফুটবলের জন্য বিখ্যাত",
    "Valencia": "সমুদ্রসৈকত, খাবার ও City of Arts-এর জন্য বিখ্যাত",
    "Seville": "Flamenco, ঐতিহ্য ও স্থাপত্যের জন্য বিখ্যাত",
    "Bilbao": "Guggenheim Museum ও শিল্পের জন্য বিখ্যাত",
    "Lisbon": "ঐতিহাসিক স্থাপনা, সমুদ্র ও Portuguese culture-এর জন্য বিখ্যাত",
    "Porto": "Port wine, নদী ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Braga": "ঐতিহাসিক গির্জা ও ধর্মীয় স্থাপনার জন্য বিখ্যাত",
    "Coimbra": "প্রাচীন বিশ্ববিদ্যালয় ও ইতিহাসের জন্য বিখ্যাত",
    "Faro": "Algarve region ও সমুদ্রসৈকতের জন্য বিখ্যাত",
    "Istanbul": "ইউরোপ-এশিয়ার সংযোগ, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
    "Ankara": "তুরস্কের রাজধানী ও প্রশাসনিক কেন্দ্র হিসেবে বিখ্যাত",
    "Izmir": "সমুদ্র, বন্দর ও পর্যটনের জন্য বিখ্যাত",
    "Bursa": "ঐতিহাসিক স্থাপনা ও শিল্পের জন্য বিখ্যাত",
    "Antalya": "সমুদ্রসৈকত ও পর্যটনের জন্য বিখ্যাত",
    "Riyadh": "রাজধানী, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Jeddah": "লাল সাগর, বন্দর ও ব্যবসার জন্য বিখ্যাত",
    "Dammam": "তেল-গ্যাস, শিল্প ও সমুদ্রের জন্য বিখ্যাত",
    "Mecca": "ইসলামের পবিত্রতম স্থান হিসেবে বিখ্যাত",
    "Medina": "মসজিদে নববী ও ইসলামী ইতিহাসের জন্য বিখ্যাত",
    "Beijing": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Shanghai": "Finance, বন্দর ও আধুনিক skyline-এর জন্য বিখ্যাত",
    "Guangzhou": "ব্যবসা, বাণিজ্য ও Canton Fair-এর জন্য বিখ্যাত",
    "Shenzhen": "Technology, manufacturing ও innovation-এর জন্য বিখ্যাত",
    "Chengdu": "Panda, খাবার ও প্রযুক্তির জন্য বিখ্যাত",
    "Seoul": "Technology, K-pop, fashion ও আধুনিক সংস্কৃতির জন্য বিখ্যাত",
    "Busan": "সমুদ্রসৈকত, বন্দর ও চলচ্চিত্র উৎসবের জন্য বিখ্যাত",
    "Incheon": "আন্তর্জাতিক বিমানবন্দর ও বন্দরনগরী হিসেবে বিখ্যাত",
    "Daegu": "Textile industry ও সংস্কৃতির জন্য বিখ্যাত",
    "Daejeon": "Science, research ও technology-এর জন্য বিখ্যাত"
}

NAME_BANK = {
    "bd": ["মাহমুদুল হাসান", "সাইফুল ইসলাম", "রাকিব হাসান", "নুসরাত জাহান", "সুমাইয়া আক্তার", "তানজিলা রহমান"],
    "in": ["Aarav Sharma", "Arjun Patel", "Rahul Mehta", "Priya Singh", "Ananya Gupta", "Rohan Verma"],
    "my": ["Muhammad Faris", "Ahmad Hakim", "Nur Aisyah", "Siti Aminah", "Hafiz Rahman", "Amir Hakim"],
    "qa": ["Mohammed Al-Kuwari", "Ahmed Al-Thani", "Fatima Al-Hajri", "Mariam Al-Mansoori"],
    "om": ["Ahmed Al-Harthy", "Mohammed Al-Balushi", "Fatma Al-Rawahi", "Aisha Al-Hinai"],
    "ae": ["Omar Al-Mansouri", "Ahmed Al-Nuaimi", "Fatima Al-Mazrouei", "Maryam Al-Hashimi"],
    "jp": ["Haruto Sato", "Yuki Tanaka", "Ren Suzuki", "Aoi Yamamoto", "Daiki Ito"],
    "us": ["James Williams", "Michael Johnson", "William Davis", "Daniel Brown", "Emily Wilson"],
    "gb": ["Oliver Smith", "George Williams", "Harry Taylor", "Emily Brown", "Sophie Wilson"],
    "de": ["Lukas Müller", "Thomas Schneider", "Anna Weber", "Sophie Fischer"],
    "fr": ["Jean Martin", "Pierre Bernard", "Claire Dubois", "Marie Laurent"],
    "it": ["Marco Rossi", "Luca Romano", "Giulia Bianchi", "Sofia Conti"],
    "es": ["Carlos García", "Miguel Fernández", "Lucía Martínez", "Sofía López"],
    "pt": ["João Silva", "Miguel Santos", "Tiago Pereira", "Ana Ferreira"],
    "tr": ["Mehmet Yılmaz", "Ahmet Kaya", "Elif Demir", "Zeynep Aydın"],
    "sa": ["Ahmed Al-Qahtani", "Mohammed Al-Harbi", "Fatimah Al-Shehri", "Noura Al-Otaibi"],
    "cn": ["Wei Zhang", "Li Wang", "Chen Liu", "Mei Zhang", "Jun Chen"],
    "kr": ["Kim Min-jun", "Lee Ji-hoon", "Park Seo-jun", "Choi Min-seo"]
}

DEFAULT_NAMES = [
    "Alexander Martin",
    "Daniel Thomas",
    "Michael Anderson",
    "James Wilson",
    "Emma Taylor",
    "Sarah Johnson"
]

LEADERS = {
    "in": "নরেন্দ্র মোদি",
    "my": "আনোয়ার ইব্রাহিম",
    "qa": "শেখ মোহাম্মদ বিন আবদুর রহমান",
    "om": "হাইথাম বিন তারিক",
    "ae": "শেখ মোহাম্মদ বিন জায়েদ আল নাহিয়ান",
    "jp": "সানায়ে তাকাইচি",
    "cn": "শি জিনপিং",
    "us": "ডোনাল্ড ট্রাম্প",
    "gb": "রাজা তৃতীয় চার্লস",
    "fr": "ইমানুয়েল ম্যাক্রোঁ",
    "de": "ফ্রিডরিখ মের্ৎস",
    "it": "সেরজিও মাত্তারেল্লা",
    "es": "রাজা ষষ্ঠ ফিলিপ",
    "pt": "লুইস মন্টেনেগ্রো",
    "tr": "রেজেপ তাইয়েপ এরদোয়ান",
    "sa": "বাদশাহ সালমান বিন আবদুলআজিজ",
    "br": "লুইজ ইনাসিও লুলা দা সিলভা",
    "mx": "ক্লাউদিয়া শেইনবাউম"
}

FACTS = {
    "bd": ("প্রায় ১৭.৫ কোটি", "প্রায় ১,৪৭,৫৭০ বর্গকিলোমিটার", "ভাত, মাছ, ডাল ও ভর্তা", "গার্মেন্টস / কৃষি / ব্যবসা / সেবা"),
    "in": ("প্রায় ১৪৬ কোটি", "প্রায় ৩২,৮৭,২৬৩ বর্গকিলোমিটার", "ভাত, রুটি, ডাল ও বিরিয়ানি", "IT / ব্যবসা / কৃষি / শিল্প"),
    "my": ("প্রায় ৩.৫ কোটি", "প্রায় ৩,৩০,৮০৩ বর্গকিলোমিটার", "Nasi Lemak, Satay ও Laksa", "Manufacturing / Business / Services"),
    "qa": ("প্রায় ৩০ লাখ", "প্রায় ১১,৫৮৬ বর্গকিলোমিটার", "Machboos, Harees ও Dates", "তেল-গ্যাস / Business / Construction"),
    "om": ("প্রায় ৫৫ লাখ", "প্রায় ৩,০৯,৫০০ বর্গকিলোমিটার", "Shuwa, Majboos ও Dates", "তেল-গ্যাস / Business / Tourism"),
    "ae": ("প্রায় ১ কোটি", "প্রায় ৮৩,৬০০ বর্গকিলোমিটার", "Machboos, Hummus ও Shawarma", "Business / Oil-Gas / Tourism"),
    "jp": ("প্রায় ১২.৩ কোটি", "প্রায় ৩,৭৭,৯৭৫ বর্গকিলোমিটার", "Sushi, Ramen ও Tempura", "Technology / Automobile / Industry"),
    "us": ("প্রায় ৩৪ কোটি", "প্রায় ৯৮,৩৩,৫১৭ বর্গকিলোমিটার", "Burger, Steak ও Pizza", "Technology / Business / Services"),
    "gb": ("প্রায় ৬.৯ কোটি", "প্রায় ২,৪৩,৬১০ বর্গকিলোমিটার", "Fish and Chips ও Roast", "Finance / Services / Technology")
}

STATE_MAP = {
    "my": {
        "Kuala Lumpur": "Kuala Lumpur Federal Territory",
        "George Town": "Penang",
        "Johor Bahru": "Johor",
        "Malacca": "Malacca",
        "Kota Kinabalu": "Sabah"
    },
    "in": {
        "Mumbai": "Maharashtra",
        "Delhi": "Delhi",
        "Kolkata": "West Bengal",
        "Bengaluru": "Karnataka",
        "Chennai": "Tamil Nadu",
        "Hyderabad": "Telangana"
    },
    "ae": {
        "Dubai": "Dubai Emirate",
        "Abu Dhabi": "Abu Dhabi Emirate",
        "Sharjah": "Sharjah Emirate",
        "Ajman": "Ajman Emirate",
        "Al Ain": "Abu Dhabi Emirate"
    },
    "qa": {
        "Doha": "Doha Municipality",
        "Al Rayyan": "Al Rayyan Municipality",
        "Al Wakrah": "Al Wakrah Municipality"
    },
    "om": {
        "Muscat": "Muscat Governorate",
        "Salalah": "Dhofar Governorate",
        "Sohar": "North Al Batinah",
        "Nizwa": "Ad Dakhiliyah Governorate"
    }
}


# ==========================================
# GENERATOR FUNCTIONS
# ==========================================

def postal_code(code):
    if code == "bd":
        return random.choice(["1000", "1100", "1205", "4000", "6000", "3100"])
    if code == "in":
        return random.choice(["110001", "400001", "700001", "560001", "600001", "500001"])
    if code == "my":
        return random.choice(["50000", "50100", "50450", "80000", "75000"])
    if code in ["qa", "om", "ae"]:
        return "N/A"
    if code == "jp":
        return random.choice(["100-0001", "530-0001", "600-8001", "160-0022"])
    if code == "us":
        return str(random.randint(10000, 99999))
    if code == "gb":
        return random.choice(["SW1A 1AA", "EC1A 1BB", "M1 1AE", "B1 1AA"])
    if code == "ca":
        return random.choice(["M5V 2T6", "V6B 1A1", "H2X 1Y4"])
    if code == "au":
        return random.choice(["2000", "3000", "4000", "6000"])
    if code == "de":
        return random.choice(["10115", "20095", "80331", "50667"])
    if code == "fr":
        return random.choice(["75001", "69001", "13001"])
    if code == "it":
        return random.choice(["00118", "20121", "80100"])
    if code == "pt":
        return random.choice(["1000-001", "4000-001", "3000-001"])
    if code == "es":
        return random.choice(["28001", "08001", "41001"])
    if code == "tr":
        return random.choice(["06000", "34000", "35000"])
    return str(random.randint(10000, 999999))

def make_street(code):
    special = {
        "my": ["Jalan Ampang", "Jalan Bukit Bintang", "Jalan Tun Razak", "Jalan Sultan Ismail"],
        "qa": ["Al Corniche Street", "Salwa Road", "Al Rayyan Road", "Airport Road"],
        "om": ["Sultan Qaboos Street", "Al Khuwair Street", "Al Wadi Street", "Al Noor Street"],
        "ae": ["Sheikh Zayed Road", "Al Wasl Road", "Jumeirah Street", "Al Khaleej Street"],
        "jp": ["Chuo Street", "Meiji Avenue", "Sakura Street", "Shibuya Street"],
        "in": ["MG Road", "Park Street", "Link Road", "Station Road"]
    }
    normal = ["Main Street", "Central Road", "Market Road", "Station Road", "Park Avenue", "King Street"]
    roads = special.get(code, normal)
    return str(random.randint(10, 999)) + " " + random.choice(roads) + ", Block " + random.choice(["A", "B", "C", "D"])

def get_state(code, city):
    if code in STATE_MAP and city in STATE_MAP[code]:
        return STATE_MAP[code][city]
    return city + " Region"

def generate_data(code, old_data=None):
    country = COUNTRIES[code]
    cities = country["cities"]

    # CITY MUST CHANGE
    old_city = old_data.get("city", "") if old_data else ""
    available_cities = [c for c in cities if c != old_city]
    if not available_cities:
        available_cities = cities
    city = random.choice(available_cities)

    # NAME MUST CHANGE
    names = NAME_BANK.get(code, DEFAULT_NAMES)
    old_name = old_data.get("name", "") if old_data else ""
    available_names = [n for n in names if n != old_name]
    if not available_names:
        available_names = names
    name = random.choice(available_names)

    # STREET MUST CHANGE
    old_street = old_data.get("street", "") if old_data else ""
    street = make_street(code)
    attempts = 0
    while street == old_street and attempts < 20:
        street = make_street(code)
        attempts += 1

    # POSTAL MUST CHANGE
    old_postal = old_data.get("postal", "") if old_data else ""
    postal = postal_code(code)
    attempts = 0
    while postal == old_postal and attempts < 30:
        postal = postal_code(code)
        attempts += 1

    state = get_state(code, city)
    facts = FACTS.get(code, ("দেশভেদে পরিবর্তনশীল", "দেশভেদে পরিবর্তনশীল", "স্থানীয় খাবার", "Business / Job / Services"))
    famous = FAMOUS.get(city, "স্থানীয় ইতিহাস, সংস্কৃতি, ব্যবসা ও পর্যটনের জন্য পরিচিত")

    return {
        "country": country["name"],
        "flag": country["flag"],
        "leader": LEADERS.get(code, "রাষ্ট্রপ্রধান / সরকারপ্রধান"),
        "name": name,
        "street": street,
        "city": city,
        "famous": famous,
        "state": state,
        "postal": postal,
        "population": facts[0],
        "area": facts[1],
        "food": facts[2],
        "work": facts[3],
        "duty": random.choice(["সাধারণত ৮ ঘণ্টা", "সাধারণত ৮–৯ ঘণ্টা", "সাধারণত ৮–১০ ঘণ্টা"])
    }

# ==========================================
# DISPLAY FORMAT (ALL VALUES ARE MONO FORMATTED `...`)
# ==========================================

def display_text(data):
    return (
        f"<b>{data['country']} {data['flag']} ({data['leader']})</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"– <b>Name:</b> <code>{data['name']}</code>\n"
        f"– <b>Street:</b> <code>{data['street']}</code>\n"
        f"– <b>City:</b> <code>{data['city']}</code>\n"
        f"  ↳ <b>বিখ্যাত:</b> {data['famous']}\n"
        f"– <b>State/Region:</b> <code>{data['state']}</code>\n"
        f"– <b>Postal Code:</b> <code>{data['postal']}</code>\n"
        f"– <b>Country Population:</b> {data['population']}\n"
        f"– <b>Country Area:</b> {data['area']}\n"
        f"– <b>প্রধান খাদ্য:</b> {data['food']}\n"
        f"– <b>প্রধান কর্মক্ষেত্র:</b> {data['work']}\n"
        f"– <b>Job Duty Hour:</b> {data['duty']}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

def copy_text(data):
    return (
        f"Name: {data['name']}\n"
        f"Street: {data['street']}\n"
        f"City: {data['city']}\n"
        f"State/Region: {data['state']}\n"
        f"Postal Code: {data['postal']}\n"
        f"Country: {data['country']}"
    )


# ==========================================
# TELEGRAM ENGINE
# ==========================================

def api(method, data=None):
    if data is None:
        data = {}
    try:
        encoded = urllib.parse.urlencode(data).encode("utf-8")
        request = urllib.request.Request(API + method, data=encoded)
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as e:
        print("API ERROR:", e)
        return None

def make_keyboard(data, code):
    old_city = data["city"].replace(":", "").replace("|", "")
    old_name = data["name"].replace(":", "").replace("|", "")
    old_postal = data["postal"].replace(":", "").replace("|", "")

    callback = (
        "generate:" + code + ":" +
        urllib.parse.quote(old_city, safe="") + ":" +
        urllib.parse.quote(old_name, safe="") + ":" +
        urllib.parse.quote(old_postal, safe="")
    )

    if len(callback.encode("utf-8")) > 64:
        callback = "generate:" + code + ":" + urllib.parse.quote(old_city, safe="")

    copied = copy_text(data)

    return {
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
    }

def send_message(chat_id, text, keyboard):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard, ensure_ascii=False)
    }
    return api("sendMessage", data)

def edit_message(chat_id, message_id, text, keyboard):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard, ensure_ascii=False)
    }
    return api("editMessageText", data)

def answer_callback(callback_id):
    return api("answerCallbackQuery", {"callback_query_id": callback_id})

def find_country(text):
    value = text.strip().lower()
    if value in COUNTRIES:
        return value
    if value in ALIASES:
        return ALIASES[value]
    return None

def handle_message(message):
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip()

    if text.lower().startswith("/start"):
        send_message(
            chat_id,
            "<b>🌍 COUNTRY DETAILS 🚀</b>\n\n"
            "Example:\n\n"
            "<code>/fake india</code>\n"
            "<code>/fake malaysia</code>\n"
            "<code>/fake qatar</code>\n"
            "<code>/fake oman</code>\n"
            "<code>/fake portugal</code>\n"
            "<code>/fake japan</code>\n\n"
            "📋 টেক্সটের ওপর ট্যাপ করলে বা 'Copy Address' চাপলে সরাসরি কপি হবে।\n"
            "🔄 Generate চাপলে সব তথ্য পরিবর্তিত হবে।",
            {"inline_keyboard": []}
        )
        return

    if text.lower().startswith("/fake"):
        parts = text.split(None, 1)
        if len(parts) < 2:
            send_message(
                chat_id,
                "❌ Country লিখুন।",
                {"inline_keyboard": []}
            )
            return

        code = find_country(parts[1])
        if not code:
            send_message(
                chat_id,
                "❌ Country পাওয়া যায়নি।\n\n"
                "Example:\n"
                "<code>/fake india</code>\n"
                "<code>/fake malaysia</code>\n"
                "<code>/fake qatar</code>\n"
                "<code>/fake japan</code>",
                {"inline_keyboard": []}
            )
            return

        data = generate_data(code)
        output = display_text(data)
        kb = make_keyboard(data, code)
        send_message(chat_id, output, kb)
        return

def handle_callback(callback):
    callback_id = callback.get("id")
    callback_data = callback.get("data", "")
    message = callback.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    message_id = message.get("message_id")

    answer_callback(callback_id)

    if callback_data.startswith("generate:"):
        parts = callback_data.split(":")
        code = parts[1]

        if code not in COUNTRIES:
            return

        old_data = {}
        if len(parts) >= 3:
            try:
                old_data["city"] = urllib.parse.unquote(parts[2])
            except:
                old_data["city"] = ""
        if len(parts) >= 4:
            try:
                old_data["name"] = urllib.parse.unquote(parts[3])
            except:
                old_data["name"] = ""
        if len(parts) >= 5:
            try:
                old_data["postal"] = urllib.parse.unquote(parts[4])
            except:
                old_data["postal"] = ""

        new_data = generate_data(code, old_data)
        new_text = display_text(new_data)
        new_keyboard = make_keyboard(new_data, code)

        edit_message(chat_id, message_id, new_text, new_keyboard)

        print(f"GENERATED: {new_data['country']} | {new_data['name']} | {new_data['city']} | {new_data['state']} | {new_data['postal']}")

def run_bot():
    print("================================")
    print("🌍 COUNTRY DETAILS BOT")
    print("================================")
    print("Countries loaded:", len(COUNTRIES))
    print("Bot is running...\n")

    offset = 0

    while True:
        try:
            result = api("getUpdates", {"timeout": 50, "offset": offset})
            if not result:
                time.sleep(2)
                continue

            if not result.get("ok"):
                print("Telegram Error:", result)
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
            print("BOT STOPPED")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            time.sleep(5)

if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❌ BOT TOKEN বসাও।")
    else:
        run_bot()
