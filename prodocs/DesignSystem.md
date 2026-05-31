# 🌈 Design System (Tasarım Sistemi) - VibeCheck

VibeCheck'in görsel dili, kullanıcının uygulayacağı aktiviteye başlamadan önce modunu yükseltmeyi amaçlayan, cıvıl cıvıl, enerjik ve modern bir estetik üzerine kurulmuştur.

## 1. Renk Paleti (Color Palette)
Geliştirme sürecinde tüm renkler CSS `:root` seçicisinde değişken olarak tanımlanmış ve tutarlılık sağlanmıştır.
* **Arka Plan (Deep Space):** `#0f172a` (Derin ve sakinleştirici lacivert/siyah tonu).
* **Birincil Gradyan (Rainbow Glow):** `linear-gradient(45deg, #ff007a, #7000ff, #00d4ff)` (Kullanıcıya dinamizm ve sihir hissi veren pembe-mor-turkuaz geçişi).
* **Kart Arka Planı (Glassmorphic White):** `rgba(30, 41, 59, 0.7)` ile `%70` opaklık ve `backdrop-filter: blur(20px)` uygulanarak modern cam efekti elde edilmiştir.
* **Yazı Renkleri:** Ana metinler için saf beyaz yerine gözü yormayan parlak gri `#f1f5f9` ve alt başlıklar için `#94a3b8` seçilmiştir.

## 2. Tipografi (Typography)
* **Yazı Tipi:** Standart ve temiz bir görünüm, yüksek okunabilirlik için sistem fontu ailesi (`'Inter', -apple-system, sans-serif`) tercih edilmiştir.
* **Hiyerarşi:**
    * Uygulama Başlığı: `2.8rem`, Ekstra Kalın (`900`), Gradyan Renkli.
    * Etiketler (Labels): `0.85rem`, Kalın (`700`), Gri Renkli.

## 3. Mikro-Etkileşimler & Animasyonlar (Animations)
* **Süzülen Baloncuklar (Floating Bubbles):** Arka planda `rise` animasyonu ile dipten yukarıya rastgele hızlarda süzülen şeffaf baloncuklar ile dinamik bir derinlik yaratılmıştır.
* **Sonuç Alanı Animasyonu (Slide Up):** Sihirli öneri üretildiğinde sonuç kutusu aşağıdan yukarıya doğru `translateY` efekti ile yumuşak bir şekilde belirmektedir.
