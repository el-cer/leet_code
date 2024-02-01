
class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        list =[]
        list = nums1+nums2
        list.sort()
        if len(list) %2 !=0:
            result = list[int(len(list)/2)]
        else:
            result = (list[int(len(list)/2)-1]+list[int(len(list)/2)])/2
        return result

"""https://leetcode.com/problems/median-of-two-sorted-arrays/"""


