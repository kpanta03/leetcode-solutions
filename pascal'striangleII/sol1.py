class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]
            row.append(1)
        return row
s=Solution()
print(s.getRow(3))