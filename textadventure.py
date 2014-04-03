# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:59:55 2014

@author: Simon
"""
import time

class Character:
    name = ""
    maxHitPoints = 0
    hitPoints = 0
    damage = 0
    specialAction = 0
    specialActionName = ""
    selected = None
    
    def startCharacter(self):
        cs = CharacterSelect()
        self.selected = cs.opprettCharacter() 
        return self
    
    def opprettMed(self, hp, dmg, sa, saNavn, mx):
        self.hitPoints = hp
        self.damage = dmg
        self.specialAction = sa
        self.specialActionName = saNavn
        self.maxHitPoints = mx
        print "you have " + str(self.hitPoints) + " hitpoints"
        print "you deal " + str(self.damage) + " damage"
        print "your special action is " + str(self.specialActionName)
        return self

    def giNavn(self, navnet):
        self.name = navnet
        
    def printCharacterInfo(self):
        print "Name: " +self.name
        print "Class: " +self.selected.valgtKlasseNavn
        print "hitpoint: " +self.hitPoint
        print "damage: " +self.damage
        print "name: "+self.valgtKlasse.name
        print "special action: " +self.specialActionName
        
        
  
class CharacterSelect:
    valgtKlasseNavn = ""
    valgtKlasse = Character()
    hitpoints = 0
    alleklasser = ["warrior", "priest", "archer", "jew"]
    
    def opprettCharacter(self):
        self.velgKlasse()
        self.delUtKlassePoeng()
        self.velgNavn()
        self.delUtKlassePoeng()
        return self.valgtKlasse
            
    
    def velgKlasse(self):
        duSkrev =raw_input("choose your class: ")
        for kl in self.alleklasser:
            if duSkrev == kl:
                self.valgtKlasseNavn = duSkrev
                print "you are a(n) " + self.valgtKlasseNavn
                return self
        print duSkrev + " is not a valid class"
        return self.velgKlasse()
        
    def velgNavn(self):
        duSkrev = raw_input("choose your name: ")
        self.valgtKlasse.giNavn(duSkrev)
        print "your name is " + self.valgtKlasse.name

    
    def delUtKlassePoeng(self): 
        if self.valgtKlasseNavn == "warrior":
            self.valgtKlasse.opprettMed(20, 5, 0, "none", 20)
        
        elif self.valgtKlasseNavn == "priest":
            self.valgtKlasse.opprettMed(15, 7, 1, "heal", 15)
        
        elif self.valgtKlasseNavn == "archer":
            self.valgtKlasse.opprettMed(17, 4, 2, "snipe", 17)
        
        elif self.valgtKlasseNavn == "jew":
            self.valgtKlasse.opprettMed(20, 20, 3, "jew-jitsu", 20)
        else:
            print "Syntax terror!"
            exit

        
      
chargen = Character()
hero = chargen.startCharacter()

print "you are in a dark room, in the room there is a door,"
print "a window, a book shelf, and a lamp"
alleactions = ["use lamp", "take book", "open window", "open door"]

skrevetAction = raw_input("choose your action: ")
valgtaction = ""

for action in alleactions:
    if action == skrevetAction:
        valgtaction = skrevetAction
        break



if valgtaction == "":
    print action + " is not a valid action"
else:
    print "you try to " + valgtaction
cs.hitpoint -= 5


exit()
