from datetime import date


def saat():
    import datetime
    return datetime.datetime.now().hour


def isimData():
    return input("İsminiz nedir: ")


def selamlama():
    if (saat() < 12):
        return "Günaydın " + isimData()
    else:
        return "İyi akşamlar " + isimData()


print(selamlama())
