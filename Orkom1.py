desimal = int(input("Masukkan Angka Desimal :"))

#Validasi Input
if desimal <0:
    print("Masukkan bilangan bulat Non-negatif")
#Jika angka 0
elif desimal ==0:
    print("0 dalam biner adalah 0")

else:
    angka = desimal
    biner = ""
    proses = ""

#Perulangan Pembagian 2
while angka >0:
    hasilBagi = angka // 2
    sisa = angka % 2
    #Menyimpan proses
    proses += (
        str(angka) +
        " ÷ 2 = " +
        str(hasilBagi) +
        " sisa " +
        str(sisa) +
        "\n"
    )
    # Sisa dimasukan ke depan
    biner = str(sisa) + biner
    #Angka Berikutnya
    angka = hasilBagi
    print()
    print("Bilangan Desimal:", desimal)
    print()
    print("Tahapan Perhitungan :")
    print(proses)
    print("Baca sisa daari bawah ke atas :")
    print(biner)
    print()
    print(
        "jadi,",
        desimal,
        "desimal = ",
        biner,
        "biner"
    )