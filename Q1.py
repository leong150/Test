from tabulate import tabulate

class Solution:
    def Q1(self, size: int):
        table = []
        for row in range(size):
            table.append([])
            for column in range(size):
                if row == column:
                    table[row].append(1)
                else:
                    table[row].append(0)
        return tabulate(table)

ans = Solution()
print(ans.Q1(size=5))