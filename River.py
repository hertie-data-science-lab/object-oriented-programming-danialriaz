# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np
import random
from Creatures import Bear
from Creatures import Fish

class River:
    
    def __init__(self, n_room):
        self.n_room = n_room
        self.list = [None] * n_room
       
    def initialize(self):
        for i in range(self.n_room):
            random_number = random.randint(0, 2)
            if (random_number == 0):
                self.list[i] = Fish(i)
            elif (random_number == 1):
                self.list[i] = Bear(i)
            elif (random_number == 2):
                pass;               
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        for i in self.list: 
            if i == None:       
                print("None")
            else: 
                print(i.type)
        print("===================")
        
    def next_time_step(self, no_iter):
        for t in range(no_iter):
            # loop over each position in the river
            for i in range(len(self.list)):
                # get the animal at this position, if there is one
                animal = self.list[i]

                if animal is not None:
                    # move the animal to a random adjacent position
                    animal.move(self.list, i)
        

        
        