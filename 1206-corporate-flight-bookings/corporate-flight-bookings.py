class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = dict()
        for first, last, seats in bookings:
            if first not in events:
                events[first] = seats
            else:
                events[first] += seats

            if last+1 not in events:
                events[last+1] = -1*seats
            else:
                events[last+1] += -1*seats

        events = dict(sorted(events.items()))

        # events.pop()  # Remove the last index that has extra info
        print(events)
        cumSum = 0
        result = []
        for i in range(1,n+1):
            if i not in events:
                result.append(cumSum)
            else:
                cumSum += events[i]
                result.append(cumSum)

        return result