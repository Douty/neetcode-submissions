class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_seen = defaultdict(set)
        c_seen = defaultdict(set)
        b_seen = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]

                if cell == ".":
                    continue

                if (cell in r_seen[r] 
                or cell in c_seen[c] 
                or cell in b_seen[(r//3,c//3)]):
                    return False

                r_seen[r].add(cell)
                c_seen[c].add(cell)
                b_seen[(r//3,c//3)].add(cell)
            
        return True