class Solution:
    
    # ================= Solution 1 ======================== #
    # Overall a much cleaner solution in my opinion and is something more plausible for me
    def isValid(self, s: str) -> bool:
        # Have a dict and if its a LHS bracket put it on stack
        # Else if its a RHS bracket try to find its matching bracket
        # based on the stack
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0
    
    # ================= Solution 1 ======================== #
    # A solution that is simialr to the first one but just a bit more lines of code
    def isValidV2(self, s: str) -> bool:
        matches = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        stack = []

        for bracket in s:
            if bracket not in matches:
                stack.append(bracket)
            else:
                if stack and stack[-1] == matches[bracket]: # If the stack exists and the last value matches the bracket
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True