r_number="XC"

number=0

length=len(r_number)

sec_last=False

jump = False

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

        number+=1000
            
    if r_number[i]=="D":

        number+=500
            
    if r_number[i]=="C":

        if sec_last == False:

            if r_number[i+1]=="M":

                jump=True

                number+=900
            
            elif r_number[i+1]=="D":

                jump=True

                number+=400
            
            else :

                number+=100

        elif sec_last == True:

            number+=100
        
            
    if r_number[i]=="L":

        number+=50
            
    if r_number[i]=="X":

        if sec_last == False:
            
            if r_number[i+1]=="C":

                jump=True

                number+=90
            
            elif r_number[i+1]=="L":
                
                jump=True

                number+=40
            
            else :

                number+=10

            
        elif sec_last == True:

            print("OK")
            number+=10
            
    if r_number[i]=="V":

        number+=5
            
    if r_number[i]=="I":

        if sec_last == False:

            if r_number[i+1]=="X":

                jump=True

                number+=9
            
            elif r_number[i+1]=="V":

                jump=True

                number+=4
            
            else :

                number+=1
        
        elif sec_last == True:

            print("OK")
            number+=1
            
print(number)