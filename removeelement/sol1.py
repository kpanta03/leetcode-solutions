class Solution(object):
    def removeElement(self, nums,val):
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j=j+1
        return j
s=Solution()
print(s.removeElement([3,1,2,3,4,5],3))
