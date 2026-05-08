class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        reserve=0
        for i in nums[::-1]:
            if i == reserve:
                return True
            else:
                reserve=nums.pop()
        if nums==[]:
            return False

        