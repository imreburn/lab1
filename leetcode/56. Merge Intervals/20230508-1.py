'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []

        for e in intervals:
            if not merged:  # empty
                merged.append(e)
            else:
                l = merged[-1]
                if e[0] <= l[1]:    # overlap
                    l[1] = max(l[1], e[1])
                else:   # not overlap
                    merged.append(e)
        
        return merged


if __name__ == "__main__":
    a = Solution()
    # intervals = [[1,1],[2,2],[0,0],[2,3],[1,3],[3,5],[2,3],[3,5]]
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(a.merge(intervals))
