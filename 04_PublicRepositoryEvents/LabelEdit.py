import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master):
        self.stringVar = tk.StringVar()
        self.cursorPosition = 0
        tk.Label.__init__(self, master,
                          anchor='w',
                          cursor='xterm',
                          highlightthickness=1,
                          padx=2,
                          pady=2,
                          takefocus=1,
                          textvariable=self.stringVar,
                          width=20)
        self.master = master
        self.bind('<Button-1>', self.on_mouse_click)
        self.bind('<Key>', self.on_key_pressed)

    def on_mouse_click(self, event):
        event.widget.focus_set()

    def on_key_pressed(self, event):
        if self.focus_get() is self:
            if event.char.isprintable() and len(event.char) > 0:
                s = self.stringVar.get()
                self.stringVar.set(s[:self.cursorPosition] + event.char + s[self.cursorPosition:])
                self.cursorPosition += 1
            if event.keysym == 'Left' or event.keysym == 'Home':
                self.cursorPosition = max(self.cursorPosition - 1, 0)
            if event.keysym == 'Right' or event.keysym == 'End':
                self.cursorPosition = min(self.cursorPosition + 1, len(self.stringVar.get()))


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