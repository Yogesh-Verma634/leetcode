class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dist_map = {}

        for st in strings:
            dist = []
            for i in range(1, len(st)):
                reach = ord(st[i]) - ord(st[i-1])
                if reach < 0:
                    reach = 26 + reach
                dist.append(reach)

            if tuple(dist) not in dist_map:
                dist_map[tuple(dist)] = []
            dist_map[tuple(dist)].append(st)
        
        # print(dist_map)
        return [val for key, val in dist_map.items()]
        