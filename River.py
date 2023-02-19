# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Danial & Fernandao
"""
import random
from Creatures import Bear
from Creatures import Fish

class River:
    # We introduce n indices and initially populate them all with None
    def __init__(self, n_room):
        self.n_room = n_room
        self.list = [None] * n_room
     
    # We introduce the method of initialize where we input the number of indices and then randomly assign them to be either Fish, Bear or None
    def initialize(self):
        for i in range(self.n_room):
            random_number = random.randint(0, 2)
            if (random_number == 0):
                self.list[i] = Fish(i)
            elif (random_number == 1):
                self.list[i] = Bear(i)
            elif (random_number == 2):
                pass;               
     
    # We introduce a method of display where we display which of; Fish, Bear, None occupies the indices
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        for i in self.list: 
            if i == None:       
                print("None")
            else: 
                print(i.type)
        print("===================")
    
    # We introduce a method 'next_time_step' where we input the number of iterations to be done
    def next_time_step(self, no_iter):
        for t in range(no_iter):
            # loop over each position in the river
            for i in range(len(self.list)):
                # get the animal at this position, if there is one
                animal = self.list[i]

                if animal is not None:
                    # move the animal to a random adjacent position
                    animal.move(self.list, i)
        

        
        