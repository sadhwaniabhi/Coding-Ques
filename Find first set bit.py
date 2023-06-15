"""Given an integer N. The task is to return the position of first set bit found from the right side in the binary representation of the number.
Note: If there is no set bit in the integer N, then return 0 from the function.  

Input: N = 18
Output: 2
Explanation: Binary representation of 
18 is 010010,the first set bit from the 
right side is at position 2.

"""

# ***Program***

"""the idea is simple we will use And and right shift bitwise operators for solving this problem"""
"""we will keep shifting bits of n to right by 1 and with each shift we will take n bitwise and of 1 
   and keep increasing the count with each shift and this will continue till n > 0
"""       
"""if output of n&1 is != 0, then we will return the count+1 (+1 for the current iteration) otherwise
   continue the interation by shifting n.
"""     
"""Time complexity is - O(logn) as max loop will run till n and we are reducing n by 2 each time"""

class Solution:
    def getFirstSetBit(self,n):
        count = 0
        while n > 0:
            if n&1 != 0:           # due to and operator the the number returned will be output greater than 0 only if there is a set bit in n
                return count+1
            else:
                count+=1
               
            n=n>>1                 #if we don't want to use shift operator, we can also divide by 2
            
        return 0                   # if the loop ends, then there was no set bit and output would be 0


