import numpy as np

class WTA:
    def __init__(self, folderName, fileName):
        self.folderName = folderName
        self.fileName = fileName
        self.values = []
        self.probabilities = []        
        
        with open(f"{folderName}/{fileName}") as f:
            self.dimension = int (f.readline())
            for i in range(self.dimension):
                self.values.append(int (f.readline()))
            for i in range(self.dimension * self.dimension):
                 self.probabilities.append(float (f.readline()))
                
    
    def objective_function(self, sol):
        total_cost = 0
        for i in range(self.dimension):
            total_cost = total_cost + (self.values[i] * (1 - self.probabilities[self.dimension * sol[i] + i]))
            
        return total_cost


"""
problem = WTA('wta','wta5.txt')
operator = Operators(problem.dimension, op_name='swap')
hc = hillClimbing(problem, operator)
res = hc.run()
"""
#problem = WTA('wta','wta5.txt')
#operator = Operators(problem.dimension, op_name='swap')
#ssa = SSA(problem, operator, swarm_size = 15, min_values = [-5,-5], max_values = [5,5], iterations = 200, target_function = rosenbrocks_valley)






