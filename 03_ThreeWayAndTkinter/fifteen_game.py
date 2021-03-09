import tkinter as tk

class FifteenGame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.createGameField()
        self.startButton = tk.Button(self, text='New Game')
        self.quitButton  = tk.Button(self, text='Quit', command=self.quit)
        self.startButton.grid(row=4, column=0)
        self.quitButton.grid(row=4, column=1)


    def createGameField(self):
        self.gameButtons = [tk.Button(self, text=str(i)) for i in range(1, 16)]
        for i, button in enumerate(self.gameButtons):
            row = i // 4
            column = i % 4
            button.grid(row=row, column=column, sticky=tk.W+tk.N+tk.S+tk.E)


def main():
    game = FifteenGame()
    game.master.title('Fifteen Game')
    game.mainloop()


if __name__ == '__main__':
    main()
