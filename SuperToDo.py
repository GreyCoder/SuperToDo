######
#  SUPER TO DO!!!!!
#   by erik redding <erik@erikerikerik.com>
#  
#	A web-based ToDo List for personal use.  Possibly extend to CLI
#
# Goals:  
#	- create simple data structure to represent a password-protected
#       todo list that is easily pickle-able
#	- extend to simple web interface that prompts for list password 
#		- lists out any existing items with options:
#			[d]one
#			[e]dit item
#			[r]emove item
#		- have a textbox at the top of the page that lets you enter a new item
#			and pressing return adds the items. 
#   - Maybe?? create command-line interface for adding/removing items 
#		- TUI that lists ToDo's available
#		- select list, prompt for password
#		- if correct passwd, list out items and then readline for d,e,r,a
######
import os


class ToDo(object):
	"""base ToDo class - simple datastructure for defining a ToDo Item"""
	def __init__(self, description, location = None):
		super(ToDo, self).__init__()
		self._description = description
		self._isThisDone = False
		self._location = location
	
	@property
	def description(self): 
		return self._description if hasattr(self, '_description') else None

	@description.setter
	def description(self, d):
		self._description = d

	@description.deleter
	def description(self):
		del self._description

	@property
	def location(self): 
		return self._location if hasattr(self, '_location') else None

	@location.setter
	def location(self, s):
		self._location = s

	@location.deleter
	def location(self):
		del self._location

	@property
	def isThisDone(): 
		return self._isThisDone if hasattr(self, '_isThisDone') else False

	def done(self):
		self._isThisDone = True

	def notDone(self):
		self._isThisDone = False
	
	def __str__(self):
		if self._location is not None:
			if self._isThisDone:
				return "ToDo Object: '%s' at %s is complete" % (self._description, self._location)
			else:
				return "ToDo Object: '%s' at %s is not complete" % (self._description, self._location)
		if self._location is None:
			if self._isThisDone:
				return "ToDo Object: '%s' is complete" % (self._description)
			else:
				return "ToDo Object: '%s' is not complete" % (self._description)

	def __eq__(self, input):
		if isinstance(input, ToDo):
			return input._description == self._description
		if isinstance(input, str):
			return input == self._description
		if isinstance(input, unicode):
			return input == self._description
		return False




class ToDoList(object):
	"""
	This is a ToDoList object - an interface for a collection of ToDo classes

	The interface provides methods to add, remove, mark ToDo items complete, 
		save ToDoLists 
	"""

	def __init__(self, listName, password):
		super(ToDoList, self).__init__()
		self._listName = listName
		self._password = password
		self._todoList = []
		self.index = len(self._todoList)

	def _selectToDo(self, input):
		"""
		Select which ToDo in the List was requested by 'input' - detects 
		if it was a string or an actual ToDo object and then returns
		the array index
		"""
		# if isinstance(toDo, basestring):
		# 	if self._todoList(ToDo)

		# if isinstance(toDo, ToDo):
		# 	self._todoList.remove(toDo)
		pass

	#addToDo
	def addToDo(self, desc):
		self._todoList.append(ToDo(desc))
	def removeToDo(self, toDo):
		pass

	#markDone
	def markDone(self,toDo):	
		self._todoList[toDo].done()

	#print
	def __str__(self):
		return '\n'.join(str(todo) for todo in self._todoList)
		


	def authenticate(self):
		""" 
		provides authentication for the class.  
		It should require that password is set to the correct value.
		"""
		pass

