matrix = [[1,2,3,4,5],
          [6,7,8,9,1],
          [2,3,4,5,6],
          [7,8,9,1,2]]

top=0
bottom=len(matrix)-1

left=0
right=len(matrix[1])-1



while top <= bottom and left <= right:
 
    for i in range(left, right + 1):

        print(matrix[top][i])

    top += 1 

    for i in range(top, bottom + 1):

        print(matrix[i][right])

    right -= 1 

    if top <= bottom: 
     
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i]) 

        bottom -= 1 

    if left <= right: 
     
        for i in range(bottom, top - 1, -1): 

            print(matrix[i][left]) 
            
        left += 1