 """
     ***Brute force Approach (TC - O(n^2))***
     We can use two for loops to find two numbers from list whose sum is equal target.
     We will run first loop from 0 - (len(list) -1) and second loop will run from 1 - (len(list)-1)
 """
 for i in range(len(nums)):
	for  j in range(i+1,len(nums)):
		if target - nums[j] == nums[i]:
			return [i,j]
             
"""
     ***Optimized appraoch using Hashmap and two pass(TC=O(n))***
     We will create a hashmap using for loop where array items will be keys and there index will be values.
     We will use one more for loop and pass traverse the array and find z ( z= target - array element) where index of z should not be equal to index of array element. if yes, then return the index of z and index of array element.
"""
  hash = {}
  for i,v in enumerate(nums):
    hash[v] = i
  for i,v in enumerate(nums):   
     z = target -v 
     if z in hash and i != hash[z]:
        return [i,hash[z]]

"""
     ***Optimized hashmap approach with one for loop(TC= O(n))***
     In these approach we use only one for loop where we create an empty hash and then traverse through array element and find z
     z = target - array element , if z exist in hash then return index of z and index of array element otherwise we store the array element in hash with it's index as value
"""
  hash = {}
  for i,v in enumerate(nums):
    z= target - v
    if z in hash:
        return [i,hash[z]]
    else:
        hash[v] = i
