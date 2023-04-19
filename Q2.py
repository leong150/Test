from tabulate import tabulate

class Solution:
    def Q2(self, size: int):
        table = []
        for row in range(size):
            table.append([])
            for column in range(size):
                if (row == 0 or row == size-1) and (column == 0 or column == size-1):
                    table[row].append("A")
                elif row == column == (size-1)/2:
                    table[row].append(0)
                elif (row + column)%2 == 0:
                    table[row].append(1)
                elif (row + column)%2 == 1:
                    table[row].append(0)
        return tabulate(table)

ans = Solution()
print(ans.Q2(size=5))