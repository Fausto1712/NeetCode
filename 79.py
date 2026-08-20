class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False
        
        board_counts = {}
        for row_idx in range(rows):
            for col_idx in range(cols):
                char = board[row_idx][col_idx]
                board_counts[char] = board_counts.get(char, 0) + 1
                
        for char in word:
            if char not in board_counts or word.count(char) > board_counts[char]:
                return False
            
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        def dfs(row_val, col_val, index):
            if index == len(word):
                return True
            
            if (row_val < 0 or col_val < 0 or 
                row_val >= rows or col_val >= cols or 
                board[row_val][col_val] != word[index]):
                return False
            
            temp_char = board[row_val][col_val]
            board[row_val][col_val] = "#"
            
            found = (dfs(row_val + 1, col_val, index + 1) or
                     dfs(row_val - 1, col_val, index + 1) or
                     dfs(row_val, col_val + 1, index + 1) or
                     dfs(row_val, col_val - 1, index + 1))
            
            board[row_val][col_val] = temp_char
            
            return found

        for row_idx in range(rows):
            for col_idx in range(cols):
                if dfs(row_idx, col_idx, 0):
                    return True
                    
        return False

if __name__ == "__main__":
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(f"There is {'' if solution.exist(board, word) else 'not '}a path")