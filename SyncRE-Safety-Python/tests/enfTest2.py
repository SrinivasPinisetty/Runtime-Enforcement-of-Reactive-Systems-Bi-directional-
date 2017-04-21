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
#
#################################################################################################################
###Define automaton describing property to enforcer phi##########################################################
######### (actions, states, initial state, final states, transitions)############################################
##This automaton defines property "B and R cannot happen simultaneously, where I = {A, B}, and O = {R, W}."######
#################################################################################################################
phiAut = Automata.NFA(
#actions#
[('00','00'), ('00','01'), ('00','10'), ('00','11'), ('01','00'), ('01','01'), ('01','10'), ('01','11'), 
     ('10','00'),('10','01'), ('10','10'), ('10','11'), ('11','00'), ('11','01'), ('11','10'), ('11','11')],
#locations#
['q0', 'qv'],
#initial location#
'q0',
#accepting locations#
lambda q: q in ['q0'],
#transitions#
lambda q, a: {
        ('q0', ('00','00')) : ['q0'],
        ('q0', ('00','01')) : ['q0'],
        ('q0', ('00','10')) : ['q0'],
        ('q0', ('00','11')) : ['q0'],
        ('q0', ('01','00')) : ['q0'],
        ('q0', ('01','01')) : ['q0'],
        ('q0', ('01','10')) : ['qv'],
        ('q0', ('01','11')) : ['qv'],
        ('q0', ('10','00')) : ['q0'],
        ('q0', ('10','01')) : ['q0'],
        ('q0', ('10','10')) : ['q0'],
        ('q0', ('10','11')) : ['q0'],
        ('q0', ('11','00')) : ['q0'],
        ('q0', ('11','01')) : ['q0'],
        ('q0', ('11','10')) : ['qv'],
        ('q0', ('11','11')) : ['qv'],
        
        ('qv', ('00','00')) : ['qv'],
        ('qv', ('00','01')) : ['qv'],
        ('qv', ('00','10')) : ['qv'],
        ('qv', ('00','11')) : ['qv'],
        ('qv', ('01','00')) : ['qv'],
        ('qv', ('01','01')) : ['qv'],
        ('qv', ('01','10')) : ['qv'],
        ('qv', ('01','11')) : ['qv'],
        ('qv', ('10','00')) : ['qv'],
        ('qv', ('10','01')) : ['qv'],
        ('qv', ('10','10')) : ['qv'],
        ('qv', ('10','11')) : ['qv'],
        ('qv', ('11','00')) : ['qv'],
        ('qv', ('11','01')) : ['qv'],
        ('qv', ('11','10')) : ['qv'],
        ('qv', ('11','11')) : ['qv'],
        }[(q, a)]
)


#
###############################################################################
### Invoke the enforcer with property phi, and some test env input sequencences ###
######### (phi, env input sequence.)#######################################
###############################################################################

Sigma_I = SyncRE.getInputAlphabet(phiAut)
Sigma_O = SyncRE.getOutAlphabet(phiAut)

print "######################"
print "TEST1.." 
inputTraceEnv = EnvSimulator.genEnvInputTrace(Sigma_I, 10)
print "property is..'B and R cannot happen simultaneously, where I = {A,B}, and O = {R,W}.'" 
t1 = time.clock()
e1= SyncEnforcer.enforcer(copy.copy(phiAut), inputTraceEnv)
t2 = time.clock()
print "total time is.." + str(t2-t1)
print "######################" 

 
#print "######################"
#print "TEST2.." 
#inputTraceEnv = EnvSimulator.genEnvInputTrace(Sigma_I, 100)
#print "property is..'B and R cannot happen simultaneously, where I = {A,B}, and O = {R,W}.'" 
#e1= SyncEnforcer.enforcer(copy.copy(phiAut), inputTraceEnv)
#print "######################"











