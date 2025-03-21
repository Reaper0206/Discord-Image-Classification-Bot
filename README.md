Bu Discord botu, görsellerden Türkiye'deki tarihi yapıları tanıyan ve bu yapılar hakkında bilgi veren bir yapay zeka modeline sahiptir. Model, Google Teachable Machine kullanılarak eğitilmiş olup, bot yüklenen resimleri analiz eder ve yapıyı tanımlayarak konumu, tarihi, giriş ücreti ve açık saatleri gibi bilgileri kullanıcıya sunar.

🚀 Özellikler

Kullanıcıların yüklediği görsellerdeki Türkiye'nin tarihi ve doğal yapıları tanır.

Tanınan yapının konumu, tarihi, giriş ücreti ve açık saatleri hakkında bilgi verir.

Teachable Machine ile eğitilmiş model kullanır.

ZIP dosyasından model dosyalarını çıkarma işlemini otomatik yapar.

📜 Kurulum

1️⃣ Gerekli Bağımlılıkları Kur

Aşağıdaki komutları çalıştırarak gerekli kütüphaneleri yükleyin:

pip install discord tensorflow numpy pillow

2️⃣ ZIP Dosyanızı Hazırlayın

Teachable Machine'den indirdiğiniz modelin ZIP dosyasını, botun olduğu klasöre yerleştirin (örneğin my_model.zip).

3️⃣ Bot Tokeninizi Ekleyin

Discord Developer Portal adresine gidin.

Bir bot oluşturun ve TOKENİNİZİ alın.

bot.run("TOKENİNİZİ_BURAYA_YAZIN") satırına botunuzun tokenini ekleyin.

4️⃣ Botu Çalıştırın

Botu başlatmak için aşağıdaki komutu çalıştırın:

python bot.py

🛠 Kullanım

Discord sunucunuzda bir kanala gidin.

Bir yapı fotoğrafı gönderin ve !tanı komutunu yazın.

Bot, yapıyı tanıyacak ve size şu bilgileri gönderecek:

📍 Konum

📜 Tarih

💰 Giriş Ücreti

🕰 Açık Saatler

📌 Desteklenen Yapılar

Bu bot aşağıdaki tarihi ve doğal yapıları tanıyabilir:

🏛 Taş Köprü (Adana)

⛪ Sümela Manastırı (Trabzon)

🌋 Peri Bacaları (Kapadokya)

💦 Pamukkale Travertenleri (Denizli)

🎅 Noel Baba Kilisesi (Antalya)

⛰ Nemrut Dağı (Adıyaman)

🏰 Kız Kulesi (İstanbul)

🏺 Hattuşaş Antik Kenti (Çorum)

🏺 Göbeklitepe (Şanlıurfa)

🏗 Galata Kulesi (İstanbul)

🏛 Efes Antik Kenti (İzmir)

🏚 Cennet Cehennem Mağarası (Mersin)

🕌 Ayasofya Camii (İstanbul)

🎭 Aspendos Antik Tiyatrosu (Antalya)

🏛 Ani Harabeleri (Kars)

🏔 Ağrı Dağı (Ağrı)


📜 Lisans

Bu proje açık kaynaklıdır ve MIT Lisansı ile paylaşılmaktadır. Herkes geliştirmeye katkıda bulunabilir!

📩 Geri bildirim ve önerileriniz için şu e-posta adresine yazabilirsiniz:
✉️ [doruk.brk04@gmail.com]

🎯 Geliştirmek veya sorun bildirmek için GitHub'da yıldız bırakmayı unutmayın! 🚀
