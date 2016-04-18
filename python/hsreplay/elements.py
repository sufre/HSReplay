from xml.etree import ElementTree


class Node:
	attributes = ()

	def __init__(self, *args):
		self.nodes = []
		for k, arg in zip(("ts", ) + self.attributes, args):
			setattr(self, k, arg)

	def append(self, node):
		self.nodes.append(node)

	def xml(self):
		element = ElementTree.Element(self.tagname)
		for node in self.nodes:
			element.append(node.xml())
		for attr in self.attributes:
			attrib = getattr(self, attr)
			if isinstance(attrib, int):
				# Check for enums
				attrib = str(int(attrib))
			if attrib is not None:
				element.attrib[attr] = attrib
		if self.timestamp and self.ts:
			element.attrib["ts"] = self.ts.isoformat()
		return element

	def __repr__(self):
		return "<%s>" % (self.__class__.__name__)


class GameNode(Node):
	tagname = "Game"
	timestamp = True

	def __init__(self, ts):
		super().__init__(ts)
		self.first_player = None
		self.second_player = None


class GameEntityNode(Node):
	tagname = "GameEntity"
	attributes = ("id", )
	timestamp = False


class PlayerNode(Node):
	tagname = "Player"
	attributes = ("id", "playerID", "accountHi", "accountLo", "name")
	timestamp = False


class FullEntityNode(Node):
	tagname = "FullEntity"
	attributes = ("id", "cardID")
	timestamp = False


class ShowEntityNode(Node):
	tagname = "ShowEntity"
	attributes = ("entity", "cardID")
	timestamp = False


class ActionNode(Node):
	tagname = "Action"
	attributes = ("entity", "type", "index", "target")
	timestamp = True


class MetaDataNode(Node):
	tagname = "MetaData"
	attributes = ("meta", "entity", "info")
	timestamp = False


class MetaDataInfoNode(Node):
	tagname = "Info"
	attributes = ("index", "entity")
	timestamp = False


class TagNode(Node):
	tagname = "Tag"
	attributes = ("tag", "value")
	timestamp = False


class TagChangeNode(Node):
	tagname = "TagChange"
	attributes = ("entity", "tag", "value")
	timestamp = False


class HideEntityNode(Node):
	tagname = "HideEntity"
	attributes = ("entity", "zone")
	timestamp = True


##
# Choices

class ChoicesNode(Node):
	tagname = "Choices"
	attributes = ("entity", "id", "taskList", "type", "min", "max", "source")
	timestamp = True


class ChoiceNode(Node):
	tagname = "Choice"
	attributes = ("index", "entity")
	timestamp = False


class ChosenEntitiesNode(Node):
	tagname = "ChosenEntities"
	attributes = ("entity", "id")
	timestamp = True


class SendChoicesNode(Node):
	tagname = "SendChoices"
	attributes = ("id", "type")
	timestamp = True


##
# Options

class OptionsNode(Node):
	tagname = "Options"
	attributes = ("id", )
	timestamp = True


class OptionNode(Node):
	tagname = "Option"
	attributes = ("index", "entity", "type")
	timestamp = False


class SubOptionNode(Node):
	tagname = "SubOption"
	attributes = ("index", "entity")
	timestamp = False


class OptionTargetNode(Node):
	tagname = "Target"
	attributes = ("index", "entity")
	timestamp = False


class SendOptionNode(Node):
	tagname = "SendOption"
	attributes = ("option", "subOption", "target", "position")
	timestamp = True
