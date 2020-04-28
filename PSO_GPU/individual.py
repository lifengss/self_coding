
# from pop import POP

class Individual(object):

    def __init__(self, n_POP, dim, limit=None):
        """
        Initial position and velocity.
        """
        self.__n_POP = n_POP    # not used
        self.__dim = dim
        self.__limt = limit
        self.__p_bset = None
        self.__fitness = None

        if self.__limit is not None:
            sup_bound = np.max(self.__limit)
            inf_bound = np.min(self.__limit)
        else:
            sup_bound = float('Inf')
            inf_bound = float('-inf')