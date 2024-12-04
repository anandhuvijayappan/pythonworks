nums = [-4,-2,1,4,8]

closest=0

distence=0

num_s=sorted(nums)

if len(nums) == 0:

    print("This is an empty List")

else:

    for i in num_s:

        if distence==0:

            closest=i

            distence=abs(i)

        if abs(i) < distence:

            closest=i

            distence=abs(i)

        if abs(i) == distence:

            if closest < i:

                closest=i

                distence=abs(i)

    print(closest)