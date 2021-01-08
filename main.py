import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import pygame
import random

##pygame.mixer.init()
##
##def play():
##    pygame.mixer.music.load("song.mp3")
##    pygame.mixer.music.play(loops = 2)
##
##play()

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
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
        label = ttk.Label(self, text="Are you ready for your first semester of college??", font=controller.title_font)
        label.grid(row=0, column=0, columnspan=2)

        name_label = tk.Label(self, text="Enter your name and choose an avatar to start ").grid(row=1, column=0)
        name = tk.Entry(self)
        name.grid(row=1, column=1)

##        self.img = ImageTk.PhotoImage(file="characters.png")
##        img_label = ttk.Label(self, image=self.img)
##        img_label.pack()

        self.Student1=ImageTk.PhotoImage(Image.open("Student1.jpeg").resize((250, 200)))
        self.Student2=ImageTk.PhotoImage(Image.open("Student2.jpeg").resize((250, 200)))
        self.Student3=ImageTk.PhotoImage(Image.open("Student3.jpeg").resize((250, 200)))
        self.Student4=ImageTk.PhotoImage(Image.open("Student4.jpeg").resize((250, 200)))

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

        #label = tk.Label(self, text="It is the last day of your orientation camp! ", font=controller.title_font).grid(row=1, column=0, columnspan=4)

        self.img = ImageTk.PhotoImage(file="orientation.png")
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=0, column=0)

        # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Go Clubbing! WOOHOO ♪┏(・o･)┛♪",
                          command=lambda: self.option1(controller))
        #  and put .grid() in a new line :)
        self.opt1.grid(row=1, column=0)
        self.opt2 = ttk.Button(self, text="Camp was tiring, go home and sleep",
                          command=lambda: self.option2(controller))
        self.opt2.grid(row=2, column=0)
        self.opt3 = ttk.Button(self, text="School is starting, need to study!!",
                          command=lambda: self.option3(controller))
        self.opt3.grid(row=3, column=0)
        self.opt4 = ttk.Button(self, text="Was that a prof you saw?? Go stalk him ☉ ‿ ⚆",
                          command=lambda: self.option4(controller))
        self.opt4.grid(row=4, column=0)
##        home_button = ttk.Button(self, text="Home",
##                           command=lambda: controller.show_frame("StartPage")).grid(row=5, column=1)

    # makes sure plaer cannot choose another option after pressing a button
    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()

        # 1/2 chance to get bad outcome
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text="You had a great time dancing and drinking with your friends :D \n +1 social life, -2 money",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editMoney(2, 0)
        else:
            text = tk.Label(self, text="You got drunk and puked all over your friend (ew gross) \n -1 social life, -2 money",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 0)
            player.editMoney(2, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option2(self, controller):
        self.disable_buttons()

        # 1/10 chace to get a bad outcome
        outcome = random.randint(0,9)

        if outcome == 0:
            text = tk.Label(self, text="You fell asleep on the bus ride and missed your stop! \n - no changes -",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
        else:
            text = tk.Label(self, text="You had a great rest ^^ \n +1 mental health",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editPHealth(1, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/4 chace to get a bad outcome
        outcome = random.randint(0,4)

        if outcome == 0:
            text = tk.Label(self, text="Feeling stressed and overworked even before school starts! \n +2 academics, -1 mental health",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editMHealth(1, 0)
            player.editAcad(2, 1)
        else:
            text = tk.Label(self, text="Feeling stressed prepared for the new semester! ᕙ(`▽´)ᕗ \n +1 academics",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option4(self, controller):
        self.disable_buttons()

        # good social skills, 
        if player.social_life >= 8:
            text = tk.Label(self, text="Thanks to your great social skills, you and prof are now good friends~ \n +1 social life, +1 academics",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editAcad(1, 1)
        else:
            text = tk.Label(self, text="People think you're slightly weird :( \n -1 social life, -1 mental health",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editMHealth(1, 0)
            player.editSL(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Scenario 1 goes here ", font=controller.title_font).grid(row=1, column=0, columnspan=4)
        #label.pack(side="top", fill="x", pady=10)
        
        
        self.img = ImageTk.PhotoImage(Image.open("ddl/ddl.png").resize((480, 270)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0, columnspan=4)

        self.opt1 = ttk.Button(self, text="Submit anyway, and go for a drink to celebrate", command=lambda: self.option2(controller))
        self.opt1.grid(row=3, column=0, columnspan=2)
        self.opt2 = ttk.Button(self, text="Email your professor and ask for an extension", command=lambda: self.option1(controller))
        self.opt2.grid(row=4, column=0, columnspan=2)
        self.opt3 = ttk.Button(self, text="Upload an empty document", command=lambda: self.option1(controller))
        self.opt3.grid(row=5, column=0, columnspan=2)
        self.opt4 = ttk.Button(self, text="Just submit late and pray professor won’t find out", command=lambda: self.option1(controller))
        self.opt4.grid(row=6, column=0, columnspan=2)

    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("ddl/ddl_response1a.png").resize((400, 200)))
        self.img2 = ImageTk.PhotoImage(Image.open("ddl/ddl_response1b.png").resize((400, 200)))
        
        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=1, columnspan=2)
        
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
            player.editmHealth(-1, 1)
            player.editAcad(-1, 1)
        else:
            text = tk.Label(self, image=self.img2).grid(row=7, column=0, columnspan=4)
            player.editmHealth(1, 1)
            player.editAcad(1, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=0)
            
    def option2(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("ddl/ddl_response2.png").resize((400, 200)))
        
        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=1, columnspan=2)
        
        outcome = random.randint(0,9)
        player.editAcad(-2,1)
        player.editmHealth(1,1)
        player.editPHealth(-1, 1)
        plaer.editSL(1,1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=9, column=0)

##class PageTwo(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        self.controller = controller
##
##        self.img = ImageTk.PhotoImage(file="orientation.png")
##        img_label = tk.Label(self, image=self.img)
##        img_label.grid(row=0, column=0)
##
##        # make all buttons an attribute of the class (i.e. self.opt1)
##        self.opt1 = ttk.Button(self, text="Go Clubbing! WOOHOO ♪┏(・o･)┛♪",
##                          command=lambda: self.option1(controller))
##        #  and put .grid() in a new line :)
##        self.opt1.grid(row=1, column=0)
##        self.opt2 = ttk.Button(self, text="Camp was tiring, go home and sleep",
##                          command=lambda: self.option2(controller))
##        self.opt2.grid(row=2, column=0)
##        self.opt3 = ttk.Button(self, text="School is starting, need to study!!",
##                          command=lambda: self.option3(controller))
##        self.opt3.grid(row=3, column=0)
##        self.opt4 = ttk.Button(self, text="Was that a prof you saw?? Go stalk him ☉ ‿ ⚆",
##                          command=lambda: self.option4(controller))
##        self.opt4.grid(row=4, column=0)
####        home_button = ttk.Button(self, text="Home",
####                           command=lambda: controller.show_frame("StartPage")).grid(row=5, column=1)
##
##    # makes sure plaer cannot choose another option after pressing a button
##    def disable_buttons(self):
##        self.opt1['state'] = tk.DISABLED
##        self.opt2['state'] = tk.DISABLED
##        self.opt3['state'] = tk.DISABLED
##        self.opt4['state'] = tk.DISABLED
##
##    def option1(self, controller):
##
##
##    def option2(self, controller):
##
##
##    def option3(self, controller):
##
##
##    def option4(self, controller):
        

class PageThree(tk.Frame):

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
