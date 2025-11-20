class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        top, left = 0,0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        # traverse pointers for traversal
        while top <= bottom and left <= right:
            #  move left to right from the top row
            for i in range(left,right + 1):
                result.append(matrix[top][i])
            top += 1
            # move top to bottom along the right column
            for i in range(top,bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            # move right to left across the bottom row (if still valid)
            if top <= bottom:
                for i in range(right, left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            # move bottom to top along the left columnn (if still valid)
            if left <= right:
                for i in range(bottom,top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result