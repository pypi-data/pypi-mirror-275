

import os
import typing

import jk_typing


from .INode import INode






class Node(INode):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self, graph, nodeID:int, name:str):
		self.__graph = graph
		self.__nodeID = nodeID
		self.__name = name
		self.__tag = None

		self._incomingLinks = {}
		self._outgoingLinks = {}
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def name(self) -> str:
		return self.__name
	#

	@property
	def nodeID(self) -> int:
		return self.__nodeID
	#

	@property
	def isStartNode(self) -> bool:
		return len(self._incomingLinks) == 0
	#

	@property
	def isEndNode(self) -> bool:
		return len(self._outgoingLinks) == 0
	#

	@property
	def tag(self) -> typing.Any:
		return self.__tag
	#

	@tag.setter
	def tag(self, tag:typing.Any):
		self.__tag = tag
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def __str__(self):
		return "Node<({}, {})>".format(self.__nodeID, repr(self.__name))
	#

	def __repr__(self):
		return "Node<({}, {})>".format(self.__nodeID, repr(self.__name))
	#

	def __hash__(self) -> int:
		return self.__nodeID.__hash__()
	#

	def __eq__(self, other: object) -> bool:
		if isinstance(other, Node):
			return other.__nodeID == self.__nodeID
		else:
			return False
	#

#







