import tkinter as tk


class GraphEdit(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.enableStretching()
        self.grid(sticky='NSEW')

    def createWidgets(self):
        self.textEditor = tk.Text(self, undo=True, wrap=tk.WORD)
        self.colorPicker = tk.Button(self, text='Color')
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.graphEditor = tk.Canvas(self, bg='#eeeeee')
        self.textEditor.grid(row=0, column=0, rowspan=2, sticky='NSEW')
        self.colorPicker.grid(row=0, column=1, sticky='NSEW')
        self.quitButton.grid(row=0, column=2, sticky='NSEW')
        self.graphEditor.grid(row=1, column=1, columnspan=2, sticky='NSEW')

        self.graphEditor.bind('<ButtonPress-1>', self.select_oval)
        self.graphEditor.bind('<B1-Motion>', self.change_oval)
        self.graphEditor.bind('<ButtonRelease-1>', self.release_oval)

    def enableStretching(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1, minsize=60, pad=2)
        self.columnconfigure(0, weight=1, minsize=100, pad=2)
        self.rowconfigure(1, weight=1, minsize=100)
        self.columnconfigure(1, weight=1, minsize=50, pad=2)
        self.columnconfigure(2, weight=1, minsize=50, pad=2)

    def select_oval(self, event):
        self.startX = event.x
        self.startY = event.y
        self.figures = self.graphEditor.create_oval(event.x, event.y, event.x, event.y)
        #logic for existing ovals

    def change_oval(self, event):
        self.graphEditor.coords(self.figures, self.startX, self.startY, event.x, event.y)

    def release_oval(self, event):
        pass


def main():
    app = GraphEdit()
    app.master.title('Graph Edit')
    app.mainloop()


if __name__ == '__main__':
    main()