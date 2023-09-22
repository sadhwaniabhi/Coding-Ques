# We have to find if the given two strings are anagram or not.
# I/P -> s = anagram         s = cat
#        t = agraman         t = rat
# O/P -> True                False

######Solution###########
"""
1st Approach (using Two hashtables)

    -> First thing is to check if the len of both the strings is equal or not, if not then return False
        and if equal then we will poceed with other steps.
    -> For each string we can count the number of occurences for each character and store them in
        a hashtable, where characters will be the key and there count will be value.
    -> Then we will have two hashtables which can be used to compare characters of both the strings.
    -> As we have both the strings of same length, so we can traverse through hashtable of any one 
        string and we will check if the key of hash1 is present in hash2, if yes then we will compare it's value. 
        if the value is not equal we will return false and the loop will end.
    -> At the end of the loop if no return false was triggered then we will return true.
    -> TC = O(n) and SC = O(n)
    
"""
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    hash1 = {}
    hash2 = {}

    for i in range(len(s)):
      hash1[s[i]] = 1 + hash1.get(s[i],0)
      hash2[t[i]] = 1 + hash2.get(t[i],0)


    for n in hash1:
      if hash1[n] != hash2.get(n,0):
        return False

    return True


"""
2nd Approach (using only one Hashtable)

    -> The idea is to add one for each character in string 1 and subtract 1 for each character 
       in string 2, if the same characters are there in both the strings then at the end of the loop
       for each character in hash table the value for all the keys will be zero.
    -> if not then return false else return true
    -> TC - O(n) and SC - O(n)

"""

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    hash_t = {}
    for i in range(len(s)):
      hash_t[s[i]] = 1 + hash_t.get(s[i],0)
      hash_t[t[i]] = hash_t.get(t[i],0) - 1

    for k in hash_t:
      if hash_t[k] != 0:
        return False
      
    return True


"""
3rd Approach (Using Sorting- Constant Space Complexity)
    -> If we are asked to use constant space to solve this problem then it can also be done.
    -> We can use the sorting method to solve this problem in constant space but the code will not be 
       that efficient.
    -> Generally it is considered that sorting doesn't take extra memory so SC - O(1)
    -> And a good sorting algo in worst case would take nlogn time so , TC - O(nlogn) 

"""

class Solution:
  def isAnagram(self, s : str, t : str) -> bool:
    return sorted(s) == sorted(t)
