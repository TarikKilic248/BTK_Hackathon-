# **Hackathon 2024 - Yapay Zeka Destekli Matematik Çözücü**

## **1. Giriş**
Hackathon 2024, Türkiye'de yazılım geliştirme ve yapay zekâ alanına ilgi duyan herkesin teorik bilgilerini pratikte uygulama imkânı bulduğu bir etkinlik olarak tasarlanmıştır. Bu hackathonun amacı, katılımcıların veri bilimi ve yapay zekâ konusundaki bilgilerini gerçek dünyadaki problemlere uygulayarak deneyim kazanmalarını sağlamaktır.

Bu doğrultuda, biz de yarışma şartlarına uygun olarak **Gemini destekli bir matematik çözücü uygulaması** geliştirdik. Bu uygulama, yapay zekâ kullanarak belirli bir problemi çözmek için veri bilimi becerilerimizi ortaya koymamız açısından bize önemli bir pratik alan sundu.

Uygulamamızın temel amacı, kullanıcıların matematik problemlerini çözmelerine yardımcı olmaktır. Kullanıcılar, problemlerini yazılı olarak girebilir veya dosya yoluyla yükleyebilir. Yapay zekâ desteğiyle problemleri analiz eden ve çözen bu sistem, özellikle öğrenciler ve profesyoneller için etkili bir çözüm platformu sağlamaktadır.

---

## **2. Ürün Tanımı**
Uygulamamız, kullanıcıların matematik problemlerini çözmelerine yardımcı olmak için çeşitli özellikler sunmaktadır. Bu özellikler, kullanıcının farklı yollarla matematiksel soruları sisteme yüklemesini ve çözümleri detaylı bir şekilde incelemesini sağlar.

### **Öne Çıkan Özellikler**
- **Girdi Seçenekleri:**
  - **Metin Girişi:** Kullanıcılar, problemlerini doğrudan metin olarak yazabilir.
  - **Dosya Yükleme:** Kullanıcılar, PDF veya metin dosyaları yoluyla birden fazla problemi toplu olarak yükleyebilir.
  - **Sesli Giriş:** Kullanıcılar, matematik problemlerini sesli olarak söyleyebilir ve yapay zekâ bu sesi işleyerek problemi analiz edebilir.
  - **Fotoğraf Çekme:** Kullanıcılar, problem içeren bir fotoğraf yükleyerek çözüme ulaşabilir. Bu özellikle el yazısıyla yazılmış problemleri kolayca sisteme aktarmak mümkündür.

- **Gemini Yapay Zekâ Desteği:**
  - Uygulama, matematik problemlerini çözerken **Gemini API**’sini kullanır. Yapay zekâ, karmaşık matematiksel işlemleri analiz ederek doğru ve güvenilir sonuçlar sunar.
  
- **Açıklamalı Çözüm:**
  - Uygulama yalnızca doğru sonuç vermekle kalmaz, aynı zamanda **adım adım açıklamalı çözümler** sunar. Böylece kullanıcılar yalnızca sonucu görmekle kalmayıp, çözüm sürecini de detaylı şekilde anlayabilir.

- **Eğitim Desteği:**
  - Kullanıcılara **detaylı dökümanlar ve eğitim videoları** sunularak, çözümleri daha iyi anlamaları sağlanır.

---

## **3. Teknik Yapı**
Projemiz **backend, frontend ve API entegrasyonu** olmak üzere üç temel bileşenden oluşmaktadır. Bu bileşenler, projenin düzenli bir yapıya sahip olmasını ve etkili çalışmasını sağlamaktadır.

### **Proje Dosya Yapısı**
- **`app.py`**: Backend’in ana dosyasıdır. Kullanıcının girdiği matematik problemleri burada işlenerek Gemini API’sine gönderilir ve sonuçlar alınarak kullanıcıya sunulur.
- **`html/`**: Kullanıcı arayüzünün temel HTML dosyalarını içerir. Form yapıları, sonuç gösterim bölümleri ve kullanıcı girdileri burada yönetilir.
- **`script.js`**: Frontend tarafında etkileşimli işlemleri yöneten JavaScript dosyasıdır. Kullanıcıdan veri alımı, dosya yükleme ve API çağrılarının yönetimi bu dosyada gerçekleştirilir.
- **`css/`**: Uygulamanın görsel tasarımını içeren CSS dosyalarıdır. Kullanıcı deneyimini iyileştirmek için butonlar, renkler ve sayfa düzeni gibi bileşenleri düzenler.

Bu dosya yapısı, projenin backend ve frontend arasında net bir ayrım yaparak düzenli bir yapı oluşturmasını sağlar.

---

## **4. Kullanıcı Deneyimi**
Uygulama, **kullanıcı dostu** bir arayüze sahiptir. Öğrencilerden profesyonellere kadar herkesin rahatlıkla kullanabileceği bir yapıya sahiptir.

- **Responsive Tasarım:** Mobil, tablet ve bilgisayar gibi farklı ekran boyutlarına uyum sağlayarak esnek kullanım imkânı sunar.
- **İnteraktif Çözüm Adımları:** Kullanıcılar, yapay zekâ tarafından adım adım çözülen matematik problemlerini detaylıca inceleyebilir.
- **Öğrenmeyi Destekleyici Yapı:** Kullanıcılar sadece sonucu görmekle kalmaz, aynı zamanda çözüm sürecini öğrenebilir ve ilgili eğitim materyallerine ulaşabilir.

---

## **5. Hackathon Değerlendirmesi**

### **Hackathon Süreci ve Karşılaşılan Zorluklar**
Hackathon 2024 sürecinde ekip olarak çeşitli teknik ve organizasyonel zorluklarla karşılaştık:
- **Gemini API Entegrasyonu:** Performans sorunları ve veri uyumluluğunu optimize etmek için detaylı testler gerçekleştirdik.
- **Responsive Tasarım:** Uygulamanın farklı cihazlarda sorunsuz çalışmasını sağlamak için duyarlı tasarım üzerine çalışmalar yaptık.
- **Ekip Çalışması:** Git versiyon kontrol sistemini etkin bir şekilde kullanarak, üç kişilik ekibimizle paralel geliştirme süreçlerini yönettik.

### **Sonuç**
Hackathon sürecinde, **yapay zekâ destekli pratik bir çözüm** geliştirme fırsatı yakaladık. Bu proje, eğitim alanında öğrencilere ve profesyonellere büyük kolaylık sağlayabilecek bir uygulama olarak ortaya çıktı.

- **Öğrencilere eğitim desteği sağlayarak matematik problemlerini çözme yeteneklerini geliştirmeye yardımcı olur.**
- **Adım adım açıklamalar sunarak, matematik kavramlarının daha iyi anlaşılmasını destekler.**
- **Kullanıcı dostu arayüzü sayesinde kolay ve hızlı kullanım imkânı sunar.**

Hackathon gibi etkinlikler, yazılım geliştirme ve yapay zekâ alanında genç yazılımcılara **gerçek dünya deneyimi kazanma** fırsatı sunmaktadır. Bu süreçte **ekip çalışması, proje yönetimi ve teknik yetkinliklerimizi geliştirme** imkânı bulduk.

---

## **6. Gelecek Planları**
Bu projeyi daha da ileriye taşımak için şu geliştirmeleri planlıyoruz:
- **Farklı matematik dallarına destek sağlama** (geometri, istatistik vb.).
- **Kullanıcıların çözümleri daha iyi anlamalarına yönelik interaktif öğrenme modülleri ekleme.**
- **Mobil uygulama entegrasyonu ve offline kullanım desteği.**

---

## **7. Ekip Üyeleri**
- **[Adınız]** – Backend ve API Entegrasyonu
- **[Adınız]** – Frontend Geliştirme ve UI/UX Tasarımı
- **[Adınız]** – Veri İşleme ve Yapay Zekâ Entegrasyonu

Hackathon 2024'te gösterdiğimiz başarıdan dolayı ekibimizi tebrik ediyoruz ve daha ileriye taşıyacak geliştirmeleri sabırsızlıkla bekliyoruz! 🚀

