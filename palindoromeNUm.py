class Solution:
    def isPalindrome(self, x: int) -> bool:
        test =x 
        palin =0
        while x > 0:
            residue= x%10 
            x=x // 10
            palin= palin*10+residue
        if palin == test: return True 
        else : return False
soluion = Solution()
num = input("Enter any number (integer): ")
passNumber=int(num)
print(soluion.isPalindrome(passNumber))

