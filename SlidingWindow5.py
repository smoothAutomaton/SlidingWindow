'''
🚀 Question

You are given an array of integers arr[] of size N, and two integers K and X.

Your task is to count how many contiguous subarrays of size exactly K have a sum Smaller than or equal to X.

If K > N, return 0.

📥 Input Format

An integer N → size of the array

An integer K → size of each subarray (window)

An integer X → minimum required sum

An array arr[] of N integers

📤 Output Format

A single integer →
the number of subarrays of size K whose sum is ≥ X
Input:
N = 7
K = 3
X = 7
arr = [2, 1, 5, 1, 3, 2, 8]

'''
N = 7
K = 3
X = 7
arr = [2, 1, 5, 1, 3, 2, 8]
i=0
j=0
winsum =0
count =0
while j<len(arr):
    winsum +=arr[j]
    if (j - i+1)<K:
        j +=1
    elif (j -i +1) ==K:
        if winsum <=X:
            count +=1
        winsum -=arr[i]
        i +=1
        j+=1

print(count)
