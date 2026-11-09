class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # Visit every cell in the 9x9 board.
        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Empty cells don't need validation.
                if value == ".":
                    continue

                # Find the 3x3 box containing this cell.
                # Example: (4, 5) belongs to box (1, 1).
                box_id = (r // 3, c // 3)

                # Check all three Sudoku rules.
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box_id]
                ):
                    return False

                # No duplicate found.
                # Record the digit in its row, column, and box.
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_id].add(value)

        # All existing digits satisfy the rules.
        return True
            