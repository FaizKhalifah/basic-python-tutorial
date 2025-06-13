class mobil:
    def __init__(self,merk,warna,nomor_plat):
        self.merk = merk
        self.warna = warna
        self.nomor_plat = nomor_plat
    
    def maju(self):
        print("Mobil maju")

    def mundur(self):
        print("Mobil mundur")


x = mobil("Toyota", "Merah", "B1234XYZ")
print(x.merk)
print(x.warna)
print(x.nomor_plat)
x.maju()
x.mundur()
     