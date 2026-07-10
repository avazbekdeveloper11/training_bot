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
        "gif": "https://media.giphy.com/media/Kajbi6oGHMvqo8MnSv/giphy.gif",
        "category": "asosiy"
    },
    "pike_pushup": {
        "name": "🔺 Pike Push-up",
        "sets": 3,
        "reps": "8-12",
        "duration": None,
        "instructions": [
            "Belni yuqoriga ko'taring",
            "Boshingizni yerga tushiring",
            "Qo'llar bilan itarib yana tepaga chiqing"
        ],
        "gif": "https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif",
        "category": "asosiy"
    },
    "plank": {
        "name": "🧘 Plank",
        "sets": 3,
        "reps": None,
        "duration": 45,  # sekund
        "instructions": [
            "Bilaklarga tayaning",
            "Tana tekis chiziqda bo'lsin",
            "Belni tushirmang, ko'tarmang"
        ],
        "gif": "https://media.giphy.com/media/xT8qBff8cRRFf7k2u4/giphy.gif",
        "category": "asosiy"
    },
    "side_plank": {
        "name": "📐 Side Plank",
        "sets": 3,
        "reps": None,
        "duration": 30,  # har tomon
        "instructions": [
            "Yon bilan yoting",
            "Tirsak va oyoq bilan tayangan holda belni ko'taring",
            "Tanani tekis ushlang"
        ],
        "gif": "https://media.giphy.com/media/3oriNYQX2lC6dfW2Ji/giphy.gif",
        "category": "asosiy"
    },
    "mountain_climber": {
        "name": "🏔 Mountain Climber",
        "sets": 3,
        "reps": "20",
        "duration": None,
        "instructions": [
            "Plank holatida turing",
            "Tizzalarni navbatma-navbat ko'krakka torting",
            "Tez va ritmik bajaring"
        ],
        "gif": "https://media.giphy.com/media/l3q2VZLzFKvFzAtUc/giphy.gif",
        "category": "asosiy"
    },
    "leg_raise": {
        "name": "🦵 Leg Raise",
        "sets": 3,
        "reps": "12-15",
        "duration": None,
        "instructions": [
            "Orqa bilan yoting",
            "Oyoqlarni tekis holda ko'taring",
            "Sekin tushiring, yerga tegmasdan yana ko'taring"
        ],
        "gif": "https://media.giphy.com/media/fxZPrsux3vlFY00F4A/giphy.gif",
        "category": "asosiy"
    },
    "superman": {
        "name": "🦸 Superman",
        "sets": 3,
        "reps": "12-15",
        "duration": None,
        "instructions": [
            "Qorin bilan yoting",
            "Qo'l va oyoqlarni bir vaqtda ko'taring",
            "2 soniya ushlab, sekin tushiring"
        ],
        "gif": "https://media.giphy.com/media/YqbByPtLwVrBcpKJOK/giphy.gif",
        "category": "asosiy"
    },
    "burpee": {
        "name": "🔥 Burpee",
        "sets": 3,
        "reps": "8-10",
        "duration": None,
        "instructions": [
            "Tik turing",
            "Cho'kkalang, qo'llarni yerga qo'ying",
            "Oyoqlarni orqaga sakrating",
            "Push-up qiling",
            "Oyoqlarni oldinga olib keling",
            "Tepaga sakrab qayting"
        ],
        "gif": "https://media.giphy.com/media/23hPPMRgPxbNBlPQe3/giphy.gif",
        "category": "asosiy"
    },

    # BILAK MASHQLARI
    "dead_hang": {
        "name": "🏋️ Dead Hang (Turnikda osilish)",
        "sets": 3,
        "reps": None,
        "duration": 45,
        "instructions": [
            "Turnikni mahkam ushlang",
            "Faqat osilib turing",
            "Yelkalaringizni bo'shashtiring"
        ],
        "gif": "https://media.giphy.com/media/l0Ex6kDPwiuswTXs4/giphy.gif",
        "category": "bilak"
    },
    "wrist_curl": {
        "name": "💪 Wrist Curl (Bilakni bukish)",
        "sets": 3,
        "reps": "15-20",
        "duration": None,
        "instructions": [
            "Bilagingizni tizzaga qo'ying",
            "Kaft tepaga qarasin",
            "Faqat bilakni yuqoriga buking",
            "Sekin tushiring"
        ],
        "gif": "https://media.giphy.com/media/l4FGlcBatEK8aaL4Y/giphy.gif",
        "category": "bilak"
    },
    "reverse_wrist_curl": {
        "name": "🔄 Reverse Wrist Curl",
        "sets": 3,
        "reps": "15-20",
        "duration": None,
        "instructions": [
            "Kaft pastga qarasin",
            "Faqat bilakni tepaga ko'taring",
            "Sekin tushiring"
        ],
        "gif": "https://media.giphy.com/media/3oKIP9cJEOO9ljKoCc/giphy.gif",
        "category": "bilak"
    },
    "farmer_carry": {
        "name": "🧑‍🌾 Farmer's Carry",
        "sets": 3,
        "reps": None,
        "duration": 45,
        "instructions": [
            "Ikki qo'lda og'ir yukni ushlang",
            "Qo'llarni bukmasdan to'g'ri yurib boring",
            "Bilak va ushlash kuchini oshiradi"
        ],
        "gif": "https://media.giphy.com/media/wOXQJTA67Yxtm/giphy.gif",
        "category": "bilak"
    },

    # ISINISH
    "neck_rotation": {
        "name": "🔄 Bo'yin aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Bo'yinni sekin aylantiring"],
        "gif": None,
        "category": "isinish"
    },
    "shoulder_rotation": {
        "name": "🔄 Yelka aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Yelkalarni oldinga va orqaga aylantiring"],
        "gif": None,
        "category": "isinish"
    },
    "arm_circles": {
        "name": "⭕ Qo'llarni aylantirish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Qo'llarni oldinga va orqaga aylantiring"],
        "gif": None,
        "category": "isinish"
    },
    "jogging": {
        "name": "🏃 Joyda yugurish",
        "sets": 1,
        "reps": None,
        "duration": 60,
        "instructions": ["Joyda yuguring, tizzalarni ko'taring"],
        "gif": "https://media.giphy.com/media/l3fZPYrlEGoSXneWQ/giphy.gif",
        "category": "isinish"
    },

    # CHO'ZILISH
    "shoulder_stretch": {
        "name": "🧘 Yelkani cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Yelkangizni cho'zing, har tomon 30 soniya"],
        "gif": None,
        "category": "chozilish"
    },
    "triceps_stretch": {
        "name": "💪 Triceps cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Tricepsni cho'zing"],
        "gif": None,
        "category": "chozilish"
    },
    "back_stretch": {
        "name": "🔙 Belni burib cho'zish",
        "sets": 1,
        "reps": None,
        "duration": 30,
        "instructions": ["Belni burib cho'zing"],
        "gif": None,
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
