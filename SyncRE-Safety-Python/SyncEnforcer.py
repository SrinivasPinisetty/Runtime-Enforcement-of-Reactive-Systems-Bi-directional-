##imports###########################
import SyncRE
import random
import ProgramSim
import FuncLists
####################################
#
#############################################################################
####EditI function ##########################################################
####Input: Automaton phiI, and a state qI of the automaton phiI##############
####Output: Returns all input actions that lead to an accepting state #######
############# in phiI from qI (in one step). ################################
#############################################################################  
def editI(phiI, qI):
    goodAct = []
    for act in phiI.S:
        for loc in phiI.d(qI,act):
            if phiI.F(loc):
                if not act in goodAct:
                    goodAct.append(act)
    return goodAct
########################################################################
#
######################################################################### 
def rand_editI(actions):
    if actions.__len__() >= 0:
        return random.choice(actions)
    else:
        return "NONE" 
##########################################################################    
#
######################################################################### 
def min_editI(actions, event):
    diff_count = []
    if actions.__len__() >= 0:
        for act in actions:
            count = 0
            u=zip(event, act)
            #print str(u)
            for i,j in u:
                if not i==j:
                    count = count+1
            diff_count.append(count)    
        min_indexes = FuncLists.all_indices(min(diff_count), diff_count)
        return actions[random.choice(min_indexes)]
    else:
        return "NONE" 
############################################################################
 
########################################################################
####EditO function. ####################################################
####Input: Automaton phi, a state q of the automaton phi, ##############
####################################and an input action x. #############
####Output: Returns all output actions y that lead to acc state ########
####################### (in one step) in phi from qI upon event (x, y)##
########################################################################
def editO(phi, q, x):
    outAct = []
    goodOutAct = []
    for act in phi.S:
        if not (act[1] in outAct):
            outAct.append(act[1])
    for act in outAct:
        for loc in phi.d(q,(x,act)):
            if phi.F(loc):
                if not act in goodOutAct:
                    goodOutAct.append(act)
    return goodOutAct
########################################################################
########################################################################        

######################################################################### 
def rand_editO(actions):
    if actions.__len__() >= 0:
        return random.choice(actions)
    else:
        return "NONE" 
##########################################################################  
#
######################################################################### 
def min_editO(actions, outEvent):
    diff_count = []
    if actions.__len__() >= 0:
        for act in actions:
            count = 0
            u=zip(outEvent, act)
            #print str(u)
            for i,j in u:
                if not i==j:
                    count = count+1
            diff_count.append(count)    
        min_indexes = FuncLists.all_indices(min(diff_count), diff_count)
        return actions[random.choice(min_indexes)]
    else:
        return "NONE" 
##########################################################################   
#    
########################################################################
###Enforcer takes a DFA phi and an input sequence of events#############
####Computes the output sequence incrementally.#########################
########################################################################
def enforcer(phi, sigma_I):
    ##Initially output is empty.###
    outputE= []
    ##Input automaton phiI from input-output automaton phi.##
    phiI = SyncRE.getPhiI(phi)
    
    Sigma_I = SyncRE.getInputAlphabet(phi)
    Sigma_O = SyncRE.getOutAlphabet(phi)
            
    ## q keeps track of current state of automaton phi.###
    ## qI keeps track of current state of automaton phiI.###
    q=phi.q0
    qI=phiI.q0
   
    #print "input from env to the enforcer is.." + str(sigma_I) 
    
    ## Replace with While ###
    for in_event in sigma_I:
        print "env input x is.."+str(in_event)
        
        ## transformed input xNew, and transformed output yNew initialized to "NONE" ##
        xNew = "NONE"
        yNew = "NONE"
        
        ## If from qI upon x, there is a transition in phiI to an accepting state##
        for qI_next in phiI.d(qI,in_event):
            if phiI.F(qI_next):
                xNew = in_event
                qI = qI_next
                #outputEI.append(xNew)
                print "Transformed input: "+str(xNew)
                break
            else: continue
        ## If from qI upon x, there is NO transition in phiI to an accepting state##
        ###and there is a transition in phiI from qI upon some other action to an accepting state##    
        if (xNew == "NONE" and not editI(phiI, qI) == "NONE"): 
            #xNew = rand_editI(editI(phiI, qI))
            xNew = min_editI(editI(phiI, qI), in_event)
            #outputEI.append(xNew)
            print "Transformed env input x' is: "+str(xNew)
            for qi in phiI.d(qI,xNew):
                if phiI.F(qi):
                    qI = qi
                    break
        ###There is no transition in phiI from qI to an accepting state##         
        elif (xNew == "NONE" and editI(phiI, qI) == "NONE"):
            return
        
        ######Invoke program with transformed input xNew ###########
        ########Process and transform output y returned by program ###############
        y = ProgramSim.progSimulator(Sigma_I, Sigma_O, xNew)
        print "Program output y is: " + str(y)        
        ## If from q upon (xNew,y), there is a transition in phi to an accepting state ##
        ## phi.d(q,(xNew,y)): all states reachable from q upon (xNew,y) ####
        for q_next in phi.d(q,(xNew,y)):
            if phi.F(q_next):
                yNew = y
                q = q_next
                print "Transformed prog output y' is: "+str(yNew)
                print "output event is.."+ str((xNew,yNew))
                outputE.append((xNew,yNew))
                break
            else: continue
        
        ## If from q upon (xNew,y), there is NO transition in phi to an accepting state ##
        ## but there is a transition from q to an accepting state upon (xNew, y') ######        
        if (yNew == "NONE" and not editO(phi, q, xNew) == "NONE"): 
            #yNew = rand_editO(editO(phi, q,xNew))
            yNew = min_editO(editO(phi, q,xNew), y)
            outputE.append((xNew,yNew))
            print "Transformed prog output y' is: "+str(yNew)
            print "output event is.."+ str((xNew,yNew))
            for q_next in phi.d(q,(xNew,yNew)):
                if phiI.F(q_next):
                    q = q_next
                    break
        elif (yNew == "NONE" and editO(phi, q, xNew) == "NONE"):
            print "Not enforceable..exiting.."
            return
    print "output of the enforcer is.." + str(outputE)
#######################################################################
########################################################################            
