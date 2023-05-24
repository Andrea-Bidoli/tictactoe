from tkinter import *


class Vector:
    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
        except ValueError:
            raise ValueError("insert int number")

    def display(self):
        print(f"x: {self.x}\ny: {self.y}\n\n")

    def __str__(self):
        return f"x: {self.x} y: {self.y}"


class Cell:
    def __init__(self, pos: Vector, width, height, player):
        """return a Cell object of dimension width height in a position:
           the position given is the center of the cell"""
        self.pos = pos
        self.width = width
        self.height = height
        self.player = player
        self.boundary = self.create_boundary()

    def create_boundary(self):
        tmp = [Vector(self.pos.x - self.width / 2, self.pos.y - self.height / 2),
               Vector(self.pos.x + self.width / 2, self.pos.y - self.height / 2),
               Vector(self.pos.x - self.width / 2, self.pos.y + self.height / 2),
               Vector(self.pos.x + self.width / 2, self.pos.y + self.height / 2)
               ]
        return tmp


class Game(Tk):
    cell_width = 100
    board = [["2", "2", "2"], ["2", "2", "2"], ["2", "2", "2"]]
    players = {"x": 1, "o": 0}

    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.title("TicTacToe")
        self.config(background="#fffffe")
        self.board_cell = [[Cell(Vector(j*self.cell_width+self.cell_width/2, i*self.cell_width+self.cell_width/2),
                            self.cell_width, self.cell_width, "2") for i in range(3)] for j in range(3)]

        width = self.cell_width * 3 + 40
        height = self.cell_width * 3 + 40
        x = int(screen_width / 2) - int(self.cell_width * 3 / 2)
        y = int(screen_height / 2) - int(self.cell_width * 3 / 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        self.Canvas = Canvas(self, width=self.cell_width * 3, height=self.cell_width * 3, background="white")
        self.Canvas.grid(column=0, row=0, padx=20, pady=20)
        self.Canvas.bind("<Button-1>", self.mouse_press)
        self.draw_board()
        self.Canvas.create_line(self.board_cell[0][0].boundary[0].x, self.board_cell[0][0].boundary[0].y, self.board_cell[0][0].boundary[2].x, self.board_cell[0][0].boundary[2].y)

        self.mainloop()

    def mouse_press(self, e):
        # TODO: check where the player has pressed
        x, y = e.x // self.cell_width, e.y // self.cell_width
        self.draw_x(x, y)
        self.draw_o(x, y)

    def draw_board(self):
        # vertical
        self.Canvas.create_line(self.cell_width, 0, self.cell_width, self.cell_width * 3)
        self.Canvas.create_line(self.cell_width * 2, 0, self.cell_width * 2, self.cell_width * 3)
        # horizontal
        self.Canvas.create_line(0, self.cell_width, self.cell_width * 3, self.cell_width)
        self.Canvas.create_line(0, self.cell_width * 2, self.cell_width * 3, self.cell_width * 2)

    def draw_x(self, x, y):
        cell = self.board_cell[x][y]
        self.Canvas.create_line(cell.boundary[0].x, cell.boundary[0].y, cell.boundary[2].x, cell.boundary[2].y)
        self.Canvas.create_line(cell.boundary[1].x, cell.boundary[1].y, cell.boundary[3].x, cell.boundary[3].y)
        print(f"x0:{cell.boundary[0].x}\ny0:{cell.boundary[0].y}\n\nx1:{cell.boundary[2].x}\ny1:{cell.boundary[2].y}"
              f"\n" + "-" * 20)

    def draw_o(self, x, y):
        # TODO: draw o in the center of the cell
        cell = self.board_cell[x][y]
        self.Canvas.create_oval(cell.boundary[0].x, cell.boundary[0].y, cell.boundary[2].x, cell.boundary[2].y)
        print(f"x0:{cell.boundary[0].x}\ny0:{cell.boundary[0].y}\n\nx1:{cell.boundary[2].x}\ny1:{cell.boundary[2].y}"
              f"\n" + "-" * 20)
        pass


if __name__ == "__main__":
    Game()


