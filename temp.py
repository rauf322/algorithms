class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


a = Solution().containsDuplicate([2,14,18,22,22])
print(a)