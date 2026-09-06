class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = []
        ans = 0

        for i in range (len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i
                ans = max(ans, h*w)
            stack.append(i)
        return ans       