# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Danial
"""

from abc import ABCMeta, abstractmethod
import numpy as np
import random

class Creature(metaclass=ABCMeta):
    
    def __init__(self,ind):
        self.ind = ind #Index of a creature in ecosystem
        self.type = "None"
    
    @abstractmethod 
    def move(self, river, i):
        pass
  
        
class Bear(Creature):
  
    def __init__(self, ind):
       self.type = "bear"
    
    def move(self, river, i):
        new_i = random.choice([i-1, i, i+1])
        if new_i >= 0 and new_i < len(river):
            if river[new_i] is None:
                river[new_i] = self
                river[i] = None
            elif river[new_i].type == "bear":
                new_location = random.choice([i-1, i, i+1])
                if new_location >= 0 and new_location < len(river) and river[new_location] is None:
                    river[new_location] = Bear(new_location)
            elif river[new_i].type == "fish":
                river[i] = None
                river[new_i] = self
        
class Fish(Creature):
    
    def __init__(self, ind):
        self.type = "fish"

    def move(self, river, i):
        new_i = random.choice([i-1, i, i+1])
        if new_i >= 0 and new_i < len(river):
            if river[new_i] is None:
                river[new_i] = self
                river[i] = None
            elif river[new_i].type == "fish":
                new_location = random.choice([i-1, i, i+1])
                if new_location >= 0 and new_location < len(river) and river[new_location] is None:
                    river[new_location] = Fish(new_location)
            elif river[new_i].type == "bear":
                river[i] = None
                
                
                
                