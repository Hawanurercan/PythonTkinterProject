from tkinter import *

class AnaMenu:
    def __init__(self, master):
        self.master = master
        master.title("Ana Menü")
        master.geometry("200x200")

        self.aralik_etiket = Label(master, text="             ")
        self.aralik_etiket.pack()

        self.aralik_etiket = Label(master, text="             ")
        self.aralik_etiket.pack()

        self.buton1 = Button(master, text="GİRİŞ YAP", command=self.giris_ekrani_ac)
        self.buton1.pack()

        self.aralik_etiket = Label(master, text="           ")
        self.aralik_etiket.pack()

        self.aralik_etiket = Label(master, text="           ")
        self.aralik_etiket.pack()

        self.buton2 = Button(master, text="KAYIT OL", command=self.kayit_ol_ekrani_ac)
        self.buton2.pack()

    def giris_ekrani_ac(self):
        self.giris_ekrani = Toplevel(self.master)
        self.giris_ekrani.title("Giriş Ekranı")
        self.giris_ekrani.geometry("300x300")

        kullaniciAdiSor = Label(self.kayit_ol_ekrani, text="Kullanıcı Adı")
        kullaniciAdiSor.pack()

        kullaniciAdi = Entry(self.kayit_ol_ekrani)
        kullaniciAdi.pack()

        sifreSor = Label(self.kayit_ol_ekrani)
        sifreSor.config(text=u"Şifre")
        sifreSor.pack()

        sifre = Entry(self.kayit_ol_ekrani)
        sifre.pack()

        # Giriş ekranına ait widget'ları ekleyebilirsiniz.

    def kayit_ol_ekrani_ac(self):
        self.kayit_ol_ekrani = Toplevel(self.master)
        self.kayit_ol_ekrani.title("Kayıt Ol Ekranı")
        self.kayit_ol_ekrani.geometry("300x300")

        # Kayıt ol ekranına ait widget'ları

        aralik_etiket = Label(self.kayit_ol_ekrani, text="")
        aralik_etiket.pack()

        isimSor = Label(self.kayit_ol_ekrani, text="İsim")
        isimSor.pack()

        isim = Entry(self.kayit_ol_ekrani)
        isim.pack()

        soyisimSor = Label(self.kayit_ol_ekrani, text="Soyisim")
        soyisimSor.pack()

        soyisim = Entry(self.kayit_ol_ekrani)
        soyisim.pack()

        kullaniciAdiSor = Label(self.kayit_ol_ekrani, text="Kullanıcı Adı")
        kullaniciAdiSor.pack()

        kullaniciAdi = Entry(self.kayit_ol_ekrani)
        kullaniciAdi.pack()

        sifreSor = Label(self.kayit_ol_ekrani)
        sifreSor.config(text=u"Şifre")
        sifreSor.pack()

        sifre = Entry(self.kayit_ol_ekrani)
        sifre.pack()

        aralik_etiket = Label(self.kayit_ol_ekrani, text="")
        aralik_etiket.pack()

        buton_kaydet = Button(self.kayit_ol_ekrani, text="Kaydet", command=self.kaydet)
        buton_kaydet.pack()

        aralik_etiket = Label(self.kayit_ol_ekrani, text="")
        aralik_etiket.pack()

        uyarı_etiket = Label(self.kayit_ol_ekrani, text="")
        uyarı_etiket.pack()

        ad = isim.get()
        soyad = soyisim.get()
        kullanici_adi = kullaniciAdi.get()
        sifre_text = sifre.get()

        if ad == "" or soyad == "" or kullanici_adi == "" or sifre_text == "":
            uyarı_etiket.config(text="Lütfen bütün alanları doldurun.")
        else:
            uyarı_etiket.config(text="Kayıt başarıyla eklendi.")
            isim.delete(0, END)
            soyisim.delete(0, END)
            kullaniciAdi.delete(0, END)
            sifre.delete(0, END)


def kaydet(self):
    ad = isim.get()
    soyad = soyisim.get()
    kullanici_adi = kullaniciAdi.get()
    sifre_text = sifre.get()

    if ad == "" or soyad == "" or kullanici_adi == "" or sifre_text == "":
        uyarı_etiket.config(text="Lütfen bütün alanları doldurun.")
    else:
        uyarı_etiket.config(text="Kayıt başarıyla eklendi.")
        isim.delete(0, END)
        soyisim.delete(0, END)
        kullaniciAdi.delete(0, END)
        sifre.delete(0, END)


if __name__ == '__main__':
    root = Tk()
    app = AnaMenu(root)
    root.mainloop()

