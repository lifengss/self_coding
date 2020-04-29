
# from pop import POP
import numpy as np
class Individual(object):

    def __init__(self, dim, limit=None):
        """
        Initial position and velocity.

        :dim: dimension of a solution.
        :limit: constrain of solutions. A numpy array in the shape of [2, dim]
        """
        self.__pos = None    # not used
        self.__dim = dim
        self.__limit = limit
        self.__p_bset = None
        self.__fitness = None

        if self.__limit is not None:
            sup_bound = np.max(self.__limit, axis=0)
            inf_bound = np.min(self.__limit, axis=0)
        else:
            sup_bound = float(1)
            inf_bound = float(-1)
        
        self.__pos = inf_bound + np.random.random(dim) * (sup_bound - inf_bound)
    
    @property
    def pos(self,):
        return self.__pos
    
    @pos.setter
    def pos(self,pos):
        self.__pos = pos
    

    @property
    def fitness(self,):
        return self.__fitness

    @fitness.setter
    def fitness(self, fitness):
        self.__fitness = fitness

if __name__ == "__main__":
    limit = np.asarray([[-10,1],[2,-5],[3,10]])
    print(np.transpose(limit))
    indi = Individual(3,limit=np.transpose(limit))

    print(indi.pos)