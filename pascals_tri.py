class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        assert 1 <= numRows <= 30
        tri=[[1]]
        for i in range(numRows-1):
            currentrow=tri[-1]
            row=[1]
            for i in range(len(currentrow)-1):
                row.append(currentrow[i]+currentrow[i+1])
                
            row.append(1)
            tri.append(row)
        return tri
