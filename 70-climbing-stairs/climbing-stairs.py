class Solution:
    def climbStairs(self, n: int) -> int:
        count_map = dict()
        def traverse(current_stair, target):
            if current_stair>target:
                return 0
            if current_stair in count_map:
                return count_map[current_stair]
            if current_stair==target:
                return 1
            count_map[current_stair+1] = traverse(current_stair+1, target)
            count_map[current_stair+2] = traverse(current_stair+2, target)
            return count_map[current_stair+1]+count_map[current_stair+2]
        print(count_map)
        return traverse(0, n)