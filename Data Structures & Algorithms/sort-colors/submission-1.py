class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_pointer, i, right_pointer = 0, 0, len(nums)-1

        while i <= right_pointer:
            if nums[i] == 0:
                nums[left_pointer], nums[i] = nums[i], nums[left_pointer]
                i += 1
                left_pointer += 1
            elif nums[i] == 2:
                nums[right_pointer], nums[i] = nums[i], nums[right_pointer]
                right_pointer -= 1
            else:
                i += 1            