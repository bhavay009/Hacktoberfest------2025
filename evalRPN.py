class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for to in tokens:
            if to=="+":
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)

            elif to=="*":
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
               

            elif to=="/":
                b=stack.pop()
                a=stack.pop()
                stack.append(int(a/b)) 
              


            elif to=="-":
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b) 
              

            else:
                stack.append(int(to))    



        return stack[0]   
