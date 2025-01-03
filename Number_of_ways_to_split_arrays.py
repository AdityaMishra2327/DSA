class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = sum(nums)
        left , count = 0,0
        for i in range(n-1):
            left = left + nums[i]
            count = count + (2*left >=Sum)
        return count 
        
        
        
