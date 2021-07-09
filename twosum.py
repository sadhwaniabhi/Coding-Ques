class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        flag=False
        for index,j in enumerate(nums):
            z=target-j
            if z in arr:
                flag=True
                break
            else:
                arr.append(j)
                
        if flag:
            return [arr.index(z),index]
