class Mahasiswa:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim
        self._nilai_matakuliah = {}

    @property 
    def nama(self):
        return self._nama

    @property
    def nim(self):
        return self._nim

    @property
    def nilai_rata_rata(self):
        if not self._nilai_matakuliah:
            return 0
        
        total_nilai = sum(self._nilai_matakuliah.values())
        jumlah_matkul = len(self._nilai_matakuliah)
        return total_nilai / jumlah_matkul

    def tambah_nilai(self, matkul, nilai):
        if isinstance(nilai, (int, float)) and 0 <= nilai <= 100:
            self._nilai_matakuliah[matkul] = nilai
            print(f"Nilai {matkul} berhasil ditambahin: {nilai}")
        else:
            print("Error: Nilai harus angka antara 0 - 100!")

    def info_mahasiswa(self):
        return (f"Mahasiswa: {self.nama} ({self.nim}), "
                f"Rata-rata Nilai: {self.nilai_rata_rata:.2f}")

mhs1 = Mahasiswa("Zidan Achilla Muhammad Azka", "241011450306")
print(mhs1.info_mahasiswa())

mhs1.tambah_nilai("Algoritma & Pemrograman 2", 85)
mhs1.tambah_nilai("Struktur Data", 90)
mhs1.tambah_nilai("Jaringan Komputer", 78)

print(mhs1.info_mahasiswa())