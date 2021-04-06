import tkinter as tk


class GraphEdit(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.enableStretching()
        self.grid(sticky='NSEW')
        self.figures = []
        self.selected = False

    def createWidgets(self):
        self.textEditor = tk.Text(self, undo=True, wrap=tk.WORD)
        self.colorPicker = tk.Button(self, text='Color')
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.graphEditor = tk.Canvas(self, bg='#eeeeee')
        self.textEditor.grid(row=0, column=0, rowspan=2, sticky='NSEW')
        self.colorPicker.grid(row=0, column=1, sticky='NSEW')
        self.quitButton.grid(row=0, column=2, sticky='NSEW')
        self.graphEditor.grid(row=1, column=1, columnspan=2, sticky='NSEW')

        self.graphEditor.bind('<ButtonPress-1>', self.draw_oval)
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

    def draw_oval(self, event):
        if self.selected == True:
            return
        self.selected = False
        self.startX = event.x
        self.startY = event.y
        self.curId = self.graphEditor.create_oval(event.x, event.y, event.x, event.y, fill='#cccccc')
        self.graphEditor.tag_bind(self.curId, '<Button>', self.select_oval)
        self.figures.append(self.curId)

    def change_oval(self, event):
        if self.selected == False:
            self.graphEditor.coords(self.curId, self.startX, self.startY, event.x, event.y)
        else:
            self.graphEditor.move(self.curId, event.x - self.startX, event.y - self.startY)
            self.startX = event.x
            self.startY = event.y

    def release_oval(self, event):
        self.selected = False
        self.description = f'Oval {self.curId} {self.startX} {self.startY} {event.x} {event.y}\n'
        self.textEditor.insert(tk.END, self.description)

    def select_oval(self, event):
        self.selected = True
        self.startX = event.x
        self.startY = event.y
        self.curId = event.widget.find_closest(event.x, event.y)


def main():
    app = GraphEdit()
    app.master.title('Graph Edit')
    app.mainloop()


if __name__ == '__main__':
    main()