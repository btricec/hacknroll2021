import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import pygame

pygame.mixer.init()

def play():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops = 2)

play()

class Player():
    def __init__(self, name, acad, p_health, social_life):
        self.name = name
        self.acad = acad
        self.p_health = p_health
        self.social_life = social_life
        self.m_health = 5
        self.money = 10

    # 1 for add 0 for subtract
    def editPHealth(self, value, action):
        if action == 1:
            self.p_health += value
        else:
            self.p_health -= value

    def editMHealth(self, value, action):
        if action == 1:
            self.m_health += value
        else:
            self.m_health -= value

    def editSL(self, value, action):
        if action == 1:
            self.social_life += value
        else:
            self.social_life -= value

    def editAcad(self, value, action):
        if action == 1:
            self.acad += value
        else:
            self.acad -= value

    def editMoney(self, value, action):
        if action == 1:
            self.money += value
        else:
            self.money -= value

player = Player("nil", 0, 0, 0)

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        stats_frame = tk.Frame(self)
        phy_health = tk.Label(stats_frame, text="Physical Health: 0", padx=20).pack(side="left")
        mental_health = tk.Label(stats_frame, text="Mental Health: 0", padx=20).pack(side="left")
        social_life = tk.Label(stats_frame, text="Social Life: 0", padx=20).pack(side="left")
        acad = tk.Label(stats_frame, text="Academics: 0", padx=20).pack(side="left")
        money = tk.Label(stats_frame, text="Money: 0", padx=20).pack(side="left")

        stats_frame.place(x=0, y=0)

        container = tk.Frame(self)
##        container.pack(side="top", fill="both", expand=True)
        container.place(x=0, y=30)
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
        # update stats

        stats_frame = tk.Frame(self)
        phy_health = tk.Label(stats_frame, text="Physical Health:" + str(player.p_health), padx=20).pack(side="left")
        mental_health = tk.Label(stats_frame, text="Mental Health:" + str(player.m_health), padx=20).pack(side="left")
        social_life = tk.Label(stats_frame, text="Social Life:" + str(player.social_life), padx=20).pack(side="left")
        acad = tk.Label(stats_frame, text="Academics:" + str(player.acad), padx=20).pack(side="left")
        money = tk.Label(stats_frame, text="Money:" + str(player.money), padx=20).pack(side="left")

        stats_frame.place(x=0, y=0)

        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = ttk.Label(self, text="This is the start page", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2)

        name_label = tk.Label(self, text="Enter your name: ").grid(row=1, column=0)
        name = tk.Entry(self)
        name.grid(row=1, column=1)

##        self.img = ImageTk.PhotoImage(file="characters.png")
##        img_label = ttk.Label(self, image=self.img)
##        img_label.pack()

        self.Student1=ImageTk.PhotoImage(Image.open("Student1.jpeg").resize((300, 200)))
        self.Student2=ImageTk.PhotoImage(Image.open("Student2.jpeg").resize((300, 200)))
        self.Student3=ImageTk.PhotoImage(Image.open("Student3.jpeg").resize((300, 200)))
        self.Student4=ImageTk.PhotoImage(Image.open("Student4.jpeg").resize((300, 200)))

        opt1 = tk.Button(self, image = self.Student1, command=lambda: self.drMagic(name.get(), controller)).grid(row=2, column=0, columnspan=2)
        opt2 = tk.Button(self, image = self.Student2, command=lambda: self.snakeMaster(name.get(), controller)).grid(row=2, column=2, columnspan=2)
        opt3 = tk.Button(self, image = self.Student3, command=lambda: self.wonderGuitar(name.get(), controller)).grid(row=3, column=0, columnspan=2)
        opt4 = tk.Button(self, image = self.Student4, command=lambda: self.tricepMan(name.get(), controller)).grid(row=3, column=2, columnspan=2)

    def drMagic(self, name, controller):
        global player
        player = Player(name, 7, 5, 8)
        text = tk.Label(self, text="Hello " + name + " you have chosen Dr Magic!", padx=40).grid(row=4, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=5, column=0, columnspan=2)

    def snakeMaster(self, name, controller):
        global player
        player = Player(name, 9, 5, 6)
        text = tk.Label(self, text="Hello " + name + " you have chosen Snake Master!", padx=40).grid(row=4, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=5, column=0, columnspan=2)

    def wonderGuitar(self, name, controller):
        global player
        player = Player(name, 6, 5, 9)
        text = tk.Label(self, text="Hello " + name + " you have chosen Wonder Guitar!", padx=40).grid(row=4, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=5, column=0, columnspan=2)

    def tricepMan(self, name, controller):
        global player
        player = Player(name, 4, 9, 7)
        text = tk.Label(self, text="Hello " + name + " you have chosen Tricep Man!", padx=40).grid(row=4, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=5, column=0, columnspan=2)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Scenario 1 goes here ", font=controller.title_font).grid(row=1, column=0, columnspan=4)
        #label.pack(side="top", fill="x", pady=10)

        self.img = ImageTk.PhotoImage(file="placeholder.png")
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0, columnspan=4)

        opt1 = ttk.Button(self, text="Option 1", command=lambda: self.option1(controller)).grid(row=3, column=0, columnspan=2)
        opt2 = ttk.Button(self, text="Option 2").grid(row=3, column=2, columnspan=2)
        opt3 = ttk.Button(self, text="Option 3").grid(row=4, column=0, columnspan=2)
        opt4 = ttk.Button(self, text="Option 4").grid(row=4, column=2, columnspan=2)
##        home_button = ttk.Button(self, text="Home",
##                           command=lambda: controller.show_frame("StartPage")).grid(row=5, column=1)

    def option1(self, controller):
        player.editPHealth(100, 1)
        text = tk.Label(self, text="+100 health!").grid(row=5, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=1, columnspan=2)

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
    app.wm_geometry("1000x1000")
    app.mainloop()
