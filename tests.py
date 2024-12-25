import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols: int = 12
        num_rows: int = 10
        m1: Maze = Maze(0,0,num_rows,num_cols,10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_break_entr_and_exit(self):
        num_rows: int = 35
        num_cols: int = 25
        maze: Maze = Maze(10,10,num_rows,num_cols,20,20)
        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[num_cols-1][num_rows-1].has_right_wall)


if __name__ == "__main__":
    unittest.main()
