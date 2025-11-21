'''
📘 First Negative Number in Every Window of Size K
🚀 Question

You are given an array of integers arr[] of size N, and an integer K.

Your task is to find the first negative number in every contiguous subarray (window) of size exactly K.

If a window does not contain any negative number, output 0 for that window.

📥 Input Format

An integer N → size of the array

An integer K → size of the sliding window

An array arr[] of N integers

📤 Output Format

An array/list of integers →
Each element represents the first negative number from each window of size K.
If no negative exists in a window, output 0.

Input:
N = 8
K = 3
arr = [12, -1, -7, 8, -15, 30, 16, 28]

Output:
[-1, -1, -7, -15, -15, 0]

'''
N = 8
K = 3
arr = [12, -1, -7, 8, -15, 30, 16, 28]
i=0
j=0
list1 = []
neg=[]
count = False
while j<len(arr):
    if arr[j] <0:
        neg.append(arr[j])
    if (j-i+1)<K:
        j+=1
    elif (j-i+1)==K:
        if len(neg)>0:
            list1.append(neg[0])
        i+=1
        j+=1
        if arr[i]<0:
            neg.pop(0)

print(list1)
