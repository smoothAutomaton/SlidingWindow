'''
Maximum Sum of Any Subarray of Size K
Question:

You are given an array of integers arr[] of size N, and a number K.
Your task is to find the maximum possible sum of any contiguous subarray of size exactly K.

If no such subarray exists (i.e., K > N), return -1.

Input Format:

An integer N — size of array

An integer K — size of subarray

An array arr[] of N integers

Output Format:

A single integer — the maximum sum among all subarrays of size K.

Example 1:

Input:
N = 7, K = 3  
arr = [2, 1, 5, 1, 3, 2, 8]
Output:
10    
'''
i = 0
j=0
k=3
arr=[2,1,5,1,3,2,8]
winsum =0
mainsum = 0

while j <len(arr):
    winsum +=arr[j]
    if j-i+1 <k:
        j+=1
    elif j-i+1 ==k:
        if winsum >mainsum:
            mainsum =winsum
        winsum -=arr[i]
        i=i+1
        j = j+1
print(mainsum)
