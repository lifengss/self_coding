import torch
from torch.autograd import Variables
import numpy as np

from individual import Individual


class POP(object):
    
    def __init__(self,n_POP,limit=None, fitness_fun=None, cluster='', **kargs):
        '''
        Generate PSO population and their relative parameters.
        
        :n_POP: number of population, a scale.
        :limit: constrain of population postion. An array in the shape of [2, dim]--direct range constrain of pop. TODO: extend to equation/unequation constrain.
        '''
        self.__n_POP = n_POP
        self.__limit = limit
        self.__cluster = cluster
        self.__iter = None
        self.__fitness = None
        self.__fitness_fun = fitness_fun # must be a graph
        self.__POP, = None
        self.__g_best = None
        self.__POP_pos = None

    def initialize(self):
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

        self.__iter = 0

        # if self._limit is not None:
        #     sup_bound = np.max(self.__limit)
        #     inf_bound = np.min(self.__limit)
        # else:
        #     sup_bound = float('Inf')
        #     inf_bound = float('-inf')
        
        for i in range(self.__n_POP):
            self.__POP[i] = Individual(self.__n_POP, limit=self.__limit)
        
            
    @property
    def fitness(self,):
        return self.__fitness

    @property
    def iter(self,):
        return self.__iter

    @property
    def n_POP(self,):
        return self.__n_POP

    @property
    def POP(self,):
        return self.__POP

    @property
    def POP_pos(self,):
        self.__POP_pos = self.get_pos()
        return self.__POP_pos

    @POP_pos.setter
    def POP_pos(self,pos):
        self.__POP_pos = pos
        self.__POP = self.set_pos()
    
    def reset_pop(self,):
        self.initialize()

