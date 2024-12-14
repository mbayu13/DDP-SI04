from animals import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print(f"hewan ini berbulu {self.jenis_bulu}, dan hewan ini berbunyi {self.bunyi} ")
        
print("----- cetak burung -----")
print("----- cetak burung -----")
beo = Burung("Burung beo", "biji-bijian", "udara", "bertelur", "blu and orange", "kamu jelek")
beo.cetak_burung()       

# object kedua
merpati = Burung("Burung merpati", "biji-bijian", "udara", "bertelur", "putih", "cuakks" )

merpati.cetak_burung()



