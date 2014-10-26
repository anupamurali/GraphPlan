"""
Created on Oct 20, 2013

@author: Ofra
"""
from action import Action
from actionLayer import ActionLayer
from util import Pair
from proposition import Proposition
from propositionLayer import PropositionLayer

class PlanGraphLevel(object):
  """
  A class for representing a level in the plan graph.
  For each level i, the PlanGraphLevel consists of the actionLayer and propositionLayer at this level in this order!
  """
  independentActions = []  # updated to the independentActions of the propblem GraphPlan.py line 31 
  actions = []             # updated to the actions of the problem GraphPlan.py line 32 and planningProblem.py line 25
  props = []               # updated to the propositions of the problem GraphPlan.py line 33 and planningProblem.py line 26
  
  @staticmethod
  def setIndependentActions(independentActions):
    PlanGraphLevel.independentActions = independentActions
  
  @staticmethod  
  def setActions(actions):
    PlanGraphLevel.actions = actions
  
  @staticmethod    
  def setProps(props):
    PlanGraphLevel.props = props   
  
  def __init__(self):
    """
    Constructor
    """
    self.actionLayer = ActionLayer()    		# see actionLayer.py
    self.propositionLayer = PropositionLayer()	# see propositionLayer.py

  
  def getPropositionLayer(self):
    return self.propositionLayer
  
  def setPropositionLayer(self, propLayer):
    self.propositionLayer = propLayer  
  
  def getActionLayer(self):
    return self.actionLayer
    
  def setActionLayer(self, actionLayer):
    self.actionLayer = actionLayer

  def updateActionLayer(self, previousPropositionLayer):
    """ 
    Updates the action layer given the previous proposition layer (see propositionLayer.py)
    allAction is the list of all the actions (include noOp in the domain)
    """ 
    allActions = PlanGraphLevel.actions
    "*** YOUR CODE HERE ***"
   

  def updateMutexActions(self, previousLayerMutexProposition):
    """
    Updates the mutex list in self.actionLayer,
    given the mutex proposition from the previous layer.
    currentLayerActions are the actions in the current action layer
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"
   

  def updatePropositionLayer(self):
    """
    Updates the propositions in the current proposition layer,
    given the current action layer.
    don't forget to update the producers list!
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"


  def updateMutexProposition(self):
    """
    updates the mutex propositions in the current proposition layer
    """
    currentLayerPropositions = self.propositionLayer.getPropositions()
    currentLayerMutexActions =  self.actionLayer.getMutexActions()
    "*** YOUR CODE HERE ***"   
	

  def expand(self, previousLayer):
    """
    Your algorithm should work as follows:
    First, given the propositions and the list of mutex propositions from the previous layer,
    set the actions in the action layer. 
    Then, set the mutex action in the action layer.
    Finally, given all the actions in the current layer, set the propositions and their mutex relations in the proposition layer.   
    """
    previousPropositionLayer = previousLayer.getPropositionLayer()
    previousLayerMutexProposition = previousPropositionLayer.getMutexProps()

    "*** YOUR CODE HERE ***"   

            
  def expandWithoutMutex(self, previousLayer):
    """
    Questions 11 and 12
    You don't have to use this function
    """
    previousLayerProposition = previousLayer.getPropositionLayer()
    "*** YOUR CODE HERE ***"
	
		
def mutexActions(a1, a2, mutexProps):
  """
  Complete code for deciding whether actions a1 and a2 are mutex,
  given the mutex proposition from previous level (list of pairs of propositions).
  Your updateMutexActions function should call this function
  """
  # Get preconditions of both actions
  pre1 = a1.getPre()
  pre2 = a2.getPre()

  # Competing needs: Check if a1 and a2 have preconditions that are mutex
  for p1 in pre1:
    for p2 in pre2:
      if Pair(p1, p2) in mutexProps:
        return True
  # Check if a1 and a2 have inconsistent effects or interfere
  ## TODO: CHECK IN INDEPENDENTACTIONS INSTEAD OF CALLING FUNCTION
  if !GraphPlan.independentPair(a1, a2):
    return True
  return False

  
		
def mutexPropositions(prop1, prop2, mutexActions):
  """
  complete code for deciding whether two propositions are mutex,
  given the mutex action from the current level (list of pairs of actions).
  Your updateMutexProposition function should call this function
  """
  prod1 = prop1.getProducers()
  prod2 = prop2.getProducers()
  for a1 in prod1:
    for a2 in prod2:
      if Pair(a1,a2) in mutexActions:
        return True
  return False
 