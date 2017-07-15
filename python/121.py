class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        minNum = 2**31
        for p in prices:
            result = max(result, p - minNum)
            if minNum > p:
                minNum = p
        return result
        

if __name__ == '__main__':        
    prices = [5]
    print(Solution().maxProfit(prices))