# 🛠 Tech Stack & AI Kullanım Dokümanı

VibeCheck, modern web standartlarına ve esnek servis mimarisine (Decoupled Architecture) uygun olarak Frontend ve Backend katmanları tamamen ayrı servisler olarak kurgulanmıştır.

## 1. Teknoloji Bileşenleri (Tech Stack)

### Frontend (Ön Yüz)
* **HTML5 & CSS3:** Semantik yapı, esnek yerleşim tasarımları (Flexbox) ve modern responsive uyumluluk.
* **JavaScript (ES6+):** Asenkron veri transferi (Fetch API), dinamik DOM manipülasyonu ve arayüz etkileşimleri.
* **Tasarım Yaklaşımı:** Canlı renk paletleri, CSS animasyonları, cam efekti (glassmorphism) ve bol emoji entegrasyonu içeren özel bir **Design System**.

### Backend (Arka Yüz)
* **Python 3.10+:** Veri işleme ve yapay zeka kütüphaneleri entegrasyonu.
* **FastAPI:** Asenkron, yüksek performanslı, otomatik OpenAPI (Swagger) dokümantasyonu sunan modern web framework'ü.
* **Uvicorn:** ASGI sunucusu olarak backend'in hızlı ve kesintisiz servis vermesini sağlar.

## 2. Yapay Zeka (AI) Entegrasyonu & Kararlar
Uygulamanın çekirdek mantığı statik `if-else` kurallarına değil, dinamik bir Büyük Dil Modeline (LLM) dayanmaktadır.
* **Kullanılan AI Servisi:** Google Gemini API veya OpenRouter (Model: Gemini 1.5 Flash).
* **Entegrasyon Amacı:** Kullanıcının seçtiği mod (örn: *kaygılı*) ve zaman (örn: *30 dk*) girdilerini alarak, prompt engineering teknikleriyle kişiye özel, motive edici ve o ana uygun özgün bir aktivite metni üretmek.
* **Mühendislik Kararı:** Yapay zeka çağrılarının frontend'i kilitlememesi için backend tarafında asenkron (async/await) mimari tercih edilmiştir. API anahtarları `.env` dosyalarında güvenli bir şekilde saklanmaktadır.
