def add_value(value):

    global number

    global previous

    global d

    global c

    global l

    global x

    global v

    global i

    if number==0:

        previous=value

        number+=value

        return True

    else:

        if (value < previous) or (value and previous==1000):

            previous = value

            number+=value


            return True
        
        elif (value and previous == 1) and i != 0:

            previous = value

            number+=value

            i-=1


            return True
        
        elif (value and previous == 5) and v != 0:

            previous = value

            number+=value

            v-=1


            return True
        elif (value and previous == 10) and x != 0:

            previous = value

            number+=value

            x-=1


            return True
        elif (value and previous == 50) and l != 0:

            previous = value

            number+=value

            l-=1


            return True
        elif (value and previous == 100) and c != 0:

            previous = value

            number+=value

            c-=1


            return True
        elif (value and previous == 500) and d != 0:

            previous = value

            number+=value

            d-=1


            return True
        
        else:

            return False



            





r_number = "MMMCMXXXXXXCIX"

number = 0

previous = 0

d = 2

c = 2

l = 2

x = 2

v = 2

i = 2

length = len(r_number)

sec_last = False

jump = False

valued = True

for i in range(0,length):

#   Checking for jump Eg: CM, CD, XL, XL, IX, IV
    if jump==True:

        jump=False

        continue
#   Checking for second last iteration
    if i==(length-1):

        sec_last=True

#   Finding the value and adding to the number
    if r_number[i]=="M":

        valued=add_value(1000)
            
    if r_number[i]=="D":

        valued=add_value(500)
            
    if r_number[i]=="C":

        if sec_last == False:

            if r_number[i+1]=="M":

                jump=True

                valued=add_value(900)
            
            elif r_number[i+1]=="D":

                jump=True

                valued=add_value(400)
            
            else :

                valued=add_value(100)

        elif sec_last == True:

            valued=add_value(100)
        
            
    if r_number[i]=="L":

        valued=add_value(50)
            
    if r_number[i]=="X":

        if sec_last == False:
            
            if r_number[i+1]=="C":

                jump=True

                valued=add_value(90)
            
            elif r_number[i+1]=="L":
                
                jump=True

                valued=add_value(40)
            
            else :

                valued=add_value(10)

            
        elif sec_last == True:

            valued=add_value(10)
            
    if r_number[i]=="V":

        valued=add_value(5)
            
    if r_number[i]=="I":

        if sec_last == False:

            if r_number[i+1]=="X":

                jump=True

                valued=add_value(9)
            
            elif r_number[i+1]=="V":

                jump=True

                valued=add_value(4)
            
            else :

                valued=add_value(1)
        
        elif sec_last == True:

            valued=add_value(1)
            
if valued == True:

    print(number)

elif valued == False:

    print("invalued")

        