import tkinter as tk
from tkinter import simpledialog, messagebox

class KisiKayitUygulamasi:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Kişi Kayıt Uygulaması")

        self.kisiler = []

        self.buton_ekle_adi = tk.Button(ana_pencere, text="Adı Ekle", command=self.adi_ekle)
        self.buton_ekle_soyadi = tk.Button(ana_pencere, text="Soyadı Ekle", command=self.soyadi_ekle)
        self.buton_kaydet = tk.Button(ana_pencere, text="Kaydet", command=self.kaydet)
        self.buton_sil = tk.Button(ana_pencere, text="Sil", command=self.sil)
        self.buton_yeni_kayit = tk.Button(ana_pencere, text="Yeni Kayıt", command=self.yeni_kayit)
        self.buton_goster = tk.Button(ana_pencere, text="Göster", command=self.goster)

        self.buton_ekle_adi.pack()
        self.buton_ekle_soyadi.pack()
        self.buton_kaydet.pack()
        self.buton_sil.pack()
        self.buton_yeni_kayit.pack()
        self.buton_goster.pack()

    def adi_ekle(self):
        ad = self.input_al("Adı Girin")
        if ad:
            self.kisiler.append({"Ad": ad, "Soyad": ""})
            self.bilgi_penceresi(f"{ad} adı eklendi.")

    def soyadi_ekle(self):
        soyad = self.input_al("Soyadı Girin")
        if soyad:
            if self.kisiler:
                self.kisiler[-1]["Soyad"] = soyad
                self.bilgi_penceresi(f"{soyad} soyadı eklendi.")
            else:
                self.uyari_penceresi("Önce bir isim ekleyin.")

    def kaydet(self):
        if self.kisiler:
            self.bilgi_penceresi("Kişi bilgileri kaydedildi.")
        else:
            self.uyari_penceresi("Kaydedilecek bir bilgi yok.")

    def sil(self):
        if self.kisiler:
            self.kisiler.pop()
            self.bilgi_penceresi("Son eklenen kişi bilgisi silindi.")
        else:
            self.uyari_penceresi("Silinecek bir bilgi yok.")

    def yeni_kayit(self):
        self.kisiler = []
        self.bilgi_penceresi("Yeni bir kişi kaydı oluşturuldu.")

    def goster(self):
        if self.kisiler:
            yeni_pencere = tk.Toplevel(self.ana_pencere)
            yeni_pencere.title("Kişi Bilgileri")

            for kisi in self.kisiler:
                etiket = tk.Label(yeni_pencere, text=f"{kisi['Ad']} {kisi['Soyad']}")
                etiket.pack()
        else:
            self.uyari_penceresi("Gösterilecek kişi bilgisi yok.")

    def input_al(self, prompt):
        return simpledialog.askstring("Giriş", prompt)

    def bilgi_penceresi(self, mesaj):
        messagebox.showinfo("Bilgi", mesaj)

    def uyari_penceresi(self, mesaj):
        messagebox.showwarning("Uyarı", mesaj)

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = KisiKayitUygulamasi(root)
    root.mainloop()