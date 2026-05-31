# 📈 Progress & Hata Günlüğü (Progress Log)

Bu doküman, VibeCheck projesinin geliştirme sürecinde karşılaşılan teknik zorlukları, yapılan kritik revizyonları ve gelişim aşamalarını kaydeder.

## Hafta 2: Temel Mimari Kararı
* **Gelişme:** Projenin backend kısmı FastAPI ile kurgulandı, frontend ve backend klasörleri tamamen birbirinden ayrıldı.
* **Alınan Karar:** Monolitik bir yapı yerine, ileride mobil veya farklı platformlara da hizmet verebilmesi için bağımsız bir API mimarisi (Decoupled) seçildi.

## Hafta 4: Frontend Geliştirme & Fonksiyonel Hatalar
* **Karşılaşılan Hata (Bug):** İlk prototipte kullanıcı girdileri serbest metin (text input) olarak alınıyordu. Test aşamasında kullanıcının "uykusuzum" gibi rastgele girdiler yazdığında, statik mock verilerin bunu yakalayamadığı ve alakasız yüksek enerjili öneriler çıktığı fark edildi. (Kullanıcı deneyimi hatası).
* **Çözüm & Revizyon:** Serbest metin girişi iptal edildi. Girdi kontrolü (Input Validation) sağlamak adına 15 farklı duygu durumunu içeren sabit bir açılır menü (`<select>`) entegre edildi. 
* **Fonksiyonel Hata (Bug):** Kod birleştirme esnasında JavaScript fonksiyon isimlerindeki (`checkVibe` vs `generateMockResult`) uyuşmazlıktan dolayı butonun tetiklenmediği görüldü. Fonksiyon isimleri refaktör edilerek hata çözüldü.
* **Görsel İlerleme:** Kullanıcı testlerinden gelen geri bildirimler doğrultusunda arka plan koyu/parlak gradyana çevrildi ve CSS animasyonlu süzülen baloncuklar eklenerek UX zenginleştirildi.
