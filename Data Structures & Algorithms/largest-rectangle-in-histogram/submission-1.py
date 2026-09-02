class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  
        largest = 0

        for i, h in enumerate(heights):

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                largest = max(largest, height * width)

            stack.append(i)

        
        n = len(heights)

        while stack:
            height = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            largest = max(largest, height * width)

        return largest       


