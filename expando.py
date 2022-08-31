#expando.py
from datetime import datetime
from multiprocessing import current_process
from nis import match
from operator import ne
import importlib
# importlib.reload(module)
import time
import os
import re
import json
from typing import OrderedDict
# import inspect

from dill.source import getsource
import dill

# class Expando(object):
# 	"""docstring for SelfNamed."""
# 	__id = "xxx"
# 	_hiddenAttr = ["_id", "_name", "_parent", "_val", "_zzz"]
	
# 	def __init__(self, id = None, val = None):
# 		super().__init__()
# 		pass #print("|||||||||||||||||||||||||||||||||||||||||||||||||||")
# 		self.__id = id
# 		self[Expando._valueArg] = val
# 		#### self.arg = arg

# 	def __setattr__(self, name, value):
# 		pass #printx("EEEEEEEEEEEEEEEEEEEE---1")


# 	def __assign__(self, v):
# 		pass #print('called with %s' % v)



# TODO: improve
# def getWatchablesForFormulaMock(func):
# 	return ["name.first","name.last"]
def getWatchablesForFormula(func):
	try:
		# dill.detect.code(func)
		return getAllObjects(getsource(dill.detect.code(func)))
	except:
		return getAllObjects(getsource(func))
	#TODO: fix for lambda in interpreter
		
	reg = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
	return re.search(reg, getsource(func)).groups()


def getAllObjects(given):
	given = given.split('<<=')[-1]
	regex = re.compile(r'(?P<xo>xo(\.\w+)*)')
	# regex = re.compile(r'(?P<name>xo.name\.[a-zA-Z]+)')
	# regex = re.compile(r'\\w+(?:\\.\\w+)+')

	def removeHiddenAtEnd(s):
		print("st1",s)
		end = s.split('.')[-1]
		if not end.startswith('_'):
			return s
		else:
			return removeHiddenAtEnd('.'.join(s.split('.')[:-1]))

	return [removeHiddenAtEnd(x[0].lstrip("xo.")) for x in re.findall(regex, given)]




# class Expando(dict):
class Expando(OrderedDict):
	"""docstring for Expando."""
	_hiddenAttr = ["value", "_val", "getattr",
                "show", "_id", "__dict__", "startswith"]
	_rootName = "xo"
	_valueArg = "value"

	__id = "xxx"

	
	# def __assign__(self, v):
	# 	print('called with %s' % v)
	
	#### def __init__(self, val, id = None):
	#### 	super().__init__(id = id)
	#### 	self.__id = id


#### 	def __init__(self, val = "__17__", id = None, **entries):####, wrapper = False, main = True):
#### #### ####expando.py
#### #### 		#### def __init__(self):
#### #### 		#### es=traceback.extract_stack()
#### #### 		super().__init__(id = id)
#### #### 		self.name = self.GetName()
#### #### 		self.__dict__.update(entries)
#### #### 		self.__validID_ = False
#### #### 		#### global GD
#### #### 		#### self.xxx = self.get_my_name()
#### #### 		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
#### 		super().__init__(id = id)
####
#### 		exist = True
#### 		'''
#### 		birth = str(time.time())
#### 		if id is None:
#### 			id = birth
#### 		'''
####
#### 		#### self.__main__ = main
#### 		self.__id__ = "hidden"
#### 		self.__dict__.pop("__id__")
#### 		self[Expando._valueArg] = val
#### 		print("obj created! =",self[Expando._valueArg])
#### 		#### self._zzz = 5
####
####
####
####
#### 		#### print("******---",self.get_my_name())
#### 		#### self["_id"] = self.get_my_name()[0]
####
#### 		#### self.xxx.yyy.zzz = 13
#### 		#### updateID = Thread(target = self.makeID, args = [list,])
#### 		#### updateID.start()
####
#### 		print("AAAAAAAAAAA	AAA",entries,self.__name__)
#### 		for arg_name in entries:
#### 			print("AAAAAAAAAAAAA",arg_name)

	def tree(self):
		for a in self:
			if not a.startswith("_") and a not in Expando._hiddenAttr:
				yield self[a]
				if self[a] != None:
					for z in self[a].tree():
						yield z

	

	# def subscribe(self, func = None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	# 	if func is None:
	# 		func = lambda a, *aa, **aaa : [a,aa,aaa]
	# 		withID = True
	# 	channel = self._id.replace(".","/")
	# 	# print("CCCCCCCCCCCCCCCCCC",channel)
	# 	return xo.subscribe(channel, func=func, autoPub = autoPub, block = block, once= once, echo=echo, debug = debug, withID = withID)

	def fill(self, inputs):
		index = {}
		for z in self.tree():
			if z._name in inputs:
				inputs.remove(z._name)
				print("enter",z._name+": ")
				if "/" in z._id:
					si = len(self._id)
					index[z._id[si:]] = input()
		for a in index.keys():
			self[a] = index[a]
		print("\nDONE")

	# def kids(self):

	# 			for a in self:
	# 				if not a.startswith("_") and a not in Expando._hiddenAttr:
	# 					yield self[a]



	# def children(self):
	# 	# childs = []
	# 	childs = {}
	# 	for a in self:
	# 		if not a.startswith("_") and a not in Expando._hiddenAttr:
	# 			# childs.append(self[a])
	# 			childs[a]=self[a]
	# 	return childs

	def reloadImport(self, module):
		return importlib.reload(module)
		
# 	def __init__(self, val = None, id = None, main = True, parent = None, **entries):####, wrapper = False, main = True):
# 	####expando.py
# 		#### def __init__(self):
# 		#### es=traceback.extract_stack()
# 		# super().__init__(id = id, val = val)
# 		super().__init__()
# 		pass #print("PPPPPPPPPPPPPP", id)
# 		#### self.name = self.GetName()

# 		self.__dict__.update(entries)
# 		if id is None:
# 			id = Expando._rootName
# 		self._name = id.split("/")[-1]
# 		self._id = id
# 		# self._birth = datetime.now()

# 		# self.__id = id
# 		# # print("........")
# 		# super().__init__(val=val, id=id)
# 		# # print("........ddd")

# 		# self.__id = id
# 		self._isRoot = False
# 		if parent is None:
# 			self._isRoot = True
# 		self._parent = parent
# 		#### self.__validID_ = False
# 		#### global GD
# 		#### self.xxx = self.get_my_name()
# 		#### print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
# 		exist = True
# 		'''
# 		birth = str(time.time())
# 		if id is None:
# 			id = birth
# 		'''

# 		self._subscribers = []
# 		# self._triggers = []


# 		#### self.__main__ = main
# 		self.__id__ = "hidden"
# 		self.__dict__.pop("__id__")
# 		self[Expando._valueArg] = val
# 		# print("obj created! =",self[Expando._valueArg])
# 		self._zzz = 5
# 		#### print("******---",self.get_my_name())
# 		#### self["_id"] = self.get_my_name()[0]

# 		#### self.xxx.yyy.zzz = 13
# 		#### updateID = Thread(target = self.makeID, args = [list,])
# 		#### updateID.start()

# 		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
# 		for arg_name in entries:
# 			pass #print("AAAAAAAAAAAAA",arg_name)


# # 		# Binding the object to the value
# #		# global manager
# # 		# self._manager = manager
# # 		# self[Expando._valueArg] = manager.bind(self.__id, val, ref=[self])
	


	def __hash__(self):
		pass #print(hash(str(self)))
		return hash(str(self))

	def getID(self):
		return self.__id__


	def __xset__(self, key, val):
		pass
		# print("eeeeeeeeeeeeeeeeeeeee")
		self.__dict__[key] = val
		return True

	def __xget__(self,key):
		pass
		print("eeeeeeeeeeeeeeeeeeeeeaaa")
		return self.__dict__[key]


	# def __setattr__(self, name, value):
	# 	pass ## print("EEEEEEEEEEEEEEEEEEEE1")
	# 	if "str" not in str(type(name)):
	# 		name = str(name)
	# 	if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr:#### and "__skip" in self.__dict__ and name not in self.skip:
	# 		if "Expando" not in str(type(value)):
	# 			pass ## print("_____________________",str(type(value)))
	# 			if name not in self.__dict__:
	# 				pass ## print("2222222222")
	# 				# print("ppp33333",self._id)
	# 				# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
	# 				self[name] = Expando(id = self._id+"/"+name, val= value, parent = self)
	# 			else:
	# 				pass ## print("33333333")
	# 				#### self.__set__(name,value)
	# 				#### self.save(id = self._id+"/"+name, val= value)
	# 				# if data binding
	# 				# manager.save(channel = self._id+"/"+name, data=value)
	# 				self[name][Expando._valueArg] = value #?????
	# 				self[name]._updateSubscribers_(value)
	# 		else:
	# 			pass ## print("44444")
	# 			self.__dict__[name] = value

	# 	else:
	# 		pass ## print("555555555")
	# 		self.__dict__[name] = value

	# def keys(self):
	# 	return self.keys()

	def __xgetitem__(self, name):
		print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr

		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
			# print("ppp44444")
			#EX1
			self.__dict__[name] = Expando(_id = self._id+"/"+name, _parent = self, _behaviors=self._behaviors)

		if name in self.__dict__:
			#### print("FUUCKKKKKKKKKKKKKKKKKKKKKk")

			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr




	def __assign__(self, v):
		print('called with %s' % v)

	def __xsetitem__(self, name, value):
		pass #print("iiiiiiiiiiiiiiiiioooooooo")
		if "str" not in str(type(name)):
			name = str(name)
		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr:#### and "__skip" in self.__dict__ and name not in self.skip:
			pass #print("VVVVVVVV",str(type(value)))
			if "Expando" not in str(type(value)):
				pass #print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass #print("1",name)
					# print("ppp5555",self)
					#EX2
					self.__dict__[name] = Expando(_id = self._id+"/"+name, _val = value, _parent = self, _behaviors=self._behaviors)
				else:
					pass #print("2",name)
					self[name].set(value)
			else:
				pass #print("22222222222222222222222",name,value)
				self.__dict__[name] = value
				pass #print("YESSSSSSSSS",	self.__dict__[name])
		else:
			pass #print("3",name)
			self.__dict__[name] = value

		#### print("FINISHED SETTING ITEM", self.__dict__)

	def __xgetattribute__(self, name, loop = True):
		# print("NAME:",name)
		# time.sleep(0.1)
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr
		atr = object.__getattribute__(self, name)
		return atr
		
	# def __getattr__(self, name, loop = True):
	# 	print("getttt")
	# 	if "str" not in str(type(name)):
	# 		name = str(name)
	# 	#### return name
	# 	if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
	# 		pass #print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
	# 		pass #print("aaaaaaaaaaaaaa")
	# 		# print("ppp66666",self)
	# 		# self[name] = obj(id = self._id+"/"+name, parent = self)
	# 		self[name] = Expando(id = self._id+"/"+name, parent = self)
	# 		return self[name] #?
	# 	if name in self.__dict__:
	# 		pass #print("bbbbbbbbbbbbbbb")
	# 		atr = object.__getattribute__(self, name)

	# 		return atr
	# 	#### return 13
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	# 	pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

	def _setValue(self, val):
		self[Expando._valueArg] = val
		object.__setattr__(self, "value", val)
		# if name == Expando._valueArg:
		# 				self[name] = value
		# 				self[name] = value
		# 			else:
		# 				print("........")
		# 				#final .x =
		# 				self[name] = Expando(id=self._id+"/"+name, val=value, parent=self)
		# 				object.__setattr__(self, name, Expando(
		# 					id=self._id+"/"+name, val=value, parent=self))
		self._updateSubscribers_(val)

	def __xgetstate__(self):
		pass #print ("I'm being pickled")
		pass #print(self.__dict__)
		pass #print()
		return False

	def __xsetstate__(self, d):
		pass #pprint ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		#### self[Expando._valueArg] *= 3
	

	def __xiter__(self):
		for a in self.__dict__:
			print("ITER",a)
			
			def x():
				print("xxxxxxxxxxxx")
			

			# if not a.startswith("_"):# and a not in Expando._hiddenAttr:
			# 	res = self[a]
			# 	if "Expando" in str(type(res)):
			# 		yield res.__iter__()
			# 	yield (a, res)
				
	# def __iter__(self):
	# 	return iter(self.__dict__)
	# 	# print("ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
	# 	# return self.kids()

	def __xstr__(self):
		# print(f"!!!!!!! {self._name}")
		if self[Expando._valueArg] is not None:
			if "formula" in self and True:  # TODO: check valid formula
				# print("iiiiiiiiiiiiiiiiiiiiiiiiiiistr",self._lastLoaded,self._lastUpdated)
				if self._lastLoaded == self._lastUpdated:
					return str(self[Expando._valueArg])
				return str(self._runFormula())
			return str(self[Expando._valueArg])
		# [:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		return "{xobject "+str({str(self._id.replace("/", ".")): str(self[Expando._valueArg])}
						 )[1:-1]+f" ::: children({len(self.children())})"
		# return "{xobject "+str({str(self._name):self[Expando._valueArg][0]})[1:]#[:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		# return str({"_val":self[Expando._valueArg]})
		# return str(self[Expando._valueArg])
		# return str(self.__get__())

	def __xrepr__(self):
		justShow = True
		if justShow:
			self.show(ret=False)
			print()
		# print("where are we ?")
		recursiveDict = False
		if self[Expando._valueArg] is not None:
			# self._setValue([[]])
			if "function" in str(type(self[Expando._valueArg])):
				print("iiiiiiiiiii",self._id)
				return str(self[Expando._valueArg]())
			if "formula" in self and True:  # TODO:`` check valid formula
				# print("iiiiiiiiiiiiiiiiiiiiiiiiiiiRRRRRR")
				if self._lastLoaded == self._lastUpdated:
					return str(self[Expando._valueArg])
				return str(self._runFormula())
		# ret = "{xobject "+str({str(self._name):self[Expando._valueArg][0]})[1:-1]+f" ::: children({len(self.children())})"
		ret = "{xobject "+str({str(self._id.replace("/",".")): str(self[Expando._valueArg])}
							  )[1:-1]+f" ::: children({len(self.children())})"
		childs = []
		if self.children() is not None and len(self.children()) > 0:
			if recursiveDict:  # TODO DICT XXX
				ret += f" ::: {self.children()}"
			else:
				for c in self.children():
					# print("CCCCC",c)
					childs.append(c)
				ret += ":"+str(childs)
		ret += "}"
		return ret

	def __name__(self):
		return str(self.__id.replace("/","."))

	def _getRoot(self):
		return self if self._isRoot else self._parent._getRoot()
	# def _getRoot(self):
	# 	return self if "None" in str(type(self._parent)) else self._parent._getRoot()


	def _GetXO(self, get="", allow_creation=False, getValue=False, follow=None):
		# print("GGGGGGGGGGGGGGGGGetXO", self._id, get, getValue)
		# if "None" not in str(type(self._parent)):
		if not self._isRoot:
			# get = ".".join(self._id.replace("/",".").split(".")[1:] + get.split("."))
			return self._getRoot()._GetXO(get, allow_creation, getValue, follow)
		# print(";;@;;;;;",self._id, get)
		
		final = self
		print("FFFFFFFFFFFFFFF")
		print("FFFFFFFFFFFFFFF")
		print("FFFFFFFFFFFFFFF")
		print(final, final._id)
		for child in get.split("."):
			final = final[child]
		# print(final,final._id)
		print("FFFFFFFFFFFFFFF")
		print("FFFFFFFFFFFFFFF")
		print("FFFFFFFFFFFFFFF")
		return final

	def GetXOx(self, get="", allow_creation=False, getValue=False, follow=None):
		# print("GGGGGGGGGGGGGGGGG", get, getValue)
		if "None" not in str(type(self._parent)):
			get = ".".join(self._id.replace("/",".").split(".")[1:] + get.split("."))
			def root(xobject):
				return xobject if "None" in str(type(xobject._parent)) else root(xobject._parent)

			return root(self)._GetXO(get, allow_creation, getValue, follow)
		# get = ".".join(".".join(self._id.replace("/",".").split(".")[1:] + get.split(".")).split(".")[1:])
		# print("XXXXXXXXXXXXXXXXXXXX",get, self._id, self,)
		if "str" not in str(type(get)):
			print(self._id, "Please provide a string as a key", get)
			return None
		c = 0
		# print(c,c,c,c,c,c,c,c,c,c);c+=1
		sp = get.split(".")
		first = get.split(".")[0]
		if follow is None:
			if len(first) > 0:
				if allow_creation or True:
					# print("FIRST",first)
					return self._GetXO(get=".".join(sp[1:]), allow_creation=allow_creation, follow=xo[first], getValue=getValue)
			return None

		# print(c,c,c,c,c,c,c,c,c,c);c+=1
		if get == "":
			# print(c,c,c,c,c,c,c,c,c,c);c+=10
			if follow is not None and follow[Expando._valueArg] is not None:
				# print(c,c,c,c,c,c,c,c,c,c);c+=100
				if "list" in str(type(follow[Expando._valueArg])):
					if len(follow[Expando._valueArg]) > 0:
						if getValue:
							return follow[Expando._valueArg][0]
						return follow
				if getValue:
					return follow[Expando._valueArg]
				return follow

			# print(c,c,c,c,c,c,c,c,c,c);c+=1000
			return follow
		else:
			if allow_creation or first in follow.children():
				return self._GetXO(get=".".join(sp[1:]), allow_creation=allow_creation, follow=follow[first], getValue=getValue)

		return None

	def _updateSubscribers_(self, *v, **kw):
		# for trigger in self._triggers:
		# 	#TODO: in new thread
		# 	trigger()
		# xo.a.<s>.a = 3
		for sub in self._subscribers:
			#TODO: in new thread
			# print(sub)
			# print("&&&",self[Expando._valueArg], sub)
			# print("***************")
			# print(sub(*v, **kw))
			sub(*v, **kw)
			# sub(*v, **kw)
		# print("................")
		# print(self)
		# print("................")

	# def subscribe(self, func = None, autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	# , autoPub = None, block = False, once= False, echo=True, debug = False, withID = False):
	def subscribe(self, funcOrXo=None):
		print(" ::: Subscribing to",self._name)
		# print("SSSSSSSSSSSSSSS",self, funcOrXo)
		if funcOrXo is None:
			# print("XxxxxxX")
			funcOrXo = lambda a, *aa, **aaa: [a, aa, aaa]
			# withID = True
		# else:
		# print("ffffffffff", funcOrXo)
		if funcOrXo not in self._subscribers and funcOrXo not in self._subscribers:
			self._subscribers.append(funcOrXo)
			# if "function" in str(type(funcOrXo)):
			# 	self._triggers.append(funcOrXo)
			# elif "Expando" in str(type(funcOrXo)):
			# 	self._subscribers.append(funcOrXo)
			# 	pass
		return self
		
	def __delattr__(self, __name: str) -> None:
		return super().__delattr__(__name)

	# lambda x: x@xo
	def __matmul__(self, other):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@     x     @@@@@@@")
		print("@@@@@@@@     x     @@@@@@@")
		print("@@@@@@@@           @@@@@@@",type(other))
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@",other)
		if "value" in self:
			if "function" in str(type(self.value)) or "method" in str(type(self.value)):
				return self.value(*other)
		return self

	def __rmatmul__(self, other):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@           @@@@@@@")
		print("@@@@@@@@           @@@@@@@",type(other))
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@",other)
		self._setValue(other)
		# if "tuple" in str(type(other)):
		# 	res = None
		# 	for func in other:
		# 		res = self.subscribe(func)
		# 	return res
		# return self.subscribe(other)

	# xo.trigger @= lambda Subscribe to changes
	def __imatmul__(self, other):
		if "tuple" in str(type(other)):
			res = None
			for func in other:
				res = self.subscribe(func)
			return res
		return self.subscribe(other)

	# def _lastUpdatedNow(self):
	# 	self._lastUpdated = time.time()
	def _runFormula(self):
		if True or "formula" in self:
			if self._lastUpdated == self._lastLoaded:
				return self[Expando._valueArg]
				# return self.formula.currentValue
			else:
				# formula = self.formula[Expando._valueArg]
				# newValue = formula()
				newValue = self.formula()
				# self.formula.currentValue = newValue
				# self[Expando._valueArg] = newValue
				# self = newValue
				self._lastLoaded = self._lastUpdated
				# print("xxxxxxxx", self, formula, getsource(formula))
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				self._setValue(newValue)
				# print("=========-",newValue)
				
				return newValue
		return None

	# xo.form <<= Formula
	def __ilshift__(self, formula):
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print(formula)
		self.formula = formula
		self._lastLoaded = time.time()
		self._lastUpdated = time.time() # not matching same time on purpose -> will trigger fetch
		# self.currentValue = formula()
		# self[Expando._valueArg] = currentValue
		# print("@@@@@@@@@ expando?",type(self))

		# self._setValue(lambda : self._runFormula())
		# self()
		

		# self[Expando._valueArg] = lambda : self._runFormula()
		# self.formula = lambda : self._parent() 
		# self[Expando._valueArg] = lambda : self._parent() if self._lastUpdated == self._lastLoaded else runFormula(self.formula)
		# setValue(self, currentValue)
		# self = lambda : self[Expando._valueArg] if self._lastUpdated == self._lastLoaded else self._formula()

		
		def setLastUpdated(xobject):
			# print("!!!! UUUUUUUUUUUUUUUU", xobject)
			xobject._lastUpdated = time.time()
			if xobject._subscribers != None and len(xobject._subscribers) > 0:
				xobject()

		keys = getWatchablesForFormula(formula)
		print("keys",keys)
		for key in keys:
			#TODO: remove after xo[longKey] is working
			# check = key 
			# def getLast(xobj, path):
			# 	if "." in path:
			# 		return getLast(xobj[path.split(".")[1]], ".".join(path.split(".")[1:]))
			# 	else:
			# 		return xobj[path]
			# xobject = getLast(xo,key)
			# print("LLLLLLLLLLLLLLL",key)
			
			xobject = self._GetXO(key)
			# print("LLLLLLLL",xobject._id,":::::",xobject)
			
			xobject @= lambda *args,**kw:  setLastUpdated(self),  # self._lastUpdated = time.time()
		self._runFormula()
		return self
		# return self





	# def __is__(self, other):
	# 	return self.__eq__(other)

	# def __and__(self, other):
	# 	return self & other

	# def __or__(self, other):
	# 	return self | other

	# def __contains__(self, key):
	# 	return key in self.__dict__

	def __xor__(self, other):
		return self ^ other

	def __invert__(self, other):
		return ~self[Expando._valueArg]

	def __lshift__(self, other):
		return self << other

	def __rshift__(self, other):
		return self >> other

	def __bool__(self, other):
		return bool(self[Expando._valueArg])

	# def __abs__(self, other):
	# 	return abs(self[Expando._valueArg])

	# def __abs__(self, other):
	# 	return abs(self[Expando._valueArg])


	#### by value of main
	# def __eq__(self, other):
	# 	if type(self[Expando._valueArg]) is not list:
	# 		return None == other
	# 	if "bool" in str(type(other)) and ("bool" in str(type(self[Expando._valueArg])) or (self[Expando._valueArg] is not None and ("dict" in str(type(self[Expando._valueArg][0])) or "dict" in str(type(self[Expando._valueArg][0])) )and len(self[Expando._valueArg]) > 0 and "bool" in str(type(self[Expando._valueArg][0])))):
	# 		return self[Expando._valueArg][0] == other
	# 	if self.__isObj(other):
	# 		return self[Expando._valueArg][0] == other[Expando._valueArg][0]
	# 	elif "str" in str(type(other)):
	# 		return str(self[Expando._valueArg][0]) == other
	# 	return self[Expando._valueArg][0] == other
	# def __cmp__(self):
	# 	print("$$$$$$$$$$$$$$$$$$$$$$")
	# 	return self[Expando._valueArg]
	def __ge__(self, other):
		# TODO: Check if "value" in 
		if type(other) is Expando:
			return self[Expando._valueArg] >= other[Expando._valueArg]
		return self[Expando._valueArg] >= other

	def __gt__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] > other[Expando._valueArg]
		return self[Expando._valueArg] > other

	def __le__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] <= other[Expando._valueArg]
		return self[Expando._valueArg] <= other

	def __lt__(self, other):
		# if self.__isObj(other):
		if type(other) is Expando:
			return self[Expando._valueArg] < other[Expando._valueArg]
		return self[Expando._valueArg] < other


	def __iadd__(self, other):
		self[Expando._valueArg] += other
		return self
		
	def __add__(self, other):
		if self[Expando._valueArg] is None:
			return other
		matchWith = other
		if self.__isObj(other):
			matchWith = other[Expando._valueArg]
			# print("$$$$$$$$$$$$$$$$$$$$$$1")
			# return self[Expando._valueArg] + other[Expando._valueArg]
		# if str(type(other)) != str(type(self[Expando._valueArg][0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self[Expando._valueArg][0])):
		# 		self[Expando._valueArg][0] = [self[Expando._valueArg][0]]
		# 	return self[Expando._valueArg][0] + other
		return type(matchWith)(self[Expando._valueArg]) + matchWith

	def __radd__(self, other):
		if self[Expando._valueArg] is None:
			return other
		matchWith = other
		if self.__isObj(other):
			print("$$$$$$$$$$$$$$$$$$$$$$2")
			matchWith = other[Expando._valueArg]
		# if str(type(other)) != str(type(self[Expando._valueArg][0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self[Expando._valueArg][0])):
		# 		self[Expando._valueArg][0] = [self[Expando._valueArg][0]]
		# 	return other + self[Expando._valueArg][0]
		return matchWith + type(matchWith)(self[Expando._valueArg])

	def __pos__(self, other):
		#### # print("!!!!!!!!!")
		#### # print(type(other))
		#### # print()
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] + other

	def __sub__(self, other):
		#### print("!!!!!!!!!")
		pass  # print(type(other))
		pass  # print()
		if self.__isObj(other):
			return self[Expando._valueArg] - other[Expando._valueArg]
		elif "str" in str(type(other)):
			pass  # print("::::::::::::::xxxx:::::::::")
			return str(self[Expando._valueArg]) - other
		return self[Expando._valueArg] - other

	def __rsub__(self,other):
		pass ## print(type(other))
		pass ## print()
		if self.__isObj(other):
			return other[Expando._valueArg] - self[Expando._valueArg]
		elif "str" in str(type(other)):
			# print("::::::::::::::xxxx:::::::::")
			return other - str(self[Expando._valueArg])
		return other - self[Expando._valueArg]


	def __truediv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] / other
		
	def __rtruediv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other / self[Expando._valueArg]

	def __floordiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] // other
		
	def __rfloordiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other // self[Expando._valueArg]
		
	def __mod__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] % other

	def __rmod__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other % self[Expando._valueArg] 

	def __pow__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] ** other

	def __rpow__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] ** other

	def __mul__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] * other

	def __rmul__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] * other

	def __div__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return self[Expando._valueArg] / other
		
	def __rdiv__(self, other):
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return str(self[Expando._valueArg]) + other
		return other / self[Expando._valueArg]

	def __neg__(self):
		return -self[Expando._valueArg]
		#### print("!!!!!!!!!")
		#### print(type(other))
		#### print()
		if self.__isObj(other):
			return self[Expando._valueArg] + other[Expando._valueArg]
		elif "str" in str(type(other)):
			return self[Expando._valueArg] + other

	def __isObj(self, o):
		#### print("################################################################################################################",str(type(o)))
		#### time.sleep(100)
		pass #print("@@@@@@@@@@@@@@@@@@@@@@asdasdasd")
		return "Expando" in str(type(o))


	def _inThread(self, data):
		target, vars, kwargs = data
		print(" ::: Running Async Thread ::: ",target.__name__,"::: with params:\n :::",vars,str(kwargs).replace("'","").replace("}","").replace(":","=").replace("{",""))
		print()
		return target(*vars,**kwargs)

	def _startThread(self, target, vars, kwargs, ):
		sT = Thread(target = self._inThread, args = [[target, vars, kwargs]])
		sT.start()

	def __call__(self, *args, **kwargs):
		# print(Expando.__call__ in self._behaviors)
		# print("CCCCCCCCCCCCC",self,args,kwargs, self._behaviors)

		if "_skip_overload" not in kwargs or kwargs["_skip_overload"] == False:
			return self._behaviors[Expando.__call__](self, *args, **kwargs) \
				if Expando.__call__ in self._behaviors \
					else self.__call__(_skip_overload = True,*args, **kwargs);

		kwargs.pop("_skip_overload") if "_skip_overload" in kwargs else 0
		# for a in vars:
		# 	print(type(a),"AAAAAAAAAAAAAAA,", a)
		# for a in kwargs:
		# 	print(type(kwargs),type(a),"KKKKKKKKK,", a,"=", kwargs[a])
		# print(type(vars),type(*vars),"xxxxxxxxAAAAAAAAAAAAAAA,", vars)

		if self._id.endswith("learn"):
			newDict = {}
			appendToLearn = []
			for f in args:
				if f is not None and "function" in str(type(f)):
					ap = str(f).split(' ')[1]
					newDict[ap] = f
				elif "list" in str(type(f)):
					for ff in f:
						if ff is not None and "function" in str(type(ff)):
							ap = str(f).split(' ')[1]
							newDict[ap] = ff
				elif "dict" in str(type(f)):
					for fkey in f:
						if f[fkey] is not None:
							newDict[fkey] = f[fkey]
				else:
					appendToLearn.append(f)

			# selff = xo._GetXO(self._id)

			# print( f"Learning new trick {self}{str(self._id+" ").split(" ")[1] } yo")
			owner = "/".join(self._id.split("/")[:-1])+"/"

			for key in newDict:
				# print(owner,",,,",key)
				v = newDict[key]
				if "function" in str(type(v)):
					print(f" ::: Learning new trick {owner.strip('/')}.{key} :D")
				else:  # "function" in str(type(v)):
					# print( f" ::: New Element xo.{self._id.replace('/','.')}.{	key} = {v}")
					print(f" ::: New Element xo.{owner.strip('/')}.{	key} = {v}")
				self._parent[key] = v # type:ignore
				# print("SSSSSSSSSSSS",owner+key)

				# print(xo.GetXO(owner)+key, v,retXO=True)
			for a in appendToLearn:
				if self._parent is not None:
					self._parent.learned += [a]
				else:
					print(" ::: WTF")
					self[Expando._valueArg](ref=True).append(a)
				print(f" ::: New Element xo.{owner.strip('/')}.learned = {a}")

			return self._GetXO(owner)
			# print(vars)
			# print(".....")
			# print(kwargs)
		# print(":::::::::::::::::::::::",)
		# for v in vars:
		# 	print(v)
		retXO = False
		# if "function" in str(type(self[Expando._valueArg])) or "method" in str(type(self[Expando._valueArg])):
		# print()

		if "value" in self and "function" in str(type(self[Expando._valueArg])):
			# print("!!!!!!!!!!#####",str(type(self[Expando._valueArg])))
			return self[Expando._valueArg](*args, **kwargs)
		# print(self[Expando._valueArg]) if Expando._valueArg in self else print()
		if "formula" in self and True:  # TODO: check valid formula
			# print("ccccccccccccccccccccccccall",self._lastLoaded, self._lastUpdated)
			if self._lastLoaded == self._lastUpdated:
				# print("@@@@@@@")
				return self[Expando._valueArg]
			# print("+++++++",self._id)
			return self._runFormula()
		elif "value" in self and self[Expando._valueArg] is not None and len(self[Expando._valueArg]) > 0 and "function" in str(type(self[Expando._valueArg])):
			# print("!!!!!!!!!![0]")
			if "asyn" in kwargs and kwargs["asyn"] == True:
				xkwargs = {}
				for a in kwargs:
					if (a != "asyn" or "asyn" in self._id) and "retxo" not in a.lower():
						xkwargs[a] = kwargs[a]
					elif "retxo" in a.lower():
						retXO = True
				if not retXO:
					return self._startThread(self[Expando._valueArg], args, xkwargs)
				else:
					self._startThread(self[Expando._valueArg], args, xkwargs)
					return self
			if not retXO:
				return self[Expando._valueArg](*args, **kwargs)
			else:
				self[Expando._valueArg](*args, **kwargs)
				return self

		# print(" XXX CCC",self._id, self[Expando._valueArg])
		if not retXO:
			if "value" in self and self[Expando._valueArg] is not None and ("ref" not in kwargs or kwargs["ref"] is not True):
				if "list" in str(type(self[Expando._valueArg])) and len(self[Expando._valueArg]) == 1:
					return self[Expando._valueArg]
			# print(self._id, ":::x:::", args, ":::", kwargs)
			if "value" in self:
				return self[Expando._valueArg]
			# return self[Expando._valueArg][0](*vars, **kwargs)
		elif "value" in self:
			return self[Expando._valueArg] if "value" in self else None
			# self[Expando._valueArg][0](*vars, **kwargs)
			# return self
		# print(":::::::::::::::::::::::", self.keys(), len(self.keys()))
		newData = {}
		# print(";;;;;;;;;;;;;:::", vars)
		for d in args:
			if "dict" in str(type(d)):
				# print(";;;;;;;;;;;;;", d)
				newData = {**d, **newData}
		# newData = {**kwargs, **newData,**self}
		newData = {**kwargs, **newData}
		if (len(self.keys()) == 0):
			ddd = None
			if Expando._valueArg in kwargs:
				ddd = Expando.__init__(self, _id=self._id, _parent = self._parent, **newData)
			else:
				# print(kwargs,args)
				# ddd = Expando.__init__(self,val = self.value if "value" in self else None, 
                #                     id=self._id, parent=self._parent, **newData)
				# print("@@@@@@")
				# print(newData)
				# print("@@@@@@@@")
				# print(".............",self._id, newData["_id"] if "_id" in newData else "")
				ddd = Expando.__init__(self,_id=self._id,_val = self.value if "value" in self else None, 
                                   _parent=self._parent, **newData)
			# ddd =  dict.__init__(self, *vars,**kwargs)
			# print("tttttttx", ddd, type(ddd))
			# self._convertAll()
			return ddd
		# Update new entries
		# TODO: make this work, update

		# print("xxxxxx", args, kwargs)
		# for k in dict(vars[0]):
		# 	print("......",k,vars[0][k])
		# 	self[k] = vars[0][k]
		# print("-------", dict(self), args)
		
		self.update(newData) #working

		#self.__init__(**{**dict(self), **kwargs})
		# for

		return self

		# Add the new attributes to the instance's dictionary.
		for k, v in kwargs:
			self[k] = v

		return self._id
		# return self.update({**dict(self), **kwargs})

	def update(self, entries, *vars, **kwargs):
		newData = {}
		# print(";;;;;;;;;;;;;:::", vars, kwargs)
		for d in vars:
			if "dict" in str(type(d)):
				# print(";;;;;;;;;;;;;", d)
				newData = {**d, **newData}
		newData = {**kwargs, **newData}
		newData = {**newData, **entries}
		# print("@@@@@@@@", newData)
		
		for key in newData:
			# if isinstance(newData[key],dict):
			if "dict" in str(type(newData[key])) or "Expando" in str(type(newData[key])):
				# print("DDDDDDDD",key)
				val = None
				# if 
				if "value" in newData[key]:
					val = newData[key].pop("value")
				#EX3
				self[key] = Expando(_id=self._id+"/"+key, _val=val,
				                    _parent=self, _behaviors=self._behaviors, ** newData[key])
			else:
				# print("DDDDDDDD",key)
				# print("NNNNNNDDDDDDDD",key,type(self))
				val = newData[key]
				# self[key] = val
				# self[key] = Expando(_id=self._id+"/"+key, _val=val, _parent=self)
				if key in self:
					# print("AAAAAAAA")
					if "Expando" in str(type(self[key])):
						self[key].value = val
						# self[key] = val
					else:	
						# print("BBBBBBBB",self[key],val)
						#EX4
						self[key] = Expando(_id=self._id+"/"+key, _val=val, _parent=self, _behaviors=self._behaviors)
						# self[key] = val
					# print("fffffffffaaa")
					# @self[key].setter
					# check hooks updates
				else:
					#EX5
					self[key] = Expando(_id=self._id+"/"+key, _val=val, _parent=self, _behaviors=self._behaviors)
					# print("fffffffff",type(self[key]))
		########## self.update(newData)

	def show(self,t = "    ",count = 0, inLoop = False, ret = False):
		# print("ssssssssssssssss..............",self._id)
		s = ""
		#### print("///////////",self[Expando._valueArg],type(self[Expando._valueArg]))
		p = ""
		val = ""
		if "value" in self:
			# print("1111111")
			if "str" in str(type(self[Expando._valueArg])):
				# print("11111112")
				s = "\'"
			val = str(self[Expando._valueArg])
		# else:
			# print("00000000000000")
			# print("00000000000000",self._id)
			# print("00000000000000")
		finalval = " = " + s+str(val)+s if val is not None or True else ""
		p = self._id.split("/")[-1] +finalval
		tab = ""
		for i in range(count):
			tab+=t

		retList = []
		res = []
		p = tab+p
		if ret:
			# print("22222221")
			retList.append(p)
		else:
			# print("22222222")
			print(p.replace("\t","    "))
		for a in self:
			# print("33333", a, type(self[a]))
			# if "_" not in a:
			print("st2", s)
			if not a.startswith("_"):
				if "Expando" in str(type(self[a])) or "dict" in str(type(self[a])):
					# print("33334",a)
					if ret:
						# print("33335555",a)
						res = self[a].show(count= count+1, ret = ret)
					else:
						# print("3333466666",a)
						self[a].show(count= count+1, ret = ret)
				# else:
					# print("33337",a)
		if count == 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

		if ret:
			# print("444444444")
			if count == 0:
				# print("4444444445")
				return str(retList + res)
			# print("55555555",count)
			return retList +["\n"]+ res
		# print("777777",ret,count,retList,res,)
		# return dict(self)

	def show0(self,t = "    ",count = 0, inLoop = False):
		#### print("ssssssssssssssss..............")
		s = ""
		#### print("///////////",self[Expando._valueArg],type(self[Expando._valueArg]))

		if "str" in str(type(self[Expando._valueArg])):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self[Expando._valueArg])+s
		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p.replace("\t","    "))
		for a in self.__dict__:
			# if "_" not in a:
			if not a.startswith("_"):
				if "Expando" in str(type(self.__dict__[a])):
					self.__dict__[a].show(count= count+1)
		if count == 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

	def showMag(self,t = "    ",count = 0):
		return self.show(t=t,count = count)
		## print("ssssssssssssssss..............")
		s = ""
		## print("///////////",self[Expando._valueArg],type(self[Expando._valueArg]))

		if "str" in str(type(self[Expando._valueArg])):
			s = "\'"


		if "list" in str(type(self[Expando._valueArg][0])):

			fullid = ""
			for i in self._id.split("/")[1:]:
				fullid += i + " "
			fullid = fullid[:-1]
			#p = self._id.split("/")[-1] +" = "+ s+str(len(self[Expando._valueArg][0]))+s + etab + str(self[Expando._valueArg])
			p = fullid +"  = x"+ s+str(len(self[Expando._valueArg][0])) + " times"
			l = len(p)%len(t)
			etab = ""
			for i in range((60 - len(t)*count) - len(p)):
				etab+=" "

			p += etab + "index: " + str(self[Expando._valueArg])+s
		else:
			p = self._id.split("/")[-1] +" = "+ s+str(self[Expando._valueArg])+s

		tab = ""
		for i in range(count):
			tab+=t

		p = tab+p
		print(p)
		for a in self.__dict__:
			if "Expando" in str(type(self.__dict__[a])):
				self.__dict__[a].showMag(count= count+1)


# class Expando(Expando):
# 	"""docstring for obj."""

# 	def __init__(self, val=None, id=None, parent=None):
# 		self.__id = id
# 		# print("........")
# 		super().__init__(val=val, id=id)
# 		# print("........ddd")

# 		self.__id = id
# 		self._parent = parent
# 		# print("!!!!!!!!", self.__id, "PPPPPPP",self._parent)
# 		# print("........xxxxx")

	def Del(self):
		if "_parent" in self.__dict__:
			if self._parent is not None:
				# self._parent.__dict__[self._name] = None
				self._parent.__dict__.pop(self._name)

	def Show(self, inLoop=False):
		pass  # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().show(inLoop=inLoop)

	def ShowMag(self):
		pass  # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS..............")
		super().showMag()

	def whileShow(self):
		while (True):
			self.show(inLoop=True)
			time.sleep(0.2)
			os.system("clear")

	def whileShowMag(self):
		while (True):
			self.showMag(inLoop=True)
			time.sleep(0.2)
			os.system("clear")

	def turnTo5(self):
		pass  # print("5555555555555555")
		self = 5

	# def set(self, value):
	# 	#### id = self._id+"/"+name, val= value
		
	# 	# with data binding
	# 	# manager.save(self._id, value)
	# 	pass

	# def value(self, ref=False):
	# 	if ref:
	# 		return self[Expando._valueArg]
	# 	return self[Expando._valueArg]

	def __init__(self, _val=None, _id=None, _parent=None, _behaviors = {},*vars, **entries):
		# dict.__init__(self,**entries)
		# dict.__init__(self, *vars, **entries) #
		super().__init__(self, *vars, **entries)
		####expando.py
		#### def __init__(self):
		#### es=traceback.extract_stack()
		# super().__init__(id = id, val = val)
		if _id is None:
			_id = Expando._rootName
		# super().__init__(*(None, val))
		# super().__init__(val)
		# super().__init__()
		pass  # print("PPPPPPPPPPPPPP", id)
		#### self.name = self.GetName()

		self._id = _id
		self._name = _id.split("/")[-1]
		# self._birth = datetime.now()

		# self.__id = id
		# # print("........")
		# super().__init__(val=val, id=id)
		# # print("........ddd")

		# self.__id = id
		self._isRoot = False
		if _parent is None:
			self._isRoot = True
		# self._parent:Expando = Expando(**parent)
		self._parent= _parent
		#### self.__validID_ = False
		#### global GD
		#### self.xxx = self.get_my_name()
		#### print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@",mod_retrieve_name(self))
		exist = True
		'''
		birth = str(time.time())
		if id is None:
			id = birth
		'''

		self._subscribers = []
		# self._triggers = []

		#### self.__main__ = main
		# self.__id__ = "hidden"
		# self.__dict__.pop("__id__")
		# self[Expando._valueArg] = val
		if _val is not None:
			# self[Expando._valueArg] = val
			self[Expando._valueArg] = _val
		# self.__dict__["val"] = 3
		# print("obj created! =",self[Expando._valueArg])
		# self._zzz = 5
		self._behaviors = _behaviors
		#### print("******---",self.get_my_name())
		#### self["_id"] = self.get_my_name()[0]
		self.update(entries)

		#### self.xxx.yyy.zzz = 13
		#### updateID = Thread(target = self.makeID, args = [list,])
		#### updateID.start()

		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
		# for arg_name in entries:
		# 	pass  # print("AAAAAAAAAAAAA",arg_name)


# 		# Binding the object to the value
#		# global manager
# 		# self._manager = manager
# 		# self[Expando._valueArg] = manager.bind(self.__id, val, ref=[self])

	def __setattr__(self, name, value, *args, **kwargs):
		# print("sssasasaaaaaaaasaaaaaaaas", self._id, name, value,":::", args,":::", kwargs)
		print(str(type(name)))
		print()
		if "str" not in str(type(name)):
			print("XXSXSXSXSXSXSXSXSX")
			print("XXSXSXSXSXSXSXSXSX")
			print("XXSXSXSXSXSXSXSXSX")
			print("XXSXSXSXSXSXSXSXSX")
			name = str(name)
		print("st3")
		if name not in Expando._hiddenAttr and (not name.startswith("_") or name == Expando._valueArg):
			if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False) and name != "_behaviors":
				# print("EEEEEEEEEEEEEEEEEEEE1", name, value)
				return self._behaviors[Expando.__setattr__](self, name, value, *args, **kwargs) \
					if Expando.__setattr__ in self._behaviors \
						else self.__setattr__(name, value, _skip_overload=True, *args, **kwargs)

		# and "__skip" in self.__dict__ and name not in self.skip:
		if name not in Expando._hiddenAttr and (not name.startswith("_") or name == Expando._valueArg):
			if "Expando" not in str(type(value)):
				# if type(value) is not Expando:
				# print(f"____________{name}_________", str(type(value)))
				if name not in self:
					# print("2222222222")
					# print("ppp33333",self._id)
					# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
					if name == Expando._valueArg:
						self[name] = value
						object.__setattr__(self, name, value)
						self[name] = value
					else:
						# print("........")
						#EX6
						#final .x =
						res = Expando(_id=self._id+"/"+name, _val=value, _parent=self, _behaviors=self._behaviors)
						self[name] = res
						object.__setattr__(self, name, res)
				else:
					# print("33333333")
					#### self.__set__(name,value)
					#### self.save(id = self._id+"/"+name, val= value)
					# if data binding
					# manager.save(channel = self._id+"/"+name, data=value)
					# self[name]._value = value  # ?????
					self[name][Expando._valueArg] = value  # ?????
					# self[name+"2"]._val = value  # ?????
				self[name]._updateSubscribers_(value)
			else:
				# print("44444")
				self[name] = value
				# print("44444")
				# self[name]._updateSubscribers_(value)


		else:
			# print("555555555", name)
			# self.__dict__[name] = value
			# self[name] = value
			object.__setattr__(self, name, value)
		# time.sleep(.1)

	def __getattr__(self, name, loop=True, *args, **kwargs):

		if "str" not in str(type(name)):
			name = str(name)
		#### return name
		if name == "value":
			# self[name] = Expando(id=self._id+"/"+name, parent=self)
			return self[name]

		# print(" ", name, name in self, ":::::::",
			#   dict(self), ":::::::", self.__dict__)
 
		# print(name in self.__dict__, name in self)
		# if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
		if not name.startswith("_") and name not in dict(self) and name not in Expando._hiddenAttr:
			pass  # print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			# print("aaaaaaaaaaaaaa", name, dict(self))
			# print("ppp66666",self)
			# self[name] = obj(id = self._id+"/"+name, parent = self)
			#EX7
			self[name] = Expando(_id=self._id+"/"+name, _parent=self, _behaviors=self._behaviors)
			return self[name]
		if name in self:
			# atr = object.__getattribute__(self, name)
			atr = self[name]

			# print("bbbbbbbbbbbbbbb", name, atr, type(atr))

			return atr
		# print("!!!!!!!!!!!!!!!", name)
		return self[name]


	# def __repr__(self) -> str:
	# 	return super().__repr__()
	def __repr__(self, *args, **kwargs):
		# if (not name.startswith("_") or name == Expando._valueArg) and name not in Expando._hiddenAttr:
		if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False):
			# print("YYYYYYYYYYYYYYYYYYYYYYYYYESS GETTTTTTTTT repr")
			return str(self._behaviors[Expando.__repr__](self, *args, **kwargs)) \
				if Expando.__repr__ in self._behaviors \
					else self.__repr__(_skip_overload=True, *args, **kwargs)
		# TODO and no other attributes
		# print("!!!!!!!!!!!!!!!", )
		if Expando._valueArg in self and len(self) == 1:
			return self[Expando._valueArg].__repr__()
		return str(dict(self))
		# return str(self.show())
		# return super().__repr__()

	def __str__(self, *args, **kwargs):
		# print("!!!!!!!!!!!!!!!2",)
		if ("_skip_overload" not in kwargs or kwargs["_skip_overload"] == False):
			# print("YYYYYYYYYYYYYYYYYYYYYYYYYESS GETTTTTTTTT str", args, kwargs)
			return str(self._behaviors[Expando.__str__](self, *args, **kwargs)) \
				if Expando.__str__ in self._behaviors \
					else self.__str__(_skip_overload=True, *args, **kwargs)

		if Expando._valueArg in self and len(self) == 1:
			return self[Expando._valueArg].__str__()
		return str(dict(self))
		return super().__repr__()

	def default(self, o):
		return dict(o)


	@property
	def __json__(self):
		return dict(self)

	def toJSON(self): # NOT READY
		print("####################")
		print("####################")
		print("####################")
		print("####################")
		print("####################", dict(self))
		print("####################")
		# print(dict(self))
		jsonD = {k:v for (k,v) in dict(self).items() if "function" not in str(type(v)) if "method" not in str(type(v))}
		print("####################", jsonD)
		print("####################")
		# print(jsonD)
		# return json.dumps(jsonD, default=self.default, indent=4)
		return json.dumps(jsonD, indent=4)
		# return json.dumps(self, default=lambda *a,**kv: dict(self))
		# print(json.dumps(self, indent=4, default=lambda x: x.__json__))
		print(json.dumps(self.__dict__))



# xo = Expando()

# 	def __setattr__(self, name, value):
# 		pass  # print("EEEEEEEEEEEEEEEEEEEE000")
# 		return super().__setattr__(name=name, value=value)

# 	def __getitem__(self, name):
# 		return super().__getitem__(name=name)

# 	def __setitem__(self, name, value):
# 		return super().__setitem__(name=name, value=value)

# 	def __getattribute__(self, name, loop=True):
# 		return super().__getattribute__(name=name, loop=loop)

# 	def __getattr__(self, name, loop=True):
# 		return super().__getattr__(name=name, loop=loop)

# input = "some sentence xo.url.address "
# regex to get url from input

if __name__ == "__xmain__":
	# 	print("ssssssssssssssss..............")
	# 	s = child(val= "ssssssssssssssss", id= "ssssssssssssssss")
	# 	s.show()
	# 	s.showMag()

	
	xo.foo = lambda x: print(f"!!!!!!!{x}")
	xo.foo(5)
	print(type(xo.a))

	xo.a = 3
	xo.ff = lambda x: print(x.a,f"!!!!!!!{x}")
	ff = xo.ff[Expando._valueArg]
	# inspect.getsource(ff)
	getsource(ff)
	for c in ff.__code__.__dir__():
		print(c,":::",ff.__code__.__getattribute__(c))

	prefix = "xo"
	getsource(ff)


	for name in ff.__code__.co_names:
		print("name",name)
		if prefix+"."+name in getsource(ff):
			print("found", prefix+"."+name)
			print(prefix,"[",name,"]", "::::::", xo[name])

		# import importlib
		# importlib.reload(module)	


# xo
# xo.a = Expando(val = 3)
# xo.a @= lambda x: print(x)
# xo.a = 4

# xo.a = Expando(val = 3)
# xo.a @= xo.b
# xo.a = 4
	
	# xo.name.first = "tami"
	# xo.name.last = "bar"
	# xo.fullname <<= lambda: xo.name.first() + ", " + xo.name.last()
	
	# # xo.fullname >>= lambda: xo.name.first() + ", " + xo.name.last()

	# xo.show()
	# print("__________________", xo.fullname._lastUpdated)
	# xo.name.first = "po"
	# print("__________________", xo.fullname._lastUpdated)
	# xo.fullname()
	# xo.fullname.show()
	# print("_______________")
	# xo





# (Warm) Reload a module
# import importlib
# importlib.reload(module)

# from dill.source import getsource
# inspect.getsource(function)


#xo.f = lambda : xo.self.name.first[Expando._valueArg] + "," + xo.self.name.last[Expando._valueArg]
#