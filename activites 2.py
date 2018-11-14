##Activites2
##Program Akun
##Dibuat oleh Donny L200183161
import random 
Nama = 'Donny Rizal Adhi Pratama'
TTL = 'Rembang, 15 Agustus 1999'
Shortname = Nama[0] + '.' + Nama[6] + '.' + Nama[12] + '.' + Nama[-7:]
Username = Nama[0] + TTL[9-11] + TTL[-4:]
Password = Nama[0:4] + str(random.randint(0,1000))