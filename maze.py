import time
from typing import List, Optional

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


