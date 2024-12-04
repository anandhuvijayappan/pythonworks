#result=dict()

arr=[10,20,30,40,2,3,7,8,9]


#for i in arr:

#    result[i]=i**2  
    
result={num:num**3 for num in arr }

odd_cubes={i:i**3 for i in arr if i%2!=0}

even_squares={i:i**2 for i in arr if i%2==0}



print(result)

print(odd_cubes)

print(even_squares)