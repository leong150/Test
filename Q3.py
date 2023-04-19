from tabulate import tabulate

class Solution:
    def Q3(self, size: int):
        table = []
        for row in range(size):
            table.append([])
            for column in range(size):
                if row + column >= size - 1:
                    table[row].append("X")
                else:
                    table[row].append(0)
        return tabulate(table)

ans = Solution()
print(ans.Q3(size=5))