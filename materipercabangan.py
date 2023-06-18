#if dengan 1 kondisi
nilai = int(input("Masukkan Bilangan bulat : "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")


#if dengan 2 kondisi
nilai = int(input("Masukkan Bilangan bulat : "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")

else:   #if 2 kondisi
    print("Bilangan", nilai, "merupakan bilangan negatif")


#if 3 kondisi atau lebih, menggunakan elif
nilai = int(input("Masukkan Bilangan bulat : "))
if (nilai > 0):
    print("Bilangan", nilai, "merupakan bilangan positif")
elif(nilai < 0):
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print("Anda memasukkan bilangan nol")