users=["rahul","rohit","kohli","rishab","sanju","pandya"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

suggections=set(users).intersection(set(rahul_followers))

mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

print("rahul suggections : ",suggections)

print("Mutual friends : ",mutual_friends)



