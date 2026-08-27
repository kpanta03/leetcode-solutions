class Solution(object):
    def removeDuplicates(self, nums):
        i=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i=i+1
        return i
s=Solution()
print(s.removeDuplicates([1,1,2,3,3,3,4,4,5]))
