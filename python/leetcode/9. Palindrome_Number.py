def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        # reverse number logic
        temp=x
        rev_num=0
        while temp!=0:
            current=temp%10
            rev_num=rev_num*10+current
            temp=temp//10
        if rev_num==x:
            return True
        return False 
