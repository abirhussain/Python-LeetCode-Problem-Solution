class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        margedIntervals = []
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                margedIntervals.append([start, end])
                start = interval[0]
                end = interval[1]
        margedIntervals.append([start, end])
        return margedIntervals
