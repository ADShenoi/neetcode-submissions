class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, len(nums1)-1

        while i >= 0 and j >= 0:
            print(i, j, nums1[i], nums2[j])
            if nums1[i] < nums2[j]:
                print('nums2 is bigger')
                nums1[k] = nums2[j]
                j -= 1
            else:
                print('nums1 is bigger')
                nums1[k] = nums1[i]
                i -= 1
            print(nums1)
            k -= 1
            
        
        while i >= 0:
            print('nums1 balance', i)
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        
        while j >= 0:
            print('nums2 balance', j)
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
    