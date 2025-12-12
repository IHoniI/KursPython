import random
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None, title="Kostka"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title(title)
        self.pack()   # self to master
        self.create_widgets()

    def create_widgets(self):
        self.out = tk.StringVar()
        self.out.set("rzuć")

        self.label1 = tk.Label(self, text="Wynik:", font="Times 20")
        self.label1.pack()   # label to self

        self.label_outcome = tk.Label(self, textvariable=self.out, font="Times 40")
        self.label_outcome.pack()

        self.label_describe = tk.Label(self, text="Kliknij przycisk aby rzucić kostką")
        self.label_describe.pack()

        self.button1 = tk.Button(self, text="Rzuć kostką", bg="lightblue", font="Times 20", command=self.on_click)
        self.button1.pack()

    def on_click(self):
        self.out.set(str(random.randint(1,6)))

if __name__ == "__main__":

    root = tk.Tk()
    app = Application(root)
    root.mainloop()
