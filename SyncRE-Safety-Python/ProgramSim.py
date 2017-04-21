###########################################################################
##Simulator of synchronous program.
##Input: set of input actions Sigma_I, set of output actions Sigma_O, and an input action x in Sigma_I. 
########Output: Return an output action y in Sigma_O.
############################################################################
import random
###########################################################################
def progSimulator(Sigma_I, Sigma_O, inAction):
    
    if inAction in Sigma_I:
        return random.choice(Sigma_O)
    else:
        return "Error, not valid input action."
###########################################################################    

