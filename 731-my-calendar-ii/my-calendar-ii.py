class MyCalendarTwo:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        bookings = 0
        for currentTime, booking in self.events:
            bookings += booking
            if bookings>2:
                self.events.remove((startTime, 1))
                self.events.remove((endTime, -1))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)