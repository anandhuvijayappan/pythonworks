amount=5000
interest=10/(12*100) # monthly rate of interest
tenure=36 # number of months

emi=amount*interest*((1+interest)**tenure)/(((1+interest)**tenure)-1)


print(emi)