# 🗺️ Proje Geliştirme Planı (Plan.md) - VibeCheck

Bu doküman, VibeCheck PRD'sinden türetilen ve 8 haftalık sürece yayılan teknik adımları ve kullanıcı hikayelerini (User Stories) listeler.

## 1. Kullanıcı Hikayeleri (User Stories)
* **Mod Seçimi:** Bir kullanıcı olarak, o anki anlık mental durumumu (15 farklı duygu) listeden kolayca seçebilmeliyim.
* **Zaman Kısıtı:** Bir kullanıcı olarak, aktiviteye ayırabileceğim süreyi (30, 60, 120 dk) seçerek zamanımı optimize edebilmeliyim.
* **Dinamik Öneri:** Bir kullanıcı olarak, statik ve tekrarlayan öneriler yerine, yapay zekanın o an bana özel ürettiği özgün reçeteyi görebilmeliyim.

## 2. Teknik Geliştirme Adımları & Hafta Planı

### Faz 1: Altyapı ve API Tasarımı (Hafta 1 - Hafta 3)
- [x] GitHub reposunun bağımsız frontend ve backend mimarisine uygun kurulması.
- [x] FastAPI iskeletinin oluşturulması ve CORS politikalarının ayarlanması.
- [x] Proje Gereksinim Dokümanlarının (PRD) hazırlanması.

### Faz 2: Frontend & Tasarım Sistemi (Hafta 4 - Hafta 5)
- [x] Cıvıl cıvıl, hareketli baloncuklara sahip Glassmorphism kullanıcı arayüzünün kodlanması.
- [x] 15 duygu durumu ve 3 zaman kısıtının arayüz bileşenlerine (Dropdown) dönüştürülmesi.
- [x] JavaScript Fetch API entegrasyonu ile asenkron yapıya geçiş.

### Faz 3: AI Entegrasyonu & Canlıya Dağıtım (Hafta 6 - Hafta 8)
- [x] Google Gemini 1.5 Flash API entegrasyonunun backend tarafında tamamlanması.
- [x] API anahtarlarının güvenliği için `.env` ve `.gitignore` yapılandırması.
- [x] Backend servisinin Render/Railway üzerinde canlıya alınması.
- [x] Frontend servisinin Vercel/Render üzerinde canlıya alınması ve sistemlerin bağlanması.
