# From: Artifical Intelligence, A Modern Approach by Russell and Norvig

"""
	Percept 					SequenceAction			
	---------------------------------------------			
	[A, Clean]					Right					
	[A, Dirty]					Suck			
	[B, Clean]					Left			
	[B, Dirty]					Suck			
	[A, Clean],[B, Clean]		No Operation	
	---------------------------------------------
"""

# Please give credit when used


class ModelBasedAgent():
	def __init__(self):
		self.model = {'loc_A': None, 'loc_B': None}

	def agent_program(self, percept):
		location, status = percept
		self.model[location] = status #update the model
		if self.model['loc_A'] == self.model['loc_B'] == 'Clean':
			return 'No Operation'
		if status == 'Dirty':
			return 'Suck'
		elif location == 'loc_A':
			return 'Right'
		elif location == 'loc_B':
			return 'Left'

agent = ModelBasedAgent()
print(agent.agent_program(('loc_A', 'Dirty')))
print(agent.agent_program(('loc_A', 'Clean')))
print(agent.agent_program(('loc_B', 'Dirty')))
print(agent.agent_program(('loc_B', 'Clean')))
