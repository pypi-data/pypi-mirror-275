

import os
import typing

import jk_typing


from .INode import INode
from .ILink import ILink






class Link(ILink):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self, graph, linkID:int, fromNode:INode, toNode:INode):
		self.__graph = graph
		self.__linkID = linkID
		self.__fromNode = fromNode
		self.__toNode = toNode
		self.__tag = None
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def linkID(self) -> int:
		return self.__linkID
	#

	@property
	def fromNode(self) -> INode:
		return self.__fromNode
	#

	@property
	def toNode(self) -> INode:
		return self.__toNode
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
		return "Link<({}, {}->{})>".format(self.__linkID, repr(self.__fromNode._name), repr(self.__toNode._name))
	#

	def __repr__(self):
		return "Link<({}, {}->{})>".format(self.__linkID, repr(self.__fromNode._name), repr(self.__toNode._name))
	#

	def __hash__(self) -> int:
		return self.__linkID.__hash__()
	#

#







