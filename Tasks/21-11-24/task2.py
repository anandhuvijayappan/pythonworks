word1="ab"
word2="pqrs"
output=""

word1_len=len(word1)
word2_len=len(word2)
greater_len=0

if word1_len < word2_len:

    greater_len = word2_len
else:

    greater_len = word1_len

for i in range(0,greater_len):

    if i < word1_len:

        output=output+word1[i]
    
    if i < word2_len:
        
        output=output+word2[i]

print(output)

