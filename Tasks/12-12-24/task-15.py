
def IsAddictiveNumber(sequence) -> bool:

    def helper(first,second,remaining):

        if len(remaining) < max(len(first), len(second)):

            return False
        if (first[0] == 0 and len(first) !=1) or (second[0] ==0 and len(second) !=1):

            return False
        
        first = int (first)
        second = int(second)
        res = str(first+second)
        len_res = len(res)

        if len(remaining) < len_res:

            return False
        
        if res == remaining[0:len_res]:

            if len(remaining) == len_res:

                return True
            first = second
            second = res
            remaining = remaining[len_res:]
            return helper (str(first), str(second),remaining)
        
    
        
    indx1 = 0

    for indx2 in range(indx1+1,len(sequence)):
        
        for indx3 in range(indx2+1,len(sequence)):

            first = sequence[indx1 : indx2]

            second = sequence[indx2 : indx3]

            remaining= sequence[indx3 : ]
            if helper(first, second, remaining):

                return True
            
    return False

sequence="199100199"

print(IsAddictiveNumber(sequence))
