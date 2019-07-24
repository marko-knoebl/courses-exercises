import tkinter
import transaction
from ZODB import DB, FileStorage


class Game:

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    def __init__(self):
        self.new_game()
        self._event_listeners = {"place_mark": [], "game_over": [], "new_game": []}

    def new_game(self):
        self.field = [[None, None, None], [None, None, None], [None, None, None]]
        self.round = 0
        self.game_over = False

    def place_mark(self, row, col):
        if self.game_over:
            return
        if self.field[row][col]:
            # cell is already full - ignore
            return
        if self.round % 2 == 0:
            self.field[row][col] = "X"
        else:
            self.field[row][col] = "O"
        self.round += 1
        for listener in self._event_listeners["place_mark"]:
            listener(row, col)
        if self.winner():
            self.game_over = True
            for listener in self._event_listeners["game_over"]:
                listener()
        if hasattr(self, "save"):
            self.save()

    def winner(self):
        for comb in self.winning_combinations:
            symbols = [self.field[comb[i] // 3][comb[i] % 3] for i in range(3)]
            if symbols[0] == symbols[1] == symbols[2]:
                return symbols[0]
        return None

    def add_event_listener(self, event_name, callback):
        self._event_listeners[event_name].append(callback)


class PersistentGame(Game):
    def __init__(self, filename="game.fs"):
        super().__init__()
        # set up zodb storage
        db = DB(FileStorage.FileStorage(filename))
        self.connection = db.open()
        self.root = self.connection.root()

    def save(self, filename="game.fs"):
        self.root["field"] = self.field
        self.root["round"] = self.round
        self.root["game_over"] = self.game_over
        transaction.commit()

    def load(self, filename="game.fs"):
        self.field = self.root["field"]
        self.round = self.root["round"]
        self.game_over = self.root["game_over"]


class GameUI:
    def __init__(self):

        self.game = Game()
        try:
            self.game.load()
        except:
            pass

        self.window = tkinter.Tk()
        self.buttons = []
        for i, row in enumerate(self.game.field):
            button_row = []
            button_frame = tkinter.Frame(master=self.window)
            button_frame.pack()
            for j, cell in enumerate(row):
                btn = tkinter.Button(
                    master=button_frame,
                    text="  ",
                    command=self.make_click_handler(i, j),
                )
                btn.pack(side=tkinter.LEFT)
                button_row.append(btn)
            self.buttons.append(button_row)
        self.update_button_labels()
        self.new_btn = tkinter.Button(
            master=self.window, text="New Game", command=self.new_game
        )
        self.new_btn.pack()
        self.game.add_event_listener("place_mark", self.on_mark_placed)
        self.game.add_event_listener("game_over", self.on_game_over)

    def update_button_labels(self):
        for i, button_row in enumerate(self.buttons):
            for j, button in enumerate(button_row):
                button.config(text=self.game.field[i][j] or "  ")

    def make_click_handler(self, row, col):
        def click_handler():
            self.game.place_mark(row, col)

        return click_handler

    def on_mark_placed(self, row, col):
        symbol = self.game.field[row][col]
        self.buttons[row][col].config(text=symbol)

    def on_game_over(self):
        for button_row in self.buttons:
            for button in button_row:
                button.config(state=tkinter.DISABLED)

    def new_game(self):
        self.game.new_game()
        for button_row in self.buttons:
            for button in button_row:
                button.config(text="  ", state=tkinter.NORMAL)

    def run(self):
        self.window.mainloop()


ttt = GameUI()
ttt.run()
