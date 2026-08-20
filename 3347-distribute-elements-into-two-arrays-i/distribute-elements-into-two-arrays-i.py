class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        arr = [0]*n

        arr[0] = nums[0]
        arr[n-1] = nums[1]
        idx , revidx = 0,n-1

        for i in range(2,n):
            if arr[idx] > arr[revidx]:
                idx+=1
                arr[idx] = nums[i]

            else :
                revidx -=1
                arr[revidx] = nums[i]
        l , r = revidx , n-1
        while l<r:
            arr[l] ,arr[r] = arr[r] , arr[l]
            l+=1
            r-=1

        return arr
