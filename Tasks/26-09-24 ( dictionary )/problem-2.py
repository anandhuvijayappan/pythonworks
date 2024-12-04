# 2. Write a Python program to merge two dictionaries.

dictionary1={"A":"b","B":"b","C":"c","D":"d"}

dictionary2={1:1,2:4,3:9,4:16}

merged_dict=dict()

for i,j in dictionary1.items():

    merged_dict[i]=j

for k,v in dictionary2.items():

    merged_dict[k]=v

print(merged_dict)