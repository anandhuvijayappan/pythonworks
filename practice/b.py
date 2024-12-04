string="ABCDCDC"
sub_string="CDC"
    
sub_len=len(sub_string)
s_string=""
for i in string:
    s_string=s_string+i
    if s_string==sub_string:
        repeat=repeat+1
    if sub_len<len(s_string):
        l=list(s_string)
        l.pop(0)
        s_string=''.join(l)
        if s_string==sub_string:
            repeat=repeat+1
print(repeat)