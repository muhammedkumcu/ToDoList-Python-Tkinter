import tkinter as tk
from tkinter import messagebox
import json

class ToDoListUygulamasi:
    def __init__(self, root):
        #Uygulama penceresinin ayarları:
        self.root = root
        self.root.title("To-Do List Uygulaması")
        self.root.geometry("600x400")
        self.root.configure(bg='#F0F0F0')  #Arka plan rengini gri yapıyoruz.
        self.gorevlerUst = []  #Her fonksiyonun üstünde olan, görevleri tuttuğumuz liste

        #3 adet frame oluşturuyoruz: ana, menü, giriş
        ana_frame = tk.Frame(root)
        ana_frame.pack(fill=tk.BOTH, expand=True)

        menu_frame = tk.Frame(ana_frame)
        menu_frame.pack(side=tk.LEFT, padx=10, pady=10)

        giris_frame = tk.Frame(ana_frame)
        giris_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        #Butonları menü kısmında, fonksiyonlarını, metin renklerini ve arka plan renklerini belirleyerek oluşturuyoruz.
        tk.Button(menu_frame, text="Tamamla", command=self.gorev_tamamla, bg='#98FB98').pack(pady=5)  #Yeşil üzerine siyah (default) yazı
        tk.Button(menu_frame, text="Sil", command=self.gorev_sil, bg='#FF6347').pack(pady=5)  #Kırmızı üzerinde siyah (default yazı
        tk.Button(menu_frame, text="Tamamlananları Sil", command=self.tamamlananlari_sil, bg='#800000', fg='white').pack(pady=5)  #Bordo üzerinde beyaz yazı

        #Görev eklerken yazdığımız bölümü belirtmek için üstüne bir label ekliyoruz.
        tk.Label(giris_frame, width=20 ,text="Görev Ekle", font=('Verdana', 12, 'normal'), bg='#87CEEB').pack(pady=5)  #Açık mavi üzerine siyah (default) yazı

        #Görev eklediğimiz textbox'ın genişliğini listbox ile aynı yapıp yazdığımız yazının özelliklerini belirtiyoruz.
        self.gorev_text = tk.Entry(giris_frame, width=50, font=('Verdana', 12, 'normal'), fg='black', bg='white')
        self.gorev_text.pack(pady=5)

        #Görevleri yazdırdığımız kaydırmalı bir tablo oluşturuyoruz.
        self.tablo = tk.Listbox(giris_frame, height=10, width=50, selectmode=tk.SINGLE, bg='#F0F0F0', font=('Verdana', 12))
        self.tablo.pack(pady=5)

        self.root.bind("<Return>", self.gorev_ekle)  #Enter'a basıldığında gorev_ekle fonksiyonu çalışacak.
        self.dosya_oku()  #

    def gorev_ekle(self, event=None):
        gorev = self.gorev_text.get()
        if gorev:
            #gorevlerUst listesine sözlük şeklinde yazdığımız yeni görevi tamamlanmadığını belirterek ekliyoruz.
            self.gorevlerUst.insert(0, {"gorev": gorev, "tamamlandi": False})
            self.dosyaya_yazdir()
            self.tabloyu_guncelle()
            self.gorev_text.delete(0, tk.END)  #textbox'ı temizliyoruz yeni görevler için.
        else:
            #Eğer hiçbir şey yazmadan görev eklemeye çalışırsak uyarı veriyoruz.
            tk.messagebox.showwarning("Uyarı", "Görev içeriği boş olamaz!")

    #Tablodan seçtiğimiz görevin indisinden içeriğine erişiyoruz. Sonra tüm görevler içerisinde gezinip seçtiğimiz görevi bulup tamamlandi olarak işaretliyoruz.
    def gorev_tamamla(self):
        index = self.tablo.curselection()
        if index:  #Boş değilse yani bir görev seçildiyse içerisi çalışır.
            secili_gorev = self.tablo.get(index)
            for gorev in self.gorevlerUst:
                if gorev["gorev"] == secili_gorev:
                    gorev["tamamlandi"] = True
            self.dosyaya_yazdir()
            self.tabloyu_guncelle()

    #Tablodan seçtiğimiz görevin indisinden içeriğine erişiyoruz. Sonra tüm görevler içerisinde gezinip seçtiğimiz görevi bulup gorevlerUst listesinden kaldırıyoruz.
    def gorev_sil(self):
        secili_index = self.tablo.curselection()
        if secili_index:  #Boş değilse yani bir görev seçildiyse içerisi çalışır.
            secili_gorev = self.tablo.get(secili_index)
            for gorev in self.gorevlerUst:
                if gorev["gorev"] == secili_gorev:
                    self.gorevlerUst.remove(gorev)
                    break
            self.tabloyu_guncelle()
            self.dosyaya_yazdir()

    #Lokal bi liste oluşturup bu listeye tamamlanmayan görevleri atıyoruz. Daha sonra bu listeyi gorevlerUst'e kopyalıyoruz.
    def tamamlananlari_sil(self):
        yeni_gorevler = []
        for gorev in self.gorevlerUst:
            if not gorev["tamamlandi"]:
                yeni_gorevler.append(gorev)
        self.gorevlerUst = yeni_gorevler

        self.tabloyu_guncelle()
        self.dosyaya_yazdir()

    def tabloyu_guncelle(self):
        #Önce tabloyu baştan sona siliyoruz.
        self.tablo.delete(0, tk.END)
        #Tüm görevlere tek tek bakıp tamamlanmayan görevleri olduğu gibi, tamamlananları ise arka planı renkli şekilde tabloya yazdırıyoruz.
        for gorev in self.gorevlerUst:
            if not gorev["tamamlandi"]:
                self.tablo.insert(tk.END, gorev["gorev"])
            else:
                self.tablo.insert(tk.END, gorev["gorev"])
                self.tablo.itemconfig(tk.END, {'bg': '#87CEEB'})  #Tamamlanan görevlerin arka plan rengini açık mavi seçtim.

    def dosya_oku(self):
        try:
            #Dosyayı okunur şekilde açıyoruz, dosyadaki görevleri gorevlerUst listesinde tutuyoruz ve tabloya görevleri yazdırıyoruz.
            with open("gorevler.json", "r") as dosya:
                self.gorevlerUst = json.load(dosya)
                self.tabloyu_guncelle()
        except FileNotFoundError:
            pass

    #Dosyayı yazma modunda açıyoruz (içindekiler siliniyor) ve görev listesini dosyaya yazdırıyoruz.
    def dosyaya_yazdir(self):
        with open("gorevler.json", "w") as dosya:
            json.dump(self.gorevlerUst, dosya)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = ToDoListUygulamasi(root)
    root.mainloop()
