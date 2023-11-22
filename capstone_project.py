    # Rental Mobil DImpi
# Daftar Yang Tersedia
Daftarmobil = [{'Code Mobil' : "001",
        'Jenis Mobil' : 'Ferrari',
        'Pembuat' : 'Italy',
        'Type' : 'Sedan',
        'Stock' : 70
    },
    {
        'Code Mobil' : "002",
        'Jenis Mobil' : 'Bugatti',
        'Pembuat' : 'England',
        'Type' : 'Luxury Sedan',
        'Stock' : 50
    },
    {
        'Code Mobil' : "003",
        'Jenis Mobil' : 'Tesla',
        'Pembuat' : 'United States',
        'Type' : 'SUV',
        'Stock' : 150
    },
    {
        'Code Mobil' : "004",
        'Jenis Mobil' : 'Mercedes Benz',
        'Pembuat' : 'Germany',
        'Type' : 'Minibus',
        'Stock' : 100
    }
]

# Var Sementara
Cart=[]
DataBasePeminjam =[]
NoPinjaman = 0

# Fungsi Tabel Database Peminjam
def Database (listdata0):
    print('\t =============== Daftar Peminjam ===============')
    print('\tNo Pinjaman\t| Nama Peminjam | Jenis Mobil\t\t| Qty\t| Code Mobil')
    for i in range(len(listdata0)) :
        print('\t{}\t\t|  {} \t| {} \t| {} \t| {}'.format(listdata0[i]['No Pinjaman'],listdata0[i]['Nama Peminjam'],listdata0[i]['Jenis Mobil'],listdata0[i]['Qty'],listdata0[i]['Code Mobil']))

# Fungsi Tabel Daftar
def Showlist (listdata):
    print('\t =============== Daftar Mobil ===============')
    print('\Code Mobil\t| Jenis Mobil \t\t| Pembuat\t\t| Type\t| Stock\t\t')
    for i in range(len(listdata)) :
        print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(listdata[i]['Code Mobil'],listdata[i]['Jenis Mobil'],listdata[i]['Pembuat'],listdata[i]['Type'],listdata[i]['Stock']))

# Fungsi Tabel Keranjang
def Cartfung (listdata2):
    print('\t =============== Daftar Keranjang ===============')
    print('\tJenis Mobil\t\t| Qty\t| Code Mobil')
    for i in range(len(listdata2)) :
        print('\t{}\t| {} \t| {}'.format(listdata2[i]['Jenis Mobil'],listdata2[i]['Qty'],listdata2[i]['Code Mobil']))

# Fungsi Tabel Daftar Sebelum Diupdate
def ShowListUpdate (listdata,x,NewData):
    print('\t =============== Daftar Mobil ===============')
    print('\Code Mobil\t| Jenis Mobil \t| Pembuat\t| Type\t| Stock\t'),
    if x == 1:
        for i in range(len(listdata)) :
            print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(NewData,listdata[i]['Code Mobil'],listdata[i]['Jenis Mobil'],listdata[i]['Pembuat'],listdata[i]['Type'],listdata[i]['Stock']))
    elif x == 2:
        for i in range(len(listdata)) :
            print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(listdata[i]['Code Mobil'],NewData,listdata[i]['Jenis Mobil'],listdata[i]['Pembuat'],listdata[i]['Type'],listdata[i]['Stock']))
    elif x == 3:
        for i in range(len(listdata)) :
            print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(listdata[i]['Code Mobil'],listdata[i]['Jenis Mobil'],NewData,listdata[i]['Pembuat'],listdata[i]['Type'],listdata[i]['Stock']))
    elif x == 4:
        for i in range(len(listdata)) :
            print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(listdata[i]['Code Mobil'],listdata[i]['Jenis Mobil'],listdata[i]['Pembuat'],NewData,listdata[i]['Type'],listdata[i]['Stock']))
    elif x == 5:
        for i in range(len(listdata)) :
            print('\t{}\t|  {} \t| {} \t| {} \t| {} \t'.format(listdata[i]['Code Mobil'],listdata[i]['Jenis Mobil'],listdata[i]['Pembuat'],listdata[i]['Type'],NewData,listdata[i]['Stock']))

# Fungsi Update Kendaraan Sesuai Kolom
def UpdateBarang(Data, Kolom,Newdata2):
    InputUpdateBarang= (input("\t Apakah Data Yang Diupdate Benar? (Yes/No): ")).lower()
    if InputUpdateBarang == "Yes":
        Data[0][Kolom] = Newdata2
        print("\tData Sudah Diperbarui")
    else:
        print("\tData Tidak Terupdate")

# Fungsi Filter Dict Dalam List 
def SearchList(input):
    SearchList = (list(filter(lambda data: data['Code Mobil'] == str(input), Daftarmobil)))
    return SearchList

# Fungsi Membaca Daftar
def Read():
    inputRead = (int(input('''
        Menu Menampilkan Daftar:
            1. Tampilkan Semua
            2. Mencari
            3. Kembali Ke Menu Utama
        Masukkan Angka Menu Yang Ingin DIjalankan:''')))
    if inputRead == 1 and len(Daftarmobil):
        Showlist(Daftarmobil)
    elif inputRead == 2 and len(Daftarmobil):
        CarCode = (input("\tMasukkan COde Yang Ingin Dicari: "))
        SearchList(CarCode)
        if len(SearchList(CarCode)):
            Showlist(SearchList(CarCode))
        else:
            print("\n\t Tidak Ada Data")
    elif inputRead == 3:
        Menu()
    else:
        print("\n\t Tidak Ada Data")
    Read()
    
# Fungsi Menambah Daftar
def Add():
    inputAdd = (int(input('''
        Menu Menambah Daftar:
            1. Menambah Daftar
            2. Kembali Ke Menu                                                                             
        Masukkan Angka Menu Yang Dijalankan''')))
    if inputAdd == 1:
        AddCarCode = (input("\n\tMasukkan Code Mobil Baru:"))
        ListValue = [value for DataMobil in "DaftarMobil" for value in DataMobil]
        if AddCarCode in ListValue:
            print("\n\tData Sudah Ada")
        else:
            JenisBaru = (input("\tSilahkan Masukkan Jenis Mobil:"))
            pembuatbaru = (input("\tSilahkan Masukkan Asal Pembuat:"))
            TypeBaru = (input("\tSilahkan Masukkan Type Baru:"))
            StockBaru = (input("\tSilahkan Masukkan Stock Baru:"))
            DaftarmobilBaru=[{
                'Code Mobil' : AddCarCode,
                'Jenis Mobil' : JenisBaru,
                'Pembuat' : pembuatbaru,
                'Type' : TypeBaru,
                'Stock' : StockBaru
            }]
            Showlist(DaftarmobilBaru)
            save = (input("\n\t Simpan Data (Yes/No)?")).lower()
            if save == "Yes":
                Daftarmobil.extend(DaftarmobilBaru)
                Showlist(Daftarmobil)
                print("\n \tData Mobil Baru Tersimpan")
            else:
                print("\n \t Data Tidak Tersimpan")
    
# Fungsi Merubah Daftar
def Update():
    inputUpdate = (int(input('''
        Menu mengubah daftar mobil:
            1. Mengubah daftar mobil
            2. kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputUpdate == 1:
        Showlist(Daftarmobil)
        UpdateCar = (input("\n\tMasukkan Code Mobil yang ingin dirubah"))
        listvalue = [value for datamobil in Daftarmobil for value in datamobil.values()]
        if UpdateCar not in listvalue:
            print("\n\t Data yang ingin dirubah tidak tersedia")
            Update()
        else:
            SearchList(UpdateCar)
            Showlist(SearchList(UpdateCar))
            inputUpdate = (input("\tUpdate data berikut? (yes/no): ")).lower()
            if inputUpdate== "yes":
                inputKategori = int(input('''
                    \tKategori database mobil:
                        1. Code Mobil
                        2. Jenis Mobil
                        3. Pembuat
                        4. Type
                        5. Stock              
                    Masukkan Kategori yang ingin dirubah: '''))
            if inputKategori == 1:
                MasukkanData = input("\tMasukkan data baru: ")
                ShowListUpdate(SearchList(UpdateCar),1,MasukkanData)
                UpdateBarang(SearchList(UpdateCar), "Code Mobil",MasukkanData)
            elif inputkategori == 2:
                MasukkanData = input("\tMasukkan data baru: ")
                ShowListUpdate(SearchList(UpdateCar),2,MasukkanData)
                UpdateBarang(SearchList(UpdateCar), "Jenis Mobil",MasukkanData)
            elif inputkategori == 3:
                MasukkanData = input("\tMasukkan data baru: ")
                ShowListUpdate(SearchList(UpdateCar),3,MasukkanData)
                UpdateBarang(SearchList(UpdateCar), "Pembuat",MasukkanData)
            elif inputkategori == 4:
                MasukkanData = input("\tMasukkan data baru: ")
                ShowListUpdate(SearchList(UpdateCar),4,MasukkanData)
                UpdateBarang(SearchList(UpdateCar), "Type",MasukkanData)
            elif inputkategori == 5:
                MasukkanData = input("\tMasukkan data baru: ")
                ShowListUpdate(SearchList(UpdateCar),1,MasukkanData)
                UpdateBarang(SearchList(UpdateCar), "Stock",MasukkanData)
            else:
                print("\tkategori tidak ada")
    elif inputUpdate == 2:
        Menu()
    Update()

# Fungsi Menghapus Daftar
def Delete():
    inputDel = (int(input('''
        Menu menghapus daftar Mobil:
            1. menghapus daftar Mobil:
            2. kembali ke menu utama:
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputDel == 1:
        Showlist(Daftarmobil)
        DelCarCode = (input("\n\tMasukkan Code Mobil Mobil yang ingin dihapus"))
        listvalue2 = [value2 for datamobil in Daftarmobil for value2 in datamobil.values()]
        if DelCarCode not in listvalue2:
            print("\n\tData yang ingin anda hapus tidak ada")
        else:
            SearchList(DelCarCode)
            Showlist(SearchList(DelCarCode))
            hapus = (input("\n\t Hapus data (yes/no)? ")).lower()
            if hapus == "yes":
                for e in SearchList(DelCarCode) :
                    Daftarmobil.remove(e)
                print("\n\t Data berhasil terhapus")
            else:
                print("\n\t Data tidak berhasil dihapus")
    elif inputDel == 2:
        Menu()
    Update()

# Fungsi Meminjam Daftar
def Borrow():
    inputBorrow = (int(input('''
        Menu Meminjam mobil:
            1. meminjam mobil
            2. kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan''')))
    if inputBorrow == 1:
        Showlist(Daftarmobil)
        while True:
            inputBor = (input("\n\tMasukkan Code Mobil yang ingin anda pinjam:"))
            listvalue3 = [value3 for datamobil in Daftarmobil for value3 in datamobil.values()]
            if inputBor not in listvalue3:
                print("\n\tMobil yang ingin anda pinjam tidak tersedia")
                Borrow()
            else:
                print("\t Data mobil yang ingin di pinjam")
                var = SearchList(inputBor)
                Showlist(var)
                tambahkan = (input('\n\tTambahkan daftar mobil kedalam keranjang? (yes/no):')).lower()
                if tambahkan := 'yes':
                    Qty = int(input('\t Berapa mobil yang ingin dipinjam?'))
                    if Qty > var[0]['Stock']:
                        print("\n\tMohon maaf stock tidak cukup")
                    else:
                        Cart.append({'jenis': (var[0]['jenis']),
                    'Qty' : Qty,
                    'code' : (var[0]['code'])
                    }),
                else:
                    print("\n\tKeranjang tidak terupdate")
                    Cart.clear()
                    Borrow()
            Cartfung(Cart)
            checker = (input("\n\tmau pinjam mobil lain? (yes/no):")).lower()
            if (checker == "yes") :
                True
            else:
                break

        Cartfung(Cart)
        checkout = (input("\n\tmau pinjam mobil lain? (yes/no): ")).lower()
        if checkout == "no":
            print("\ttidak jadi meminjam")
            Borrow()
        elif checkout == "yes":
            global NoPinjaman
            NamaPeminjam = (input("\tMasukkan nama peminjam"))
            print(f"""\t\n ========== No Pinjaman anda adalah: {NoPinjaman} ==========""")
            NoPeminjam = NoPinjaman
            NoPinjaman+= 1
            penampungansementara = {"No Pinjaman": NoPeminjam, "nama peminjam": NamaPeminjam}
            for item in range(len(Cart)):
                Cart[item].Update(penampungansementara)
            DataBasePeminjam.extend(Cart)
            print("\n\n\t xxxxx pengembalian mobil 1 hari dari sekarang xxxxx \n\n\t xxxxx selamat berkendara xxxxx")
            for item in Cart:
                (SearchList(item['Code Mobil']))[0]['stock']-=item['Qty']
            print("\n\t info : stock mobil terupdate")
        else:
            Cart.clear()
        
        Cart.clear()
        Showlist(Daftarmobil)
        print("\n")
        Database(DataBasePeminjam)
    elif inputBorrow == 2:
        Menu()
    Borrow()

# Fungsi Mengembalikan
def returnCar():
    inputreturn = (int(input('''
        Menu mengembalikan mobil:
            1. mengembalikan mobil
            2. kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputreturn == 1:
        Database(DataBasePeminjam)
        while True:
            inputRet = int(input("\n\tMasukkan no pinjaman untuk mengembalikan mobil"))
            listvalue4 = [value4 for datapeminjam in DataBasePeminjam for value4 in datapeminjam.values()]
            if inputRet not in listvalue4:
                print("\n\tNo pinjaman tidak tersedia")
                returnCar()
            else:
                print("\t data mobil yang ingin dikembalikan")
                SearchList4= (list(filter(lambda data: data['NoPinjaman'] == (inputRet), DataBasePeminjam)))
                Database(SearchList4)
                hapus1 = (input('\n\t kembalikan semua mobil? (yes/no):')).lower()
                if hapus1 == 'yes':
                    for item in SearchList4:
                        (SearchList(item['code']))[0]['stock']+=item['Qty']
                        DataBasePeminjam.remove(item)
                    print("\n\t xxxxx mobil sudah dikembalikan xxxxx")
                    print("\n\t info : stock mobil terupdate")
                else:
                    print("\n\t Mobil belum kembali")
                    returnCar()
            checker = input('\t mau kembalikan mobil lain? (yes/no):')
            if (checker == 'yes') :
                True
            else:
                print("\n\t *** terimakasih dan sampai jumpa ***")
                break
    elif inputreturn == 2:
        Menu()
        returnCar()
            
# Fungsi Menu Utama
def Menu():
    while True :
        pilihanMenu = input('''
        Selamat Datang Di Rental Dimpi

        List Menu :
        1. Menampilkan Daftar
        2. Menambah Daftar
        3. Mengubah Daftar
        4. Menghapus Daftar
        5. Meminjam
        6. Mengembalikan
        7. exit

        Masukkan Angka Menu Yang Ingin Dijalankan : ''')

        if(pilihanMenu == '1') :
            Read()
        elif(pilihanMenu == '2') :
            Add()
        elif(pilihanMenu == '3') :
            Update()
        elif(pilihanMenu == '4') :
            Delete()
        elif(pilihanMenu == '5') :
            Borrow()
        elif(pilihanMenu == '6') :
            returnCar()
        elif(pilihanMenu == '7') :
            exit()

# memanggil menu utama               
Menu()
  