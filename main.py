import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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

    def warning(self):
        warnings = []
        if self.acad < 3:
            warnings.append("academics")
        if self.social_life < 3:
            warnings.append("social life")
        if self.p_health < 3:
            warnings.append("physical health")
        if self.m_health < 3:
            warnings.append("mental health")
        if self.money < 3:
            warnings.append("money")
        return warnings

    def gameOver(self):
        if self.acad < 1:
            return "Academics"
        if self.social_life < 1:
            return "Social life"
        if self.p_health < 1:
            return "Physical health"
        if self.m_health < 1:
            return "Mental health"
        if self.money < 1:
            return "Money"
        return "none"

player = Player("nil", 10, 10, 10)


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

        self.container = tk.Frame(self)
##        container.pack(side="top", fill="both", expand=True)
        self.container.place(x=0, y=30)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def doChecks(self):
        end = player.gameOver()
        if end != "none":
            frame = PageGameover(parent=self.container, controller=self, stat=end)
            frame.tkraise()
            return
            
        warnings = player.warning()
        if len(warnings) == 1:
            messagebox.showwarning("WARNING!", warnings[0] + " has fallen below 3!")
        elif len(warnings) > 1:
            string = ""
            for i in warnings:
                string += (i + " and ")
            messagebox.showwarning("WARNING!", string + "has fallen below 3!")

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

        self.doChecks()


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
            text = tk.Label(self, text="Feeling prepared for the new semester! ᕙ(`▽´)ᕗ \n +1 academics",
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

        self.opt1 = ttk.Button(self, text="Submit anyway, and go for a drink to celebrate",
                          command=lambda: self.option2(controller))
        #  and put .grid() in a new line :)
        self.opt1.grid(row=2, column=0)
        
        self.opt2 = ttk.Button(self, text="Email your professor and ask for an extension",
                          command=lambda: self.option1(controller))
        #  and put .grid() in a new line :)
        self.opt2.grid(row=3, column=0)
        
        self.opt3 = ttk.Button(self, text="Upload an empty document",
                          command=lambda: self.option3(controller))
        #  and put .grid() in a new line :)
        self.opt3.grid(row=4, column=0)
        
        self.opt4 = ttk.Button(self, text="Just submit late and pray professor won’t find out",
                          command=lambda: self.option1(controller))
        #  and put .grid() in a new line :)
        self.opt4.grid(row=5, column=0)
        

    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED
        
    def option1(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("ddl/ddl_response1a.png").resize((480, 270)))
        self.img2 = ImageTk.PhotoImage(Image.open("ddl/ddl_response1b.png").resize((480, 270)))
        
        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=1, columnspan=2)
        
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
            player.editMHealth(-1, 1)
            player.editAcad(-1, 1)
        else:
            text = tk.Label(self, image=self.img2).grid(row=7, column=0, columnspan=4)
            player.editMHealth(1, 1)
            player.editAcad(1, 1)
            
    def option2(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("ddl/ddl_response2.png").resize((480, 270)))
        
        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=1, columnspan=2)
        
        outcome = random.randint(0,9)
        player.editAcad(-2,1)
        player.editMHealth(1,1)
        player.editPHealth(-1, 1)
        player.editSL(1,1)
        
    def option3(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("ddl/ddl_response3a.png").resize((480, 270)))
        self.img2 = ImageTk.PhotoImage(Image.open("ddl/ddl_response3b.png").resize((480, 270)))
        
        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=1, columnspan=2)
        
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
            player.editMHealth(1, 1)
            player.editAcad(1, 1)
            player.editPHealth(-1, 1)
        else:
            text = tk.Label(self, image=self.img2).grid(row=7, column=0, columnspan=4)
            player.editMHealth(-1, 1)
            player.editAcad(-2, 1)
            player.editPHealth(-1, 1)

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(file="snack.png")
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=0, column=0)

        # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Raid the pantry (even though you own nothing inside)",
                          command=lambda: self.option1(controller))
        #  and put .grid() in a new line :)
        self.opt1.grid(row=1, column=0)
        self.opt2 = ttk.Button(self, text="Call GrabFood",
                          command=lambda: self.option2(controller))
        self.opt2.grid(row=2, column=0)
        self.opt3 = ttk.Button(self, text="Jio friends to go supper stretch with you",
                          command=lambda: self.option3(controller))
        self.opt3.grid(row=3, column=0)
        self.opt4 = ttk.Button(self, text="On a diet, ignore it",
                          command=lambda: self.option4(controller))
        self.opt4.grid(row=4, column=0)

    # makes sure player cannot choose another option after pressing a button
    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()

        outcome = random.randint(0,2)

        if outcome == 0:
            text = tk.Label(self, text="Found a tub of Ben and Jerry's ice cream in the fridge, score!! \n -1 physical health ",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editMHealth(1, 0)
            player.editAcad(2, 1)
        elif outcome == 1:
            text = tk.Label(self, text="""Found a packet of Indomie on the counter!
While cooking it, Indomie owner walks in and catches you in the act ヽ(`Д´)ﾉ
Now you are known as the resident food theif...
-1 social life, -1 mental health """,
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 0)
            player.editPHealth(1, 0)
        else:
            text = tk.Label(self, text="""Found some yogurt and a banana!
Yogurt tasted a bit funny... Turned out to be expired (≧︿≦)
Spent a day on the toilet!
-2 physical health""",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
        player.editPHealth(2, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)


    def option2(self, controller):
        self.disable_buttons()

        text = tk.Label(self, text="Stomach is happy, wallet is not\n -2 money ",
                        font=controller.title_font, wraplength=1000).grid(row=5, column=0)
        player.editMoney(2, 0)
        
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/4 chance to get bad outcome
        outcome = random.randint(0,3)

        if outcome == 0:
            text = tk.Label(self, text="None of your friends wanted to eat supper with you... \n -1 social life, -1 mental health",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 0)
            player.editMHealth(1, 0)
        else:
            text = tk.Label(self, text="Prata and cheese fries... YUM \n +1 social life, -1 money",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editMoney(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)


    def option4(self, controller):
        self.disable_buttons()

        # 1/4 chance to get bad outcome
        outcome = random.randint(0,3)

        if outcome == 0:
            text = tk.Label(self, text="So hungry... Could not sleep\n Ending up binge eating D: \n -1 physical health, -1 mental health",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)
            player.MHealth(1, 0)
            player.MHealth(1, 0)
        else:
            text = tk.Label(self, text="Can't feel hungry if you're sleeping! Woke up and had a good breakfast. \n - no changes -",
                            font=controller.title_font, wraplength=1000).grid(row=5, column=0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scenario 2 goes here", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame("PageFive"))
        button.pack()

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #label = tk.Label(self, text="It is the last day of your orientation camp! ", font=controller.title_font).grid(row=1, column=0, columnspan=4)
        
        self.img = ImageTk.PhotoImage(Image.open("sick/sick.png").resize((480, 270)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0, columnspan=4)

        # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Go to class to impress the professor. Complete the assignment because you are never late",
                          command=lambda: self.option1(controller))
        self.opt1.grid(row=2, column=0)
        
        self.opt2 = ttk.Button(self, text="Email the professor using your last energy, and go to the hospital ",
                          command=lambda: self.option2(controller))
        #  and put .grid() in a new line :)
        self.opt2.grid(row=3, column=0)

        self.opt3 = ttk.Button(self, text="Lie on the bed like it's the end of the world",
                          command=lambda: self.option3(controller))
        self.opt3.grid(row=4, column=0)
        self.opt4 = ttk.Button(self, text="Spam everyone you know and cry to them",
                          command=lambda: self.option4(controller))
        self.opt4.grid(row=5, column=0)
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

        text = tk.Label(self, text="It is COVID time. You NEVER go to class when you are sick!!!! \n -2 physical life, -1 mental health",
                        font=controller.title_font, wraplength=1000).grid(row=6, column=0)
        player.editMHealth(-1, 1)
        player.editPHealth(-2, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSix")).grid(row=7, column=0)

    def option2(self, controller):
        self.disable_buttons()

        # 1/10 chace to get a bad outcome
        text = tk.Label(self, text="It is obviously what human being do when they are sick. Good job kid. \n - no changes -",
                        font=controller.title_font, wraplength=1000).grid(row=6, column=0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSix")).grid(row=7, column=0)
    
    
    def option3(self, controller):
        self.disable_buttons()

        # 1/10 chace to get a bad outcome
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text="""You fell asleep. It is 9 pm when you wake up again.
You have missed all the classes and deadlines. Luckily, you feel better now.
Academics -1 """,
                            font=controller.title_font, wraplength=1000).grid(row=6, column=0)
            player.editAcad(-1,1)
        else:
            text = tk.Label(self, text="""You got sicker and sicker. You waked up in hospital.
Your friend called you an ambulance.
Money -5, Physical health -2, Mental health -2""",
                            font=controller.title_font, wraplength=1000).grid(row=6, column=0)
            player.editMHealth(-2, 1)
            player.editMoney(-5, 1)
            player.editPHealth(-2, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSix")).grid(row=7, column=0)


    def option4(self, controller):
        #self.disable_buttons()

        # 1/10 chace to get a bad outcome
        outcome = random.randint(0,9)

        if outcome == 0:
            text = tk.Label(self, text="""Your friend sends you to the hospital.
Everyone knew you were sick, and got presents for you!.
Social life +1, Mental health +1""",
                            font=controller.title_font, wraplength=1000).grid(row=6, column=0)
            player.editSL(-1, 1)
            player.editMHealth(1, 1)

        else:
            text = tk.Label(self, text="Nobody replied your message, so you were greatly depressed \n Mental health -1, Physical health -1",
                            font=controller.title_font, wraplength=1000).grid(row=6, column=0)
            player.editPHealth(-1, 1)
            player.editMHealth(-1, 1)

        next_button = ttk.Button(self, text="Next",
                                 command=lambda: controller.show_frame("PageSix")).grid(row=7, column=0)

class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scenario 2 goes here", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()

class PageGameover(tk.Frame):

    def __init__(self, parent, controller, stat):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=stat + " has fallen below 0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Home",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.wm_geometry("1000x1000")
    app.mainloop()
