import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import ImageTk, Image

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        self.img = ImageTk.PhotoImage(file="characters.png")
        img_label = ttk.Label(self, image=self.img)
        img_label.pack()

        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
##        button2 = tk.Button(self, text="Go to Page Two",
##                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
##        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        stats_frame = tk.Frame(self)
        phy_health = tk.Label(stats_frame, text="Physical Health:").pack(side="left")
        mental_health = tk.Label(stats_frame, text="Mental Health:").pack(side="left")
        social_life = tk.Label(stats_frame, text="Social Life:").pack(side="left")
        acad = tk.Label(stats_frame, text="Academics:").pack(side="left")
        money = tk.Label(stats_frame, text="Money:").pack(side="left")

        stats_frame.grid(row=0, column=0, columnspan=4)
        
        label = tk.Label(self, text="Scenario 1 goes here ", font=controller.title_font).grid(row=1, column=0, columnspan=4)
        #label.pack(side="top", fill="x", pady=10)

        self.img = ImageTk.PhotoImage(file="placeholder.png")
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0, columnspan=4)
        
        opt1 = ttk.Button(self, text="Option 1").grid(row=3, column=0, columnspan=2)
        opt2 = ttk.Button(self, text="Option 2").grid(row=3, column=2, columnspan=2)
        opt3 = ttk.Button(self, text="Option 3").grid(row=4, column=0, columnspan=2)
        opt4 = ttk.Button(self, text="Option 4").grid(row=4, column=2, columnspan=2)
        home_button = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage")).grid(row=5, column=1)
        next_button = ttk.Button(self, text="Next",
                                command=lambda: controller.show_frame("PageTwo")).grid(row=5, column=2)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scenario 2 goes here", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
