# 🛠 VibeCheck: Teknik Ürün Gereksinimleri Belgesi (PRD)

**Sürüm:** 1.0.0  
**Durum:** Taslak / Geliştirme Aşamasında  
**Ürün Sahibi:** Fatma Miray Öztürk

---

## I. ÜRÜN ÖZETİ
VibeCheck, kullanıcıların anlık psikolojik ve fiziksel durumlarını veri olarak işleyip, dış dünyadaki aktivitelerle en yüksek uyumu sağlayan bir kişisel yaşam küratörüdür.

## II. KULLANICI HİKAYELERİ (USER STORIES)
1.  **Sınav Sonrası Öğrenci:** "Haftalardır kütüphanedeydim, enerjim çok düşük ama birileriyle iki kelime etmek istiyorum. 45 dakikam var, bana en uygun aktiviteyi bul."
2.  **Karar Yorgunu Yönetici:** "İşten çıktım, beynim durmuş durumda. Eve gitmek istemiyorum ama nereye gideceğimi düşünemiyorum. Tek tıkla bana bir 'mood' öner."

## III. TEKNİK SİSTEM MİMARİSİ

### 1. Veri Modelleme (Weighted Scoring Model)
Uygulama arka planda bir **Çok Kriterli Karar Verme (MCDM)** modeli çalıştırır. Her aktivite (i) için bir fayda puanı ($U_i$) hesaplanır:

$$U_i = \sum (w_j \cdot c_{ij})$$

* $w_j$: Kullanıcı girdisinin ağırlığı (Mod, Zaman, Sosyal İhtiyaç).
* $c_{ij}$: Aktivitenin o kriterle olan uyum katsayısı (Örn: "Kitap okumak" aktivitesinin "Düşük Enerji" katsayısı 0.9'dur).

### 2. Yapay Zeka Katmanı (AI Strategy)
* **LLM (OpenAI GPT-4 / Gemini Pro):** Kullanıcı metinlerini "Sentiment Analysis" ve "Entity Extraction" ile işleyerek sayısal vektörlere dönüştürür.
* **Embedding Space:** Aktiviteler bir vektör uzayında tutulur ve kullanıcın o anki "Vibe Vektörü"ne en yakın olan (Cosine Similarity) aktivite seçilir.

### 3. Teknoloji Yığını (Tech Stack)
* **Language:** Python 3.9+
* **Framework:** FastAPI (Hızlı ve asenkron veri işleme için)
* **Frontend:** Streamlit veya Flutter (Hızlı prototip ve mobil uyumluluk)
* **Database:** MongoDB (Esnek aktivite etiketleme için NoSQL tercih edilmiştir)

## IV. FONKSİYONEL GEREKSİNİMLER (FR)

### FR-1: Mod Analiz Modülü
* Sistem, kullanıcın sesli veya yazılı girdisinden 5 temel duyguyu (Yorgun, Mutlu, Stresli, Yalnız, Enerjik) %85 doğrulukla tespit etmelidir.

### FR-2: Zaman ve Konum Kısıtı
* Sistem, önerilen aktivitenin gidiş-dönüş süresini Google Maps API kullanarak hesaplamalı ve kullanıcın toplam boş vaktinden düşmelidir.

### FR-3: Akıllı Filtreleme
* Kullanıcı "Yalnız kalmak istiyorum" dediyse, sistem "Kalabalık/Gürültülü" etiketi %30'un üzerinde olan mekanları otomatik olarak elemeli (Hard Constraint).

## V. FONKSİYONEL OLMAYAN GEREKSİNİMLER (NFR)
* **Tepki Süresi:** Öneri oluşturma süreci 3 saniyeyi geçmemelidir.
* **Ölçeklenebilirlik:** Sistem eş zamanlı 10.000 isteği işleyebilecek yapıda (Containerized via Docker) tasarlanmalıdır.
* **Kullanılabilirlik:** Ana ekranda karar verme süreci maksimum 2 tıklama ile tamamlanmalıdır.

## VI. BAŞARI METRİKLERİ (KPI)
1.  **Conversion Rate:** Kullanıcıya sunulan önerinin kullanıcı tarafından "Kabul Edildi" olarak işaretlenme oranı (Hedef: %70).
2.  **Churn Reduction:** Kullanıcıların haftalık geri dönüş oranı (Retention).
3.  **Efficiency Gain:** Kullanıcın plan yapmak için harcadığı sürenin geleneksel yöntemlere göre %90 azalması.

---

## VII. RİSK ANALİZİ VE B PLANI
* **Risk:** AI yanlış duygu tespiti yapabilir.
* **Çözüm:** Kullanıcıya öneriyi görmeden önce AI'nın çıkardığı parametreleri (Örn: "Şu an yorgun olduğunuzu tespit ettim, doğru mu?") onaylatma adımı eklenecek.