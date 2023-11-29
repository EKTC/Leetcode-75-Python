# This version does work but its a bit messier
# It also uses up more space when we can just modify our result list
# To have the answer than create our postfix and prefix arrays
def product_except_self(nums):
    # There are two ways of doing this
    # Calculating the prefix and postfix and combining them into the final array
    prefix = []
    postfix = []
    for n in nums:
        if len(prefix) > 0:
            prefix.append(prefix[len(prefix)- 1] * n)
        else:
            prefix.append(n)
    
    # We need to reverse it as the last index is where it starts for postfix
    # And it goes to smaller indexs
    for n in nums[::-1]:
        if len(postfix) > 0:
            postfix.append(postfix[len(postfix)- 1] * n)
        else:
            postfix.append(n)
    # Reverse the final list as the order is reversed based on prefix
    postfix = postfix[::-1]
    
    # For each number
    # We grab its prefix and its postfix and multiply them to give the result
    # We have to check if that prefix / postfix exists before using its values
    
    final = []
    for x in range(0, len(nums)):
        print(x)
        pre = x - 1
        post = x + 1
        total = 1
        if pre >= 0:
            total *= prefix[pre]
        
        if post < len(nums):
            total *= postfix[post]
        final.append(total)

    return final
            
# Or we can just do both prefix and postfix together 
def product_except_self_v2(nums):
    result = [1] * (len(nums))

    
    # Sets up all the prefix values
    # The prefix value accumulates to get bigger each iteration
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # This is grabbing the last index and moving it in reverse by 1 step each time
    # postfix is the same as the prefix setup
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

if __name__ == "__main__":
    # print(product_except_self([1,2,3,4]))
    print(product_except_self([0,0]))