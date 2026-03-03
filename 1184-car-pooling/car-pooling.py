class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for numPassengers, up, down in trips:
            events.append((up, numPassengers))
            events.append((down, -1*numPassengers))

        events.sort()

        passengers = 0
        for location, numPassengers in events:
            passengers += numPassengers
            if passengers>capacity:
                return False
        return True