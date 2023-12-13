def binarysearch(nums:list[int]):
    head,tail = 0,len(nums)-1


    while head <= tail:
        m = head + (tail - head) // 2
        if ((m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m] != nums[m+1])):
            return nums[m]

        leftSize = m-1 if nums[m - 1] == nums[m] else m
        if leftSize % 2:
            tail = m - 1
        else:s
            head = m + 1 


binarysearch([1,1,2,2,3,3,4,5,5])