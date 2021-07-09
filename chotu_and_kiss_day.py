
#funtion
def help_chotu(s,l,k):
    for i in range(0,l-1):
        x=set()
        curr_sum=k-s[i]
        for j in range(i+1,l):
            if (curr_sum-s[j]) in x:
                return "YES"
            x.add(s[j])
    return "NO"

#inputs 
number=int(input())    #total no of places
Si=input()             #Si value of places
si_array=[]
for n in Si.split():
  si_array.append(int(n))

si_length=len(si_array)
k=int(input())        #total threat value of three places
