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
    
    
    def opprettMed(self, hp, dmg, sa, saNavn, mx):
        hitPoints = hp
        damage = dmg
        specialAction = sa
        specialActionName = saNavn
        maxHitPoints = mx
        print "you have " + str(hitPoints) + " hitpoints"
        print "you deal " + str(damage) + " damage"
        print "your special action is " + str(specialActionName)
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
        return self.valgtKlasse
            
    
    def velgKlasse(self):
        duSkrev =raw_input("choose your class: ")
        for kl in self.alleklasser:
            if duSkrev == kl:
                self.valgtKlasseNavn = duSkrev
                print "you are a(n) " + self.valgtKlasseNavn
                return 
        print duSkrev + " is not a valid class"
        return self.velgKlasse() #rekursjon hvis feil klassenavn
        
    def velgNavn(self):
        duSkrev = raw_input("choose your name: ")
        self.valgtKlasse.giNavn(duSkrev)
        print "your name is " + self.valgtKlasse.name

    
    def delUtKlassePoeng(self):
        sa = SpecialAction()
        if self.valgtKlasseNavn == "warrior":            
            self.valgtKlasse.opprettMed(20, 5, 0, "none", 20)
        
        elif self.valgtKlasseNavn == "priest":
            sa.create("heal, 0, 5, false, 2")
            self.valgtKlasse.opprettMed(15, 7, 1, "heal", 15)
        
        elif self.valgtKlasseNavn == "archer":
            self.valgtKlasse.opprettMed( 17, 4, 2, "snipe", 17)
        
        elif self.valgtKlasseNavn == "jew":
            self.valgtKlasse.opprettMed(20, 20, 3, "jew-jitsu", 20)
        else:
            print "Syntax terror!"
            exit
            
class SpecialAction:
    damage = 0
    heal = 0
    instaKill = False
    waitPeriod = 0
    name = ""
    
    def create(self, name, damage, heal, instaKill, waitPeriod):
        self.damage = damage
        self.heal = heal
        self.instaKill = instaKill
        self.waitPeriod = waitPeriod
        self.name = name 
             
cs = CharacterSelect()
hero = cs.opprettCharacter()   
