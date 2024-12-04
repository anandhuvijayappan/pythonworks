text1="PQRST"

text2="ABCDEFGHIJKL"

text1_len=0

text2_len=0

merged=""

for i in text1:
    
    text1_len=text1_len+1

for i in text2:
    
    text2_len=text2_len+1

if text1_len<text2_len:

    g_len=text2_len

else:

    g_ind=text1_len

for i in range(0,g_len):

    if i<text1_len:

        merged=merged+text1[i]

    if i<text2_len:

        merged=merged+text2[i]

print(merged)