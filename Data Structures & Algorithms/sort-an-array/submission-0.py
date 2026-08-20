class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if not nums:
            return nums
        
        return self.mergeSort(0, len(nums)-1, nums)


    
    def mergeSort(self, left: int, right: int, arr: List[int]):

        if (left == right):
            return [arr[left]]

        mid = left + ((right - left)//2)

        leftArr = self.mergeSort(left, mid, arr)
        rightArr = self.mergeSort(mid + 1, right, arr)

        return self.merge(leftArr, rightArr)
    
    def merge(self, leftArr: List[int], rightArr: List[int]):

        i = 0
        j = 0
        res = []

        while(i < len(leftArr) and j < len(rightArr)):

            if (leftArr[i] > rightArr[j]):
                res.append(rightArr[j])
                j += 1
            else:
                res.append(leftArr[i])
                i += 1
        
        while(i < len(leftArr)):

            res.append(leftArr[i])
            i += 1 

        while(j < len(rightArr)):

            res.append(rightArr[j])
            j += 1 

        return res
