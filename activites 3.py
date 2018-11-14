Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Practical 6, Activity 3, Donny Rizal Adhi Pratama, L200183161
>>> Name ='Donny Rizal Adhi Pratama'
>>> #This command put the name into value
>>> Name
'Donny Rizal Adhi Pratama'
>>> NIM = 'L200183161'
>>> #This command put the NIM data into value
>>> NIM
'L200183161'
>>> X ='1' + NIM[7:]
>>> #This command put the slice data NIM from 7 until the end and add the first number 1 into the line
>>> X
'1161'
>>> a = int(X)
>>> #This command change it into integer of X
>>> a
1161
>>> b = len(Name)
>>> #This command count how much the Name data
>>> b
24
>>> type(a)
<class 'int'>
>>> #this command check the type of each data we want check
>>> a
1161
>>> #this 'a' value is the data from Name that has added by '1' in the front of line
>>> b
24
>>> #this 'b' value is how much the data has been checked by length the data is
>>> type(b)
<class 'int'>
>>> #this command to check the type of data
>>> a/b
48.375
>>> #this command to devide a to b and the result is still float data
>>> a//b
48
>>> #this command to devide a and b, the result is integrated to down
>>> 10 * (a-999)
1620
>>> #this command is ten times (a-999) and the result is integer
>>> b ** 2
576
>>> #this command is 'b' square to 2
>>> a % b
9
>>> #this command is 'a' modulo 'b' and the remain is 9 becase of the devide function the remaining
>>> c = 12.5
>>> #this command add 'c' into the shell
>>> type(c)
<class 'float'>
>>> #this command to check the type of data and the result is float
>>> a / c
92.88
>>> #this command to check that 'a' devide 'c'
>>> a // c
92.0
>>> #this command to devide a to c but rounded down(integrated)
>>> a % c
11.0
>>> #this command to devide and the remaining result from modulo
>>> c > b
False
>>> #this command is (bool) and check there is a function 'true' or 'false'
>>> type (c > b)
<class 'bool'>
>>> #this is boolean (bool) and it is class boolean
>>> a > b and b > c
True
>>> #this command to check the function that require the data both of them are true
>>> a > 1100 or b < 10
True
>>> #this command to check the function that if the first one result can checked and so on
>>> 
