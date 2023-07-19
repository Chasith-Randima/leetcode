class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        n = len(nums)
        return nums[n//2]
        
#         count = len(nums)
#         tempDict = defaultdict(int)
        
#         for num in nums:
#             tempDict[num] += 1
        
#         count = count//2
        
#         for key,value in tempDict.items():
#             if value > count:
#                 return key
#         return 0