# From: Artifical Intelligence, A Modern Approach by Russell and Norvig

"""
|	Percept Sequence				Action			|
|	---------------------------------------------	|		
|	[A, Clean]						Right			|		
|	[A, Dirty]						Suck			|
|	[B, Clean]						Left			|
|	[B, Dirty]						Suck			|
|	---------------------------------------------	|
"""

# Please give credit when used


class SimpleReflexAgent():
	def __init__(self):
		pass

	def agent_program(self, percept):
		location, status = percept
		if status == 'Dirty':
			return 'Suck' # Action
		elif location == 'loc_A':
			return 'Right'
		elif location == 'loc_B':
			return 'Left'

agent = SimpleReflexAgent()
print(agent.agent_program(('loc_A', 'Dirty')))
print(agent.agent_program(('loc_A', 'Clean')))
print(agent.agent_program(('loc_B', 'Dirty')))
print(agent.agent_program(('loc_B', 'Clean')))
