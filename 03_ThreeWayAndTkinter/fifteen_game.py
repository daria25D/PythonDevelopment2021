import tkinter as tk

class FifteenGame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky='NSEW')
        self.createWidgets()


    def enableStretching(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(4):
            self.rowconfigure(i, weight=1, minsize=100, pad=2)
            self.columnconfigure(i, weight=1, minsize=100, pad=2)
        self.rowconfigure(4, weight=1, minsize=50)


    def createWidgets(self):
        self.enableStretching()
        self.createGameField()
        self.startButton = tk.Button(self, text='New Game')
        self.quitButton  = tk.Button(self, text='Quit', command=self.quit)
        self.startButton.grid(row=4, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)
        self.quitButton.grid(row=4, column=2, columnspan=2, sticky='NSEW', padx=10, pady=10)


    def createGameField(self):
        self.gameButtons = [tk.Button(self, text=str(i)) for i in range(1, 16)]
        for i, button in enumerate(self.gameButtons):
            row = i // 4
            column = i % 4
            button.grid(row=row, column=column, sticky='NSEW')


def main():
    game = FifteenGame()
    game.master.title('Fifteen Game')
    game.mainloop()


if __name__ == '__main__':
    main()
