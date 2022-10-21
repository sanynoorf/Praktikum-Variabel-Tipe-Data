#!/usr/bin/env python
# coding: utf-8

# <h1>Praktikum Variabel & Tipe Data</h1>
# 
# <h3>Soal 1</h3>
# Kiki belanja ke alf$$a M$a$r$t membeli 3 hepitos, 2 silperkuin, telor 2kg, beras 5kg, isi ulang akua galon seharga Rp 13.000. Harga hepitos yaitu Rp 15.000, telor Rp 13.000/kg, silperkuin Rp 21.000 beras kemasan 2.5kg seharga Rp 20.000. Toko tersebut memberikan discount 5%, ketika customer membeli makanan lebih dari 3 jenis. Berapakah total bayar belanjaan dari Kiki?
# 

# <h1>Analyze Here</h1>
# .....

# In[1]:


#Code here
a = hepitos = 15000 * 3
b = silperkuin = 21000 * 2
c = telor = 13000 * 2
d = beras =  20000 * 2.5 * 2
e = galon = 13000

totalharga = a + b + c + d + e 
discound = totalharga * 0.05
hasilBelanja_setelah_discound = totalharga - discound
print ("Total Harga Belanja :",totalharga)
print ("Harga Setelah Discound :",discound)
print ("Total Belanja Yang Harus Di Bayar :",hasilBelanja_setelah_discound)


# <h3>Soal 2</h3>
# Roni menabung pada bulan agustus yaitu setiap tanggal ganjil sejumlah Rp 50.000, setiap tanggal genap sejumlah RP 10.000 dan setiap tanggal kelipatan 5 sejumlah Rp 5.000, Berapakah total tabungan Roni diakhir bulan?

# <h1>Analyze Here</h1>
# .....

# In[2]:


#Code here
#BULAN AGUSTUS ADA 31 HARI
total_hari = 31
total_tabungan = 0

tanggal = 1
while (tanggal <= total_hari) :
    
    if (tanggal % 5 == 0):
        total_tabungan += 5000
    elif (tanggal % 2 != 0):
        total_tabungan += 50000
    else :
        total_tabungan += 10000
                
    tanggal += 1
    
print ("Jumlah Tabungan Selama Agustus :",total_tabungan)


# <h3>Soal 3</h3>
# Saat hari raya, Deni ingin menukarkan uang sejumlah Rp 5.000.000 ke pecahan 20rb, 10rb, 5rb, 2rb. berapa jumlahnya yang didapatkan Deni jika 20rb maksimal 100, 10rb maksimal 50.Jika :
# <ol>
#     <li>3(a)Semua pecahan harus ada</li>
#     <li>3(b)Hanya pecahan 20rb, 10rb dan 5rb</li>
#     <li>3(c)Hanya pecahan 20rb, 10rb dan 2rb</li>
# </ol>

# <h1>Analyze Here</h1>
# .....

# In[3]:


#Code here
# A
pecahan_20 = 20_000 * 100
pecahan_10 = 10_000 * 50
pecahan_5 = 5000 * 400
pecahan_2 = 2000 * 250
Total_3_A = pecahan_20 + pecahan_10 + pecahan_5 + pecahan_2

print("SEMUA PECAHAN HARUS ADA")
print("100 Lembar 20 Ribu :",pecahan_20)
print("50 Lembar 10 RB :",pecahan_10)
print("400 Lembar 5 RB :",pecahan_5)
print("250 Lembar 2 RB :",pecahan_2)

#B
pecahan_20 = 20_000 * 100
pecahan_10 = 10_000 * 50
pecahan_5 = 5000 * 400
pecahan_2 = 2000 * 250
rupiah_5_2 = 5000 * 500 
Total_3_B = pecahan_20 + pecahan_10 + rupiah_5_2

print("HANYA PECAHAN 20RB 10RB DAN 5RB")
print("100 Lembar 20RB :",pecahan_20)
print("50 Lembar 10RB :",pecahan_10)
print("500 Lembar 5RB :",pecahan_5)
print("Harga Yang Herus Di Bayar :",Total_3_B)

#C
pecahan_20 = 20_000 * 100
pecahan_10 = 10_000 * 50
pecahan_5 = 5000 * 400
pecahan_2 = 2000 * 250
rupiah_2_2 = 2000 * 1250 
Total_3_C = pecahan_20 + pecahan_10 + rupiah_2_2

print("HANYA PECAHAN 20RB, 10RB DAN 2RB")
print("100 Lembar 20RB :",pecahan_20)
print("50 Lembar 10RB :",pecahan_10)
print("1250 Lembar 2RB :",rupiah_2_2)
print("Harga Yang Harus Di Bayarkan :",Total_3_C)


# <h3>Soal 4</h3>
# Berapakah hasil dari (10/23-6+4-(20//3%2)) ?
# Lakukan analisa perhitungan dari hasil tersebut!
# Berdasarkan hasil tersebut urutkan operator yang dikerjakan!

# <h1>Analyze Here</h1>
# .....

# In[4]:


#Code here
hasil = (10/23-6+4-(20//3%2)) 
print("hasil dari  (10/23-6+4-(20//3%2)) =",hasil)
print("hasil analisa")

oprator_bagi_kurang = 10/23-6
oprator_bagi_sisabagi = 4-(20//3%2)

print("1. terdapat oprator bagi dan kurang = 10/23 - 6 =",oprator_bagi_kurang)
print("2. terdapat oprator pembagian pembulatan dan bagi = 4-(20//3%2)",oprator_bagi_sisabagi)
print("HASIL SETELAH DI TAMBAHKAN :",oprator_bagi_kurang + oprator_bagi_sisabagi)


# <h3>Soal 5</h3>
# Jika terdapat string yaitu "UFLOPYXTKJACSWRBGQZVDMEHIN", maka susunlah nama kalian masing-masing dari data tersebut, berdasarkan index dari masing-masing huruf yang ada pada string tersebut!
# 

# <h1>Analyze Here</h1>
# .....

# In[14]:


#Code here
huruf = str("UFLOPYXTKJACSWRBGQZVDMEHIN")
nama = "ARULMAULANASIDIK"
print(huruf[10]+huruf[14]+huruf[0]+huruf[2]+huruf[21]+huruf[10]+huruf[0]+huruf[2]+huruf[10]+huruf[25]+huruf[10]+huruf[12]+huruf[24]+huruf[20]+huruf[24]+huruf[8])


# In[ ]:




