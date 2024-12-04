# 3. Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.

students_scores = {"Alice": 85,"Bob": 78,"Charlie": 92,"David": 88,"Eva": 95}

count=0

total=0

for i in students_scores.values():

    total=total+i

    count=count+1

average=total/count

print("Average of the score : ",average)