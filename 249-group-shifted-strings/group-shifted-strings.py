class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dist_map = {}

        for st in strings:
            key = ()
            for i in range(len(st)-1):
                diff = ord(st[i+1]) - ord(st[i])
                if diff < 0:
                    diff += 26
                key += (diff, )
            dist_map[key] = dist_map.get(key, []) + [st]

        return list(dist_map.values())
        