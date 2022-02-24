def basicMedian(fir: List[int]) -> float:
    l = len(fir)
    print("l", l)
    if (l % 2) == 0:
        l = int(l / 2) - 1
        print("r5", fir[l] + fir[l + 1])
        return (fir[l] + fir[l + 1]) / 2
    
    l = int(l / 2)
    print("r6", fir[l])
    return fir[l]

    
class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        nums = []
        n1 = 0
        n2 = 0
        for i in range(l):
            if n2 >= len(nums2):
                nums.append(nums1[n1])
                n1 += 1
            elif n1 < len(nums1) and nums1[n1] < nums2[n2]:
                nums.append(nums1[n1])
                n1 += 1
            else:
                nums.append(nums2[n2])
                n2 += 1
        return basicMedian(nums)
    
        
