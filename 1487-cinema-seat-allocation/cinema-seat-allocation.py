class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        count = 2*n
        seat_map = dict()
        for seat in reservedSeats:
            if seat[1]==1 or seat[1]==10:
                continue
            if seat[0] not in seat_map:
                seat_map[seat[0]] = [seat[1]]
            else:
                seat_map[seat[0]].append(seat[1])
        for row in seat_map:
            temp = set(seat_map[row])
            left = 2 in temp or 3 in temp or 4 in temp or 5 in temp
            center = 4 in temp or 5 in temp or 6 in temp or 7 in temp
            right = 6 in temp or 7 in temp or 8 in temp or 9 in temp
            if left and right and center:
                count -= 2
            elif not left and not right:
                continue
            else:
                count-=1
        return count