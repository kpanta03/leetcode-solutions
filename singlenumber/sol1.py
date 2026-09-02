class Solution:
    def singleNumber(self, nums):
        output = 0

        for num in nums:
            output ^= num

        return output
s=Solution()
print(s.singleNumber([4,1,1,3,2,3,2]))