 #*********table lookup method******(this one will take constant time if table is preprocessed)
	   # table = [0]*256
	    
	   # for i in range(1,256):
	   #     table[i] = (i&1) + table[i//2]
	        
	      
	   # return table[N & 0xff] + table[N>>8 & 0xff] + table[N>>16 & 0xff]+ table[N>>24 & 0xff]
	        
	    
	    
	   #*******brian kerningam algo (fastest if table has to be created in the table lookup method)
	   count = 0
	   
	   while N >0:
	       N = N & (N-1)
	       count+=1
	       
	   return count
	    
	    
	    
	    #*********simple approach	
# 		count = 0
# 		while N >0:
# 		    count += (N&1)
# 		    N = N>>1
		    
		
# 		return count
		
		
		
		# code here
# 		x = bin(N).replace("0b","")
		
# 		count = 0
# 		for i in x:
# 		    if i == "1":
# 		        count+=1

        
#         return count
