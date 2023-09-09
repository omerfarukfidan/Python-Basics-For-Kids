# Kullanıcıdan girdiyi alın
hayvan = input("Bir hayvan seçin (köpek veya kedi): ")

# Girdiyi kontrol edin ve ilgili sesi çıkarın
if hayvan == "köpek":
    print("havhav")
elif hayvan == "kedi":
    print("meow")
else:
    print("Bilinmeyen hayvan girdisi.")
