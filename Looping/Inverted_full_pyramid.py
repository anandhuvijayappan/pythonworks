height=int(input("Enter the height of the pyramid : "))

for row in range(height,1,-1):

    spc=height-row

    for sp in range(1,spc):

        print(" ",end="")

    for col in range(1,row):

        print("* ",end="")

    print("")