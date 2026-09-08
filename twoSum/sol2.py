class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in seen:
                return [seen[diff],i]
            seen.setdefault(num,i)
s=Solution()
print(s.twoSum([1,2,3,4,5],7))