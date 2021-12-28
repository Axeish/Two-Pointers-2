
# Time Complexity : O(m+n)
# Space Complexity : 0(1)

# Did this code successfully run on Leetcode : 
# YEs

# Any problem you faced while coding this : 

# Your code here along with comments explaining your approach




# adding value to nums with one pointer in nums1 and another in nums 2 comparing 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if nums1== None or len(nums1) ==0:
            return
        ptr1 =m-1
        ptr2 =n-1
        i= m+n-1
        while ptr1 >=0 and ptr2 >=0:
            if nums1[ptr1] > nums2[ptr2] :
                nums1[i] = nums1[ptr1]
                ptr1-=1
            else:
                nums1[i] = nums2[ptr2]
                ptr2-=1
            i-=1
        while ptr2 >=0:
            nums1[i] = nums2[ptr2]
            ptr2-=1
            i-=1