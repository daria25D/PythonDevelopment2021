import tkinter as tk
from tkinter import ttk


class FifteenGame(ttk.Frame):
    def __init__(self, master=None):
        self.configureStyle()
        ttk.Frame.__init__(self, master, style='Game.TFrame')
        self.grid(sticky='NSEW')
        self.createWidgets()


    def configureStyle(self):
        style = ttk.Style()
        style.configure('Game.TFrame', background='#e0e0f0')
        style.configure('Game.TButton', font=('Arial', 20), background='#ececf5', foreground='#121961', borderwidth='1')
        style.map('Game.TButton', foreground=[('active', '#3a71c9'), ('pressed', '#f0f4ff')],
                                  background=[('active', '#f0f4ff'), ('pressed', '!focus', '#3a71c9')])
        style.configure('Control.TButton', font=('Helvetica', 18), background='#ececf5', foreground='#020951')
        style.map('Control.TButton', foreground=[('active', '#c97673'), ('pressed', '#a84d4a')],
                                     background=[('active', '#fae9e8'), ('pressed', '!focus', '#fae9e8')])


    def enableStretching(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(4):
            self.rowconfigure(i, weight=1, minsize=100, pad=2)
            self.columnconfigure(i, weight=1, minsize=100, pad=2)
        self.rowconfigure(4, weight=1, minsize=60)


    def createWidgets(self):
        self.enableStretching()
        self.createGameFieldLayout()
        self.startButton = ttk.Button(self, text='NEW GAME', style='Control.TButton')
        self.quitButton  = ttk.Button(self, text='QUIT', style='Control.TButton', command=self.quit)
        self.startButton.grid(row=4, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)
        self.quitButton.grid(row=4, column=2, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)


    def createGameFieldLayout(self):
        self.currentPositions = [i for i in range(15)]  # currentPositions[buttonIdx] = coord
        self.blankPosition = 15
        self.gameButtons = [ttk.Button(self, text=str(i), style='Game.TButton') for i in range(1, 16)]
        for i, button in enumerate(self.gameButtons):
            row = i // 4
            column = i % 4
            button.grid(row=row, column=column, sticky='NSEW')
            button.configure(command= lambda idx=i: self.moveButton(idx))


    def moveButton(self, idx):
        if (self.currentPositions[idx] - 4 == self.blankPosition) and (self.blankPosition >= 0):
            # move up
            new_row = self.currentPositions[idx] // 4 - 1
            new_col = self.currentPositions[idx] % 4
            self.gameButtons[idx].grid(row=new_row, column=new_col)
            self.blankPosition = self.currentPositions[idx]
            self.currentPositions[idx] -= 4
        elif (self.currentPositions[idx] + 4 == self.blankPosition) and (self.blankPosition < 16):
            # move down
            new_row = self.currentPositions[idx] // 4 + 1
            new_col = self.currentPositions[idx] % 4
            self.gameButtons[idx].grid(row=new_row, column=new_col)
            self.blankPosition = self.currentPositions[idx]
            self.currentPositions[idx] += 4
        elif (self.currentPositions[idx] - 1 == self.blankPosition) and (self.blankPosition % 4 != 3):
            # move left
            new_row = self.currentPositions[idx] // 4
            new_col = self.currentPositions[idx] % 4 - 1
            self.gameButtons[idx].grid(row=new_row, column=new_col)
            self.blankPosition = self.currentPositions[idx]
            self.currentPositions[idx] -= 1
        elif (self.currentPositions[idx] + 1 == self.blankPosition) and (self.blankPosition % 4 != 0):
            # move right
            new_row = self.currentPositions[idx] // 4
            new_col = self.currentPositions[idx] % 4 + 1
            self.gameButtons[idx].grid(row=new_row, column=new_col)
            self.blankPosition = self.currentPositions[idx]
            self.currentPositions[idx] += 1


def main():
    game = FifteenGame()
    game.master.title('Fifteen Game')
    game.mainloop()


if __name__ == '__main__':
    main()
