
year=int(input("Enter the year : "))

leap=False

if year%4==0:
        leap = True
        if year%100==0:
            leap = False
            if year%4==0:
                leap = True


if leap == True:
     print(year," is a leap year ;) ")
elif leap == False:
     print(year," is not a leap year ! ")
                