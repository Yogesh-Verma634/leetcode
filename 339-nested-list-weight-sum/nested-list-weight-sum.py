# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from typing import List
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        ### BFS Implementation
        # TC - O(N), SC - O(N)
        depth = 1
        nested_sum = 0
        q = collections.deque(nestedList)

        while q:
            for _ in range(len(q)):
                ele = q.popleft()
                if ele.isInteger():
                    nested_sum += depth * ele.getInteger()
                else:
                    q.extend(ele.getList())
            
            depth += 1
        
        return nested_sum

