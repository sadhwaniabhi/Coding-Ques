
""" QUESTION

Given a 1-indexed array of integers numbers that are already sorted in non-decreasing order, find two numbers such that they 
add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1, and index2, added by one as an integer array [index1, index2] of length 2.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers are sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.


"""

###SOLUTION###

"""
***First Approach using hashmap and one for loop(TC = O(n), SC = O(n))***
-> We will create a hashmap and keep it empty
-> then traverse through the array element and find z (z = target - array element), if z exists in hash then return the index of z 
   and index of array element otherwise we store the array element in hash with its index as value

"""
class Solution:
  def twosum(self, numbers: List[int], target: int) -> List[int]:
      hash = {}
      for i,v in enumerate(nums):
        z= target - v
        if z in hash:
            return [i,hash[z]]
        else:
            hash[v] = i



"""
***Using two pointers and Constant Space(TC = O(n), SC = O(1))***
-> Since we are asked to use constant space and the given array of numbers is sorted we can apply the binary search approach for
   finding the elements that add up to the target
-> We will use two pointers(first & last), one pointing to the first element and one to the last element of an array.
-> Now, if the sum of the first and last is greater than the target then we move the last pointer to the second last element and
   if the sum is less than the target sum then we will move the first pointer forward.
-> We will repeat these steps and keep checking till we get the numbers that add up to the target or
   value of first > than the value of last i.e. the pointers cross each other.
"""
class Solution:
   def twosum(self, numbers: List[int], target: int) -> List(int):
      first = 0
      last = len(numbers) - 1

      while first < last:
         
        if numbers[first] + numbers[last] == target:
           return [first+1, last+1]    #we have added 1 because in question it is given we have to consider array index from 1
         
        elif numbers[first] + numbers[last] > target:
           last -= 1
        
        else:
           first += 1
