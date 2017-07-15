class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def search(board, i, j, word):
            if not word:
                return True
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
                tmp = board[i][j]
                board[i][j] = '#'
                res = search(board, i + 1, j, word[1:]) or search(board, i - 1, j, word[1:]) or search(board, i, j + 1, word[1:]) or search(board, i, j - 1, word[1:])
                board[i][j] = tmp
                return res
            return False
        
        if not word or not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, i, j, word):
                    return True
        return False
        
if __name__ == '__main__':
    board = [['C','A','A'],['A','A','A'],['B','C','D']]
    print(Solution().exist(board, "CD"))