# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 14:13:00 2021

@author: 3mrullah
"""
"""
import numpy as np
from ProblemClass import *


problem = ZeroOneKnapsack('data/01KP','f1_l-d_kp_10_269')
solution = np.random.uniform(size = problem.dimension) > 0.5

cost = problem.objective_function(solution)
"""

problem = OneMax(100)
solution = np.random.uniform(size = problem.dimension) > 0.5

cost = problem.objective_function(solution)


problem = TSP('data/TSP','a280.tsp')
solution = np.random.permutation(problem.dimension)
cost = problem.objective_function(solution)

best_sol = [1,2,242,243,244,241,240,239,238,237,236,235,234,233,232,231,246,245,247,250,251,230,229,228,227,226,225,224,223,222,221,220,219,218,217,216,215,214,213,212,211,210,207,206,205,204,203,202,201,198,197,196,195,194,193,192,191,190,189,188,187,186,185,184,183,182,181,176,180,179,150,178,177,151,152,156,153,155,154,129,130,131,20,21,128,127,126,125,124,123,122,121,120,119,157,158,159,160,175,161,162,163,164,165,166,167,168,169,170,172,171,173,174,107,106,105,104,103,102,101,100,99,98,97,96,95,94,93,92,91,90,89,109,108,110,111,112,88,87,113,114,115,117,116,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,59,63,62,118,61,60,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,22,25,23,24,14,15,13,12,11,10,9,8,7,6,5,4,277,276,275,274,273,272,271,16,17,18,19,132,133,134,270,269,135,136,268,267,137,138,139,149,148,147,146,145,199,200,144,143,142,141,140,266,265,264,263,262,261,260,259,258,257,254,253,208,209,252,255,256,249,248,278,279,3,280]

best_sol[:] = [number - 1 for number in best_sol]

best_cost = problem.objective_function(best_sol)

best_sol = [1,49,32,45,19,41,8,9,10,43,33,51,11,52,14,13,47,26,27,28,12,25,4,6,15,5,24,48,38,37,40,39,36,35,34,44,46,16,29,50,20,23,30,2,7,42,21,17,3,18,31,22]

best_sol[:] = [number - 1 for number in best_sol]

best_cost = problem.objective_function(best_sol)

temp = 999999
for i in range(1000):
    solution = np.random.permutation(problem.dimension)
    cost = problem.objective_function(solution)
    
    if cost < temp:
        temp = cost
