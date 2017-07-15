class Solution:
    # @return an integer
    def myAtoi(self, str):
        if not str:
            return 0
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0     

            
if __name__ == '__main__':
    print(Solution().myAtoi("  -0012a42"))