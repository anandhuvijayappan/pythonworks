def student_info(*args,**kwargs):

    if kwargs.get("op")=="avg":

        return (sum(args))/len(args)
    
    if kwargs.get("op")=="total":

        return sum(args)



print(student_info(45,43,44,op="avg"))

print(student_info(45,43,44,op="total"))
