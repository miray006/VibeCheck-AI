from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import uvicorn

app = FastAPI(title="VibeCheck API", version="1.0.0")

# 🔒 CORS AYARI: Frontend ile Backend'in güvenle konuşabilmesi için şart!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Geliştirme aşamasında her yerden erişime izin veriyoruz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 CANLI VERİ HAVUZUMUZ (Mühendislik Veritabanı Yapısı)
SUGGESTIONS_DB = {
    "uykusuz": [
        "☕️ Yumuşak içimli bir latte al ve sadece 15 dakika güneş ışığına bak.",
        "🎧 Chill bir lo-fi listesi aç ve gözlerini kapatıp hayal kur.",
        "🚶‍♂️ Hafif tempolu, 10 dakikalık bir oksijen yürüyüşü yap.",
        "🧊 Yüzünü buz gibi suyla yıka ve taze bir elma ye!",
        "📚 Hafif bir dergi karıştır, derin odaklanma gerektirmeyen bir hobiye bak.",
        "🛋 Evde en rahat köşene geç ve sadece 20 dakika şekerleme yap.",
        "🍵 Melisa çayı içerek vücudundaki uykusuzluk gerginliğini at.",
        "🧘‍♀️ Hafif esneme hareketleri yaparak kan akışını hızlandır."
    ],
    "yorgun": [
        "🛁 Eve gidince ılık bir duş al ve sevdiğin kokulu mumları yak.",
        "🍦 Kendine sevdiğin bir tatlı ısmarla, bugün bunu hak ettin!",
        "📱 Tüm bildirimleri kapat ve 1 saat boyunca teknoloji detoksu yap.",
        "🦶 Ayaklarına masaj yap ya da sadece havaya kaldırıp dinlendir.",
        "🎬 Daha önce izlediğin ve seni yormayacak bir film aç.",
        "🍵 Ballı ıhlamur eşliğinde battaniye altına gir.",
        "✍️ Yorgunluğunun sebebini sadece bir kağıda karala ve sonra o kağıdı yırt.",
        "🌌 Camı aç ve temiz havayı 5 kez derin derin içine çek."
    ],
    "enerjik": [
        "🏃‍♂️ Hemen dışarı çık ve en az 30 dakika tempolu yürü veya koş!",
        "💃 En sevdiğin hızlı şarkıyı aç ve evde çılgınca dans et.",
        "📸 Dışarı çıkıp şehrindeki 5 farklı rengin fotoğrafını çek.",
        "🎾 Bir arkadaşını ara ve hemen bir aktivite planla!",
        "🧹 Uzun zamandır ertelediğin o odayı topla, enerjini oraya ver.",
        "🥤 Kendi smoothie tarifini yarat ve içine bolca meyve koy.",
        "🎨 Büyük bir kağıda aklına gelen tüm fikirleri renkli kalemlerle çiz.",
        "🛹 Eğer varsa kaykayına bin veya bisikletle yeni bir rota keşfet."
    ],
    "heyecanli": [
        "📝 Bu heyecanının sebebini ve hislerini günlüğüne detaylıca yaz.",
        "🚶‍♀️ Heyecanını yatıştırmak için uzun ve sakin bir yürüyüşe çık.",
        "🗣 En sevdiğin kişiyi ara ve heyecanını onunla paylaş!",
        "🤸‍♀️ Enerjini atmak için birkaç zıplama antrenmanı yap.",
        "🧩 Bir yapboza başla, odaklanman heyecanını dengeler.",
        "🎁 Kendine küçük bir hediye al, bu anı kutla!",
        "🎤 Sevdiğin bir şarkıyı avazın çıktığı kadar söyle.",
        "📍 Heyecan duyduğun konuyla ilgili gelecek planlarını listele."
    ],
    "stresli": [
        "🧘‍♂️ 5-5-5 kuralını uygula: 5 saniye nefes al, 5 tut, 5 ver.",
        "💆‍♀️ Şakaklarına nane yağı ile masaj yap.",
        "🥣 Sıcak bir çorba iç, mideyi rahatlatmak stresi azaltır.",
        "🖍 Mandala boya veya sadece boş kağıdı karala.",
        "👟 Dışarı çık ve sadece adımlarının sesini dinleyerek yürü.",
        "📦 Kullanmadığın 5 eşyayı ayır, sadeleşmek zihnini rahatlatır.",
        "💧 Büyük bir bardak su iç ve omuzlarını gevşet.",
        "🌳 Doğada yeşil bir alana bakmak kortizol seviyeni düşürür."
    ],
    "mutlu": [
        "🌟 Bu güzel anı dondurmak için bir selfie çek!",
        "🍭 En sevdiğin çocukluk atıştırmalığını al ve tadını çıkar.",
        "🙌 Birine rastgele bir iyilik yap, mutluluğun katlansın.",
        "🌸 Kendine sevdiğin bir ene çiçek al.",
        "🧁 Mutfakta yeni bir tarif dene, sonuç harika olacak!",
        "🎶 'Happy' şarkılar listesi yap ve tüm gün çal.",
        "📝 Bugün seni mutlu eden 3 şeyi not et.",
        "🚲 Sahilde veya bir parkta bisiklet sür, rüzgarı hisset."
    ],
    "huzurlu": [
        "📖 Bitirmek istediğin kitabın en sevdiğin bölümünü oku.",
        "☁️ Gökyüzünü izle ve bulutların şekillerini bir şeye benzet.",
        "🧶 Örgü ör, resim yap veya el işiyle uğraş.",
        "🍵 Bitki çayını yudumlayarak sadece sessizliği dinle.",
        "🧘‍♂️ Evde loş bir ışıkta meditasyon yap.",
        "🪴 Bitkilerinle ilgilen, toprakla temas et.",
        "📻 Sakin bir radyo kanalı bul ve arkada çalmasına izin ver.",
        "🛌 Temiz nevresimlerin kokusunu içine çekerek uzan."
    ],
    "kaygili": [
        "✋ 5-4-3-2-1 tekniği: Gördüğün 5, dokunduğun 4, duyduğun 3 şeyi say.",
        "🧶 Elinde bir hamurla veya stres topuyla oyna.",
        "🧊 Elinde bir buz küpü tut, bu seni ana odaklayacaktır.",
        "🛁 Lavantalı bir banyo yap veya lavanta kokla.",
        "📝 Kaygılarını yaz ve yanına 'Bu sadece bir dünüce' notu düş.",
        "🐕 Bir evcil hayvanla vakit geçir veya hayvan videoları izle.",
        "☕️ Kafeini bırak, bitki çayına geç.",
        "🧩 Basit bir mobil oyun oyna, zihnini başka yöne çek."
    ],
    "mutsuz": [
        "🫂 Kendine sarıl ve bunun geçici bir bulut olduğunu hatırla.",
        "🍰 En sevdiğin tatlıyı sipariş et, bugün şımartılma günü.",
        "🎞 Nostaljik bir çizgi film izle.",
        "✍️ Hislerini kağıda dök ve sonra o kağıdı uçak yapıp fırlat.",
        "🚿 Sıcak bir duş al ve suyun tüm ağırlığı götürdüğünü hayal et.",
        "🧸 Yumuşak bir şeye sarıl ve biraz dinlen.",
        "🚶‍♀️ Yağmur yağmıyorsa bile dışarı çık ve gökyüzüne bak.",
        "🍫 Bitter çikolatanın mutluluk veren gücünü kullan."
    ],
    "sinirli": [
        "🥊 Bir yastığı yumrukla veya bir kağıdı paramparça et.",
        "🏃‍♂️ Tüm gücünle kısa süreli bir koşu yap.",
        "🧊 Ağzına bir buz al ve erimesini bekle, dikkatin dağılsın.",
        "😤 Derin derin nefes alıp 'Tamam, sakinleşiyorum' de.",
        "🧼 Evi dip bucak temizle, o siniri hareketle dışarı at.",
        "🎧 Çok sert bir müzik aç ve enerjini orada tüket.",
        "🚿 Soğuğa yakın bir duş al, hararetini dindir.",
        "🤐 Bir süre kimseyle konuşma, yalnız kalıp sakinleş."
    ],
    "yalniz": [
        "🎙️ En sevdiğin podcasti dinle.",
        "📞 Eski bir dostunu ara.",
        "☕ Kalabalık bir kafede kitap oku.",
        "💬 Online bir topluluğa mesaj at.",
        "🎟️ Kendine randevu ver ve dışarı çık.",
        "🧩 Puzzle yapmaya başla.",
        "🐈 Evcil hayvanınla oyna.",
        "✉️ Gelecekteki kendine mektup yaz."
    ],
    "merakli": [
        "🌐 Wikipedia'da rastgele bir madde oku.",
        "🐬 Yeni bir tür keşfeden belgesel izle.",
        "🗣️ Yeni bir dilden 5 kelime öğren.",
        "🌌 Gökyüzü haritasına bak.",
        "🧪 Bir deney videosu izle.",
        "📚 Eski bir sahafı gez.",
        "🤖 Yapay zeka ile sohbet et.",
        "⚙️ Bir icadın tarihini araştır."
    ],
    "tembel": [
        "🦥 Yatakta gerin.",
        "🥪 En basit yemeği hazırla.",
        "🎧 Sesli kitap dinle.",
        "✨ Yüzüne maske yap.",
        "📱 Eski mesajları temizle.",
        "🖼️ Pencereden dışarı bak.",
        "🎹 Piyano müziği aç.",
        "🧘 Hiçbir şey yapmamanın tadını çıkar."
    ],
    "romantik": [
        "✍️ Aşk şiiri yaz.",
        "🕯️ Mum ışığında yemek ye.",
        "✉️ Eski mektupları oku.",
        "🎞️ Nostaljik aşk filmi izle.",
        "🌠 Yıldızları izle.",
        "🎵 Hoşlandığın kişiye şarkı at.",
        "🌸 Güzel koku sürün.",
        "💑 Uzun bir yürüyüş hayal et."
    ],
    "ozguvenli": [
        "👑 Şık giyin ve aynada poz ver.",
        "🏆 Başarılarını listele.",
        "🦾 Zor bir işi bitir.",
        "📸 Yeni profil fotoğrafı çek.",
        "👀 Kendine güvenle bak.",
        "🗺️ Büyük planlar tasarla.",
        "🤝 Birine liderlik et.",
        "💎 Değerini hatırlatan not yaz."
    ]
}

@app.get("/")
def read_root():
    return {"message": "VibeCheck API Canli Olarak Calisiyor! 🚀"}

# 🎯 CANLI VERİ SERVİS EDEN ENDPOINT
@app.get("/api/vibe")
def get_vibe_suggestion(mood: str, time: int):
    # Eğer gelen mod listemizde yoksa genele düşmesin diye uykusuz seçelim varsayılan
    mood_key = mood.lower()
    if mood_key not in SUGGESTIONS_DB:
        mood_key = "uykusuz"
        
    vibe_list = SUGGESTIONS_DB[mood_key]
    random_suggestion = random.choice(vibe_list)
    
    return {
        "mood": mood,
        "time_allocated": time,
        "suggestion": random_suggestion,
        "source": "Live Python Backend Engine" # Canlı veri olduğunu kanıtlayan imza
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
