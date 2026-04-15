# 🚀 VibeCheck:MVP Kapsam ve Strateji Dökümanı

## 1. PROJE VİZYONU VE STRATEJİK HEDEF
VibeCheck, insan bilişsel kapasitesinin sınırlı olduğu "Karar Yorgunluğu" anlarında, bireyin mevcut duygusal verisini (vibe) ve fiziksel kısıtlarını (enerji/zaman) işleyerek en yüksek tatmini sağlayan aktiviteyi bulan bir **AI-Driven Personal Curator** sistemidir. 

Bu MVP, "Daha çok seçenek, daha çok mutluluktur" yanılgısını yıkarak, **"Mükemmel Tek Seçenek"** felsefesine odaklanır.

## 2. PROBLEMİN DERİNLİĞİ (Problem Deep-Dive)
Modern şehir hayatında birey, günde ortalama 35.000 karar vermektedir. Boş zamanlarda "Ne yapsam?" sorusu, dinlenmesi gereken beyni daha fazla yormaktadır. Mevcut çözümler (Google Maps, TripAdvisor vb.) **mekan** odaklıdır; VibeCheck ise **insan ve duygu** odaklıdır.

## 3. FONKSİYONEL KAPSAM (MVP Phase)

### 3.1. Akıllı Giriş ve Veri Yakalama (User State Acquisition)
* **NLP Mood Analysis:** Kullanıcıdan alınan serbest metin (Örn: "Çok yoğun bir gündü, sessiz bir yerlerde bir şeyler içmek istiyorum") üzerinden duygu analizi.
* **Social Battery Scaling:** 1-10 arası sosyal enerji seviyesi girişi.
* **Hard Constraints (Katı Kısıtlar):** Maksimum bütçe (isteğe bağlı), maksimum mesafe (km) ve net zaman (dk).

### 3.2. AI Karar Mekanizması (The Optimization Engine)
* **Vektör Tabanlı Eşleştirme:** Aktivitelerin "Huzur, Enerji, Sosyallik" skorları ile kullanıcının "Vibe" skorunun kosinüs benzerliği (Cosine Similarity) ile karşılaştırılması.
* **Dinamik Filtreleme:** Kullanıcı "Düşük Enerji" modundaysa, sistem otomatik olarak "Fiziksel Efor" gerektiren aktiviteleri (yürüyüş, dans, spor) %100 eler.

### 3.3. Çıktı ve Kullanıcı Deneyimi (UX)
* **The Golden Ticket:** Kullanıcıya sunulan tek bir kart. Kart içeriği: Mekan/Aktivite adı, neden bu tercihin yapıldığına dair kısa bir "AI Notu" ve rota bilgisi.
* **Instant Reroll:** Eğer öneri kesinlikle istenmiyorsa, tek seferlik "Alternatif Üret" hakkı.

## 4. TEKNİK MVP KISITLARI VE ÖNCELİKLENDİRME (MoSCoW)
* **Must Have:** Doğal dil işleme, temel lokasyon verisi, tekli öneri algoritması.
* **Should Have:** Geçmiş tercihlere göre kişiselleştirme.
* **Could Have:** Arkadaş grupları için ortak vibe analizi.
* **Won't Have:** Uygulama içi ödeme sistemleri, canlı etkinlik biletleme.

## 5. VERİ VE GÜVENLİK STRATEJİSİ
* **Data Privacy:** Kullanıcının ruh hali verileri anlıktır; sistemde kalıcı olarak depolanmaz, sadece algoritmayı eğitmek için anonimleştirilmiş skorlar tutulur.
* **Cold Start Problem:** Yeni kullanıcılar için sistem, başlangıçta genel popülasyonun "vibe" tercihlerini baz alarak öneri sunar.