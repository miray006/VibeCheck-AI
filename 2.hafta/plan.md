# VibeCheck: Proje Uygulama ve Geliştirme Planı

Bu döküman, VibeCheck MVP'sinin geliştirilme aşamalarını ve teknik iş kırılım yapısını (WBS) içerir.

## Faz 1: Altyapı ve Çatı Kurulumu (Hafta 2 - Güncel)
- [x] Proje klasör yapısının (Backend/Frontend) ayrılması.
- [x] Geliştirme ortamı bağımlılıklarının tanımlanması.
- [ ] Ana dizine `plan.md` yol haritasının eklenmesi.

## Faz 2: Backend & AI Entegrasyonu (Vibe Engine)
- [ ] **NLP Katmanı:** Kullanıcıdan gelen metni analiz edip "Duygu, Enerji, Sosyallik" parametrelerine ayıran fonksiyonun yazılması.
- [ ] **Optimizasyon Algoritması:** Kullanıcı kısıtları (zaman/konum) ile aktivite puanlarını eşleştiren "Weighted Scoring" modelinin kurulması.
- [ ] **Veri Kaynağı:** Önerilecek aktivitelerin olduğu `activities.json` veri setinin oluşturulması.

## Faz 3: Frontend & Kullanıcı Deneyimi
- [ ] **Vibe Input Interface:** Kullanıcın modunu seçtiği veya yazdığı ana ekran.
- [ ] **Result Card (The Golden Ticket):** AI tarafından seçilen tek önerinin görselleştirilmesi.
- [ ] **Feedback Loop:** Kullanıcının öneriyi puanlayabileceği etkileşim butonları.

## Faz 4: Test ve Dağıtım
- [ ] API entegrasyon testleri (Frontend-Backend haberleşmesi).
- [ ] GitHub üzerinden final "Product Release" commitinin yapılması.