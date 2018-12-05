##Practicum 9, Activites 1, by Donny Rizal Adhi Pratama
berkas = open("L200183161","w")
berkas.write("L200183161 \n")
berkas.write("15-08-1999 \n")
berkas.write("Donny Rizal Adhi Pratama \n")
berkas.close()

##Practicum 9, Activites 2, by Donny Rizal Adhi Pratama
berkas = open("L200183161","w")
berkas.write("L200183161 \n")
berkas.write("15/08/1999 \n")
berkas.write("Donny Rizal Adhi Pratama \n")
berkas.write("Rembang \n")
berkas.close()

import shelve
a = open("L200183161","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Donny")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

a = shelve.open("Donny")

print (a['b'][0])
print (a['b'][1])
print (a['b'][2])
print (a['b'][3])

##Practicum 9, Activites 3, by Donny Rizal Adhi Pratama
import shelve
a = open("L200183161","r")
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
Kota = a.readline()
a.close()

a = shelve.open("Donny")
a['b'] = [Nama, Kota, TL, NIM]
a.close()

##Practicum 9, Activites 4, by Donny Rizal Adhi Pratama
import shelve
a = shelve.open("Donny")
print ("Nama :" , a['b'][0])
print ("Kota :" , a['b'][1])
print ("TL   :" , a['b'][2])
print ("NIM  :" , a['b'][3])
