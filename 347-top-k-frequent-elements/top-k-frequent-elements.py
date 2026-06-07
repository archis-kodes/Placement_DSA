class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i]+=1

        # Sort
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        
        result = []
        for i in count:
            if k==0:
                break
            result.append(i)
            k-=1
        return result
            