start=int(input("start : "))

stop=int(input("stop  : "))

if start<stop :

    f=0

elif start>stop :

    f=1

if start==stop :

    print("There is no integer b/wn ",start," and ",stop)

else :

    if start<stop :

        f=0

    elif start>stop :

        f=1

    i = start

    while ((f==0 and i<=stop)or(f==1 and i>=stop)) : # while ( i<=stop if f==0 else i>=stop ) :# <- Also we can use 

        print(i," ")

        if f==0 :

            i=i+1

        elif f==1:

            i=i-1
