import tkinter as tk


class GraphEdit(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.grid()

    def createWidgets(self):
        self.textEditor = tk.Text(self, undo=True, wrap=tk.WORD)
        self.colorPicker = tk.Button(self, text='Color')
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.graphEditor = tk.Canvas(self)
        self.textEditor.grid(row=0, column=0, rowspan=2)
        self.colorPicker.grid(row=0, column=1)
        self.quitButton.grid(row=0, column=2)
        self.graphEditor.grid(row=1, column=1, columnspan=2)


def main():
    app = GraphEdit()
    app.master.title('Graph Edit')
    app.mainloop()


if __name__ == '__main__':
    main()