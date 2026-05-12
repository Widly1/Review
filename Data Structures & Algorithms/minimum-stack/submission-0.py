class MinStack:

    def __init__(self):
        # initialize the regular stack and the 2nd stack to hold the min value as we go along
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # append to our regular stack
        self.stack.append(val)
        
        # check if our minstack is empty or not to determine our new min value 
        # get the current min value between our current val and our last val from minStack (which holds min values)
        # if it's not empty determine our new min value and push it to our min stack
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        # if minStack is empty then we just append the current val to minStack
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        # regular pop from our regular stack && our minStack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # to see the top value in our stack we just return the last value in the stack
        return self.stack[-1]


    def getMin(self) -> int:
        # now this function, which we created our 2nd stack for is going to return the last value added to our stack
        return self.minStack[-1]