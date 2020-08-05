class Solution:
    def judge(self, idx, line):
        for i in range(idx, len(line)):
            if line[i] == 1:
                return False
        return True

    def minSwaps(self, grid):
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if self.judge(i + 1, grid[j]):
                    grid.insert(i, grid.pop(j))
                    count += (j - i)
                    break
                if j + 1 == n:
                    return -1
        return count



