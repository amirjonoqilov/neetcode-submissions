class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length
        
        # Step 1: Calculate the prefix product for each element
        prefix = 1
        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Multiply by the suffix product from right to left
        suffix = 1
        for i in range(length - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
            
        return output
