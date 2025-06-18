from tabulate import tabulate
import re


pegawai = [
    {"id": 1, "nama": "Andi Prasetyo", "nip": "19870101", "jabatan": "Staf Administrasi", "divisi": "Umum", "email": "andi.prasetyo@company.com", "no_hp": "081234567801"},
    {"id": 2, "nama": "Siti Nurhaliza", "nip": "19870102", "jabatan": "Manager HRD", "divisi": "HRD", "email": "siti.nurhaliza@company.com", "no_hp": "081234567802"},
    {"id": 3, "nama": "Budi Santoso", "nip": "19870103", "jabatan": "Programmer", "divisi": "IT", "email": "budi.santoso@company.com", "no_hp": "081234567803"},
    {"id": 4, "nama": "Dewi Lestari", "nip": "19870104", "jabatan": "Staf Keuangan", "divisi": "Finance", "email": "dewi.lestari@company.com", "no_hp": "081234567804"},
    {"id": 5, "nama": "Agus Haryanto", "nip": "19870105", "jabatan": "Marketing Executive", "divisi": "Marketing", "email": "agus.haryanto@company.com", "no_hp": "081234567805"},
    {"id": 6, "nama": "Nurul Aini", "nip": "19870106", "jabatan": "Analis Data", "divisi": "IT", "email": "nurul.aini@company.com", "no_hp": "081234567806"},
    {"id": 7, "nama": "Rizky Kurniawan", "nip": "19870107", "jabatan": "Customer Service", "divisi": "Layanan", "email": "rizky.kurniawan@company.com", "no_hp": "081234567807"},
    {"id": 8, "nama": "Mega Saputri", "nip": "19870108", "jabatan": "Manager Operasional", "divisi": "Operasional", "email": "mega.saputri@company.com", "no_hp": "081234567808"},
    {"id": 9, "nama": "Fajar Maulana", "nip": "19870109", "jabatan": "Staf Gudang", "divisi": "Logistik", "email": "fajar.maulana@company.com", "no_hp": "081234567809"},
    {"id": 10, "nama": "Intan Permatasari", "nip": "19870110", "jabatan": "Staf R&D", "divisi": "Pengembangan", "email": "intan.permatasari@company.com", "no_hp": "081234567810"},
    {"id": 11, "nama": "Ahmad Fauzi", "nip": "19870111", "jabatan": "Teknisi", "divisi": "Teknik", "email": "ahmad.fauzi@company.com", "no_hp": "081234567811"},
    {"id": 12, "nama": "Yuni Rahmawati", "nip": "19870112", "jabatan": "Staf HRD", "divisi": "HRD", "email": "yuni.rahmawati@company.com", "no_hp": "081234567812"},
    {"id": 13, "nama": "Reza Aditya", "nip": "19870113", "jabatan": "Programmer", "divisi": "IT", "email": "reza.aditya@company.com", "no_hp": "081234567813"},
    {"id": 14, "nama": "Nia Marlina", "nip": "19870114", "jabatan": "Desainer Grafis", "divisi": "Kreatif", "email": "nia.marlina@company.com", "no_hp": "081234567814"},
    {"id": 15, "nama": "Hendra Wijaya", "nip": "19870115", "jabatan": "Supervisor Produksi", "divisi": "Produksi", "email": "hendra.wijaya@company.com", "no_hp": "081234567815"},
    {"id": 16, "nama": "Linda Oktaviani", "nip": "19870116", "jabatan": "Staf Hukum", "divisi": "Legal", "email": "linda.oktaviani@company.com", "no_hp": "081234567816"},
    {"id": 17, "nama": "Doni Saputra", "nip": "19870117", "jabatan": "Logistik Officer", "divisi": "Logistik", "email": "doni.saputra@company.com", "no_hp": "081234567817"},
    {"id": 18, "nama": "Melati Anindya", "nip": "19870118", "jabatan": "Finance Manager", "divisi": "Finance", "email": "melati.anindya@company.com", "no_hp": "081234567818"},
    {"id": 19, "nama": "Gilang Ramadhan", "nip": "19870119", "jabatan": "Staf IT Support", "divisi": "IT", "email": "gilang.ramadhan@company.com", "no_hp": "081234567819"},
    {"id": 20, "nama": "Rani Yuliana", "nip": "19870120", "jabatan": "QA Analyst", "divisi": "QC", "email": "rani.yuliana@company.com", "no_hp": "081234567820"},
]

recycle_bin = []
def validate_regex(val, type):
    if type=="email":
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    elif type=="nip":
        pattern = '^\\d+$'
    elif type=="nama":
        pattern = "^[a-zA-Z]"
    elif type=="ID unik":
        pattern = '^\\d+$'
    elif type=="no_hp":
        pattern = '^\\d+$'
    elif type=="jabatan":
        pattern = "^[a-zA-Z]"
    elif type=="divisi":
        pattern = "^[a-zA-Z]"
    

    if re.match(pattern, val):
        return True
    else:
        return False

def input_int(pesan):
    try:
        return int(input(pesan))
    except ValueError:
        print("Input harus berupa angka.")
        return input_int(pesan)

def print_table(data):
    if data:
        headers = data[0].keys()
        rows = [x.values() for x in data]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("Tidak ada data untuk ditampilkan.")

def input_name(prompt, max_attemps, type):
    attempts = 0
    while attempts < max_attemps:
        nama = input(f"{prompt}: ")
        isValid = validate_regex(nama,"nama")
        if isValid:
            return nama
        elif attempts == max_attemps:
            print("Pembuatan pegawai dibatalkan karena input ID tidak valid")
            return 
        else:
            attempts += 1
    return print(f"masukkan {prompt} yang valid")

def create():
    try:
        id = input_int("Masukkan ID unik: ")
        if any(p["id"] == id for p in pegawai):
            print("[GAGAL] ID sudah digunakan.")
            return
        
        nama = input_name("nama", 3, "nama")
        
        # nama = input("Nama: ")
        # namaValidate = validate_regex(nama,"nama")
        # if namaValidate ==  False:
        #     print("masukkan nama yang valid")
        #     return

        nip = input("NIP: ")
        nipValidate = validate_regex(nip,"nip")
        if nipValidate ==  False:
            print("masukkan nip yang valid")
            return
        
        jabatan = input("Jabatan: ")
        jabatanValidate = validate_regex(jabatan,"Jabatan")
        if jabatanValidate ==  False:
            print("masukkan Jabatan yang valid")
            return
        
        divisi = input("Divisi: ")
        divisiValidate = validate_regex(divisi,"divisi")
        if divisiValidate ==  False:
            print("masukkan Divisi yang valid")
            return
        
        email = input("Email: ")
        emailValidate = validate_regex(email,"email")
        if emailValidate ==  False:
            print("masukkan email yang valid")
            return
        
        no_hp = input("No HP: ")
        no_hpValidate = validate_regex(no_hp,"no_hp")
        if no_hpValidate ==  False:
            print("masukkan no_hp yang valid")
            return
        
        pegawai.append({"id": id, "nama": nama, "nip": nip, "jabatan": jabatan, "divisi": divisi, "email": email, "no_hp": no_hp})
        
        print("[SUKSES] Data berhasil ditambahkan.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")


def read():
    while True:
        print("\n[1] Tampilkan Semua\n[2] Cari Nama\n[3] Cari Jabatan\n[0] Kembali")
        pilihan = input("Pilih: ")
        if pilihan == "1":
            print_table(pegawai)
        elif pilihan == "2":
            nama = input("Masukkan nama: ").lower()
            hasil = [p for p in pegawai if nama in p["nama"].lower()]
            print_table(hasil)
        elif pilihan == "3":
            jabatan = input("Masukkan jabatan: ").lower()
            hasil = [p for p in pegawai if jabatan in p["jabatan"].lower()]
            print_table(hasil)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

def update():
    try:
        id = input_int("Masukkan ID yang ingin diupdate: ")
        for p in pegawai:
            if p["id"] == id:
                print(f"Update data untuk: {p['nama']}")
                for key in p:
                    if key == "id": continue
                    baru = input(f"{key} lama: {p[key]} → Baru (kosongkan jika tidak diubah): ")
                    if baru:
                        p[key] = baru
                print("[SUKSES] Data berhasil diupdate.")
                return
        print("[GAGAL] Data tidak ditemukan.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")

def delete():
    try:
        id = input_int("Masukkan ID yang ingin dihapus: ")
        for i, p in enumerate(pegawai):
            if p["id"] == id:
                print("[INFO] Data yang akan dihapus:")
                print_table([p])
                konfirmasi = input("Apakah Anda yakin ingin menghapus? (y/n): ")
                if konfirmasi.lower() == "y":
                    recycle_bin.append(pegawai.pop(i))
                    print("[SUKSES] Data berhasil dipindahkan ke recycle bin.")
                return
        print("[GAGAL] Data tidak ditemukan.")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan: {e}")

def lihat_recycle_bin():
    print("\n📦 Recycle Bin:")
    print_table(recycle_bin)

def menu():
    while True:
        print("\n=== Aplikasi CRUD Data Pegawai ===")
        print("[1] Tambah Pegawai")
        print("[2] Tampilkan Data Pegawai")
        print("[3] Perbarui Data Pegawai")
        print("[4] Hapus Data Pegawai")
        print("[5] Lihat Recycle Bin")
        print("[0] Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            create()
        elif pilih == "2":
            read()
        elif pilih == "3":
            update()
        elif pilih == "4":
            delete()
        elif pilih == "5":
            lihat_recycle_bin()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    print("[INFO] Data dummy pegawai berhasil dimuat.")
    menu()
