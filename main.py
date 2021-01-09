import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont
from PIL import ImageTk, Image
import pygame
import random

pygame.mixer.init()

def play():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops = 2)

play()

gameover = "none"
final = "none"

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
        global gameover
        if self.acad < 1:
            gameover = "Academics"
        elif self.social_life < 1:
            gameover = "Social life"
        elif self.p_health < 1:
            gameover = "Physical health"
        elif self.m_health < 1:
            gameover = "Mental health"
        elif self.money < 1:
            gameover = "Money"

    def final(self):
        global final
        if max(self.acad,self.social_life,self.p_health) == self.acad:
            final = "Academics"
        elif max(self.acad,self.social_life,self.p_health)== self.social_life:
            final = "Social life"
        elif max(self.acad,self.social_life,self.p_health) == self.p_health:
            final = "Physical health"


player = Player("nil", 10, 10, 10)

def restart_program():
    import sys
    import os
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


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
        self.container.place(x=0, y=30)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def doChecks(self):
        warnings = player.warning()
        if len(warnings) == 1:
            messagebox.showwarning("WARNING!", warnings[0] + " is below 3!")
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
        player.gameOver()

        if gameover != "none":
            frame = PageGameover(parent=self.container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()
        elif page_name == "Final":
            player.final()
            frame = Final(parent=self.container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.tkraise()
        elif page_name == "PageEight":
            frame = self.frames[page_name]
            frame.tkraise()
        else:
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

        self.Student1=ImageTk.PhotoImage(Image.open("pic/Student1.png").resize((300, 200)))
        self.Student2=ImageTk.PhotoImage(Image.open("pic/Student2.png").resize((300, 200)))
        self.Student3=ImageTk.PhotoImage(Image.open("pic/Student3.png").resize((300, 200)))
        self.Student4=ImageTk.PhotoImage(Image.open("pic/Student4.png").resize((300, 200)))

        opt1 = tk.Button(self, image = self.Student1, command=lambda: self.drMagic(name.get(), controller)).grid(row=2, column=0)
        opt2 = tk.Button(self, image = self.Student2, command=lambda: self.snakeMaster(name.get(), controller)).grid(row=2, column=1)
        opt3 = tk.Button(self, image = self.Student3, command=lambda: self.wonderGuitar(name.get(), controller)).grid(row=3, column=0)
        opt4 = tk.Button(self, image = self.Student4, command=lambda: self.tricepMan(name.get(), controller)).grid(row=3, column=1)

    def drMagic(self, name, controller):
        global player
        player = Player(name, 7, 5, 8)
        text = tk.Label(self, text="Hello " + name + ", you have chosen Dr Magic!", padx=40).grid(row=4, column=0, columnspan=2)
        text2 = tk.Label(self, text="""Read each scenario and make a choice!
Every choice will affect your stats, make sure none drop to 0, or else the game will end!
Can you survive your first semester? Good luck!""", wraplength=580).grid(row=5, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=6, column=0, columnspan=2)

    def snakeMaster(self, name, controller):
        global player
        player = Player(name, 9, 5, 6)
        text = tk.Label(self, text="Hello " + name + ", you have chosen Snake Master!", padx=40).grid(row=4, column=0, columnspan=2)
        text2 = tk.Label(self, text="""Read each scenario and make a choice!
Every choice will affect your stats, make sure none drop to 0, or else the game will end!
Can you survive your first semester? Good luck!""", wraplength=580).grid(row=5, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=6, column=0, columnspan=2)

    def wonderGuitar(self, name, controller):
        global player
        player = Player(name, 6, 5, 9)
        text = tk.Label(self, text="Hello " + name + ", you have chosen Wonder Guitar!", padx=40).grid(row=4, column=0, columnspan=2)
        text2 = tk.Label(self, text="""Read each scenario and make a choice!
Every choice will affect your stats, make sure none drop to 0, or else the game will end!
Can you survive your first semester? Good luck!""", wraplength=580).grid(row=5, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=6, column=0, columnspan=2)

    def tricepMan(self, name, controller):
        global player
        player = Player(name, 4, 9, 7)
        text = tk.Label(self, text="Hello " + name + ", you have chosen Tricep Man!", padx=40).grid(row=4, column=0, columnspan=2)
        text2 = tk.Label(self, text="""Read each scenario and make a choice!
Every choice will affect your stats, make sure none drop to 0, or else the game will end!
Can you survive your first semester? Good luck!""", wraplength=580).grid(row=5, column=0, columnspan=2)
        button1 = ttk.Button(self, text="Start Game",
                            command=lambda: controller.show_frame("PageOne"))
        button1.grid(row=6, column=0, columnspan=2)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(Image.open("pic/orientation.png").resize((580, 276)))
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
            text = tk.Label(self, text="You had a great time dancing and drinking with your friends :D \n +2 social life, -4 money",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 1)
            player.editMoney(4, 0)
        else:
            text = tk.Label(self, text="You got drunk and puked all over your friend (ew gross) \n -2 social life, -3 money",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 0)
            player.editMoney(3, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option2(self, controller):
        self.disable_buttons()

        # 1/3 chace to get a bad outcome
        outcome = random.randint(0,2)

        if outcome == 0:
            text = tk.Label(self, text="""You fell asleep on the bus ride and missed your stop!
No more public transport so you had to grab home
-3 money""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMoney(3, 0)
        else:
            text = tk.Label(self, text="You had a great rest ^^ \n +1 mental health, +1 physical health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editPHealth(1, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/3 chace to get a bad outcome
        outcome = random.randint(0,2)

        if outcome == 0:
            text = tk.Label(self, text="Feeling stressed and overworked even before school starts \n +2 academics, -2 mental health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMHealth(1, 0)
            player.editAcad(2, 1)
        else:
            text = tk.Label(self, text="Feeling prepared for the new semester! ᕙ(`▽´)ᕗ \n +2 academics",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)

    def option4(self, controller):
        self.disable_buttons()

        # good social skills,
        if player.social_life >= 8:
            text = tk.Label(self, text="""Thanks to your great social skills, you and prof are now good friends~
+1 social life, +2 academics""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editAcad(1, 1)
        else:
            text = tk.Label(self, text="People think you're slightly weird :( \n -2 social life, -2 mental health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMHealth(1, 0)
            player.editSL(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageTwo")).grid(row=6, column=0)


# ASSIGNMENT DEADLINE
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.img = ImageTk.PhotoImage(Image.open("pic/ddl/ddl.png").resize((580, 276)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0)

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

        self.opt4 = ttk.Button(self, text="Just submit late and pray professor doesn’t find out",
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
        self.img1 = ImageTk.PhotoImage(Image.open("pic/ddl/ddl_response1a.png").resize((320, 180)))
        self.img2 = ImageTk.PhotoImage(Image.open("pic/ddl/ddl_response1b.png").resize((320, 180)))

        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=0)

        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, image=self.img1).grid(row=7, column=0)
            player.editMHealth(-1, 1)
            player.editAcad(-1, 1)
        else:
            text = tk.Label(self, image=self.img2).grid(row=7, column=0)
            player.editMHealth(1, 1)
            player.editAcad(1, 1)

    def option2(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("pic/ddl/ddl_response2.png").resize((320, 180)))

        text = tk.Label(self, image=self.img1).grid(row=7, column=0)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=0)

        outcome = random.randint(0,9)
        player.editAcad(-2,1)
        player.editMHealth(1,1)
        player.editPHealth(-1, 1)
        player.editSL(1,1)

    def option3(self, controller):
        self.disable_buttons()
        self.img1 = ImageTk.PhotoImage(Image.open("pic/ddl/ddl_response3a.png").resize((320, 180)))
        self.img2 = ImageTk.PhotoImage(Image.open("pic/ddl/ddl_response3b.png").resize((320, 180)))

        text = tk.Label(self, image=self.img1).grid(row=7, column=0, columnspan=4)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageThree")).grid(row=8, column=0)

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

# FIRST WEEKEND
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
         tk.Frame.__init__(self, parent)
         self.controller = controller

         self.img = ImageTk.PhotoImage(Image.open("pic/decision.jpeg").resize((580, 276)))
         img_label = tk.Label(self, image=self.img)
         img_label.grid(row=0, column=0)

         # make all buttons an attribute of the class (i.e. self.opt1)
         self.opt1 = ttk.Button(self, text="Study the whole day to prepare for class #kiasu",
                           command=lambda: self.option1(controller))
         #  and put .grid() in a new line :)
         self.opt1.grid(row=1, column=0)
         self.opt2 = ttk.Button(self, text="Hang out with your new friends and have some fun ;)",
                           command=lambda: self.option2(controller))
         self.opt2.grid(row=2, column=0)
         self.opt3 = ttk.Button(self, text="Binge drink bubble tea and spend all your money on online gambling ¯\_(ツ)_/¯",
                           command=lambda: self.option3(controller))
         self.opt3.grid(row=3, column=0)
         self.opt4 = ttk.Button(self, text="Visit your family because you miss them <3",
                           command=lambda: self.option4(controller))
         self.opt4.grid(row=4, column=0)

     # makes sure plaer cannot choose another option after pressing a button
    def disable_buttons(self):
         self.opt1['state'] = tk.DISABLED
         self.opt2['state'] = tk.DISABLED
         self.opt3['state'] = tk.DISABLED
         self.opt4['state'] = tk.DISABLED
    def option1(self, controller):
         self.disable_buttons()

         text = tk.Label(self, text="""You are very prepared for next week's quiz, but you are feeling a little lonely
+2 academics, -2 social life, -2 mental health""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
         player.editSL(2, 0)
         player.editAcad(2, 1)
         player.editMHealth(2, 0)

         next_button = ttk.Button(self, text="Next",
             command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)

    def option2(self, controller):
        self.disable_buttons()

         # 1/4 chace to get a bad outcome
        outcome = random.randint(0,3)

        if outcome == 0:
            text = tk.Label(self, text="""You had some fun, but now you are worried that you'll do poorly on Monday's quiz (´･_･`)
+2 social life, -2 academics""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(2, 0)
            player.editSL(1, 1)
        else:
            text = tk.Label(self, text="""You had a lot of fun, and there is still plenty of time to catch up on school work on Sunday
But managing social life and academics is hard! Feeling slightly overworked.
+2 social life -2 physical health""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 1)
            player.editPHealth(2, 0)

        next_button = ttk.Button(self, text="Next",
        command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/2 chance to get a bad outcome
        outcome = random.randint(0, 1)

        if outcome == 0:
            text = tk.Label(self, text="""Lost all your money gambling... (ಥ⌣ಥ)""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMoney(player.money, 0)
        else:
            text = tk.Label(self, text="""You have a stomachace from all the BBT, you are broke and you haven't revised at all
Luckily you haven't lost all your money and even made a new  friend in the process
-2 physical health, -4 money, -1 academics, +1 social life, +1 mental health""",
                                 font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editMoney(4, 0)
            player.editPHealth(2, 0)
            player.editMHealth(1, 1)
            player.editAcad(1,0)

        next_button = ttk.Button(self, text="Next",
        command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)

    def option4(self, controller):
        self.disable_buttons()

         # 2 good outcomes, 1/2-1/2 chance
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text= """You had a good time. Your parents showered you with affection and your siblings already envy your awesome college experience
Also received some pocket money “ヽ(´▽｀)ノ”
+2 mental health, +2 money""",
            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMHealth(2, 1)
            player.editMoney(2, 1)
        else:
            text = tk.Label(self, text="""You hung out with your relatives and even took your dog to the park. Fun!
But you forgot to study for your quiz on Monday... (._.) 
+2 physical health, +2 mental health, -2 academics""",
            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editPHealth(2, 1)
            player.editMHealth(2, 0)
            player.editAcad(2, 0)

        next_button = ttk.Button(self, text="Next",
        command=lambda: controller.show_frame("PageFour")).grid(row=6, column=0)


# SNACK
class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(Image.open("pic/snack.png").resize((580, 276)))
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

        # 1/3 chance for each option
        outcome = random.randint(0,2)

        if outcome == 0:
            text = tk.Label(self, text="""Found a tub of Ben and Jerry's ice cream in the fridge, score!!
Now you have energy to burn midnight oil.
-1 physical health, +1 mental health, +1 academics """,
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMHealth(1, 1)
            player.editPHealth(1, 0)
            player.editAcad(1, 1)
        elif outcome == 1:
            text = tk.Label(self, text="""Found a packet of Indomie on the counter!
While cooking it, Indomie owner walks in and catches you in the act ヽ(`Д´)ﾉ
Now you are known as the resident food theif...
-3 social life, -2 mental health """,
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(3, 0)
            player.editPHealth(2, 0)
        else:
            text = tk.Label(self, text="""Found some yogurt and a banana!
Yogurt tasted a bit funny... Turned out to be expired (≧︿≦)
Spent a day on the toilet!
-3 physical health""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
        player.editPHealth(3, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFive")).grid(row=6, column=0)


    def option2(self, controller):
        self.disable_buttons()

        text = tk.Label(self, text="Stomach is happy, wallet is not\nGrabfood is expensive! \n -4 money ",
                        font=controller.title_font, wraplength=580).grid(row=5, column=0)
        player.editMoney(4, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFive")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/3 chance to get bad outcome
        outcome = random.randint(0,2)

        if outcome == 0:
            text = tk.Label(self, text="None of your friends wanted to eat supper with you... \n -2 social life, -3 mental health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 0)
            player.editMHealth(3, 0)
        else:
            text = tk.Label(self, text="Prata and cheese fries... YUM \n +2 social life, -3 money",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 1)
            player.editMoney(3, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFive")).grid(row=6, column=0)


    def option4(self, controller):
        self.disable_buttons()

        # 1/2 chance to get bad outcome
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text="So hungry... Could not sleep\n Ending up binge eating D: \n -2 physical health, -2 mental health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editMHealth(2, 0)
            player.editPHealth(2, 0)
        else:
            text = tk.Label(self, text="Can't feel hungry if you're sleeping! Woke up and had a good breakfast. \n +1 physical health",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editPHealth(1, 1)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageFive")).grid(row=6, column=0)

### QUIZ

class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(Image.open("pic/quiz.png").resize((580, 276)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=0, column=0)

         # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Go comfort your friend",
                           command=lambda: self.option1(controller))
         #  and put .grid() in a new line :)
        self.opt1.grid(row=1, column=0)
        self.opt2 = ttk.Button(self, text="Tell your friend that you are busy studying, and ask whether you can help tomorrow",
                           command=lambda: self.option2(controller))
        self.opt2.grid(row=2, column=0)
        self.opt3 = ttk.Button(self, text="Feign a heart attack in order to avoid having to make a decision",
                           command=lambda: self.option3(controller))
        self.opt3.grid(row=3, column=0)
        self.opt4 = ttk.Button(self, text="Go help your friend, but bring your study notes to revise while you comfort them",
                           command=lambda: self.option4(controller))
        self.opt4.grid(row=4, column=0)

     # makes sure plaer cannot choose another option after pressing a button
    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()

        outcome = random.randint(0,1)

        if outcome == 1:
            text = tk.Label(self, text="""You are a very good friend. Your friend feels a lot better now, and you feel good for helping too.
The quiz doesn't go that well though
+2 social life, -3 academics""",
                         font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 1)
            player.editAcad(3, 0)

        else:
            text = tk.Label(self, text="""You are a very good friend. Your friend feels a lot better now, and you feel good for helping too.
The quiz turns out to be quite easy, so you still score well anyway :)
+2 social life, +1 academics""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editAcad(1, 1)

        next_button = ttk.Button(self, text="Next",
        command=lambda: controller.show_frame("PageSix")).grid(row=6, column=0)


    def option2(self, controller):
        self.disable_buttons()

        text = tk.Label(self, text="""You finish revising and do well on your quiz
Your friend is understanding, but seems to be a little hurt by your delayed response
+2 academics, -3 social life""",
        font=controller.title_font, wraplength=580).grid(row=5, column=0)
        player.editAcad(2, 1)
        player.editSL(3, 0)

        next_button = ttk.Button(self, text="Next",
             command=lambda: controller.show_frame("PageSix")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        text = tk.Label(self, text="""Not a terrible choice given the circumstances!
In all honesty, though, as much as we sympathise... That's a bit of a jerk move from you
-3 social life, +1 academics""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
        player.editAcad(1, 1)
        player.editSL(3, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSix")).grid(row=6, column=0)

    def option4(self, controller):
        self.disable_buttons()

         # 50% chance bad outcome, 50% no change
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text= """You are terrible at multitasking. Your friend is a little hurt that you didn't give them enough attention, and you weren't able to study much either
-2  social life, -2 academics""",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(2, 0)
            player.editAcad(2,0)
        else:
            text = tk.Label(self, text="Oddly, this kind of worked out (?) \n +1 academics",
                             font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(1, 1)
        next_button = ttk.Button(self, text="Next",
             command=lambda: controller.show_frame("PageSix")).grid(row=6, column=0)

# SICK
class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    
        self.img = ImageTk.PhotoImage(Image.open("pic/sick.png").resize((580, 276)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=1, column=0)

        # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Go to class to impress the professor. Complete the assignment because you are never late",
                          command=lambda: self.option1(controller))
        self.opt1.grid(row=2, column=0)

        self.opt2 = ttk.Button(self, text="Email the professor using your last energy, and go to UHC ",
                          command=lambda: self.option2(controller))
        #  and put .grid() in a new line :)
        self.opt2.grid(row=3, column=0)

        self.opt3 = ttk.Button(self, text="Lie on the bed like it's the end of the world",
                          command=lambda: self.option3(controller))
        self.opt3.grid(row=4, column=0)
        self.opt4 = ttk.Button(self, text="Spam everyone you know and cry to them",
                          command=lambda: self.option4(controller))
        self.opt4.grid(row=5, column=0)

    # makes sure plaer cannot choose another option after pressing a button
    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()

        # 1/2 chance to get bad outcome

        text = tk.Label(self, text="""It is COVID time. You NEVER go to class when you are sick!!!!
-2 physical health, -1 mental health, -1 social life, -1 academics""",
                        font=controller.title_font, wraplength=580).grid(row=6, column=0)
        player.editMHealth(-1, 1)
        player.editPHealth(-2, 1)
        player.editSL(1, 0)
        player.editAcad(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSeven")).grid(row=7, column=0)

    def option2(self, controller):
        self.disable_buttons()

        # 1/10 chace to get a bad outcome
        text = tk.Label(self, text="It is obviously what human beings do when they are sick. Good job kid. \n -2 money ",
                        font=controller.title_font, wraplength=580).grid(row=6, column=0)
        player.editMoney(2, 0)
        
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSeven")).grid(row=7, column=0)


    def option3(self, controller):
        self.disable_buttons()

        # 1/10 chace to get a bad outcome
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text="""You fell asleep. It is 9 pm when you wake up again.
You have missed all the classes and deadlines. Luckily, you feel better now.
-3 academics, +2 physical health, +1 mental health """,
                            font=controller.title_font, wraplength=580).grid(row=6, column=0)
            player.editAcad(-3,1)
            player.editPHealth(2, 1)
            player.editMHealth(1, 1)
        else:
            text = tk.Label(self, text="""You got sicker and sicker. You blacked out and woke up in the hospital.
Your friend called an ambulance for you.
-5 money, -2 physical health, -2 mental health""",
                            font=controller.title_font, wraplength=580).grid(row=6, column=0)
            player.editMHealth(-2, 1)
            player.editMoney(-5, 1)
            player.editPHealth(-2, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageSeven")).grid(row=7, column=0)


    def option4(self, controller):
        #self.disable_buttons()

        # 1/4 chace to get a good outcome
        outcome = random.randint(0,3)

        if outcome == 0:
            text = tk.Label(self, text="""Your friend sends you to the hospital.
Everyone knew you were sick, and got presents for you!.
+2 social life, +1 mental health, +1 physical health""",
                            font=controller.title_font, wraplength=580).grid(row=6, column=0)
            player.editSL(2, 1)
            player.editMHealth(1, 1)
            player.editPHealth(1, 1)

        else:
            text = tk.Label(self, text="Nobody replied your message, so you were greatly depressed \n -3 mental health, -2 physical health",
                            font=controller.title_font, wraplength=580).grid(row=6, column=0)
            player.editPHealth(-2, 1)
            player.editMHealth(-3, 1)

        next_button = ttk.Button(self, text="Next",
                                 command=lambda: controller.show_frame("PageSeven")).grid(row=7, column=0)

class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(Image.open("pic/online_exam.png").resize((580, 276)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=0, column=0)

        # make all buttons an attribute of the class (i.e. self.opt1)
        self.opt1 = ttk.Button(self, text="Join the Discord of course! I don't want to be put at an unfair advantage.",
                          command=lambda: self.option1(controller))
        #  and put .grid() in a new line :)
        self.opt1.grid(row=1, column=0)
        self.opt2 = ttk.Button(self, text="Don't join the discord group. I have full confidence in my abilities.",
                          command=lambda: self.option2(controller))
        self.opt2.grid(row=2, column=0)
        self.opt3 = ttk.Button(self, text="Join the Discord group, not to discuss but just to double check my answers",
                          command=lambda: self.option3(controller))
        self.opt3.grid(row=3, column=0)
        self.opt4 = ttk.Button(self, text="Be a whistleblower! Flag this discord group to your prof.",
                          command=lambda: self.option4(controller))
        self.opt4.grid(row=4, column=0)


    # makes sure plaer cannot choose another option after pressing a button
    def disable_buttons(self):
        self.opt1['state'] = tk.DISABLED
        self.opt2['state'] = tk.DISABLED
        self.opt3['state'] = tk.DISABLED
        self.opt4['state'] = tk.DISABLED

    def option1(self, controller):
        self.disable_buttons()

        # 1/4 chance to get good outcome
        outcome = random.randint(0,3)

        if outcome == 0:
            text = tk.Label(self, text="Thanks to some senpais in the group, managed to do extremely well for the quiz!\n+4 academics",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(4, 1)
        else:
            text = tk.Label(self, text="""Quiz answers were all so similar, you and your friends got caught for cheating and given an F grade
At least you all failed together?
-4 academics, +1 social life, -1 mental health""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editSL(1, 1)
            player.editAcad(4, 0)
            player.editMHealth(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageEight")).grid(row=6, column=0)

    def option2(self, controller):
        self.disable_buttons()

        # good outcome if acad > 8
        if player.acad < 6:
            text = tk.Label(self, text="""Confidence was unfounded. Somehow still did badly...
But, more importantly, you still have your integrity!
It's too bad that counts for nothing in this game.
-2 academics""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(2, 0)
        else:
            text = tk.Label(self, text="Kudos to you for studying hard and achieving good results in a morally reighteous way! \n+2 academics",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(2, 1)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageEight")).grid(row=6, column=0)

    def option3(self, controller):
        self.disable_buttons()

        # 1/2 chace to get a bad outcome
        outcome = random.randint(0,1)

        if outcome == 0:
            text = tk.Label(self, text="""Reading the discussions, you were swayed by their convincing arguments.
But your original answers were actually the right ones?
Better to rely on yourself next time...
-2 academics""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(2, 0)
        else:
            text = tk.Label(self, text="""Reading the discussions made you realise that you had fallen into the Professor's tricks!
Changed your answers and did well for the quiz!
But your friends think you're a free loader for not contributing anything.
+2 academics -2 social life""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
            player.editAcad(2, 1)
            player.editSL(2, 0)
        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageEight")).grid(row=6, column=0)

    def option4(self, controller):
        self.disable_buttons()

        text = tk.Label(self, text="""Prof ordered the closure of the discord chat and made the students involved sit for the quiz physically
Somehow it was leaked that you were the whistleblower, your friends are NOT happy
+2 academics, -4 social life, -1 mental health""",
                            font=controller.title_font, wraplength=580).grid(row=5, column=0)
        player.editAcad(2, 1)
        player.editSL(4, 0)
        player.editMHealth(1, 0)

        next_button = ttk.Button(self, text="Next",
            command=lambda: controller.show_frame("PageEight")).grid(row=6, column=0)

class PageEight(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.img = ImageTk.PhotoImage(Image.open("pic/congrat.jpeg").resize((580, 376)))
        img_label = tk.Label(self, image=self.img)
        img_label.grid(row=0, column=0)

        button = ttk.Button(self, text="See your score",
                           command=lambda: controller.show_frame("Final"))
        button.grid(row=1, column=0)

class PageGameover(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        go_label = tk.Label(self, text="Gameover ༼ ༎ຶ ෴ ༎ຶ༽", font=controller.title_font)
        go_label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text=gameover + " has fallen to 0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        if gameover == "Academics":
            text = """With your current grades, there is no way you will be able to pass this semester.
Best to turn over a new leaf and study harder!"""
        elif gameover == "Social life":
            text = "We can relate."
        elif gameover == "Physical health":
            text = "Due to ailing health, you have taken a Leave of Absence and will not be finishing the semester."
        elif gameover == "Mental health":
            text = """Due to a mental breakdown in school, you have been required to take a Leave of Absence and attend couseling. The school hopes that you will be able to return in a better state next semester.
Mental health is important! Please take care of yourself."""
        elif gameover == "Money":
            text = """University is expensive! You do not have enough funds to pay your school fees next semester. This is the start of student debt.
Manage your finances better!"""
        label2 = tk.Label(self, text=text, font=controller.title_font, wraplength=580)
        label2.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Try again",
                           command=restart_program)
        button.pack()

class Final(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        academic = tk.Label(self, text="""Good job for achieving good grades this semester!
You have made it to the Dean's List!
（ ^_^）o自自o（^_^ ）""", font=controller.title_font, wraplength=580)
        sport = tk.Label(self, text="""Wow! Keeping fit is not easy, good job!
ᕦ(ò_óˇ)ᕤ""", font=controller.title_font, wraplength=580)
        social = tk.Label(self, text="""What a social butterfly! Really building those connections in University!
ᕕ( ᐛ )ᕗ""",
                          font=controller.title_font, wraplength=580)

        score = tk.Label(self, text=str(final), font=controller.title_font)

        if final=="Academics":
            academic.pack(side="top", fill="x", pady=10)

        elif final=="Physical health":
            sport.pack(side="top", fill="x", pady=10)

        elif final == "Social life":
            social.pack(side="top", fill="x", pady=10)

        score.pack(side="top", fill="x", pady=10)
        button = ttk.Button(self, text="Try again",
                           command=restart_program)
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.title("Can you survive your first sem?")
    app.iconbitmap("icon.ico")
    app.geometry("600x1000")
    app.mainloop()

