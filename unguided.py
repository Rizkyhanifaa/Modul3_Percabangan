#HURUF VOKAL DAN KONSONAN
huruf = input("Masukkan sebuah huruf : ")

if huruf.isalpha():
    if huruf.lower() in ['a', 'i', 'u', 'e', 'o']:
        print(huruf, "Adalah salah satu huruf vokal")
    else:
        print(huruf, "Adalah salah satu huruf konsonan")
else:
    print("Inputan bukan huruf vokal maupun konsonan")



# validasi nilai
bilangan = int(input("Masukkan bilangan yang akan dibagi : "))
pembagi = int(input("Masukkan bilangan pembagi : "))

if(pembagi == 0):
    print("Pembagi tidak boleh 0" )
else:
    print(bilangan / pembagi)



#OPERASI TAHUN KABISAT
tahun = int(input("Masukkan Tahun :"))

if tahun % 4 == 0:
    print("Termasuk tahun kabisat")
else:
    print("Tidak Termasuk tahun kabisat")


    