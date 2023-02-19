# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Danial & Fernandao
"""

from River import River

#Choose number of index in the river
river = River(10)
river.initialize()
river.display()

#Choose number of timesteps (iterations)
river.next_time_step(20)
river.display()