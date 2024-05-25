# Author: https://leetcode.com/u/fortuna911/

# Liked this clean approach for topological sort,
# so keeping it here for learning
from collections import defaultdict

class Solution:
    def alienOrder(self, words) -> str:
        # Remove dupes and return as no ordering info can be deduced.
        if len(words) == 1:
            return "".join(list({char for char in words[0]}))
        # Set instead of list to avoid parallel edges when we deduce the
        # ordering between the same 2 chars again.
        graph = defaultdict(set)
        for i in range(0, len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            for c in range(min(len(w1), len(w2))):
                # At the char that is different, the char `w1` comes
                # before the `w2` lexicographically, so we create
                # that edge: w1[c] -> w2[c]
                if w1[c] != w2[c]:
                    graph[w1[c]].add(w2[c]) 
                    break

            # Include in the graph vertices that are not adjacent
            # to anything, because if they were not part of an "edge"
            # they would never have been inserted.
            [graph[char] for char in w1]
        # On last loop the last word was not processed.
        [graph[char] for char in w2]

        try:
            topol_sorting = get_topol(graph)
        except ValueError:
            return ""
        else:
            return topol_sorting

def get_topol(graph):
    def dfs(v):
        graph[v].state = State.IN_PROGRESS
        for nei in graph[v].neighbours:
            if graph[nei].state == State.TODO:
                dfs(nei)
            elif graph[nei].state == State.IN_PROGRESS:
                raise ValueError  # Cycle detected
            # else:
            # nei is DONE; means it's already been visited and added
            # to topol_sorting.
        topol_sorting.append(v)
        graph[v].state = State.DONE

    # Initialise all vertices with `TODO` state.
    graph = {v: Vertex(State.TODO, graph[v]) for v in graph.keys()}
    topol_sorting = []

    for v in graph:
        if graph[v].state == State.TODO:
            dfs(v)

    return "".join(reversed(topol_sorting))

class State:
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    
class Vertex:
    def __init__(self, state, neighbours):
        self.state = state
        self.neighbours = neighbours
