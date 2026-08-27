class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+nums2
        merged.sort()
        if len(merged)%2==0:
            mid = len(merged)//2
            median = (merged[mid]+merged[mid-1])/2
        else:
            median = merged[len(merged)//2]
        return median    

