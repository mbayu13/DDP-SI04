from animals import *

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_ular, panjang_tubuh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis_ular
        self.panjang = panjang_tubuh
    
    def cetak_ular(self):
        super(). cetak()
        print(f"jenis ular ini adalah jenis {self.jenis}, dan hewan ini panjangnya {self.panjang} ")
        
ular_sawah = Ular("ular sawah", "daging", "amphibi", "bertelur", "belang", "10km")
ular_sawah.cetak_ular()