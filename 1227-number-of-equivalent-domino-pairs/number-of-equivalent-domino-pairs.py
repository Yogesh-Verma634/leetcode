class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        LEN = len(dominoes)
        count = 0
        similar_map = {}

        for domino in dominoes:
            domino = tuple(sorted(domino))
            if domino not in similar_map:
                similar_map[domino] = 0
            else:
                similar_map[domino] += 1
        print(similar_map)
        for key, val in similar_map.items():
            count += (val*(val+1))//2
        
        return count
        