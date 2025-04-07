#========================= Brute Force ====================================
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        water = 0
        for i in range(n):
            for j in range(i+1,n):
                tall = min(height[i],height[j])
                water = max(water,tall*(j-i))
        return water
        

#========================= Optimal =========================================
