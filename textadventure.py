# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:59:55 2014

@author: Simon
"""
import time
alleklasser = ["warrior", "priest", "archer", "jew"]

klasse = raw_input("choose your class:")
valgtklasse = ""

for kl in alleklasser:
    if klasse == kl:
        valgtklasse = klasse
        break
    
if valgtklasse == "":
    print klasse + " is not a valid class"
else:
    print "you are a(n) " + valgtklasse
if valgtklasse == "warrior":
    hitpoint = 20
    damage = 5
    specialaction = 0
    print "you have " + str(hitpoint) + " hitpoints"
    print "you deal " + str(damage) + " damage"
    print "your special action is none"
elif valgtklasse == "priest":
    hitpoint = 15
    damage = 7
    specialaction = 1
    print "you have " + str(hitpoint) + " hitpoints"
    print "you deal " + str(damage) + " damage"
    print "your special action is heal"
elif valgtklasse == "archer":
    hitpoint = 15
    damage = 4
    specialaction = 2
    print "you have " + str(hitpoint) + " hitpoints"
    print "you deal " + str(damage) + " damage"
    print "your special action is snipe"
elif valgtklasse == "jew":
    hitpoint = 20
    damage = 20
    specialaction = 3
    print "you have " + str(hitpoint) + " hitpoints"
    print "you deal " + str(damage) + " damage"
    print "your special action is jew jitsu"
time.sleep(15)
print "you are in a dark room, in the room there is a door,"
print "a window, a book shelf, and a lamp"
alleactions = ["use lamp", "take book", "open window", "open door"]

action = raw_input("choose your action:")
valgtaction = ""

for kl in alleactions:
    if klasse == kl:
        valgtaction = klasse
        break
    
if valgtaction == "":
    print action + " is not a valid action"
else:
    print "yout try to" + valgtaction