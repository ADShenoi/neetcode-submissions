class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        postfix = [0]*len(nums)

        i, j = 0, len(nums)-1
        prefix_val = 1
        postfix_val = 1

        while i <= len(nums) and j >= 0:
            prefix_val *= nums[i]
            postfix_val *= nums[j]

            prefix[i] = prefix_val
            postfix[j] = postfix_val

            i += 1
            j -= 1
        
        temp = [0]*len(nums)

        print(prefix)
        print(postfix)
        
        for i in range(len(nums)):
            if i == 0:
                temp[i] = postfix[i+1]
            elif i == len(nums)-1:
                temp[i] = prefix[i-1]
            else:
                temp[i] = prefix[i-1] * postfix[i+1]
        
        return temp