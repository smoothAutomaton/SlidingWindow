'''
📘 Maximum Average of a Subarray of Size K
🚀 Question

You are given an array of integers arr[] of size N, and an integer K.

Your task is to find the maximum possible average among all contiguous subarrays of size exactly K.

If K > N, return -1.

📥 Input Format

An integer N → number of elements

An integer K → size of the subarray (window)

An array arr[] of N integers

📤 Output Format

A single floating-point number →
The maximum average of any subarray of size K.
Input:
N = 7
K = 3
arr = [2, 1, 5, 1, 3, 2, 8]
Output:
4.33
'''
arr = [2, 1, 5, 1, 3, 2, 8]
K = 3
i=0
j=0
winsum =0
avg = 0
while j < len(arr):
    winsum +=arr[j]
    if (j-i+1) <K:
        j +=1
    elif (j-i+1)==K:
        if avg < (winsum/K):
            avg = (winsum/K)
        winsum -=arr[i]
        i+=1
        j+=1
print(avg)
