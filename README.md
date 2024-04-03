TO-DO List Uygulaması
Bu proje, kullanıcının bir tabloya görevlerini ekleyebilmesini, onları tamamlandı olarak işaretleyebilmesini, seçtiği görevleri silebilmesini veya tamamlanan görevleri silebilmesini sağlar.

Proje Detayları
Proje Adı: TO-DO List Uygulaması
Ders Adı: Bilgisayar Programlama II
Öğrenci Adı: Muhammed Kumcu
Öğrenci Numarası: 170422008
Proje İçeriği
Bu proje tek bir Python dosyasından oluşmaktadır.

Fonksiyonlar ve Açıklamaları
init(self, root):

Uygulama penceresinin ayarlamaları yapılır.
3 adet frame oluşturulur:
Birinde butonlar bulunur.
Birinde görevler gösterilir.
Birinde eklenecek görev yazılır.
Butonlar ve görev tablosu (aslında listbox ama anlatım daha anlaşılır olsun diye tablo diyorum) yapılandırılır.
gorevlerUst adında global bir liste oluşturulur.
dosya_oku(self):

'gorevler.json’ adındaki dosya okunur, eğer dosya yoksa işlem yapılmaz.
gorevlerUst listesi bu dosyadan okunur ve tabloyu_guncelle() çağrılır.
tabloyu_guncelle(self):

Tablo baştan sona silinir.
gorevlerUst listesindeki tüm görevler gözden geçirilir.
Tamamlanmayan görevler dümdüz, tamamlananlar ise arka planı açık mavi şekilde tabloya yazılır.
tamamlananlari_sil(self):

Tamamlanan görevler geçici bir listede tutulur.
Geçici listedeki görevler gorevlerUst listesine kopyalanır.
dosya_yazdir() ve tabloyu_guncelle() fonksiyonları çağrılır.
Kullanım
Proje çalıştırıldığında uygulama penceresi açılır.
Görev eklemek için ekleme kutusuna görev yazıp 'enter' tuşuna basılır.
Görevler tamamlandığında veya silinmek istendiğinde ilgili butonlara tıklanır.
Bu açıklamalar README dosyasında proje hakkında genel bir bakış sunmaktadır. Detaylı kullanım ve kod yapısı için proje dosyasını inceleyebilirsiniz.






