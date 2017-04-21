##imports######################
import Automata
###############################
#
##################################################################
##Takes automaton phi (that accepts input-output words) and 
### returns automaton phiI obtained from phi.
##################################################################
def getPhiI(phi):
    actions = []
    states = phi.Q
    initialS = phi.q0
    accStates = phi.F
    trans = {}
    
    for action in phi.S:
        if not (action[0] in actions):
            actions.append(action[0])
   
    for q in states:
        for a in actions:
            trans[q,a] = []
          
    for q in phi.Q:
        for a in phi.S:
            for qi in phi.d(q, a):
                if not (qi in trans[(q,a[0])]):
                    trans[(q,a[0])].append(qi)
                    

    return Automata.NFA(actions, states, initialS, 
                accStates, 
                lambda q, a: trans[(q, a)]
                )   
    
##################################################################
##Takes automaton phi where each action is a tuple (input, output)
### returns input alphabet Sigma_I
##################################################################
def getInputAlphabet(phi):
    inAlphabet= []
    
    for action in phi.S:
        if not (action[0] in inAlphabet):
            inAlphabet.append(action[0])
    return inAlphabet
#####################################################
#####################################################    
#
##################################################################
##Takes automaton phi where each action is a tuple (input, output)
### returns output alphabet Sigma_O
#################################################################
def getOutAlphabet(phi):
    outAlphabet= []
    
    for action in phi.S:
        if not (action[1] in outAlphabet):
            outAlphabet.append(action[1])
    return outAlphabet
#####################################################
#####################################################    



