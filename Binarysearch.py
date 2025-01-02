from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid  # Target found, return the index
            
            # If the target is smaller, ignore the right half
            elif nums[mid] > target:
                right = mid - 1
            
            # If the target is larger, ignore the left half
            else:
                left = mid + 1
        
        return -1  # Target not found
