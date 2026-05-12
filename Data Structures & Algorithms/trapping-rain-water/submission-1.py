class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = [0] * len(height)
        left_max = 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max = height[i]
            left_arr[i] = left_max
        
        right_arr = [0] * len(height)
        right_max = 0
        for i in range(len(height)-1, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            right_arr[i] = right_max
        
        min_arr = [0] * len(height)
        for i in range(len(height)):
            min_arr[i] = min(left_arr[i], right_arr[i])
        
        count = 0
        for i in range(len(height)):
            val = min_arr[i] - height[i]
            if val > 0:
                count += val
        
        return count