<h1>TO-DO List Uygulaması</h1>
Bu proje, kullanıcının bir tabloya görevlerini ekleyebilmesini, onları tamamlandı olarak işaretleyebilmesini, seçtiği görevleri silebilmesini veya tamamlanan görevleri silebilmesini sağlar.

Bu proje tek bir Python dosyasından oluşmaktadır. Projenin görsel kısmı için tkinter kütüphanesinden yararlanılmıştır.

<h3>Fonksiyonlar ve Açıklamaları</h3>
1- init(self, root):
  Uygulama penceresinin ayarlamaları yapılır.
  3 adet frame oluşturulur:
  Birinde butonlar bulunur.
  Birinde görevler gösterilir.
  Birinde eklenecek görev yazılır.
  Butonlar ve görev tablosu (aslında listbox ama anlatım daha anlaşılır olsun diye tablo diyorum) yapılandırılır.
  gorevlerUst adında global bir liste oluşturulur.
2- dosya_oku(self):
  'gorevler.json’ adındaki dosya okunur, eğer dosya yoksa işlem yapılmaz.
  gorevlerUst listesi bu dosyadan okunur ve tabloyu_guncelle() çağrılır.
3- tabloyu_guncelle(self):
  Tablo baştan sona silinir.
  gorevlerUst listesindeki tüm görevler gözden geçirilir.
  Tamamlanmayan görevler dümdüz, tamamlananlar ise arka planı açık mavi şekilde tabloya yazılır.
4- tamamlananlari_sil(self):
  Tamamlanan görevler geçici bir listede tutulur.
  Geçici listedeki görevler gorevlerUst listesine kopyalanır.
  dosya_yazdir() ve tabloyu_guncelle() fonksiyonları çağrılır.
<h4>Kullanım</h4>
Proje çalıştırıldığında uygulama penceresi açılır.
Görev eklemek için ekleme kutusuna görev yazıp 'enter' tuşuna basılır.
Görevler tamamlandığında veya silinmek istendiğinde ilgili butonlara tıklanır.
Bu açıklamalar README dosyasında proje hakkında genel bir bakış sunmaktadır. Detaylı kullanım ve kod yapısı için proje dosyasını inceleyebilirsiniz.






