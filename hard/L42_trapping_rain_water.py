class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def prefixMax(height):
            if not height:
                return 
            n = len(height)
            arr = [None] * n
            arr[0] = height[0]
            for i in range(1,n):
                arr[i] = max(arr[i-1],height[i])
            return arr

        def suffixMax(height):
            if not height:
                return 
            n = len(height)
            arr = [None] * n
            arr[n-1] = height[n-1]
            for i in range(n-2,-1,-1):
                arr[i] = max(arr[i+1],height[i])
            return arr 

        n = len(height)
        prefix = prefixMax(height)
        suffix = suffixMax(height)
        water = 0
        for i in range(n):
            prefixM, suffixM = prefix[i],suffix[i]
            water += min(prefixM,suffixM) - height[i]
        return water
