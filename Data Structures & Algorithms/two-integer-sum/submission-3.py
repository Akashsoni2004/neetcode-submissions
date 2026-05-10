class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i, num in enumerate(nums):
            h[num]=i
        
        for i, num in enumerate(nums):
            diff=target-num
            if diff in h and h[diff] != i:
                return [i,h[diff]]
            h[num]=i

