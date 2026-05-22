from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="VibeCheck API")

# CRITICAL: Frontend ile Backend'in birbiriyle konuşabilmesi için CORS ayarı şart!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Her yerden erişime izin ver (Ödev teslimi için en güvenli yol)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Canlı Veri Havuzumuz (Database)
SUGGESTIONS = {
    "uykusuz": ["Pencereyi aç ve 5 dk derin nefes al. 🌬️", "Buz gibi bir suyla yüzünü yıka. 🧊", "Papatya çayı iç. 🌿", "Hafif tempo bir müzik aç. 🎶", "Güneş ışığına çık. ☀️", "Kısa bir yürüyüş yap. 🚶", "Yüzünü yıka ve gerin. 🤸", "Camı sonuna kadar aç"],
            "yorgun": ["Lavanta kokla. 🌿", "Ayaklarını yükseğe kaldır. 👣", "Ilık bir duş al. 🚿", "Gözlerini 10 dk kapat. 👁️", "Melisa çayı iç. 🍵", "Hafif bir esneme yap. 🧘", "Sevdiğin bir şarkıyı dinle. 🎵", "Karanlık bir odada dinlen. 🌑"],
            "enerjik": ["En sevdiğin dans şarkısını aç. 💃", "Hızlıca 20 squat yap. 🏋️", "Dışarı çık ve koş. 🏃", "Yeni bir proje planla. 📝", "Arkadaşlarını ara. 📞", "Yüksek sesle şarkı söyle. 🎤", "Bisiklete bin. 🚲", "Odanı topla, enerjini at. 🧹"],
            "heyecanli": ["Duygularını yaz. ✍️", "Sakinleşmek için nefes egzersizi yap. 🧘", "Geleceği hayal et. 🌠", "Bir bardak su iç. 💧", "Müzik dinle. 🎧", "Kendine bir kahve ısmarla. ☕", "Yürüyüşe çık. 🚶‍♀️", "Yeni bir şey öğren. 🧐"],
            "stresli": ["Mandala boya. 🖍️", "Telefonu kapat. 📵", "Doğaya çık. 🌳", "Papatya çayı iç. 🌼", "Stres topuyla oyna. 🎾", "Banyo yap. 🛀", "Komik video izle. 😹", "Sadece otur ve hiçbir şey yapma. 🧘‍♂️"],
            "mutlu": ["Gülümse! 😊", "Sevdiğin birine mesaj at. 💌", "Dondurma ye. 🍦", "Şarkı söyle. 🎶", "Dans et. 🕺", "Fotoğraf çek. 📸", "Hayvanları besle. 🐦🐕", "Bugüne teşekkür et. ✨"],
            "huzurlu": ["Kitap oku. 📖", "Gökyüzünü izle. ☁️", "Mum yak. 🕯️", "Yavaş yürü. 🚶", "Bitki çayı iç. 🍵", "Günlük tut. 📓", "Meditasyon yap. 🧘", "Uzaklara bak. 🔭"],
            "kaygili": ["5-4-3-2-1 kuralını uygula. 🖐️", "Su iç. 💧", "Ağır battaniye kullan. 🛌", "Kaygılarını kağıda yaz. 📝", "Seni mutlu edecek şeyler izle/oku.", "Limon kokla. 🍋", "Yavaş nefes al. 🌬️", "Sıcak bir içecek iç. ☕"],
            "mutsuz": ["Kendine sarıl. 🫂", "Seni neşelendirecek bir şeyler izle. 🎬", "Tatlı ye. 🍰", "Sıcak duş al. 🚿", "Bir arkadaşını ara. 📞", "Müzik dinle. 🎵", "Günlüğüne dök içini. ✍️", "Biraz uyu. 🛌"],
            "sinirli": ["Yastığı yumrukla. 🥊", "Bağır (mümkünse). 🗣️", "Soğuk su iç. 🧊", "100'den geriye say. 🔢", "Kağıt yırt. 📄", "Hızlı yürü. 🏃‍♂️", "Derin nefes al. 😤", "Yalnız kal. 🧘"],
            "yalniz": ["Podcast dinle. 🎙️", "Bir topluluğa katıl. 🏘️", "Eski bir dostu ara. 📞", "Kafeye git. ☕", "Evcil hayvanınla oyna. 🐾", "Mektup yaz. ✉️", "Sinemaya git. 🍿", "Kurslara bak. 🎓"],
            "merakli": ["Wikipedia'da gez. 🌐", "Belgesel izle. 🎞️", "Bulmaca çöz. 🧩", "Yeni bir dil öğren. 🗣️", "Deney yap. 🧪", "Müzeye git. 🏛️", "Soru sor. ❓", "Gözlem yap. 🔍"],
            "tembel": ["Yatakta gerin. 🛌", "Maske yap. ✨", "Sadece yat. 🦥", "Çizgi film izle. 📺", "Radyo dinle. 📻", "Abur cubur ye. 🍿", "Hayal kur. 💭", "Sosyal medyada gez. 📱"],
            "romantik": ["Şiir oku. 📜", "Şarkı gönder. 🎶", "Yemek yap. 🍳", "Yıldızlara bak. 🌠", "Çiçek al. 🌸", "Aşk filmi izle. 🎥", "El ele yürü. 👩‍❤️‍👨", "Mektup yaz. 💌"],
            "ozguvenli": ["Aynada kendine bak. 👑", "Başarılarını yaz. 🏆", "Dik yürü. 🚶", "Yeni bir şey dene. 🔥", "Yardım et. 🤝", "Şık giyin. 👗", "Hedef koy. 🎯", "Kendini alkışla. 👏"]

@app.get("/api/vibe")
def get_vibe_plan(mood: str, time: int):
    # Eğer gelen mod listemizde varsa oradan rastgele seç, yoksa genel bir şey ver
    mood_list = SUGGESTIONS.get(mood, ["Kendine güzel bir an yarat! ✨"])
    random_suggestion = random.choice(mood_list)
    
    return {
        "mood": mood,
        "time": time,
        "suggestion": random_suggestion,
        "source": "Live FastAPI Backend Engine" # Canlı veri olduğunu kanıtlayan log
    }
