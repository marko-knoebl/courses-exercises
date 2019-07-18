import tkinter

class TicTacToe():

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.round = 0

        self.window = tkinter.Tk()
        self.buttons = []
        for i, row in enumerate(self.field):
            button_row = []
            button_frame = tkinter.Frame(
                master=self.window
            )
            button_frame.pack()
            for j, cell in enumerate(row):
                btn = tkinter.Button(
                    master=button_frame,
                    text="  ",
                    command=self.make_click_handler(i, j)
                )
                btn.pack(side=tkinter.LEFT)
                button_row.append(btn)
            self.buttons.append(button_row)
        self.new_btn = tkinter.Button(
            master=self.window,
            text="New Game",
            command=self.new_game
        )
        self.new_btn.pack()
    
    def make_click_handler(self, row, col):
        def click_handler():
            self.place_mark(row, col)
        return click_handler

    def place_mark(self, row, col):
        if self.field[row][col]:
            # cell is already full - ignore
            return
        if self.round % 2 == 0:
            self.field[row][col] = "X"
            self.buttons[row][col].config(text="X")
        else:
            self.field[row][col] = "O"
            self.buttons[row][col].config(text="O")
        self.round += 1
        if self.winner():
            self.deactivate_field()

    def winner(self):
        for comb in self.winning_combinations:
            symbols = [self.field[comb[i] // 3][comb[i] % 3] for i in range(3)]
            if symbols[0] == symbols[1] == symbols[2]:
                return symbols[0]
        return None

    def deactivate_field(self):
        for button_row in self.buttons:
            for button in button_row:
                button.config(state=tkinter.DISABLED)

    def new_game(self):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.round = 0
        for button_row in self.buttons:
            for button in button_row:
                button.config(text="  ", state=tkinter.NORMAL)

    def run(self):
        self.window.mainloop()

ttt = TicTacToe()
ttt.run()
