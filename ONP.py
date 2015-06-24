"""Algorithm for the below approach is as follows:

X is input string and Y is output string.
Step 1: Scan X from left to right until its end.
Step 2: If element is operand add to Y.
Step 3: If element is "(" push to stack.
Step 4: If element is operator:
    a.) Repeatedly pop from stack and add to Y each operator which has same or higher precendence than the element operator.
    b.) Add element operaor to stack.
Step 5.) If element is ")":
    a.) Repeatedly pop from stack & add to Y until "(" is encountered.
    b.) Remove "(" from the stack."""


operators=["+", "-", "*", "/", "^"]
precedence={"+":0, "-":1, "*":2, "/":3, "^":4}
alpha='abcdefghijklmnopqrstuvwxyz'

def preCheck(op1,op2):
    if precedence[op1]>=precedence[op2]:
        return True
    else: return False
    
def main():
    t=input()
    for i in range(t):
        X=raw_input()
        stack=[]
        Y=''
        for e in X:
            if e== "(":
                stack.append(e)
            elif e in alpha:
                Y+=e
            elif e in operators:
                while stack[-1] in operators:
                    if preCheck(stack[-1],e):
                        Y+=stack.pop()
                stack.append(e)
            elif e==')':
                while not stack[-1]=='(':
                    Y+=stack.pop()
                stack.pop()
            
        while not len(stack)==0:
            if stack[-1]=='(':
                stack.pop()
            else:
                Y+=stack.pop() 
                
        print Y
                       

main()