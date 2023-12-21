class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []

        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res






        
    

a = Solution().productExceptSelf([1,2,3,4])
print(a)