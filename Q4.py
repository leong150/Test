class Solution:
    def Q4(self, array: list[int], target: int):
        hashmap = {}
        for i in range(len(array)):
            complement = target - array[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[array[i]] = i

ans = Solution()
print(ans.Q4(array= [1, 4, 7, 11, 19], target = 15))