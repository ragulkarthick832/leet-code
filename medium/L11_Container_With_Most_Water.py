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
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n - 1
        water = 0
        while l < r:
            width = r - l 
            if height[l] <= height[r]:
                #move left
                waterh = min(height[l],height[r])
                water = max(water, width*waterh)
                l += 1
            else:
                #move right
                waterh = min(height[l],height[r])
                water = max(water, width*waterh)
                r -= 1
            
        return water

        