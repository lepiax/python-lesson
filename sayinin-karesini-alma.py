while True:
    print("******************")
    sayi1 = input("Karesi alınacak sayı: ")
    if (sayi1 == "q"):
        break

    try:
        sonuc = float(sayi1 * 2)
        print(f'Sonuç: {sonuc}')
        print("******************")
        break
    except ValueError:
        print('Sayısal değer giriniz.')
        continue
