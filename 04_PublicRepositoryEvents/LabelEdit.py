import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master):
        tk.Label.__init__(self, master,
                          cursor='xterm',
                          highlightthickness=1,
                          padx=2,
                          pady=2,
                          takefocus=1,
                          width=20)
        self.master = master


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.bind('<Button-1>', self.on_mouse_click)
        self.pack()

    def createWidgets(self):
        self.label = InputLabel(self)
        self.label.bind('<Button-1>', self.on_mouse_click)
        self.label.pack()
        self.button = tk.Button(self, text='QUIT', command=quit)
        self.button.pack()

    def on_mouse_click(self, event):
        event.widget.focus_set()


def main():
    app = Application()
    app.master.title('Label Edit')
    app.mainloop()


if __name__ == '__main__':
    main()