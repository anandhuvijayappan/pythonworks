text1="PQRS"

text2="ABCDE"

text1_len=0

text2_len=0

merged=""

text1_len=len(text1)

text2_len=len(text2)

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