# Salwa Badreddine
# Assignment 5

from breezypythongui import EasyFrame
from tkinter import *

choice = ""
choice1 = ""
newOp = ""
class Calculator(EasyFrame):
	
	def __init__(self):
		
		EasyFrame.__init__(self, title = "Simple Calculator", width = 300, height = 450)	

		self.inputField = self.addFloatField(value = 0.0, row = 0, column = 0, columnspan = 3, width = 300, sticky = N+W+E+S, precision = 5)

		#Adding row 1
		self.addButton(text = "1", row = 1, column = 0, command = lambda: self.getChoice("1")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "2", row = 1, column = 1, command = lambda: self.getChoice("2")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "3", row = 1, column = 2, command = lambda: self.getChoice("3")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		#Adding row 2
		self.addButton(text = "4", row = 2, column = 0, command = lambda: self.getChoice("4")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "5", row = 2, column = 1, command = lambda: self.getChoice("5")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "6", row = 2, column = 2, command = lambda: self.getChoice("6")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		#Adding row 3
		self.addButton(text = "7", row = 3, column = 0, command = lambda: self.getChoice("7")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "8", row = 3, column = 1, command = lambda: self.getChoice("8")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "9", row = 3, column = 2, command = lambda: self.getChoice("9")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		#Adding row 4
		self.addButton(text = "-", row = 4, column = 0, command = lambda: self.getChoice("-")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = "0", row = 4, column = 1, command = lambda: self.getChoice("0")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		self.addButton(text = ".", row = 4, column = 2, command = lambda: self.getChoice(".")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		#Adding panel in row 5
		buttonPanel = self.addPanel(row = 5, column = 0, columnspan = 3)
		buttonPanel.addButton(text = "+", row = 0, column = 0, command = lambda: self.getOperation("+")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		buttonPanel.addButton(text = "-", row = 0, column = 1, command = lambda: self.getOperation("-")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		buttonPanel.addButton(text = "*", row = 0, column = 2, command = lambda: self.getOperation("*")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		buttonPanel.addButton(text = "/", row = 0, column = 3, command = lambda: self.getOperation("/")).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		buttonPanel.addButton(text = "=", row = 0, column = 4, command = lambda: self.doOperation()).grid(sticky = N+E+W+S, padx = 0, pady = 0)
		#Adding row 6
		self.addButton(text = "Clr", row = 6, column = 0, columnspan = 3, command = lambda: self.makeClear()).grid(sticky = N+E+W+S, padx = 0, pady = 0)

	def getChoice(self, number):
		global choice
		choice += str(number)
		self.inputField.setNumber(float(choice))
			
	def getOperation(self, operation):
		global choice, choice1, newOp
		choice1 = choice
		choice = ""
		if operation == "+":
			newOp = "+"
		elif operation == "-":
			newOp = "-"
		elif operation == "*":
			newOp = "*"
		elif operation == "/":
			newOp = "/"
			
	def doOperation(self):
		global choice, choice1, newOp
		if newOp == "+":
			self.inputField.setNumber(float(choice1) + float(choice))
		elif newOp == "-":
			self.inputField.setNumber(float(choice1) - float(choice))
		elif newOp == "*":
			self.inputField.setNumber(float(choice1) * float(choice))
		elif newOp == "/":
			self.inputField.setNumber(float(choice1) / float(choice))
		choice = ""
		choice1 = ""
		newOp = ""
	
	def makeClear(self):
		global choice, choice1, newOp
		self.inputField.setNumber(0.0)
		choice = ""
		choice1 = ""
		newOp = ""
		
Calculator().mainloop()