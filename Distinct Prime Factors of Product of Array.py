"""
	-> If we multiply all number of the input array and find divisors of a single number then it will be a time taking process because the single number we get 	   will be very large, so instead we find divisors of every individual item in array and use a set to store those divisiors, so that we have distinct divisors
"""
"""
	***Brute force Approach (TC- O(n^2logn))***
	-> Simply will traverse from through array elements, and for each element we fill run a loop from i = 2 to n
	-> Then, we will check if i is prime or not and if it divides n or not, if yes then we will add i in set a created to store the divisors
	-> keep on dividing n by i till it's possible and then increment i by 1
"""

class Solution:
	def distinctPrimeFactors(self, nums: List[int]) -> int:
		def isprime(x):
			if x == 2 or x == 3:
				return 1
			if x%2 == 0 or x%3 == 0:
				return 0
			i = 5
			while i*i < x:
				if x%i == 0 or x%(i+2) == 0:
					return 0
				i+=6
			return 1

		a = set()
		for prod in nums:
			j = 2
			while prod>1:
				if prod %j == 0 and isprime(j):
					prod = prod//j   
					a.add(j)
				else:
					j+=1 

		return len(a)
	
	
"""
	***Optimized approach without checking seperatly for prime (TC- O(sqrt(n)logn))***
	-> We know that divisiors always appear in pairs: if n=12 -> (1,12), (2,6), (3,4). So, if there are two pairs x*y = n, and if x<=y, then x*x = n, 			   		  x = sqrt(n)
	-> Now, we can observe that we can always write a number in multiples of prime numbers, i.e. that is prime numbers can repeat more than once but they will   		divide the number totally
	-> if we follow this approach, then we can see if n = 12 : 2*2*2*3 -> 2^3 * 3^1
	-> if we find the first prime number which divides n then, we can continuously divide the n with that number and then increase the number till n becomes 1 or 		  can't be further divided.
"""

class Solution:
	def distinctPrimeFactors(self, nums: List[int]) -> int:
		a = set()
		for n in nums:
			j = 2
			while j*j <= n:
				while n%j ==0:
					a.add(j)
					n = n//j 

				j+=1

			if n >1:				# if n left is greater than 1, then this condition is used to return the last prime divisor
				a.add(n)

		return len(a)

"""
	*** More Optimized Approach (TC-O(sqrt(n))***
	-> If we see, if a number is divisible by 2 then it will be divisible by all even integers.
	-> Similarly, if a number is divisible by 3 then it will be divisible by all the multiples of 3
	-> If we check seperately for 2 and 3, then we can reduce many iterations for our loop
"""

class Solution:
	def distinctPrimeFactors(self, nums: List[int]) -> int:
		a = set()
		for n in nums:
			# loop to check if n is divisible by 2 and we will run a loop till it's divisible by 2
			while n%2 == 0:
				a.add(2)
				n=n//2
			# loop to check if n is divisible by 3 and we will run a loop till it's divisible by 3
			while n%3 == 0:
				a.add(3)
				n = n//3
				
			# now if we skip 2 and all even numbers and 3 and all it's multiples then we can start i from 5 and go till sqrt(n) 
			j=5
			while j*j <= n:                                # since in worst case this loop will go till sqrt(n) and this case will happen when n is prime
				while n%j ==0:
					a.add(j)
					n = n//j 

				while n%(j+2) == 0:
					a.add(j+2)
					n = n//(j+2)

				j+=6
				
			if n >3:					# because we have checked for 2 and 3 now, minimum value in the end for n will be >3
				a.add(n)
		return len(a)
