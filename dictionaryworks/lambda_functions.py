# lambda functions 


#add two numbers

add=lambda num1,num2:num1+num2

print(add(10,100))

#find the cube of a number

cube=lambda num:num**3

print(cube(8))


#find the max

max=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print("The max : ",max("rakhav","sreehari"))

#find the min

min=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print("The min : ",min("rakhav","sreehari"))




