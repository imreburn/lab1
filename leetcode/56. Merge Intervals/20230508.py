from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        while True:
            overlap = False
            s1, e1 = intervals[i][0], intervals[i][1]
            for j in range(i+1, len(intervals)):
                s2, e2 = intervals[j][0], intervals[j][1]
                if (s2 <= e1 and s2 >= s1) or (s1 <= e2 and s1 >= s2):
                    overlap = True
                    s3 = min(s1, s2)
                    e3 = max(e1, e2)
                    intervals[i] = [s3, e3]
                    intervals.remove([s2, e2])
                    break
            if overlap == False:
                i += 1
                if i == len(intervals) - 1:
                    break
            else:
                continue
        return intervals                                

if __name__ == "__main__":
    a = Solution()
    # intervals = [[1,1],[2,2],[0,0],[2,3],[1,3],[3,5],[2,3],[3,5]]
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(a.merge(intervals))

