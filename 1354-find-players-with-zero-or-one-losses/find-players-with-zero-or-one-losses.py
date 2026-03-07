class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_count = dict()
        winner_count = dict()
        total_matches = len(matches)
        for winner, loser in matches:
            if loser not in loser_count:
                loser_count[loser] = 1
            else:
                loser_count[loser] +=1
            if winner not in winner_count:
                winner_count[winner] = 1

        winners1 = []
        winners2 = []
        for winner in winner_count:
            if winner not in loser_count:
                winners1.append(winner)
        for loser, freq in loser_count.items():
            if freq == 1:
                winners2.append(loser)
        
        return [sorted(winners1), sorted(winners2)]