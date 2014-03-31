# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:59:55 2014

@author: Simon
"""

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
if valgtklasse == warrior:
    hitpoint = 20
    damage = 5
    specialaction = 0
    print "you have" + hitpoint + "hitpoints"
    print "you deal " + damage + "damage"
    print "your special action is none"
elif valgtklasse == priest:
    hitpoint = 15
    damage = 7
    specialaction = 1
    print "you have" + hitpoint + "hitpoints"
    print "you deal " + damage + "damage"
    print "your special action is heal"
elif valgtklasse == archer:
    hitpoint = 15
    damage = 4
    specialaction = 2
    print "you have" + hitpoint + "hitpoints"
    print "you deal " + damage + "damage"
    print "your special action is snipe"