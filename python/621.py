class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d = {}
        for t in tasks:
            d[t] = d.get(t, 0) + 1
        freqs = [v for v in d.values()]
        freqs.sort(reverse = True)
        freq_max = freqs[0]
        freq_max_num = 0
        for freq in freqs:
            if freq == freq_max:
                freq_max_num += 1
        return max(len(tasks), (freq_max-1)*(n+1)+freq_max_num)
        

if __name__ == '__main__':
    tasks = 'AACCCBEEE'
    n = 2
    print(Solution().leastInterval(tasks, n))