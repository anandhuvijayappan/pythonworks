def swap_decorator(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return wrapper

@swap_decorator
def smart_sub(num1,num2):

    return num1-num2

@swap_decorator
def smart_div(num1,num2):

    return num1/num2

print(smart_sub(10,20))

print(smart_div(10,20))