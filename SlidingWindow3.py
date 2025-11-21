
'''
🚀 Minimum Sum of Any Subarray of Size K
📌 Question

You are given an array of integers arr[] of size N, and a number K.
Your task is to find the minimum possible sum of any contiguous subarray of size exactly K.

If K > N, return -1.

📥 Input Format

An integer N — number of elements

An integer K — size of the window

An array arr[] of N integers

📤 Output Format

A single integer → the minimum sum among all subarrays of size K

📌 Example 1

Input:
N = 7, K = 3
arr = [2, 1, 5, 1, 3, 2, 8]
Output:
6
'''
arr = [2, 1, 5, 1, 3, 2, 8]
k = 3

i=0
j=0
main_sum = 0
winsum =0
while j <len(arr):
    winsum +=arr[j]
    if j-i+1 <k:
        j +=1
    elif j-i+1==k:

        if main_sum==0:
            main_sum=winsum
        elif winsum <main_sum:
            main_sum =winsum
        winsum -=arr[i]
        i+=1
        j+=1
print(main_sum)
