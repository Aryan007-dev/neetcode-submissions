class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s:
            if c.isalnum():
                filtered += c.lower()
        p1 = 0
        p2 = len(filtered)-1
        for i in range(len(filtered)):
            if(p1>p2):
                break
            if (filtered[p1]==filtered[p2]):
                p1=p1+1
                p2=p2-1
            else:
                return False    
            
            
        return True        

                    