####Activites 1, Practicum 8, by Donny Rizal 
Data = {'NIM' : 'L200183161',
        'Name' : 'Donny Rizal Adhi Pratama',
        'Address' : 'Rembang',
        'Zip Code' : '59218',
        'Job' : 'Student',
        'Hobby' : 'Nothing',
        'Skill' : 'Looking for something special',}
print ("""
Pilihan yang tersedia:
b show the help button
N show your NIM
a show your name
A show your address
K show your zip code
j show your job
s show your skill
h show your hobby
k to exit""")
Njir = 0
while Njir != 'k':
    Njir = input('Your Choice :')
    if Njir == 'N':
        print ('Your Name is' , Data['NIM'])
    elif Njir == 'b':
        print ("""
The available choices:
b show the help button
N show your NIM
a show your name
A show your address
K show your zip code
j show your job
s show your skill
h show your hobby
k to exit""")
    elif Njir == 'a':
        print ('Your Name is:' , Data['Name'])
    elif Njir == 'A':
        print ('Your Address is in:' , Data['Address'])
    elif Njir == 'K':
        print ('Your ZIP Code is:' , Data['Zip Code'])
    elif Njir == 'j':
        print ('Your JOB is:' , Data['Job'])
    elif Njir == 's':
        print ('Your Skill is:' , Data['Skill'])
    elif Njir == 'h':
        print ('Your Hobby is:' , Data['Hobby'])        
    elif Njir == 'k':
        print ('This sesion has ended')
    else:
        print ('Unknown Call Funtion')

####Activites 2, Practicum 8, by Donny Rizal  
##def ConversionTemp(C = 0, F = 0):
##    'Conversion from Celcius to Fahrenheit'
##    Temp = 0
##    if (C == 0) and (F == 0):
##        print ("Temp 0 Celcius is equal to 32 Fahrenheit")
##    elif (C == 0) and (F == 0):
##        Temp = (F - 32) * 5/9
##        print ("Temp", F + "Fahrenheit is equal to", int(Temp), "Celcius")
##    elif (C != 0) and (F == 0):
##        Temp = (C * 9/5) + 32
##        print ("Temp", C, "Celcius is equal to", int(Temp), "Fahrenheit")
        

