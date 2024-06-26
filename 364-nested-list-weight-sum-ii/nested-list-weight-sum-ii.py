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

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.max_sum = 0
        self.max_depth = 1
        
        def maxDepth(nested: List[NestedInteger], depth):
            self.max_depth = max(self.max_depth, depth)
            for ele in nested:
                # print(ele)
                if not ele.isInteger() and ele.getList():
                    maxDepth(ele.getList(), depth+1)
                    
        def calculateListSum(nested: List[NestedInteger], depth):
            for ele in nested:
                if ele.isInteger():
                    weight = self.max_depth - depth + 1
                    # print(ele.getInteger(), weight)
                    self.max_sum += (ele.getInteger() * weight)
                else:
                    calculateListSum(ele.getList(), depth+1)
            
        maxDepth(nestedList, 1)
        # print(self.max_depth)
        calculateListSum(nestedList, 1)
        return self.max_sum