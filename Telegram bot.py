# ==========================================
# GLOBAL COUNTRY ADDRESS BOT
# 121 COUNTRIES (FULL SINGLE-FILE BOT CODE)
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

NAME_BANK = {
    "bd": "মাহমুদুল হাসান,সাইফুল ইসলাম,রাকিব হাসান,নুসরাত জাহান,সুমাইয়া আক্তার,তানজিলা রহমান",
    "in": "Aarav Sharma,Arjun Patel,Rahul Mehta,Priya Singh,Ananya Gupta,Rohan Verma",
    "my": "Muhammad Faris,Ahmad Hakim,Nur Aisyah,Siti Aminah,Hafiz Rahman,Amir Hakim",
    "qa": "Mohammed Al-Kuwari,Ahmed Al-Thani,Fatima Al-Hajri,Mariam Al-Mansoori",
    "om": "Ahmed Al-Harthy,Mohammed Al-Balushi,Fatma Al-Rawahi,Aisha Al-Hinai",
    "ae": "Omar Al-Mansouri,Ahmed Al-Nuaimi,Fatima Al-Mazrouei,Maryam Al-Hashimi",
    "jp": "Haruto Sato,Yuki Tanaka,Ren Suzuki,Aoi Yamamoto,Daiki Ito",
    "cn": "Wei Zhang,Li Wang,Chen Liu,Mei Zhang,Jun Chen",
    "kr": "Kim Min-jun,Lee Ji-hoon,Park Seo-jun,Choi Min-seo,Han Ji-won",
    "de": "Lukas Müller,Thomas Schneider,Anna Weber,Sophie Fischer",
    "fr": "Jean Martin,Pierre Bernard,Claire Dubois,Marie Laurent",
    "it": "Marco Rossi,Luca Romano,Giulia Bianchi,Sofia Conti",
    "es": "Carlos García,Miguel Fernández,Lucía Martínez,Sofía López",
    "pt": "João Silva,Miguel Santos,Tiago Pereira,Ana Ferreira",
    "tr": "Mehmet Yılmaz,Ahmet Kaya,Elif Demir,Zeynep Aydın",
    "sa": "Ahmed Al-Qahtani,Mohammed Al-Harbi,Fatimah Al-Shehri,Noura Al-Otaibi",
    "id": "Muhammad Rizky,Andi Pratama,Siti Rahmawan,Dewi Lestari",
    "th": "Nattapong Srisuk,Somsak Prasert,Siriporn Chaiyaporn",
    "vn": "Nguyen Minh Anh,Tran Quang Huy,Le Thi Mai,Pham Duc Long",
    "pk": "Muhammad Hamza,Ali Raza,Ayesha Khan,Sana Ahmed",
    "np": "Aarav Thapa,Suman Gurung,Anisha Sharma,Prakash Karki",
    "lk": "Kasun Perera,Nimal Silva,Anjali Fernando,Dilshan Jayawardena",
    "ru": "Ivan Petrov,Alexei Smirnov,Anna Ivanova,Elena Volkov",
    "br": "João Silva,Carlos Santos,Lucas Oliveira,Ana Souza",
    "mx": "Carlos Hernández,Luis García,Diego Martínez,Sofía López",
    "ar": "Mateo González,Santiago Rodríguez,Lucía Fernández,Valentina López",
    "cl": "Matías González,Diego Morales,Camila Rojas,Valentina Soto",
    "co": "Juan Rodríguez,Carlos Martínez,Andrés Gómez,Laura Torres",
    "za": "Thabo Mokoena,Sipho Dlamini,Lerato Molefe,Nomsa Ndlovu",
    "ng": "Chinedu Okafor,Emeka Nwosu,Adaobi Eze,Chioma Okoye",
    "eg": "Ahmed Hassan,Mohamed Ali,Omar Mahmoud,Mariam Ahmed",
    "ma": "Youssef Amrani,Ahmed Benali,Fatima Idrissi,Maryam Alaoui",
    "ke": "Brian Otieno,Kevin Mwangi,Aisha Hassan,Wanjiku Kamau",
    "gh": "Kwame Mensah,Kofi Asante,Akosua Boateng,Yaa Owusu",
    "et": "Dawit Bekele,Tesfaye Alemu,Hana Mekonnen,Marta Tadesse",
    "se": "Erik Andersson,Lars Johansson,Anna Karlsson,Elsa Nilsson",
    "no": "Lars Hansen,Erik Olsen,Ingrid Larsen,Nora Berg",
    "fi": "Mikko Virtanen,Juha Korhonen,Aino Nieminen,Emilia Laine",
    "dk": "Mikkel Jensen,Lars Nielsen,Emma Hansen,Sofie Andersen",
    "nl": "Daan de Vries,Jan Jansen,Emma Bakker,Sophie Visser",
    "be": "Lucas Dubois,Thomas Lambert,Marie Martin,Julie Laurent",
    "pl": "Jakub Kowalski,Piotr Nowak,Anna Wiśniewska,Zofia Wójcik",
    "gr": "Georgios Papadopoulos,Nikos Nikolaou,Maria Georgiou,Eleni Dimitriou",
    "ro": "Andrei Popescu,Alexandru Ionescu,Elena Popa,Ioana Stan",
    "cz": "Jan Novak,Petr Svoboda,Anna Dvořáková,Lucie Černá",
    "hu": "Bálint Nagy,Gábor Kovács,Anna Szabó,Eszter Horváth",
    "at": "Lukas Gruber,Johann Huber,Anna Bauer,Sophie Wagner",
    "ch": "Lukas Müller,Martin Meier,Anna Keller,Laura Weber",
    "ie": "Sean Murphy,Liam Kelly,Emma Ryan,Saoirse Byrne",
    "au": "Jack Smith,William Jones,Charlotte Brown,Amelia Wilson",
    "ca": "Liam Martin,Noah Wilson,Emma Thompson,Olivia Brown",
    "us": "James Williams,Michael Johnson,William Davis,Daniel Brown,Emily Wilson",
    "gb": "Oliver Smith,George Williams,Harry Taylor,Emily Brown,Sophie Wilson",
    "nz": "Liam Taylor,Jack Wilson,Oliver Brown,Emily Clarke",
    "fj": "Jone Ratu,Viliame Bale,Ana Naqaqa,Salote Vakaloloma",
    "ph": "Juan Santos,Mark Reyes,Angelo Cruz,Maria Garcia",
    "kh": "Sokha Chan,Dara Kim,Sophea Lim,Vanna Chea",
    "la": "Khamla Phommasone,Somchai Vong,Malai Keovongsa",
    "mn": "Bat-Erdene Bold,Batsaikhan Ganbold,Anu Enkhbayar",
    "kz": "Ayan Nurgaliyev,Dias Sarsenov,Aigerim Bekova",
    "uz": "Bekzod Karimov,Aziz Rakhimov,Madina Usmanova",
    "af": "Ahmad Rahimi,Omid Ahmadi,Fatima Noori,Maryam Waziri",
    "ir": "Reza Hosseini,Ali Mohammadi,Sara Ahmadi,Maryam Karimi",
    "iq": "Ali Hassan,Omar Abbas,Zainab Ahmed,Mariam Kareem",
    "jo": "Omar Haddad,Ahmad Khalil,Lina Saleh,Noor Mansour",
    "lb": "Karim Haddad,Michel Khoury,Nour Daher,Maya Saad",
    "kw": "Fahad Al-Sabah,Ahmed Al-Rashid,Noura Al-Ali",
    "bh": "Hassan Al-Khalifa,Ali Al-Doseri,Fatima Al-Mahdi",
    "tn": "Mohamed Ben Ali,Ahmed Trabelsi,Amira Mansour",
    "dz": "Karim Benali,Ahmed Boudiaf,Lamia Haddad",
    "ly": "Ahmed Al-Misrati,Omar Al-Fituri,Mariam Al-Werfalli",
    "sd": "Ahmed Mohamed,Omer Hassan,Mariam Ali",
    "tz": "Juma Hassan,Abdallah Said,Asha Mohamed",
    "ug": "Daniel Okello,Samuel Kato,Grace Namusoke",
    "rw": "Jean Niyonzima,Eric Habimana,Claudine Mukamana",
    "zm": "Brian Banda,Joseph Phiri,Mary Mwansa",
    "zw": "Tendai Moyo,Tawanda Dube,Rudo Ncube"
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
    "eg": "আবদেল ফাত্তাহ এল-সিসি",
    "za": "সিরিল রামাফোসা",
    "br": "লুইজ ইনাসিও লুলা দা সিলভা",
    "mx": "ক্লাউদিয়া শেইনবাউম",
    "kr": "লি জে-মিয়ং"
}

FACTS = {
    "bd": ("প্রায় ১৭.৫ কোটি","প্রায় ১,৪৭,৫৭০ বর্গকিমি","ভাত, মাছ, ডাল, ভর্তা","গার্মেন্টস / কৃষি / ব্যবসা / সেবা"),
    "in": ("প্রায় ১৪৬ কোটি","প্রায় ৩২,৮৭,২৬৩ বর্গকিমি","ভাত, রুটি, ডাল, বিরিয়ানি","IT / ব্যবসা / কৃষি / শিল্প"),
    "my": ("প্রায় ৩.৫ কোটি","প্রায় ৩,৩০,৮০৩ বর্গকিমি","Nasi Lemak, Satay, Laksa","Manufacturing / Business / Services"),
    "qa": ("প্রায় ৩০ লাখ","প্রায় ১১,৫৮৬ বর্গকিমি","Machboos, Harees, Dates","তেল-গ্যাস / Business / Construction"),
    "om": ("প্রায় ৫৫ লাখ","প্রায় ৩,০৯,৫০০ বর্গকিমি","Shuwa, Majboos, Dates","তেল-গ্যাস / Business / Tourism"),
    "ae": ("প্রায় ১ কোটি","প্রায় ৮৩,৬০০ বর্গকিমি","Machboos, Hummus, Shawarma","Business / Oil-Gas / Tourism"),
    "jp": ("প্রায় ১২.৩ কোটি","প্রায় ৩,৭৭,৯৭৫ বর্গকিমি","Sushi, Ramen, Tempura","Technology / Automobile / Industry"),
    "cn": ("প্রায় ১৪১ কোটি","প্রায় ৯৫,৯৬,৯৬০ বর্গকিমি","Rice, Noodles, Dumplings","Manufacturing / Technology / Business"),
    "us": ("প্রায় ৩৪ কোটি","প্রায় ৯৮,৩৩,৫১৭ বর্গকিমি","Burger, Steak, Pizza","Technology / Business / Services"),
    "gb": ("প্রায় ৬.৯ কোটি","প্রায় ২,৪৩,৬১০ বর্গকিমি","Fish and Chips, Roast","Finance / Services / Technology"),
    "de": ("প্রায় ৮.৪ কোটি","প্রায় ৩,৫৭,৫৮৮ বর্গকিমি","Bratwurst, Pretzel, Bread","Automobile / Engineering / Industry"),
    "fr": ("প্রায় ৬.৮ কোটি","প্রায় ৫,৫১,৬৯৫ বর্গকিমি","Baguette, Cheese, Croissant","Tourism / Fashion / Industry"),
    "it": ("প্রায় ৫.৯ কোটি","প্রায় ৩,০১,৩৪০ বর্গকিমি","Pizza, Pasta, Risotto","Fashion / Tourism / Industry"),
    "pt": ("প্রায় ১.১ কোটি","প্রায় ৯২,২১২ বর্গকিমি","Bacalhau, Pastel de Nata","Tourism / Fishing / Services"),
    "es": ("প্রায় ৪.৯ কোটি","প্রায় ৫,০৫,৯৯০ বর্গকিমি","Paella, Tapas","Tourism / Services / Industry"),
    "tr": ("প্রায় ৮.৭ কোটি","প্রায় ৭,৮৩,৫৬২ বর্গকিমি","Kebab, Pide, Baklava","Industry / Tourism / Agriculture"),
    "sa": ("প্রায় ৩.৫ কোটি","প্রায় ২১,৪৯,৬৯০ বর্গকিমি","Kabsa, Mandi, Dates","Oil-Gas / Business / Construction"),
    "br": ("প্রায় ২১.৩ কোটি","প্রায় ৮৫,১৫,৭৬৭ বর্গকিমি","Feijoada, Rice, Beans","Agriculture / Industry / Mining"),
    "mx": ("প্রায় ১৩.২ কোটি","প্রায় ১৯,৬৪,৩৭৫ বর্গকিমি","Tacos, Tamales, Mole","Manufacturing / Tourism / Business"),
    "ca": ("প্রায় ৪.১ কোটি","প্রায় ৯৯,৮৪,৬৭০ বর্গকিমি","Poutine, Salmon","Services / Technology / Natural Resources"),
    "au": ("প্রায় ২.৭ কোটি","প্রায় ৭৬,৯২,০২৪ বর্গকিমি","Meat Pie, Seafood, Barbecue","Mining / Agriculture / Services"),
    "za": ("প্রায় ৬.৪ কোটি","প্রায় ১২,২১,০৩৭ বর্গকিমি","Braai, Pap, Bobotie","Mining / Industry / Tourism")
}

FAMOUS = {
    "Dubai": "আকাশচুম্বী ভবন, ব্যবসা, পর্যটন ও শপিংয়ের জন্য বিখ্যাত",
    "Abu Dhabi": "রাজধানী, তেল-গ্যাস ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "Kuala Lumpur": "Petronas Twin Towers, ব্যবসা ও আধুনিক স্থাপত্যের জন্য বিখ্যাত",
    "George Town": "ঐতিহ্যবাহী স্থাপনা, খাবার ও সংস্কৃতির জন্য বিখ্যাত",
    "Doha": "আধুনিক স্থাপত্য, ব্যবসা ও আন্তর্জাতিক ক্রীড়া আয়োজনের জন্য বিখ্যাত",
    "Muscat": "সমুদ্র, পাহাড় ও ঐতিহ্যবাহী আরব স্থাপত্যের জন্য বিখ্যাত",
    "Tokyo": "প্রযুক্তি, ব্যবসা ও আধুনিক নগরজীবনের জন্য বিখ্যাত",
    "Mumbai": "বলিউড, আর্থিক কেন্দ্র ও সমুদ্রতটের জন্য বিখ্যাত",
    "Delhi": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Dhaka": "রাজধানী, ব্যবসা-বাণিজ্য ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "London": "রাজধানী, ব্যবসা, ইতিহাস ও পর্যটনের জন্য বিখ্যাত",
    "New York": "আর্থিক কেন্দ্র, Times Square ও Statue of Liberty-এর জন্য বিখ্যাত",
    "Paris": "Eiffel Tower, Fashion, শিল্প ও সংস্কৃতির জন্য বিখ্যাত",
    "Berlin": "ইতিহাস, সংস্কৃতি ও আধুনিক শিল্পের জন্য বিখ্যাত",
    "Rome": "Colosseum, প্রাচীন ইতিহাস ও Vatican-এর জন্য বিখ্যাত",
    "Lisbon": "ঐতিহাসিক স্থাপনা, সমুদ্র ও Portuguese culture-এর জন্য বিখ্যাত",
    "Beijing": "রাজধানী, ইতিহাস ও ঐতিহাসিক স্থাপনার জন্য বিখ্যাত",
    "Seoul": "প্রযুক্তি, K-pop, ব্যবসা ও আধুনিক সংস্কৃতির জন্য বিখ্যাত",
    "Cairo": "পিরামিড, নীলনদ ও প্রাচীন ইতিহাসের জন্য বিখ্যাত"
    
}
def postal_code(code):
    if code == "bd":
        return random.choice(["1000","1100","1205","4000","6000","3100"])
    if code == "in":
        return random.choice(["110001","400001","700001","560001","600001","500001"])
    if code == "my":
        return random.choice(["50000","50100","50450","80000","75000"])
    if code in ["qa","om","ae"]:
        return "N/A"
    if code == "jp":
        return random.choice(["100-0001","530-0001","600-8001","160-0022"])
    if code == "us":
        return str(random.randint(10000, 99999))
    if code == "gb":
        return random.choice(["SW1A 1AA","EC1A 1BB","M1 1AE","B1 1AA"])
    if code == "ca":
        return random.choice(["M5V 2T6","V6B 1A1","H2X 1Y4"])
    if code == "au":
        return random.choice(["2000","3000","4000","6000"])
    if code in ["de"]:
        return random.choice(["10115","20095","80331","50667"])
    if code == "fr":
        return random.choice(["75001","69001","13001"])
    if code == "it":
        return random.choice(["00118","20121","80100"])
    if code == "pt":
        return random.choice(["1000-001","4000-001","3000-001"])
    if code == "es":
        return random.choice(["28001","08001","41001"])
    if code == "tr":
        return random.choice(["06000","34000","35000"])
    if code == "br":
        return random.choice(["01000-000","20000-000","30100-000"])
    return str(random.randint(10000, 999999))

def state_name(code, city):
    states = {
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
            "Sohar": "North Al Batinah"
        }
    }
    if code in states and city in states[code]:
        return states[code][city]
    return city + " Region"

def street_name(code):
    number = random.randint(10, 999)
    streets = {
        "my": ["Jalan Ampang", "Jalan Bukit Bintang", "Jalan Tun Razak"],
        "qa": ["Al Corniche Street", "Salwa Road", "Al Rayyan Road"],
        "om": ["Sultan Qaboos Street", "Al Khuwair Street", "Al Wadi Street"],
        "ae": ["Sheikh Zayed Road", "Al Wasl Road", "Jumeirah Street"],
        "jp": ["Chuo Street", "Meiji Avenue", "Sakura Street"],
        "in": ["MG Road", "Park Street", "Link Road"]
    }
    options = streets.get(code, ["Main Street", "Central Road", "Market Road", "Station Road", "Park Avenue", "King Street"])
    return f"{number} {random.choice(options)}, Block {random.choice(['A','B','C','D'])}"

def generate_data(code):
    country = COUNTRIES[code]
    city = random.choice(country["cities"])
    names = NAME_BANK.get(code, ",".join(DEFAULT_NAMES)).split(",")
    name = random.choice(names)
    facts = FACTS.get(code, ("দেশভেদে পরিবর্তনশীল", "দেশভেদে পরিবর্তনশীল", "স্থানীয় খাবার", "Business / Job / Services"))

    return {
        "country": country["name"],
        "flag": country["flag"],
        "leader": LEADERS.get(code, "রাষ্ট্রপ্রধান / সরকারপ্রধান"),
        "name": name,
        "street": street_name(code),
        "city": city,
        "famous": FAMOUS.get(city, "ব্যবসা, সংস্কৃতি, ইতিহাস ও স্থানীয় বৈশিষ্ট্যের জন্য পরিচিত"),
        "state": state_name(code, city),
        "postal": postal_code(code),
        "population": facts[0],
        "area": facts[1],
        "food": facts[2],
        "work": facts[3],
        "duty": random.choice(["সাধারণত ৮ ঘণ্টা", "সাধারণত ৮–৯ ঘণ্টা", "সাধারণত ৮–১০ ঘণ্টা"])
}
def display_text(data):
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

def copy_text(data):
    return (
        f"{data['country']} {data['flag']}\n"
        f"Name: {data['name']}\n"
        f"Street: {data['street']}\n"
        f"City: {data['city']}\n"
        f"State/Region: {data['state']}\n"
        f"Postal Code: {data['postal']}\n"
        f"Country: {data['country']}"
    )

def keyboard(data, code):
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
                    "callback_data": "generate:" + code
                }
            ]
        ]
    }

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

def send_message(chat_id, text, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if reply_markup:
        data["reply_markup"] = json.dumps(reply_markup, ensure_ascii=False)
    return api("sendMessage", data)

def edit_message(chat_id, message_id, text, reply_markup):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": json.dumps(reply_markup, ensure_ascii=False)
    }
    return api("editMessageText", data)

def callback_answer(callback_id):
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
            "Country লিখে Generate করো।\n\n"
            "<code>/fake malaysia</code>\n"
            "<code>/fake qatar</code>\n"
            "<code>/fake oman</code>\n"
            "<code>/fake portugal</code>\n"
            "<code>/fake japan</code>\n"
            "<code>/fake india</code>\n"
            "<code>/fake bangladesh</code>\n\n"
            "📋 Copy Address = সরাসরি copy\n"
            "🔄 Generate = সব field নতুন"
        )
        return

    if text.lower().startswith("/countries"):
        lines = []
        for code, info in COUNTRIES.items():
            lines.append(f"{info['flag']} {info['name']} — <code>{code}</code>")
        send_message(
            chat_id,
            "<b>🌍 COUNTRY LIST</b>\n\n" + "\n".join(lines)
        )
        return

    if text.lower().startswith("/fake"):
        parts = text.split(None, 1)
        if len(parts) < 2:
            send_message(
                chat_id,
                "❌ Country লিখুন।\n\n"
                "Example:\n"
                "<code>/fake malaysia</code>"
            )
            return

        code = find_country(parts[1])
        if not code:
            send_message(
                chat_id,
                "❌ Country পাওয়া যায়নি।\n\n"
                "Example:\n"
                "<code>/fake malaysia</code>\n"
                "<code>/fake qatar</code>\n"
                "<code>/fake oman</code>\n"
                "<code>/fake portugal</code>\n"
                "<code>/fake japan</code>"
            )
            return

        data = generate_data(code)
        text_output = display_text(data)
        buttons = keyboard(data, code)
        send_message(chat_id, text_output, buttons)
        return

def handle_callback(callback):
    callback_id = callback.get("id")
    data = callback.get("data", "")
    message = callback.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    message_id = message.get("message_id")

    callback_answer(callback_id)

    if data.startswith("generate:"):
        code = data.split(":", 1)[1]
        if code not in COUNTRIES:
            return

        new_data = generate_data(code)
        new_text = display_text(new_data)
        new_keyboard = keyboard(new_data, code)
        edit_message(chat_id, message_id, new_text, new_keyboard)

def run_bot():
    print("====================================")
    print(" 🌍 COUNTRY DETAILS BOT")
    print("====================================")
    print("Loaded countries:", len(COUNTRIES))
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
                        print("BUTTON ERROR:", e)

        except KeyboardInterrupt:
            print("Bot stopped.")
            break
        except Exception as e:
            print("MAIN ERROR:", e)
            time.sleep(5)

if __name__ == "__main__":
    if not BOT_TOKEN or BOT_TOKEN == "PASTE_YOUR_BOT_TOKEN_HERE":
        print("❌ BOT TOKEN বসানো হয়নি।")
    else:
        run_bot()
