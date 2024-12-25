from __future__ import annotations

from tkinter import Canvas, Tk
from typing import Optional


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y


class Line:
    def __init__(self, a: Point, b: Point) -> None:
        self.a: Point = a
        self.b: Point = b

    def draw(self, canv: Canvas, fill_color: str) -> None:
        canv.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root: Tk = Tk()
        self.root.title("Maze solver")
        self.canvas: Canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running: bool = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.canvas.update_idletasks()
        self.canvas.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False

    def draw_line(self, line: Line) -> None:
        line.draw(self.canvas, fill_color="red")


class Cell:
    """
    positioning of the walls depends on coordinates: cell coords should be
    specified from top left to bottom right, otherwise walls could flip sides
    """

    def __init__(
        self,
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        window: Optional[Window] = None,
        has_left_wall: bool = True,
        has_right_wall: bool = True,
        has_top_wall: bool = True,
        has_bottom_wall: bool = True,
    ):
        self._x1: float = x1
        self._x2: float = x2
        self._y1: float = y1
        self._y2: float = y2
        self._win: Optional[Window] = window
        self.has_left_wall: bool = has_left_wall
        self.has_right_wall: bool = has_right_wall
        self.has_top_wall: bool = has_top_wall
        self.has_bottom_wall: bool = has_bottom_wall

    def draw(self, fill_color: str = "white"):
        if not self._win:
            raise Exception("Cannot draw with no window provided in a Cell")

        left: Line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right: Line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        bottom: Line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        top: Line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))

        default_bg = self._win.canvas.cget("bg")

        if self.has_left_wall:
            left.draw(self._win.canvas, fill_color)
        else:
            left.draw(self._win.canvas, default_bg)
        if self.has_right_wall:
            right.draw(self._win.canvas, fill_color)
        else:
            right.draw(self._win.canvas, default_bg)
        if self.has_bottom_wall:
            bottom.draw(self._win.canvas, fill_color)
        else:
            bottom.draw(self._win.canvas, default_bg)
        if self.has_top_wall:
            top.draw(self._win.canvas, fill_color)
        else:
            top.draw(self._win.canvas, default_bg)

    def draw_move(self, to_cell: Cell, undo=False):
        if not self._win:
            raise Exception("Can't draw with no window provided in a cell")
        color: str = "red"
        if undo:
            color = "gray"
        line: Line = Line(
            Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2),
            Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2),
        )
        line.draw(self._win.canvas, color)
