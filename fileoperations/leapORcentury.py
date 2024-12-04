years=open("P:\\Luminar\\pythonworks\\dataset\\years_to-2024.txt")

century=open("P:\Luminar\pythonworks\dataset\century.txt","w")

leap=open("P:\Luminar\pythonworks\dataset\leap.txt","w")

def is_century_year(year):

    return True if year%100==0 else False

def is_leap_year(year):

    if year%100==0 and year%400==0 or year%100!=0 and  year%4==0:

        return True
    
    else:

        return False
    
for year in years:

    year=int(year)

    if is_century_year(year)==True:

        century.write(str(year)+"\n")
    
    if is_leap_year(year)==True:

        leap.write(str(year)+"\n")

leap.close()

century.close()

years.close()