islem = input("Yapmak istediginiz islemin sembolunu giriniz")

if islem == "+":
    sayi1 = input("İlk sayiyi giriniz:")
    sayi2 = input("\n İkinci sayiyi giriniz:")
    toplam = int(sayi1) + int(sayi2) #burada int() ifadesinin icine yazilanlar sayiya donusur
    print(toplam)
elif islem == "-":
    sayi1=input("İlk sayiyi giriniz:")
    sayi2=input("\n İkinci sayiyi giriniz:")
    fark = int(sayi1) - int(sayi2)
    print(fark)
elif islem == "*":
    sayi1=input("İlk sayiyi giriniz:")
    sayi2=input("\n İkinci sayiyi giriniz:")
    carpim = int(sayi1) * int(sayi2)
    print(carpim)
elif islem == "/":  
    sayi1=input("İlk sayiyi giriniz:")
    sayi2=input("\n İkinci sayiyi giriniz:")
    bolum = int(sayi1) / int(sayi2)
    print(bolum)
else:
    print("Girdiğiniz işlem bulunmamaktadir.")

