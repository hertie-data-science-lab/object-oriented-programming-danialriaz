# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Danial & Fernandao
"""

from abc import ABCMeta, abstractmethod
import random

class Creature(metaclass=ABCMeta):
    
    def __init__(self,ind,type = "None"):
        self.ind = ind #Index of a creature in ecosystem
        self.type = type
    
    @abstractmethod 
    def move(self, river, i):
        pass
  
        
class Bear(Creature):
  
    def __init__(self, ind):
       self.type = "bear"
    
    def move(self, river, i):
        # Bear can move either a step back, a step forward or stay in the same place
        new_i = random.choice([i-1, i, i+1])
        if new_i >= 0 and new_i < len(river):
            # For any move, if the Bear moves to an empty space the new space becomes occupied by it and the previous one is now empty
            if river[new_i] is None:
                river[new_i] = self
                river[i] = None
            #If there's a bear in the new space then the bears remain where they are and create a new 'bear' in place of a previously 'None' index
            elif river[new_i].type == "bear":
                new_location = random.choice([i-1, i, i+1])
                if new_location >= 0 and new_location < len(river) and river[new_location] is None:
                    river[new_location] = Bear(new_location)
            #If there's a fish in the new index, it gets replaced with a bear, the previous index becomes a none
            elif river[new_i].type == "fish":
                river[i] = None
                river[new_i] = self
        
class Fish(Creature):
    
    def __init__(self, ind):
        self.type = "fish"

    def move(self, river, i):
        # Fish can move either a step back, a step forward or stay in the same place
        new_i = random.choice([i-1, i, i+1])
        # For any move, if the Fish moves to an empty space the new space becomes occupied by it and the previous one is now empty
        if new_i >= 0 and new_i < len(river):
            if river[new_i] is None:
                river[new_i] = self
                river[i] = None
        #If there's a fish in the new space then the fish remain where they are and create a new 'fish' in place of a previously 'None' index 
            elif river[new_i].type == "fish":
                new_location = random.choice([i-1, i, i+1])
                if new_location >= 0 and new_location < len(river) and river[new_location] is None:
                    river[new_location] = Fish(new_location)
        #If a fish moves to where a bear is it disappears
            elif river[new_i].type == "bear":
                river[i] = None
                
                
                
                