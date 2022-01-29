from datetime import date


def saat():
    import datetime
    return datetime.datetime.now().hour



def selamlama():
    if (saat() < 12):
        return "Günaydın"
    else:
        return "İyi akşamlar"


print(selamlama())
