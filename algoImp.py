#Matthew Cole
#3/17/21
#Psuedo code

import sqlite3
from sqlite3 import Error
from typing import Sequence
from flask_sqlalchemy import SQLAlchemy
import random as r
import csv

class workoutNode:
    
    def __init__(self):
        self.wk = []
        self.score = 0

        self.push = False
        self.pull = False
        self.squat = False
        self.hinge = False
        self.carry = False
        self.core = False

    def addEx(self, exercise):
        self.wk.append(exercise)
        self.score += exercise[4]

        if (exercise[1].lower() == "push"):
            self.push = True
        elif (exercise[1].lower() == "pull"):
            self.pull = True
        elif (exercise[1].lower() == "squat"):
            self.squat = True
        elif (exercise[1].lower() == "hinge"):
            self.hinge = True
        elif (exercise[1].lower() == "carry"):
            self.carry = True
        elif (exercise[1].lower() == "core"):
            self.core = True
        else:
            pass
            #print("Added type: {} exericse".format(exercise[4]))

    def __repr__(self):
        return "Workout: {} \nScore: {}".format(self.wk,self.score)

class workoutGen:

    def __init__(self):
        try:
            conn = sqlite3.connect("exercises.db")
            #print(sqlite3.version)
        except Error as e:
            print(e)

        self.cur = conn.cursor()

        self.stack = []
        self.nextType = "aux"

    def generator(self,sport,level): #1 beginner, bw and bands | 2 intermediate, machines, dumbells and bands | 3 advanced everything that's not bands, machines, and bw
        level = int(level) #man coding is do tedious, this line turned an infinite loop to working code
        stack = []
        chosen = []

        w = workoutNode()

        stack.append(w)

        count = 0

        while(True):
            curr = stack[-1]

            if(len(stack) == 0):
                print("No workout could be found")
                return
                #shouldn't ever happen

            #satisfies contrstaints
            if(curr.score in {16,17,18}):
                print("Workout found")              
                return curr

            #violates constrains so it yeets out the bad workout
            if(curr.score > 18):
                stack.pop()
                print("Violation")
                continue

            if(curr.push == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "push"')   
                #print("push exercsies retreived, about to filter")
                ex = self.skillFilter(ex,level)
                #print("\nfiltered")

                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted push")
                continue

            if(curr.pull == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "pull"')   
                
                ex = self.skillFilter(ex,level)

                #print(ex)
                
                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted pull")
                continue

            if(curr.squat == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "squat"')   
                
                ex = self.skillFilter(ex,level)

                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted squat")
                continue

            if(curr.hinge == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "hinge"')   

                ex = self.skillFilter(ex,level)

                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted hinge")
                continue

            if(curr.carry == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "carry"')   
                
                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted carry")
                continue

            if(curr.core == False):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "core"')   
                
                curr.addEx(r.choice(list(ex)))
                stack.append(curr)

                print("inserted core")
                continue

            if(self.nextType == "aux"):
                ex = self.cur.execute('SELECT * FROM exercises WHERE type == "aux"')
                #ex = self.skillFilter(ex,level)
                ch = []

                while(True):
                    ch = r.choice(list(ex)) #choose exercise at random
                    if(ch not in chosen):
                        break

                curr.addEx(ch)
                chosen.append(ch)
                stack.append(curr)

            else:
                sqlExe = 'SELECT * FROM exercises WHERE score == 3 AND sport == "{}"'.format(sport)
                ex = self.cur.execute(sqlExe)
                ch = []

                while(True):
                    ch = r.choice(list(ex)) #choose exercise at random
                    if(ch not in chosen):
                        break
                
                curr.addEx(ch)
                chosen.append(ch)
                stack.append(curr)

            if (r.randint(1, 9) % 2 == 1):
                self.nextType = "aux"
            else:
                self.nextType = "inj"

    def formatter(self,exs):
        r.shuffle(exs)
        wk1 = []
        wk2 = []
        for ex in exs:
            if ex[1] in {"push", "pull", "carry"}:
                wk1.insert(0, ex)
            elif ex[1] in {"squat", "hinge","core"}:
                wk2.insert(0, ex)
            else:
                if len(wk2) < len(wk1):
                    wk2.append(ex)
                else:
                    wk1.append(ex)

        wk1V2 = []
        wk2V2 = []
        for ex1,ex2 in zip(wk1,wk2):
            wk1V2.append(ex1 + ("0",))
            wk2V2.append(ex2 + ("0",))

        return(wk1V2,wk2V2)


    def skillFilter(self,ex,level):
        #print("entered filter function")
        print("About to filter for level {}".format(level))
        if level == 1:
            #print("About to filter for level {}".format(level))
            exf = [n for n in ex if n[3].lower() == "band" or n[3].lower() == "trx" or n[3].lower() == "none"]
            print(exf)
            return exf

        if level == 2:
            #print("About to filter for level {}".format(level))
            exf = [n for n in ex if n[3].lower() == "machine" or n[3].lower() == "dumbell" or n[3].lower() == "band"]
            print(exf)
            return exf

        if level == 3:
            #print("About to filter for level {}".format(level))
            exf = [n for n in ex if n[3].lower() != "none" or n[3].lower() != "band" or n[3].lower() != "machine"]
            print(exf)
            return exf


        


"""
    #no longer functional with the addition of rep ranges
    def formatterCSV(self,exs):
        r.shuffle(exs)
        wk1 = []
        wk2 = []
        for ex in exs:
            if ex[1] in {"push", "pull", "carry"}:
                wk1.insert(0, ex)
            elif ex[1] in {"squat", "hinge"}:
                wk2.insert(0, ex)
            else:
                if len(wk2) < len(wk1):
                    wk2.append(ex)
                else:
                    wk1.append(ex)

        return(self.toCSV(wk1,wk2))

    def toCSV(self,wk1,wk2):
        repRange = ["8-10*","10-12*","8+","10+","12+"]
        with open('testWorkout.csv', mode='w') as tw:
            wkWrite = csv.writer(tw, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            wkWrite.writerow(['Workout 1:', 'Exercise', 'Reps', 'Equipment', 'Workout 2:', 'Exercise', 'Reps', 'Equipment'])

            for one, two in zip(wk1, wk2):
                wkWrite.writerow(['', one[0], r.choice(repRange), one[3], '', two[0], r.choice(repRange), two[3]])

            wkWrite.writerow(['', one[0], r.choice(repRange), one[3], '', two[0], r.choice(repRange), two[3]])
            """
