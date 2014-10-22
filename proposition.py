"""
Created on Oct 20, 2013

@author: Ofra
"""

class Proposition(object):
  """
  A class for representing propositions. 
  Each proposition object has a name and a list of producers,
  that is the actions that have the proposition on their add list
  """

  def __init__(self,name):
    """
    Constructor
    """
    self.name = name	# the name of the proposition as string
    self.producers = []	# list of actions  
    
  def getName(self):
    return self.name
  
  def getProducers(self):
    return self.producers

  def setProducers(self, producers):
    self.producers = producers
  
  def addProducer(self, producer):
      self.producers.append(producer)  
  
  def __eq__(self, other):
    return (isinstance(other, self.__class__)
      and self.name == other.name)

  def __str__(self):
    return self.name

  def __ne__(self, other):
    return not self.__eq__(other)
    
