from typing import List
def plusOne(digits: List[int]) -> List[int]:
    res=[]
    n=len(digits)
    num=0
    for i in range(len(digits)):
        num+=digits[i]*(10**(n-(i+1)))
    result=num+1
    for i in  str(result):
        res.append(int(i))
    print(res)
    

plusOne([9])