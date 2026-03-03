class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        max_events = 0
        total_events = 0
        for currentTime, status  in self.events:
            total_events += status
            if total_events > max_events:
                max_events = total_events

        return max_events

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)