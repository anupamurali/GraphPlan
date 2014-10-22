"""
Created on Oct 19, 2013

@author: Ofra
"""
from util import Pair

class ActionLayer(object):
  """
  A class for an ActionLayer in a level of the graph.
  The layer contains a list of actions (action objects) and a list of mutex actions (Pair objects)
  """


  def __init__(self):
    """
    Constructor
    """
    self.actions = []      # list of all the actions in the layer
    self.mutexActions = [] # list of pairs of action that are mutex in the layer
    
  def addAction(self, act):
    self.actions.append(act)
    
    
  def removeActions(self, act):
    self.actions.remove(act)
    
  def getActions(self):
    return self.actions
  
  def getMutexActions(self):
    return self.mutexActions
    
  def addMutexActions(self, a1, a2):
    self.mutexActions.append(Pair(a1,a2))
  
  
  def isMutex(self, Pair):
    """
    Returns true if the pair of actions are mutex in this action layer
     """
    return Pair in self.mutexActions
  
  def effectExists(self, prop):
    """
    Returns true if at least one of the actions in this layer has the proposition prop in its add list
    """ 
    for act in self.actions:
      if prop in act.getAdd():
        return True
    return False
  
  def __eq__(self, other):
    return (isinstance(other, self.__class__)
      and self.__dict__ == other.__dict__)

  def __ne__(self, other):
    return not self.__eq__(other)
