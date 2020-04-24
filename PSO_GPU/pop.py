import torch
from torch.autograd import Variables
import numpy as np


class POP(object):
    
    def __init__(self,n_POP,limit=None, fitness_fun=None, **kargs):
        '''
        Generate PSO population and their relative parameters.
        
        :n_POP: number of population, a scale.
        :limit: constrain of population postion. An array in the shape of [2, dim]--direct range constrain of pop. TODO: extend to equation/unequation constrain.
        '''
        self._n_POP = n_POP
        self._limit = limit
        self._fitness = None
        self._fitness_fun = fitness_fun
        self.POP, self.V = None, None
        self.p_best = None
        self.g_best = None
        self._initialize()

    def _initialize(self):
        '''
        Initialize population, velocities and history best position of individual based on limitaions.
        :set: 
            self.POP: population position. A tensor in the shape of [n_POP, dim].
            self.V: population velocity. A tensor in the shape of [n_POP, dim].
            self.p_best: Best solution of a individual during its search history. A tensor in the shape of [n_POP, dim]
            self.g_best: Best solution among all POP during their search history. A tensor in the shape of [1, dim]
            self._fitness: fitness of POP, calculated by fitness function. A tensor in the shape of [n_POP, 1]-- single objective optimize. 
            TODO: extend to multiple objectives in future.
        '''

        if self._limit is not None:
            sup_bound = np.max(self._limit)
            inf_bound = np.min(self._limit)
            

