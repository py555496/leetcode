class Solution(object):
    def cal_area(self, x1,x2,y1,y2):
        #默认x1是前面的点
        return (x2 - x1) * min(y1,y2)
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height) - 1
        while True:
            area = self.cal_area(i, j, height[i], height[j])
            if area > max_area:
                    max_area = area
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
            if i > j:
                break
        return max_area
                
        """
        :type height: List[int]
        :rtype: int
        """
        