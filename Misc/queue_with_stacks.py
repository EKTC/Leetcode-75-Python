class MyQueue:

    # We initialise the two stacks 
    def __init__(self):
        self.enter = []
        self.exit = []

    # Push to the enter stack
    def push(self, x: int) -> None:
        self.enter.append(x)

    # We want to pop the first element that entered the queue 
    # But to utilise the two stacks and get an amortised time complexity 
    # We shall call peek function
    # After we call the peek funciton we can just remove the last element as that is the element we want to remove
    def pop(self) -> int:
        self.peek()
        return self.exit.pop()

    # When we call peek we transfer all the items in the inner stack to the outer stack
    # Where we will be removing
    # We return the first element which is at the end of hte list
    def peek(self) -> int:
        if self.exit == []:
            while self.enter != []:
                self.exit.append(self.enter.pop())
        return self.exit[-1]

    # Checks if there are no elements in either stacks
    def empty(self) -> bool:
        return self.enter == [] and self.exit == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()