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
	def __init__(self, description, location):
		super(ToDo, self).__init__()
		self.description = description
		self.isThisDone = False
		self.location = location or None
	
	@property
	def description(self): return self.description

	@property
	def location(self): return self.location

	@property
	def isThisDone(self): return self.isThisDone

	def done(self):
		self.isThisDone = True

	def notDone(self):
		self.isThisDone = False

	def changeDescription(self, newdesc):
		self.description = newdesc

	def setLocation(locationString):
		self.location = str(locationString)
	
	def __str__(self):
		if self.location is not None 
			if self.isThisDone:
				return "ToDo Object: '%s' at %s is complete" % (self.description, self.location)
			else:
				return "ToDo Object: '%s' at %s is not complete" % (self.description, self.location)
		if self.location is None
			if self.isThisDone:
				return "ToDo Object: '%s' is complete" % (self.description, self.location)
			else:
				return "ToDo Object: '%s' is not complete" % (self.description, self.location)

class ToDoList(object):
	"""docstring for ToDoList"""
	def __init__(self, listName, password):
		# super(ToDoList, self).__init__()
		self.listName = listName
		self.password = password
		self.todoList = {}
		
	def newList():





class ToDoList():
	# item

	#addToDo

	#deleteToDo

	#markDone

	#reorder

	#print


