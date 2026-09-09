class Solution(object):
    def majorityElement(self, nums):
        majority_ele=None
        count=0
        for ele in nums:
            if majority_ele==ele:
                count+=1
            elif count==0:
                majority_ele=ele
                count+=1
            else:
                count-=1
        return majority_ele
s=Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))
