#Question: Given an array of integers and a number k, find the sum of all subarrays of size k.   

i=0
j=0  
res=[]
k=3
arr=[1,2,3,4,5,6,7,8,9]
windowsum=0
while j<len(arr):
    windowsum+=arr[j]
    if j-i+1<k:
        j+=1        
    elif j-i+1==k:
        res.append(windowsum)
        windowsum-=arr[i]
        i+=1
        j+=1   
print(res)   
