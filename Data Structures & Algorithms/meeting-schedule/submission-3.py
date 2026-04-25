"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            start1 = intervals[i].start
            end1 = intervals[i].end
            for k in range(i+1, len(intervals)):
                start2 = intervals[k].start
                if start1 <= start2 < end1: return False
        return True