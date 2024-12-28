import random
import time
from typing import List, Optional, Tuple

from geomentry import Cell, Window


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Optional[Window] = None,
        seed: Optional[int] = None,
    ) -> None:
        self.x1: float = x1
        self.y1: float = y1
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_x: int = cell_size_x
        self.cell_size_y: int = cell_size_y
        self.win: Optional[Window] = win
        self._cells: List[List[Cell]] = []
        self._create_cells()
        if seed is not None:
            random.seed(seed)

    def _create_cells(self) -> None:
        for i in range(self.num_cols):
            column: List[Cell] = []
            self._cells.append(column)
            for _ in range(self.num_rows):
                new_cell = Cell(0,0,0,0, self.win)
                self._cells[i].append(new_cell)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j, self._cells[i][j])

        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _draw_cell(self, i: int, j: int, cell: Cell) -> None:
        cell._x1 = self.x1 + i*self.cell_size_x
        cell._x2 = self.x1 + (i+1)*self.cell_size_x
        cell._y1 = self.y1 + j*self.cell_size_y
        cell._y2 = self.y1 + (j+1)*self.cell_size_y

        if self.win:
            cell.draw()
            self._animate()

    def _animate(self) -> None:
        if not self.win:
            raise Exception("Cannot animate maze when no window provided")
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance: Cell = self._cells[0][0]
        entrance.has_left_wall = False
        self._draw_cell(0, 0, entrance)

        exitcell: Cell = self._cells[self.num_cols-1][self.num_rows-1]
        exitcell.has_right_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1, exitcell)

    def _break_walls_r(self, i: int, j: int):
        current: Cell = self._cells[i][j]
        current.visited = True
        while True:
            to_visit: List[Tuple[int, int]] = []
            if i+1 < self.num_cols:
                step_right: Cell = self._cells[i+1][j]
                if step_right.visited is not True:
                    to_visit.append((i+1, j))
            if j+1 < self.num_rows:
                step_down: Cell = self._cells[i][j+1]
                if step_down.visited is not True:
                    to_visit.append((i, j+1))
            if i-1 >= 0:
                step_left: Cell = self._cells[i-1][j]
                if step_left.visited is not True:
                    to_visit.append((i-1,j))
            if j-1 >= 0:
                step_up: Cell = self._cells[i][j-1]
                if step_up.visited is not True:
                    to_visit.append((i, j-1))

            if not len(to_visit):
                if self.win:
                    self._cells[i][j].draw()
                return
            
            direction: Tuple[int, int] = to_visit[random.randrange(0, len(to_visit), 1)]
            if direction[0] < i:
                current.has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False
            if direction[0] > i:
                current.has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
            if direction[1] < j:
                current.has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
            if direction[1] > j:
                current.has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False

            self._break_walls_r(direction[0], direction[1])
        
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i: int, j: int):
        if self.win:
            self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if i+1 == self.num_cols-1 and j == self.num_rows - 1 & self._cells[i][j].has_right_wall is False:
            return True
        if j+1 == self.num_rows - 1 and i == self.num_cols - 1 & self._cells[i][j].has_bottom_wall is False:
            return True
        directions: List[Tuple[int, int]] = []
        if i+1 < self.num_cols:
            if self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
                directions.append((i+1,j))
        if i-1 >= 0:
            if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
                directions.append((i-1, j))
        if j+1 < self.num_rows:
            if self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
                directions.append((i, j+1))
        if j-1 >= 0:
            if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
                directions.append((i, j-1))
        for direction in directions:
            self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]])
            res = self._solve_r(direction[0], direction[1])
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[direction[0]][direction[1]], True)

        return False



        
