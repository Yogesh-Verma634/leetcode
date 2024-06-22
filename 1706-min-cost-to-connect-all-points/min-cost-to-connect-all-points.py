class Solution:

    def prims_algo(self, adjList, points):
        min_heap = [(0, 0)] # (weight, node, parent)
        heapq.heapify(min_heap)
        in_mst = [0] * len(points)
        ans = 0
        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if in_mst[node]:
                continue
                
            ans += weight
            in_mst[node] = 1

            for nei in adjList[node]:
                dest_node, dist = nei
                if not in_mst[dest_node]:
                    heapq.heappush(min_heap, (dist, dest_node))
        
        return ans


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x_i, y_i = points[i][0], points[i][1]
                x_j, y_j = points[j][0], points[j][1]

                dist = abs(x_j - x_i) + abs(y_j - y_i)
                adjList[i].append((j, dist))
                adjList[j].append((i, dist))
        
        return self.prims_algo(adjList, points)
        