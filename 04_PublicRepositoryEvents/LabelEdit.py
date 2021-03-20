import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master):
        tk.Label.__init__(self, master)
        self.master = master


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()
        self.pack()


    def createWidgets(self):
        self.label = InputLabel(self)
        self.label.pack()
        self.button = tk.Button(self, text='QUIT', command=quit)
        self.button.pack()


def main():
    app = Application()
    app.master.title('Label Edit')
    app.mainloop()


if __name__ == '__main__':
    main()