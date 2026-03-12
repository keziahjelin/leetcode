class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        assert 0 <= rowIndex <= 33
        tri=[[1]]
        for i in range(rowIndex):
            currentrow=tri[-1]
            row=[1]
            for i in range(len(currentrow)-1):
                row.append(currentrow[i]+currentrow[i+1])
            row.append(1)
            tri.append(row)
        return tri[rowIndex]   
