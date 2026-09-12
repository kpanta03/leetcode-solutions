class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False
s=Solution()
print(s.containsNearbyDuplicate([1, 2, 3, 1],3))