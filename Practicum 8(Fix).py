####Activites 1, Practicum 8, by Donny Rizal 
Data = {'N' : 'NIM : L200183161', 'n' : 'Name : Donny Rizal Adhi Pratama','A' : 'Address : Rembang','Z' : 'Zip Code : 59218','J' : 'Job : Student','H' : 'Hobby : Nothing','S' : 'Skill : Looking for something special',}
b = ("""
Pilihan yang tersedia:
b show the help button
N show your NIM
n show your name
A show your address
Z show your zip code
J show your job
S show your skill
H show your hobby
k to exit""")
print (b)
Njir = 0
while Njir != 'k':
    Njir = input('Your Choice :')
    if Njir in Data.keys():
        print (Data[Njir])
    elif Njir == 'b':
        print (b)
    else:
        print ('Unknown Call Funtion')
print ('This sesion has ended')

####Activites 2, Practicum 8, by Donny Rizal  
def ConversionTemp(C = 0, F = 0):
    'Conversion from Celcius to Fahrenheit'
    Temp = 0
    if (C == 0) and (F == 0):
        print ("Temp 0 Celcius is equal to 32 Fahrenheit")
    elif (C == 0) and (F != 0):
        Temp = (F - 32) * 5/9
        print ("Temp", F, "Fahrenheit is equal to", int(Temp), "Celcius")
    elif (C != 0) and (F == 0):
        Temp = (C * 9/5) + 32
        print ("Temp", C, "Celcius is equal to", int(Temp), "Fahrenheit")
ConversionTemp(F=50)
ConversionTemp(C=84)
