 def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

# Note that the edge cases are different if we use <= vs < for the conditions which makes sense as now the ranges are slightly different
# Just something interesting for myself to note ig and the presence of such small changes that really change the logic slightly
 def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        
        return -1
