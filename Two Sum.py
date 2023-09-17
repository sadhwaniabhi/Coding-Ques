"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

###SOLUTION###

"""

***Brute force Approach (TC = O(n^2), SC = O(1))***
-> The approach is to compare each element to all the other elements of array and check if they add up to target
-> We can use two for loops to find two numbers from list whose sum is equal target.
-> We will run first loop from 0 - (len(list) -1) and second loop will run from 1 - (len(list)-1)

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for  j in range(i+1,len(nums)):
          if target - nums[j] == nums[i]:
            return [i,j]
                  
"""

***Optimized appraoch using Hashmap and two for loops(TC = O(n), SC = O(n))***
-> We will create a hashmap using for loop where array items will be keys and there index will be values.
-> We will use one more for loop and pass traverse the array and find z ( z= target - array element),
   where index of z should not be equal to index of array element. if yes, then return the index of z and index of array element.

"""
class Solution:
  def twosum(self, nums: List[int], target: int) -> List[int]:
      hash = {}
      for i,v in enumerate(nums):
        hash[v] = i

      for i,v in enumerate(nums):   
        z = target -v 
        if z in hash and i != hash[z]:
            return [i,hash[z]]


"""

***Optimized hashmap approach with one for loop(TC = O(n), SC = O(n))***
-> Improving the last approach, instead of creating the hashmap first and then traversing the array we will keep the hashmap empty.
-> then traverse through array element and find z (z = target - array element), if z exist in hash then return index of z 
   and index of array element otherwise we store the array element in hash with it's index as value

"""
class Solution:
  def twosum(self, nums: List[int], target: int) -> List[int]:
      hash = {}
      for i,v in enumerate(nums):
        z= target - v
        if z in hash:
            return [i,hash[z]]
        else:
            hash[v] = i
