def maxArea(height):
    left = 0
    right = len(height) - 1
    final = 0
    
    # Binary search for the heights
    # Always recalculate the area to see if its the max area
    # Note that we base it off the min height as if only one side is
    # taller it would not hold the water -> makes sense
    while left <= right:
        area_calc = abs(left - right) * min(height[left], height[right])
        final = max(final, area_calc)
        
        if height[left] < height[right]:
            
            left += 1
        else:
            right -= 1
    
    return final
        
if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))