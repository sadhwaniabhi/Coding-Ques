class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        a=set(nums)
        flag=0

        if len(a) != l:
            flag=1
            
        return flag
