import tkinter as tk
from tkinter import ttk, messagebox
import random


class FifteenGame(ttk.Frame):
    def __init__(self, master=None):
        self.configureStyle()
        ttk.Frame.__init__(self, master, style='Game.TFrame')
        self.grid(sticky='NSEW')
        self.createWidgets()
        self.randomizeNewGame()

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
        self.startButton = ttk.Button(self, text='NEW GAME', style='Control.TButton', command=self.randomizeNewGame)
        self.quitButton = ttk.Button(self, text='QUIT', style='Control.TButton', command=self.quit)
        self.startButton.grid(row=4, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)
        self.quitButton.grid(row=4, column=2, columnspan=2, sticky='NSEW', padx=10, pady=10, ipady=5)

    def createGameFieldLayout(self):
        self.currentPositions = [i for i in range(15)]  # currentPositions[buttonIdx] = coord
        self.blankPosition = 15
        self.gameButtons = [ttk.Button(self, text=str(i), style='Game.TButton') for i in range(1, 16)]
        for i, button in enumerate(self.gameButtons):
            button.configure(command=lambda idx=i: self.moveButton(idx))

    def moveButton(self, idx):
        pos = self.currentPositions[idx]
        cur_row = pos // 4
        cur_col = pos % 4
        if (pos - 4 == self.blankPosition) and (self.blankPosition >= 0):
            # move up
            self.gameButtons[idx].grid(row=cur_row - 1, column=cur_col)
            self.blankPosition = pos
            self.currentPositions[idx] -= 4
        elif (pos + 4 == self.blankPosition) and (self.blankPosition < 16):
            # move down
            self.gameButtons[idx].grid(row=cur_row + 1, column=cur_col)
            self.blankPosition = pos
            self.currentPositions[idx] += 4
        elif (pos - 1 == self.blankPosition) and (self.blankPosition % 4 != 3):
            # move left
            self.gameButtons[idx].grid(row=cur_row, column=cur_col - 1)
            self.blankPosition = pos
            self.currentPositions[idx] -= 1
        elif (pos + 1 == self.blankPosition) and (self.blankPosition % 4 != 0):
            # move right
            self.gameButtons[idx].grid(row=cur_row, column=cur_col + 1)
            self.blankPosition = pos
            self.currentPositions[idx] += 1

        self.checkWinning()

    def checkWinning(self):
        isWin = True
        for i in range(15):
            if self.currentPositions[i] != i:
                isWin = False
                break
        if isWin:
            tk.messagebox.showinfo(message='You won!')

    def randomizeNewGame(self):
        numSteps = random.randint(10, 80)
        for i in range(numSteps):
            blank_row = self.blankPosition // 4
            blank_col = self.blankPosition % 4
            newPossibleBlankPositions = []
            if blank_col != 0 and blank_col != 3:
                newPossibleBlankPositions.extend([self.blankPosition - 1, self.blankPosition + 1])
            elif blank_col == 0:
                newPossibleBlankPositions.append(self.blankPosition + 1)
            elif blank_col == 3:
                newPossibleBlankPositions.append(self.blankPosition - 1)

            if blank_row != 0 and blank_row != 3:
                newPossibleBlankPositions.extend([self.blankPosition - 4, self.blankPosition + 4])
            elif blank_row == 0:
                newPossibleBlankPositions.append(self.blankPosition + 4)
            elif blank_row == 3:
                newPossibleBlankPositions.append(self.blankPosition - 4)

            newBlankPosition = random.choice(newPossibleBlankPositions)  # coord of button
            idx = self.currentPositions.index(newBlankPosition)
            self.currentPositions[idx] = self.blankPosition
            self.blankPosition = newBlankPosition

        # reposition buttons
        for i, button in enumerate(self.gameButtons):
            row = self.currentPositions[i] // 4
            column = self.currentPositions[i] % 4
            button.grid(row=row, column=column, sticky='NSEW')


def main():
    game = FifteenGame()
    game.master.title('Fifteen Game')
    game.mainloop()


if __name__ == '__main__':
    main()
