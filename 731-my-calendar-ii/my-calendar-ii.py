class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        events = self.events.copy()  # Shallow Copy Problem
        events.append((startTime, 1))
        events.append((endTime, -1))

        events.sort()

        bookings = 0
        for currentTime, booking in events:
            bookings += booking
            if bookings>2:
                return False
        self.events = events.copy()
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)