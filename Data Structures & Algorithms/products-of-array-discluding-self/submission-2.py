class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [1] * l

        prefix = 1
        for i in range(l):
            output[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(l  -1, -1, -1):
            output[i] *= sufix
            sufix *= nums[i]
        return output    



