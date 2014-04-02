# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:59:55 2014

@author: Simon
"""
import time
print "you are in a dark room, in the room there is a door,"
print "a window, a book shelf, and a lamp"
alleactions = ["use lamp", "take book", "open window", "open door"]



class CharacterSelect:
    valgtklasse = ""
    alleklasser = ["warrior", "priest", "archer", "jew"]
    def velgKlasse(self, duSkrev):
        for kl in self.alleklasser:
            if duSkrev == kl:
                self.valgtklasse = duSkrev
                break
         
    def klassen(a, b, c, d):
        hitpoint = a
        damage = b
        specialaction = c
        specialactionnavn = d
        print "you have " + str(hitpoint) + " hitpoints"
        print "you deal " + str(damage) + " damage"
        print "your special action is " + str(specialactionnavn)
        name = raw_input("choose your name:")
        print "your name is " + name
    def klasser(class1, class2, class3, class4):
        if valgtklasse == "":
            print klasse + " is not a valid class"
        else:
            print "you are a(n) " + valgtklasse
        if valgtklasse == str(class1):
            klassen(20, 5, 0, "none")
        
        elif valgtklasse == str(class2):
            klassen(15, 7, 1, "heal")
        
        elif valgtklasse == str(class3):
            klassen(17, 4, 2, "snipe")
        
        elif valgtklasse == str(class4):
            klassen(20, 20, 3, "jew-jitsu")


cs = CharacterSelect()
skrev = raw_input("choose your class: ")
hero = cs.velgKlasse(skrev)

skrevetAction = raw_input("choose your action: ")
valgtaction = ""

for action in alleactions:
    if action == skrevetAction:
        valgtaction = skrevetAction
        break
    
if valgtaction == "":
    print action + " is not a valid action"
else:
    print "you try to" + valgtaction
cs.hitpoint -= 5


exit()
