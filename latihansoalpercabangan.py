
# Program Mengidentifikasi Suhu
suhu = int(input("Masukkan besarnya nilai suhu : "))

if(suhu <= 0):
    print("Suhu sebesar", suhu, "derajat, air akan berwujud padat (es)")
elif(suhu < 100):
    print("Suhu sebesar", suhu, "derajat, air akan berwujud cair")
elif(suhu >= 100):
    print("Suhu sebesar", suhu, "derajat, air akan berwujud gas")



#Panggilan Berdasarkan Status

gender = input("Perempuan atau Laki-Laki ? (L/P): ")

if(gender == 'L'):
    status = input("Anda sudah menikah atau belum ? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak")
    else:
        print("Hallo Mas")
elif(gender == 'P'):
    status = input("Anda sudah menikah atau belum ? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ibu")
    else:
        print("Hallo Mbak")
else:
    print("gender tidak ada dalam pilihan")


#PROGRAM DATA DIRI

print("===========INPUT==========")
nama = input("Nama : ")
gender = input("Jenis Kelamin (L/P): ")
if(gender == 'L'):
    gender = "Laki-Laki"
elif(gender == 'P'):
    gender = "Perempuan"
else:
    gender = "Jenis Kelamin tidak ditemukan"

agama = int(input("Agama : "))

if(agama == 1):
    agama = "Islam"
elif(agama == 2):
    agama = "Protestan"
elif(agama == 3):
   agama = "Katholik"   
elif(agama == 4):
    agama = "Hindhu"
elif(agama == 5):
    agama = "Buddha" 
else:
    agama = "Agama tidak ditemukan"

print("==========OUTPUT==========")
print("Nama : ", nama)
print("Jenis Kelamin : ", gender)
print("Agama : ", agama)

