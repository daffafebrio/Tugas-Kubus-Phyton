print("penghitung volume bangun ruang")

def menu ():
    print ("pilih bangun ruang")
    print ("masukkan angka1-6")
    print ("1. kubus")
    print ("2. balok")
    print ("3. prisma")
    print ("4. tabung")
    print ("5. bola")
    print ("6. limas")
    
def kubus ():
    sisi = int (input ("masukkan sisi: "))
    volume = int (sisi*sisi*sisi)
    print ("volume kubus ",volume)

def balok ():
    panjang = int (input ("masukkan panjang: "))
    lebar = int (input ("masukkan lebar: "))
    tinggi = int (input ("masukkan tinggi: "))
    volume = int (panjang*lebar*tinggi)
    print ("volume balok ",volume)

def prisma ():
    jari = int (input ("masukkan jari: "))
    tinggi = int (input ("masukkan tinggi: "))
    volume = int (3.14*jari)*(tinggi*jari)
    print ("volume prisma ",volume)

def tabung ():
    jari = int (input ("masukkan jari: "))
    tinggi = int (input ("masukkan panjang: "))
    volume = int (3.14*jari)*(jari*tinggi)
    print ("volume tabung ",volume)

def bola ():
    jari = int (input ("masukkan jari: "))
    volume = int (jari*jari*jari)*3.14*4/3
    print ("volume bola ",volume)

def limas ():
    jari = int (input ("masukkan jari: "))
    tinggi = int (input ("masukkan tinggi: "))
    volume = int (3.14*jari)*(tinggi*jari)*1/3
    print ("volume limas ",volume)    
print("++++++++++++++++++")
menu()
pilih = int(input("masukan pilihan: "))
if pilih == 1:
            kubus()
elif pilih == 2:
    balok()
elif pilih == 3:
    prisma()
elif pilih ==4:
    tabung()
elif pilih == 5:
    bola()
elif pilih == 6:
    limas()
else:
    print ("inputan salah")
