import tkinter as tk
from tkinter import font

class InputLabel(tk.Label):
    def __init__(self, master):
        self.stringVar = tk.StringVar()
        self.cursorPosition = 0
        self.labelFont = font.Font(family='Courier New', size=12, weight='normal')
        self.initialWidth = 10
        tk.Label.__init__(self, master,
                          anchor='w',
                          cursor='xterm',
                          font=self.labelFont,
                          highlightthickness=1,
                          padx=2,
                          pady=2,
                          takefocus=1,
                          textvariable=self.stringVar,
                          width=self.initialWidth)
        self.master = master
        self.cursor = tk.Frame(self, bg='#333333')
        self.cursor.place(relheight=0.98, width=2)

        self.bind('<Button-1>', self.on_mouse_click)
        self.bind('<Key>', self.on_key_pressed)
        self.bind('<FocusIn>', self.activate_cursor)
        self.bind('<FocusOut>', self.deactivate_cursor)

    def on_mouse_click(self, event):
        event.widget.focus_set()

    def activate_cursor(self, event):
        self.cursor.configure(bg='#cccccc')

    def deactivate_cursor(self, event):
        self.cursor.configure(bg='#333333')

    def move_cursor(self):
        s = self.stringVar.get()[:self.cursorPosition]
        textLengthInPixels = self.labelFont.measure(s)
        self.cursor.place(x=textLengthInPixels)

    def on_key_pressed(self, event):
        if self.focus_get() is self:
            if event.char.isprintable() and len(event.char) > 0:
                s = self.stringVar.get()
                self.stringVar.set(s[:self.cursorPosition] + event.char + s[self.cursorPosition:])
                self.cursorPosition += 1
                self.configure(width=max(self.initialWidth, len(s) + 1))
                self.move_cursor()
            if event.keysym == 'Left' or event.keysym == 'Home':
                self.cursorPosition = max(self.cursorPosition - 1, 0)
                self.move_cursor()
            if event.keysym == 'Right' or event.keysym == 'End':
                self.cursorPosition = min(self.cursorPosition + 1, len(self.stringVar.get()))
                self.move_cursor()


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