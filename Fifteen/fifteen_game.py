import tkinter as tk

class FifteenGame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.startButton = tk.Button(self, text='New Game')
        self.quitButton  = tk.Button(self, text='Quit', command=self.quit)
        self.startButton.grid()
        self.quitButton.grid()


def main():
    game = FifteenGame()
    game.master.title('Fifteen Game')
    game.mainloop()


if __name__ == '__main__':
    main()
