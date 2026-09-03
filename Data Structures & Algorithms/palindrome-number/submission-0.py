class Solution:
    def isPalindrome(self, x: int) -> bool:
        div = 10
        
        if x<0 :return False
        if x < 10:
            return True
        while x>=div*10:
            div = div*10
        while x:
           r = x%10
           l = x//div
           if r!=l: return False
           x = (x%div)//10
           
           div=div//100
        return True   


