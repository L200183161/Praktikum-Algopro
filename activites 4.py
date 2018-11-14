Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Jeneng ='Donny Rizal Adhi Pratama'
>>> #this command show Jeneng into a value
>>> NIM =161
>>> #this command show NIM into a value integer
>>> Tinggi = 1.70
>>> #this command show Tinggi into a value
>>> Berat = 100
>>> #this command show Berat into a value
>>> TahunLahir = 1999
>>> #this command show TahunLahir into a value
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Jeneng)

>>> #this command show Aku consist of TahunLahir, Berat, Tinggi, NIM, Jeneng into one line that called Aku as value
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Jeneng]
>>>  #this command show Data consist of tahun, berat, tinggi, NIM, Jeneng the samae as Aku and it called a list
>>> type(Aku)
<class 'tuple'>
>>>  #This command show the type of Aku is 'tuple' which is similar with list but the difference is tuple use parenthess(), but list using square brackets[]
>>> Aku[0]
1999
>>> #this command show the result from slicing Aku in first slice [0] is TahunLahir
>>> a = NIM % 4; Aku[a]
100
>>> #this command show that the new data a from the NIM % 4, and Aku[a] be something that merge into one and give the result from Aku[a] is from Slicing in Berat
>>> #this command show that the new data a from the NIM % 4, and Aku[a] be something that merge into one and give the result from Aku[a] is from Slicing in Berat
>>> type(Aku[a])
<class 'int'>
>>> #this slicing from Aku is 'Berat' which is an Integer result.
>>> Aku[a:4]
(100, 1.7, 161)
>>> #the slicing from Aku between a until 4 are Berat, Tinggi, NIM
>>> type(Aku[4])
<class 'str'>
>>>  #the slicing from Aku in 4 sequence is Jeneng. so the type of course a string
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #It cant be changed with that way. it should be something else.			Traceback (most recent call last):							File '<pyshell#26>', line 1, in <module>					 Aku(0) = 'ok'								TypeError: 'tuple' object does not support item assignment			----------------------------------------------------------
>>> type(Data)
<class 'list'>
>>> #This command show the type of Data is List which is similar with tuple but the difference is tuple use parenthess(), but list using square brackets[]
>>> Data[4]
'Donny Rizal Adhi Pratama'
>>> #this slicing is from Data that Slicing number 4
>>> Data[4][5]
' '
>>> #this is slice that sliced again so we can get the result from slicing, and the result after Donny is (Space) ' '
>>> Data[4][a:6]
'onny '
>>> #from the slicing we can get the result from slicing data[4] and from the a until 6 so the result is onny and one space 'onny '
>>> Data[0] = 'ok' ; Data
['ok', 100, 1.7, 161, 'Donny Rizal Adhi Pratama']
>>> #so the list can get the result to change it with another word or number or anything for example 'ok' changed in Data[0] and call the function the new Data again
>>> Data[-a]
'Donny Rizal Adhi Pratama'
>>> #this command from slice Data that write the function of Data[-a] is reversed from the normal data sequences
>>> range(a)
range(0, 1)
>>> #this command from data 'a  = NIM % 4; Aku[a]' the result is 1 so the range between is from 0 until the result of 'a'
>>> 
