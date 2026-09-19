# Approach:
# have a ptr for nums1 and a ptr for nums2
# since both are sorted in increasing order. We start with comparing
# nums2[ptr_two] <= nums1[ptr_one] place it before it, then increase ptr_two+=1
# if its not less than or equal to we increase the ptr_one

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr_1 = m - 1
        ptr_2 = len(nums2) - 1
        write_ptr = len(nums1) - 1

        while ptr_1 >= 0 and ptr_2 >= 0:
            if nums1[ptr_1] >= nums2[ptr_2]:
                nums1[write_ptr] = nums1[ptr_1]
                write_ptr -= 1
                ptr_1 -= 1
            else:
                nums1[write_ptr] = nums2[ptr_2]
                write_ptr -= 1
                ptr_2 -= 1
        
        while ptr_2 >= 0:
            nums1[write_ptr] = nums2[ptr_2]
            ptr_2 -= 1
            write_ptr -= 1
        
        return nums1


        