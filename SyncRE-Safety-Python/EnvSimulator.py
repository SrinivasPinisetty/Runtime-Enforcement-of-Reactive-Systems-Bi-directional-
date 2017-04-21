###########################################################################
##Simulator of environment.
##Input: inActions- set of input actions Sigma_I, trLength- Length of the trace to be generated.  
##Output: Returns a sequence of actions in Sigma_I.
############################################################################
import random
###########################################################################
def genEnvInputTrace(inActions, trLength):
    trace = []
    for i in range(0,trLength):
        trace.append(random.choice(inActions))
    return trace
###########################################################################    
    