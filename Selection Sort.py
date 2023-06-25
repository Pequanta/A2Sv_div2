#User function Template for python3

class Solution: 
    def select(self, arr):
        # code here 
        return arr.index(min(arr))
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            index = self.select(arr[i:]) + i
            arr[i] , arr[index] = arr[index], arr[i]
        return arr
                
