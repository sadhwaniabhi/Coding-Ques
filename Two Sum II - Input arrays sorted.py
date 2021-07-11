class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        flag=0
        r=0
        l=len(numbers)-1
        while l>r:
            if numbers[r]+numbers[l] ==target:
                flag=1
                break
            elif numbers[r] + numbers[l] < target:
                r +=1
            else:
                l-=1

        if flag:
            return [r+1,l+1]
