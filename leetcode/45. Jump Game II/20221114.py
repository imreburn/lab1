"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
"""
# This version is rejected; it exceeds the time limit!
# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         """
#         1) define subproblem: jump[i] - minimum number of jumps to reach nums[i]
#         2) recurrence: jump[i] = min(jump[i - j]) + 1, where nums[i-j] >= i-j, i-j>=0, j=1..i
#         3) base case: jump[0] = 0
#         """
#         jump = {0: 0}
#         n = len(nums)
#         for i in range(1, n):
#             candidates = [jump[j] for j in range(0, i) if nums[j] >= i-j]
#             jump[i] = min(candidates) + 1
#         return jump[n-1]

# Still O(n^2), but this is accepted
class Solution:
    def jump(self, nums: list[int]) -> int:
        from collections import defaultdict
        n = len(nums)
        jump = defaultdict(lambda : float('inf'))
        jump[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if (new_min := jump[i] + 1) < jump[i+j]:
                    jump[i+j] = new_min
        return jump[n-1]

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    a = Solution()
    print(a.jump(nums))

