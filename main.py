from geomentry import Window
from maze import Maze


def main() -> None:
    win: Window = Window(800, 600)
    maze = Maze(50, 50, 10, 15, 20, 20, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
