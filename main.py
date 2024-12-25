from geomentry import Cell, Line, Point, Window
from maze import Maze


def main() -> None:
    win: Window = Window(800, 600)

    # cell_1: Cell = Cell(400, 410, 300, 310, win, has_bottom_wall=False)
    # cell_2: Cell = Cell(
    #     400, 410, 310, 320, win, has_bottom_wall=False, has_top_wall=False
    # )
    # cell_3: Cell = Cell(
    #     400, 410, 320, 330, win, has_bottom_wall=False, has_top_wall=False
    # )
    # cell_4: Cell = Cell(
    #     400, 410, 330, 340, win, has_bottom_wall=False, has_top_wall=False
    # )
    # cell_5: Cell = Cell(
    #     400,
    #     410,
    #     340,
    #     350,
    #     win,
    #     has_top_wall=False,
    #     has_right_wall=False,
    # )
    #
    # cell_6: Cell = Cell(
    #     410, 420, 340, 350, win, has_left_wall=False, has_right_wall=False
    # )
    # cell_7: Cell = Cell(
    #     420, 430, 340, 350, win, has_left_wall=False, has_right_wall=False
    # )
    # cell_8: Cell = Cell(
    #     430, 440, 340, 350, win, has_left_wall=False, has_top_wall=False
    # )
    # cell_9: Cell = Cell(
    #     430, 440, 330, 340, win, has_bottom_wall=False, has_top_wall=False
    # )
    # cell_10: Cell = Cell(
    #     430,
    #     440,
    #     320,
    #     330,
    #     win,
    #     has_bottom_wall=False,
    # )
    # cell_1.draw()
    # cell_2.draw()
    # cell_3.draw()
    # cell_4.draw()
    # cell_5.draw()
    # cell_6.draw()
    # cell_7.draw()
    # cell_8.draw()
    # cell_9.draw()
    # cell_10.draw()
    # cell_1.draw_move(cell_2)
    # cell_2.draw_move(cell_3)
    # cell_3.draw_move(cell_4)
    # cell_4.draw_move(cell_5)
    # cell_5.draw_move(cell_6)
    # cell_6.draw_move(cell_7)
    # cell_7.draw_move(cell_8)
    # cell_8.draw_move(cell_9)
    # cell_9.draw_move(cell_10)
    #
    # cell_10.draw_move(cell_9, undo=True)
    # cell_9.draw_move(cell_8, undo=True)
    # cell_8.draw_move(cell_7, undo=True)
    # cell_7.draw_move(cell_6, undo=True)

    Maze(50, 50, 5, 9, 20, 20, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
