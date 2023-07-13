class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0

        for number in range(len(nums)):
            if nums[number] != val:
                nums[count] = nums[number]
                count += 1
        return count

