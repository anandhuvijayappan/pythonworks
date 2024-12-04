word1 = "abc"

word2 = "aebdc"

m= len(word1)

n= len(word2)

j = 0  

for i in range(n):

    if j < m and word1[j] == word2[i]:

        j += 1

result = False

if j == m:

    result=True

if result==True:

    print(word1," is a subsequence of ",word2)

else:
    
    print(word1," is not a subsequence of ",word2)
