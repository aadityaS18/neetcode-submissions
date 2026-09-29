class MinStack:

    def __init__(self):
        self.stack=[]

        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minStack[-1]if self.minStack else val) 
    # Store the minimum value at this stack dept
        self.minStack.append(val)
        

    def pop(self) -> None:    # Remove from both stacks so they stay synchronized
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:# Return normal stack top
        return self.stack[-1]
        

    def getMin(self) -> int:# Return min normal stack top
        return self.minStack[-1]
        
