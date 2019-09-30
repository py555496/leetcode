class Solution(object):
    def merge(self, num1, num2):
        if len(num1) == 0:
            return num2
        elif len(num2) == 0:
            return num1
        else:
            out = []
            while len(num1) > 0 and len(num2) > 0:
                if num1[0] > num2[0]:
                    out.append(num2.pop(0))
                else:
                    out.append(num1.pop(0))
            out += num1
            out += num2
            return out
                    
                
    def findMedianSortedArrays(self, nums1, nums2):
        out = self.merge(nums1, nums2)
        lens = len(out)
        if lens % 2 == 0:
            return float(out[(lens / 2) - 1] + out[(lens / 2)]) / 2
        else:
            return out[lens / 2]
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        