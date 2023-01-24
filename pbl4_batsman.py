from tkinter import *

import threading
import pyttsx3


class batsman:
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b1_count = 0
        self.b2_count = 0
        self.b1_runs = 0
        self.b2_runs = 0
        self.team = ''
        self.actual_name_b2 = b2
        self.actual_name_b1 = b1
        self.check = 0

    def striker(self):
        self.b1 = self.b1 + str("*")
        self.b2 = self.b2


    def batting(self, inp):
        if inp == 1 or inp == 3:
            if "*" in self.b1:
                self.b1 = self.b1.replace("*", " ")
                self.b2 = self.b2 + "*"
                self.b1 = self.b1.rstrip()
                # self.b2=self.b2.rstrip()
                self.batsman_ball_count(self.b1, inp)

                engine=pyttsx3.init()
                rate=engine.getProperty('rate')
                engine.setProperty('rate',200)
                voices=engine.getProperty("voices")
                engine.setProperty("voice",voices[1].id)
                engine.say(f"{self.b2} comes to strike ")
                engine.runAndWait()
                
            else:
                self.b2 = self.b2.replace("*", " ")
                self.b1 = self.b1 + "*"
                # self.b1=self.b1.rstrip()
                self.b2 = self.b2.rstrip()
                self.batsman_ball_count(self.b2, inp)


                engine=pyttsx3.init()
                rate=engine.getProperty('rate')
                engine.setProperty('rate',200)
                voices=engine.getProperty("voices")
                engine.setProperty("voice",voices[1].id)
                engine.say(f"{self.b1} comes to strike ")
                engine.runAndWait()

        elif inp == 2 or inp == 4 or inp == 6 or inp == 0:
            self.b1 = self.b1
            self.b2 = self.b2
            if "*" in self.b1:
                self.batsman_ball_count(self.b1, inp)
            else:
                self.batsman_ball_count(self.b2, inp)

        elif inp.startswith("l"):
            if inp.endswith("1") or inp.endswith("3"):
                if "*" in self.b1:
                    self.b1 = self.b1.replace("*", " ")
                    self.b2 = self.b2 + "*"
                    self.b1 = self.b1.rstrip()
                    # self.b2=self.b2.rstrip()
                    # self.batsman_ball_count(self.b1, inp)
                else:
                    self.b2 = self.b2.replace("*", " ")
                    self.b1 = self.b1 + "*"
                    # self.b1=self.b1.rstrip()
                    self.b2 = self.b2.rstrip()
                    # self.batsman_ball_count(self.b2, inp)
            else:
                if "*" in self.b1:
                    self.b1 = self.b1.replace("*", " ")
                    self.b2 = self.b2 + "*"
                    self.b1 = self.b1.rstrip()
                    # self.b2=self.b2.rstrip()

                else:
                    self.b2 = self.b2.replace("*", " ")
                    self.b1 = self.b1 + "*"
                    # self.b1=self.b1.rstrip()
                    self.b2 = self.b2.rstrip()

    def change_batsman(self, newBatsman):

        # if inp.startswith("wic"):

        lock = threading.Lock()
        lock.acquire()
        if "*" in self.b1:
            self.check = 0
            self.b1 = newBatsman
            self.actual_name_b1 = newBatsman
            self.b1 = self.b1 + "*"
            self.b1_count = 0
            self.b1_runs = 0
            lock.release()

        else:
            self.check = 1
            self.b2 = newBatsman
            self.actual_name_b2 = newBatsman
            self.b2 = self.b2 + "*"
            self.b2_runs = 0
            self.b2_count = 0
            lock.release()

    def NoBall_batting(self, inp1):
        self.batting(inp1)

    def batsman_ball_count(self, z, inp):
        if z == self.b1:
            self.b1_count += 1
            self.b1_runs += int(inp)
        else:
            self.b2_count += 1
            self.b2_runs += int(inp)

    def teams(self, teams_name):
        self.team = teams_name

    def setBatsman(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b1_count = 0
        self.b2_count = 0
        self.b1_runs = 0
        self.b2_runs = 0

class Bowler:
    def __init__(self, name):
        self.name = name
        self.b_wicket = 0
        self.b_runs = 0
        self.b_overs = 0.0
        self.b_index = 0
        self.b_list = [
            self.name.upper() + " " + str(self.b_wicket) + " - " + str(self.b_runs) + " (" + str(self.b_overs) + ")"]
        self.team = ''

    def bowling(self, new_bowler):
        x = 0

        for i in self.b_list:
            if new_bowler in i:
                x = 1
                self.b_index = self.b_list.index(i)
                z = i.split(" ")
                self.name = z[0]
                self.b_wicket = int(z[1])
                self.b_runs = int(z[3])
                self.b_overs = float(z[4][1:4])

        if x == 0:
            self.name = new_bowler
            self.b_wicket = 0
            self.b_runs = 0
            self.b_overs = 0.0
            self.b_list.append(self.name.upper() + " " + str(self.b_wicket) + " - " + str(self.b_runs) + " (" + str(self.b_overs) + ")")
            self.b_index = len(self.b_list) - 1

        print(self.b_list)

    def bowler_wicket(self):
        self.b_wicket += 1

    def bowler_runs(self, inp):
        self.b_runs += inp

    def bowler_overs(self):
        self.b_overs += 0.1
        self.b_overs = round(self.b_overs, 1)
        self.b_overs = str(self.b_overs)
        if self.b_overs[2] == '6':
            self.b_overs = round(float(self.b_overs)) + 0.0
            self.b_list[self.b_index] = self.name.upper() + " " + str(self.b_wicket) + " - " + str(self.b_runs) + " (" + str(self.b_overs) + ")"
        else:
            self.b_overs = float(self.b_overs)
        # self.b_list[self.b_index]=self.name.lower()+" "+str(self.b_wicket)+" - "+str(self.b_runs)+" ("+str(self.b_overs)+")"
        print("next bowler added : ",self.b_list)

    def teams(self, teams_name):
        self.team = teams_name




b1 = 'ganesh'
b2 = 'mahesh'
b3 = "STARC"
cric1 = batsman(b1, b2)
cric1.striker()
cric2 = Bowler(b3)
name = ''
