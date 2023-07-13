class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        """
        for number in range(n):
            nums1[m+number] = nums2[number]

        nums1.sort()

