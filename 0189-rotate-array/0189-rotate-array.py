class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums)

        nums.reverse()

        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        print(nums)

        # if k == 0 or k == len(nums):return

        # k = k%len(nums)
        # index = k


        # for i in range(k):
        #     print(i)
        #     tempNum = nums[i]
        #     nums[i] = nums[len(nums)-(index-i)]
        #     nums[len(nums)-(index-i)] = tempNum
        # if len(nums)%2 == 1:
        #     popped = nums.pop(len(nums)//2)
        #     nums.append(popped)


        # for i in range(k):
        #     print(i,i+k)
        #     tempNum = nums[i]
        #     nums[i]=nums[tempNum+i]
        # print(nums)