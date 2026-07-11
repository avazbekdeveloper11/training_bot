# Barcha mashqlar ma'lumotlari

EXERCISES = {
    # ASOSIY MASHQLAR
    "pushup": {
        "name": "💪 Push-up (Otjimaniya)",
        "sets": 3,
        "reps": "10-15",
        "duration": None,
        "instructions": [
            "Tana to'g'ri holatda bo'lsin",
            "Tirsaklarni bukib pastga tushing",
            "Ko'krak yerga yaqinlashgach, yana yuqoriga ko'tariling"
        ],
        "image": "https://i.imgur.com/8rLxTlC.gif",
        "category": "asosiy"
    },
    "pike_pushup": {
        "name": "🔺 Pike Push-up",
        "sets": 3,
        "reps": "8-12",
        "duration": None,
        "instructions": [
            "Oyoq va qo'llarni yerga qo'yib, belni yuqoriga ko'taring (teskari V shakl)",
            "Boshingizni yerga tushiring, tirsaklar bukiladi",
            "Qo'llar bilan itarib yana tepaga chiqing"
        ],
        "image": "https://i.imgur.com/JHfHxGN.gif",
        "category": "asosiy"
    },
    "plank": {
        "name": "🧘 Plank",
        "sets": 3,
        "reps": None,
        "duration": 45,
        "instructions": [
            "Bilaklarga tayaning (tirsak 90 daraja)",
            "Tana tekis chiziqda bo'lsin - bosh, yelka, bel, tovon bir chiziqda",
            "Belni tushirmang, ko'tarmang - qorinni ichiga torting"
        ],
        "image": "https://i.imgur.com/3bVJcMO.gif",
        "category": "asosiy"
    },
    "side_plank": {
        "name": "📐 Side Plank",
        "sets": 3,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Yon bilan yoting, tirsak yelka ostida",
            "Tirsak va oyoq yon tomoni bilan tayangan holda belni ko'taring",
            "Tanani tekis ushlang, boshdan oyoqgacha bir chiziq"
        ],
        "image": "https://i.imgur.com/WLJfVnL.gif",
        "category": "asosiy"
    },
    "mountain_climber": {
        "name": "🏔 Mountain Climber",
        "sets": 3,
        "reps": "20",
        "duration": None,
        "instructions": [
            "Plank holatida turing - qo'llar tekis, yelka ostida",
            "Tizzalarni navbatma-navbat ko'krakka torting",
            "Tez va ritmik bajaring, yugurgandek"
        ],
        "image": "https://i.imgur.com/lrCCBMt.gif",
        "category": "asosiy"
    },
    "leg_raise": {
        "name": "🦵 Leg Raise",
        "sets": 3,
        "reps": "12-15",
        "duration": None,
        "instructions": [
            "Orqa bilan yoting, qo'llar yon tomonda yoki dumba ostida",
            "Oyoqlarni tekis holda 90 gradusgacha ko'taring",
            "Sekin tushiring, yerga tegmasdan yana ko'taring"
        ],
        "image": "https://i.imgur.com/XNvZqJP.gif",
        "category": "asosiy"
    },
    "superman": {
        "name": "🦸 Superman",
        "sets": 3,
        "reps": "12-15",
        "duration": None,
        "instructions": [
            "Qorin bilan yoting, qo'l va oyoqlar cho'zilgan",
            "Qo'l va oyoqlarni bir vaqtda yerdan ko'taring",
            "2 soniya ushlab, sekin tushiring"
        ],
        "image": "https://i.imgur.com/d1HPfqD.gif",
        "category": "asosiy"
    },
    "burpee": {
        "name": "🔥 Burpee",
        "sets": 3,
        "reps": "8-10",
        "duration": None,
        "instructions": [
            "1. Tik turing",
            "2. Cho'kkalang, qo'llarni yerga qo'ying",
            "3. Oyoqlarni orqaga sakrating (plank holati)",
            "4. Push-up qiling",
            "5. Oyoqlarni oldinga sakrating",
            "6. Tepaga sakrab qayting, qo'llarni tepaga ko'taring"
        ],
        "image": "https://i.imgur.com/SfQPatF.gif",
        "category": "asosiy"
    },

    # BILAK MASHQLARI
    "dead_hang": {
        "name": "🏋️ Dead Hang (Turnikda osilish)",
        "sets": 3,
        "reps": None,
        "duration": 45,
        "instructions": [
            "Turnikni kaft bilan mahkam ushlang",
            "Tanani to'liq osiltirib turing, oyoqlar yerga tegmasin",
            "Yelkalarni biroz pastga torting, bo'shashtirib qo'ymang"
        ],
        "image": "https://i.imgur.com/ZtXgBWX.gif",
        "category": "bilak"
    },
    "wrist_curl": {
        "name": "💪 Wrist Curl (Bilakni bukish)",
        "sets": 3,
        "reps": "15-20",
        "duration": None,
        "instructions": [
            "O'tiring, bilagingizni tizzaga qo'ying, kaft tepaga qaraydi",
            "Qo'lda og'irlik (gantel/suv shishasi) ushlang",
            "Faqat bilakni yuqoriga buking, tirsak qimirlamasin",
            "Sekin tushiring"
        ],
        "image": "https://i.imgur.com/dCKWpRZ.gif",
        "category": "bilak"
    },
    "reverse_wrist_curl": {
        "name": "🔄 Reverse Wrist Curl",
        "sets": 3,
        "reps": "15-20",
        "duration": None,
        "instructions": [
            "Xuddi wrist curl kabi, lekin kaft pastga qaraydi",
            "Faqat bilakni tepaga ko'taring",
            "Sekin tushiring, harakatni nazorat qiling"
        ],
        "image": "https://i.imgur.com/YkXnVpM.gif",
        "category": "bilak"
    },
    "farmer_carry": {
        "name": "🧑‍🌾 Farmer's Carry",
        "sets": 3,
        "reps": None,
        "duration": 45,
        "instructions": [
            "Ikki qo'lda og'ir yukni (gantel, suv shishasi) ushlang",
            "Yelkalarni orqaga torting, ko'krak oldinga",
            "Qo'llarni bukmasdan to'g'ri yurib boring"
        ],
        "image": "https://i.imgur.com/hSm3qJr.gif",
        "category": "bilak"
    },

    # ISINISH
    "neck_rotation": {
        "name": "🔄 Bo'yin aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Tik turing, yelkalar bo'sh",
            "Bo'yinni sekin soat yo'nalishi bo'yicha aylantiring",
            "Keyin teskari yo'nalishda aylantiring"
        ],
        "image": "https://i.imgur.com/qJvLrGE.gif",
        "category": "isinish"
    },
    "shoulder_rotation": {
        "name": "🔄 Yelka aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Tik turing, qo'llar yon tomonda",
            "Yelkalarni oldinga doira bo'ylab aylantiring",
            "Keyin orqaga aylantiring"
        ],
        "image": "https://i.imgur.com/P3DLULN.gif",
        "category": "isinish"
    },
    "arm_circles": {
        "name": "⭕ Qo'llarni aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Qo'llarni yon tomonga tekis cho'zing",
            "Kichik doiralar bilan oldinga aylantiring",
            "Keyin orqaga aylantiring, doiralarni kattalashtiring"
        ],
        "image": "https://i.imgur.com/kCvHPLZ.gif",
        "category": "isinish"
    },
    "jogging": {
        "name": "🏃 Joyda yugurish",
        "sets": 1,
        "reps": None,
        "duration": 60,
        "instructions": [
            "Joyda yuguring",
            "Tizzalarni balandroq ko'taring",
            "Qo'llarni harakatlantiring"
        ],
        "image": "https://i.imgur.com/XvMZLXA.gif",
        "category": "isinish"
    },

    # CHO'ZILISH
    "shoulder_stretch": {
        "name": "🧘 Yelkani cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Bir qo'lni ko'krak oldidan o'tkazing",
            "Ikkinchi qo'l bilan tirsak ustidan bosib ushlab turing",
            "Har tomon 15 soniya, yelkada cho'zilish sezasiz"
        ],
        "image": "https://i.imgur.com/7wLqKVu.gif",
        "category": "chozilish"
    },
    "triceps_stretch": {
        "name": "💪 Triceps cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "Bir qo'lni tepaga ko'taring va tirsak orqali buking",
            "Kaftni yelka ortiga tushiring",
            "Ikkinchi qo'l bilan tirsakni sekin bosing"
        ],
        "image": "https://i.imgur.com/bJPqMcF.gif",
        "category": "chozilish"
    },
    "back_stretch": {
        "name": "🔙 Belni burib cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": [
            "O'tiring, oyoqlar oldinga cho'zilgan",
            "Bir oyoqni buking va ikkinchi oyoq ustidan o'tkazing",
            "Tanani bukilgan oyoq tomonga buring, orqa bilan cho'zilish sezasiz"
        ],
        "image": "https://i.imgur.com/Gk8gXuC.gif",
        "category": "chozilish"
    },
}

# Mashq tartibi
WORKOUT_ORDER = [
    # Isinish (3-4 daqiqa)
    "neck_rotation",
    "shoulder_rotation",
    "arm_circles",
    "jogging",

    # Asosiy mashqlar (15-20 daqiqa)
    "pushup",
    "pike_pushup",
    "plank",
    "side_plank",
    "mountain_climber",
    "leg_raise",
    "superman",
    "burpee",

    # Bilak mashqlari (8-10 daqiqa)
    "dead_hang",
    "wrist_curl",
    "reverse_wrist_curl",
    "farmer_carry",

    # Cho'zilish (2-3 daqiqa)
    "shoulder_stretch",
    "triceps_stretch",
    "back_stretch",
]

# Motivatsion xabarlar
MOTIVATION_MESSAGES = [
    "💪 TEZROQ! Vaqt kutmaydi!",
    "🔥 Dangasalik qilma! MASHQ QIL!",
    "⚡ Natija kerakmi? HARAKAT QIL!",
    "🏆 G'olib bo'lish oson emas! DAVOM ET!",
    "😤 Hozir azob - keyIn shon-sharaf!",
    "🎯 Maqsadingni unutdingmi? MASHQ!",
    "💥 Tanangga rahm qilma!",
    "🚀 Har kuni 1% yaxshilan!",
    "⏰ Vaqtni behuda o'tkazma!",
    "🔱 Kuchli bo'lish - TANLASH!",
    "😈 Dangasa tanani majburla!",
    "🌟 Sen buni qila olasan!",
    "💣 BOSHLA! Endi kechikmadik!",
    "🦾 Og'riq - kuch alomati!",
    "⚔️ O'zingga qarshi kurash!",
]

# Eslatma intervallar (sekundlarda)
REMINDER_INTERVALS = [30, 60, 90, 120, 180]  # 30s, 1m, 1.5m, 2m, 3m
