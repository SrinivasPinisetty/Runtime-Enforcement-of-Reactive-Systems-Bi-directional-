#######imports###########
import sys
sys.path.append("../")
import Automata
import SyncRE
import SyncEnforcer
import EnvSimulator
import copy
import time
#########################
#

#################################################################################################
###Define automaton describing property to enforcer phi##########################################
######### (actions, states, initial state, final states, transitions)############################
##This automaton defines "A and E cannot happen simultaneously, where I = {A}, and O = {E}."#####
#################################################################################################
phiAut = Automata.NFA(
[('1','1'), ('1','0'), ('0','1'), ('0','0')],
['q0', 'qv'],
'q0',
lambda q: q in ['q0'],
lambda q, a: {
        ('q0', ('1','0')) : ['q0'],
        ('q0', ('0','1')) : ['q0'],
        ('q0', ('0','0')) : ['q0'],
        ('q0', ('1','1')) : ['qv'],
        ('qv', ('1','0')) : ['qv'],
        ('qv', ('0','1')) : ['qv'],
        ('qv', ('0','0')) : ['qv'],
        ('qv', ('1','1')) : ['qv'],
    }[(q, a)]
)
#
###################################################################################
### Invoke the enforcer with property phi, and some test env input sequencences ###
######### (phi, env input sequence sigmaI)#########################################
###################################################################################

Sigma_I = SyncRE.getInputAlphabet(phiAut)
Sigma_O = SyncRE.getOutAlphabet(phiAut)


inputTraceEnv = EnvSimulator.genEnvInputTrace(Sigma_I, 5)

print "######################"
print "TEST1.." 
print "property is..'A and E cannot happen simultaneously, where I = {A}, and O = {E}.'" 

t1 = time.clock()
e1= SyncEnforcer.enforcer(copy.copy(phiAut), inputTraceEnv)
t2 = time.clock()
print "total time is.." + str(t2-t1)
print "######################" 
#############################################################################








