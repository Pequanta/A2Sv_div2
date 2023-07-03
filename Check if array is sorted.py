#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        i = 1
        for j in range(n - 1):
            if arr[i] < arr[j]: return False
            i += 1
        return True
