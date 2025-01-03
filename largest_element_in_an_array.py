from typing import List


class Solution:
    def largest(self, arr):
        l = arr[0]
        for num in arr:
            if num > l:
                l = num
        return l

