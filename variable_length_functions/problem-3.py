def calculator(*args,**kwargs):

    if kwargs.get("op")=="+":

        return sum(args)

    if kwargs.get("op")=="*":

        product=1

        for i in args:

            product*=i

        return product

print(calculator(1,2,3,4,5,op="*"))

