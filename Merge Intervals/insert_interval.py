class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert new interval
        intervals.append(newInterval)
        # place the new interval in right position
        for i in range(len(intervals)-1, 0, -1):
            if intervals[i][0]<intervals[i-1][0]:
                tmp = intervals[i]
                intervals[i] = intervals[i-1]
                intervals[i-1] = tmp
            else:
                break
        # merge the overlap
        mergedIntervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                mergedIntervals.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        mergedIntervals.append([start,end])
        return mergedIntervals
        