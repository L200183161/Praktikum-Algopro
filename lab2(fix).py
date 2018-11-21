##Activities 1, Practicum 7, by Donny Rizal
Bangun = {'Triangle':'L = 0.5 * a * t',
          'Square' : 'L = s ** 2',
          'Rectangle' : 'L = p * l',
          'Circle' : 'L = phi * r ** 2',
          'Parallelogram' : 'L = a *t'}
print ('''
        -------------------------------------------
        | No|    Nama Bangun   | Rumus Luas        |
        |---|------------------|-------------------|
        | 1 |  Triangle        | %s   |
        | 2 |  Square          | %s        |
        | 3 |  Rectangle       | %s         |
        | 4 |  Circle          | %s  |
        | 5 |  Parallelogram   | %s          |
        --------------------------------------------  
'''%(Bangun['Triangle'], Bangun['Square'], Bangun['Rectangle'],
     Bangun['Circle'], Bangun['Parallelogram']))

####Activities 2, Practicum 7, by Donny Rizal
##A = 0
##while A<3:
##    X = input ('insert the password : ')
##    A = A+1
##    if X == 'Dunno':
##        print ('You have successful to login')
##        A = 3
##    if X != 'Dunno':
##        if A == 3:
##            print('Sorry, you have tried 3 times, Your accsess is blocked ')
##        else:
##            print('Sorry, the password is wrong')

####Activities 3, Practicum 7, by Donny Rizal
C = input('Insert Your Name : ')
D = float(input('What time is it now? : '))
if D >= 21.00 and D <=23.59 :
    D = 'Night'
elif D >= 17.30 and D <=20.59:
    D = 'Evening'
elif D >= 12.01 and D <=17.29:
    D = 'Afternoon'
elif D >= 11.00 and D <=12.00:
    D = 'Day'
elif D >= 0.00 and D <=10.59:
    D = 'Morning'
print('Good ' + D + ' ' + C + '!')



