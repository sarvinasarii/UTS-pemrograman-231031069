'''UTS
1. Buat variabel jenis list berikut.
    
    BIO =  ['Nama Lengkap',
            'NIM',
            'Tanggal-Bulan-Tahun Lahir'
            'Sistem Informasi C',
            '2023-2024',
            'S1',
            'aktif',
            'ganjil',
            'Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu rencana studi mahasiswa']

#(NOTED: sesuaikan dengan data anda)
            
2. Buat variabel jenis nested list berikut.

MK =   [['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216',],
        ['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [2,3,3,2,3,3,3,2],
        ['Selasa','Senin','Rabu','Senin','Kamis','Kamis','Kamis','Kamis'],
        ['07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10','07.30-09.10']]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, waktu kuliah, dan jadwal)
        
3. Susun Kode dengan hasil runing seperti berikut.
           
            
             INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                             JURUSAN SAINS
                    KARTU RENCANA STUDI MAHASISWA
                           GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : 60022010
Program/prodi   : S1/Sistem Informasi C
Tahun Masuk     : 2023 Ganjil
Status          : Aktif
|--|--  10  --|--           26         --|--5--|-- 8  --|
---------------------------------------------------------
No. Kode      |      Mata Kuliah         | SKS |  Hari  |
---------------------------------------------------------
1   22A1209   | Matkul1                  |  2  | Senin  |
2   22A1210   | Matkul2                  |  3  | Selasa |
3   22A1211   | Matkul3                  |  3  | Rabu   |
4   22A1212   | Matkul4                  |  2  | Senin  |
5   22A1213   | Matkul5                  |  3  | Kamis  |
6   22A1214   | Matkul6                  |  3  | Kamis  |
7   22A1215   | Matkul7                  |  3  | Kamis  |
8   22A1216   | Matkul8                  |  2  | Kamis  |
---------------------------------------------------------
                        TOTAL SKS           21           
---------------------------------------------------------
|---------------------------57---------------------------|
Summary:
Jumlah Mata Kuliah       : 8
Jumlah Mata Kuliah 2 SKS : 3 Mata Kuliah
Jumlah Mata Kuliah 3 SKS : 5 Mata kuliah
Mata Kuliah hari Senin   : 2 Mata Kuliah
Mata Kuliah hari Selasa  : 1 Mata Kuliah
Mata Kuliah hari Rabu    : 1 Mata Kuliah
Mata Kuliah hari Kamis   : 1 Mata Kuliah
Mata Kuliah hari Jumat   : 0 Mata Kuliah
                                              Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!

# Data BIO
BIO = [
    'Sarvina Sari', '231031069', '17-10-2005',
    'Sistem Informasi C', '2023-2024', 'S1',
    'aktif', 'ganjil',
    'Institut Teknologi Bacharuddin Jusuf Habibie',
    'Parepare', 'Jurusan Sains',
    'kartu rencana studi mahasiswa'
]

# Data MK
MK = [
    ['22A1209', '22A1210', '22A1211', '22A1212', '22A1213', '22A1214', '22A1215', '22A1216'],
    ['pancasila', 'cinta', 'bahasa indonesia', 'agama', 'PTI', 'pengantar pemrograman', 'kalkulus', 'sainster'],
    [2,2,2,2,3,3,3,3],
    ['jumat', 'kamis', 'jumat', 'jumat', 'jumat', 'selasa', 'selasa', 'rabu'],
    ['13.00-15.10', '09.20.11.00', '09.20-11.00', '07.30-09.10', '15.30-17.00', '13.30-15.00', '07.30-09.10', '15.00-17.00']
]

# Mencetak header
print("INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE")
print("JURUSAN SAINS")
print("KARTU RENCANA STUDI MAHASISWA")
print("GANJIL 2023/2024\n")

# Data dari BIO
nama_lengkap = "Sarvina Sari"  
nim = "231031069"  
program_prodi = "S1/Sistem Informasi C"
tahun_masuk = "2023 Ganjil"
status = "Aktif"

# Mencetak informasi dari BIO
print("Nama Lengkap    :", nama_lengkap)
print("NIM             :", nim)
print("Program/Prodi   :", program_prodi)
print("Tahun Masuk     :", tahun_masuk)
print("Status          :", status)

# Mencetak tabel jadwal kuliah

print("---------------------------------------------------------")
print("| No. Kode   |      Mata Kuliah          | SKS |  Hari   |")
print("---------------------------------------------------------")

total_sks = 0

# Loop untuk mencetak jadwal kuliah
for i in range(len(MK[0])):
    no_kode = MK[0][i]
    mata_kuliah = MK[1][i]
    sks = MK[2][i]
    hari = MK[3][i]

    total_sks += sks

    print(f"{i + 1}   {no_kode}   | {mata_kuliah}{' ' * (26 - len(mata_kuliah))} |  {sks}  | {hari}  |")

print("---------------------------------------------------------")

# Mencetak total SKS
print(f"                        TOTAL SKS           {total_sks}")
print("---------------------------------------------------------")

# Mencetak summary

print("Summary:")
print(f"Jumlah Mata Kuliah       : {len(MK[0])}")
print(f"Jumlah Mata Kuliah 2 SKS : {MK[2].count(2)} Mata Kuliah")
print(f"Jumlah Mata Kuliah 3 SKS : {MK[2].count(3)} Mata kuliah")
print(f"Mata Kuliah hari Senin   : {MK[3].count('Senin')} Mata Kuliah")
print(f"Mata Kuliah hari Selasa  : {MK[3].count('Selasa')} Mata Kuliah")
print(f"Mata Kuliah hari Rabu    : {MK[3].count('Rabu')} Mata Kuliah")
print(f"Mata Kuliah hari Kamis   : {MK[3].count('Kamis')} Mata Kuliah")
print(f"Mata Kuliah hari Jumat   : {MK[3].count('Jumat')} Mata Kuliah")
print("                                          Parepare, 25 Oktober 2023\n\n")
print(f"{' ' * 53}{nama_lengkap}\n{' ' * 53}{'-' * len(nama_lengkap)}")


