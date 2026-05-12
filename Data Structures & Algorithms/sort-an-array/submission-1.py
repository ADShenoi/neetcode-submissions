class Solution:
    def sort(self, left_arr, right_arr):
        result_arr = []
        left_pointer, right_pointer = 0, 0

        while left_pointer < len(left_arr) and right_pointer < len(right_arr):
            if left_arr[left_pointer] < right_arr[right_pointer]:
                result_arr.append(left_arr[left_pointer])
                left_pointer += 1
            else:
                result_arr.append(right_arr[right_pointer])
                right_pointer += 1
        
        while left_pointer < len(left_arr):
            result_arr.append(left_arr[left_pointer])
            left_pointer += 1
        
        while right_pointer < len(right_arr):
            result_arr.append(right_arr[right_pointer])
            right_pointer += 1
        
        return result_arr
            
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums)//2
        left_arr = self.sortArray(nums[:mid])
        right_arr = self.sortArray(nums[mid:])

        return self.sort(left_arr, right_arr)

        