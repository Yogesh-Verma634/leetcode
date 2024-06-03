class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for src, dest, weight in times:
            edges[src].append((dest, weight))
        
        min_heap = [(0, k)]

        visited = set()
        min_time_taken = 0

        while min_heap:
            weight, edge = heapq.heappop(min_heap)
            if edge not in visited:
                visited.add(edge)
                min_time_taken = max(min_time_taken, weight)

                for neighbor_node, neighbor_weight in edges[edge]:
                    if neighbor_node not in visited:
                        heapq.heappush(min_heap, (weight+neighbor_weight, neighbor_node))
        
        return min_time_taken if len(visited) == n else -1