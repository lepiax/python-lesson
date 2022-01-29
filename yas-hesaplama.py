def simdikiZaman():
    import datetime
    return datetime.datetime.now().year

def dogumTarihiniz():
    return int(input("Dogum tarihiniz: "))



def yasHesapla():
    return {simdikiZaman() - dogumTarihiniz()}

def sonucYasHesaplama():
    return yasHesapla()


print(sonucYasHesaplama())
