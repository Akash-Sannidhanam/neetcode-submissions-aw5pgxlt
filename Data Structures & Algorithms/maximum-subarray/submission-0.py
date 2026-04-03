class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            arr = max(arr, curSum)

        return arr
        