string="anandhunjananandhunananandhunjananandhu"
sub_string="anandhu"
    
sub_len=len(sub_string)
#print(sub_len)
s_string=""
repeat=0
for i in string:
    s_string=s_string+i
    #print(s_string)
    if s_string==sub_string:
            repeat=repeat+1
    if sub_len<len(s_string):
        l=list(s_string)
        #print(l)
        l.pop(0)
        #print(l)
        s_string=''.join(l)
        #print("joined string : ",s_string)
        if s_string==sub_string:
            repeat=repeat+1
print("repeated ",repeat," times.")