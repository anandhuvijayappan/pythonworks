t=30
for i in range(1,t+1):
    for k in range(t-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2,):
        print("H",end="")
    print("")

#-----------------------------------

tll=(t//5)*6
width=t//2
r_width=t*3
for i in range(1,tll+1):
    print("".rjust(width," "),end="")
    for j in range(1,t+1):
        print("H",end="")
    print("".rjust(r_width," "),end="")
    for k in range(1,t+1):
        print("H",end="")
    print("")

#------------------------------------
bw=t*5
bh=t-2
width=t//2
for i in range(1,bh+1):
    print("".rjust(width," "),end="")
    for j in range(1,bw+1):
        print("H",end="")
    print("")

#--------------------------------------

tll=(t//5)*6
width=t//2
r_width=t*3
for i in range(1,tll+1):
    print("".rjust(width," "),end="")
    for j in range(1,t+1):
        print("H",end="")
    print("".rjust(r_width," "),end="")
    for k in range(1,t+1):
        print("H",end="")
    print("")
#----------------------------------

r_width=t*4
for i in range(t,0,-1):
    print("".rjust(r_width," "),end="")
    for k in range(t-i,0,-1):
        print(" ",end="")
    for j in range(1,i*2,):
        print("H",end="")
    print("")