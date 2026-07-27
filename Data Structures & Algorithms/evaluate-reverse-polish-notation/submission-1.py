class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expressions=["+","-","*","/"]
        for i in range(len(tokens)):
            if tokens[i] not in expressions:
                stack.append(tokens[i])
            else:
                ele1=int(stack.pop())
                ele2=int(stack.pop())
                if tokens[i]=="+":
                    res = ele1+ele2
                    stack.append(res)
                elif tokens[i]=="-":
                    res = ele2-ele1
                    stack.append(res) 
                elif tokens[i]=="*":
                    res = ele1*ele2
                    stack.append(res) 
                elif tokens[i]=="/":
                    res = int(ele2/ele1)
                    stack.append(res)          
        return int(stack[-1])