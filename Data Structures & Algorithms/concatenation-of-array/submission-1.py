class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        for num in nums:
            temp.append(num)
        
        return temp