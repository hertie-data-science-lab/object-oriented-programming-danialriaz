# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Danial
"""

from River import River

river = River(10)
river.initialize()
river.display()
river.next_time_step(10)
river.display()