s="RLRRRLLRLL"

r_count=0

l_count=0

sub_s=""

sub_strings=[]

for i in s:

    if i == "R":

        sub_s += "R"

        r_count += 1

    elif i == "L":

        sub_s += "L"

        l_count += 1

    if r_count==l_count and r_count!=0:

        sub_strings.append(sub_s)

        sub_s = ""

        r_count = 0

        l_count = 0

print(len(sub_strings))