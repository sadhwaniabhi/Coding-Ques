# Brute Force Approach
#-> We take first element of array and compare it with each and every element in that array
#-> For this we will use 2 for loops. For each element wer will traverse the array n times( where n is size of array).
#-> So total traversals will be n square. So, TC - O(n^2) , SC  - O(1) (Since no extra space is used)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                            return True

            return False

# Better approach
#-> If we sort the array, then we have to compare only two consicutive elements with each other instead of comparing with the whole array.
#-> sorting the array will take logn time
#-> and comparing two elements will take n comparisions so time taken will be n
#-> we will use two pointers to compare two consicutive elements

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f_p = 0        # first pointer
        s_p = 1       # second pointer
        nums = sorted(nums)

        while s_p < len(nums):
                if nums[f_p] == nums[s_p]:
                        return True

                f_p +=1
                s_p +=1
        return False


# Best Approach using a hashset
#-> We can compromise space complexity to improve the time taken
#-> Using a hashset, we will not need to compare elements 
#-> start from the first elements and check is that element is present in hashset if yes then return true, if not then add the element to set.
#-> adding the element in set takes O(1) time and to perfrom this operation for n elements  so.. .total time taken would be O(n)
#-> and Space complexity would be O(n) because we are creating an set which will in worst case will store all the elements in array and that means no duplicate element

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
                if i in hashset:
                        return True
                hashset.add(i)
 
        return False


# Bonus Approach
#-> instead of checking for each element when we use set we can just create a set from the nums array.
#-> compare the length of both array and set, if the length are same then no duplicates exists
#-> if length is not same then return True
#-> Space complexity will be O(n) and time complexity will be O(1) since just a single constant time operation is performing here

class Solution:
      def containsDuplicate(self, numsL List[int]) -> bool:
            nums_set = set(nums)

            if len(nums_set) != len(nums):
                return True
            
            return False
      
