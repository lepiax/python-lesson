i = 0
adet = int(input("Kaç adet ürün istiyorsunuz?: "))
urunler = []


while (i < adet):
    urunAdi = input("Ürün adı: ")
    urunFiyat = input("Ürün fiyat: ")
    urunler.append({
        "urunAdi" : urunAdi,
        "urunFiyat" : urunFiyat
    })
    
    i += 1 
    
print(urunler)
