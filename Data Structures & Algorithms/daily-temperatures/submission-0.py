class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            num = temperatures[i]
            it = 0
            found = False
            for j in range(i+1,len(temperatures)):
                it=it+1
                
                if (temperatures[i]<temperatures[j]):
                    found = True
                    break
            if(found==False):
                it = 0        
            result.append(it)   
        return result         