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
# 		self._val = val
# 		#### self.arg = arg

# 	def __setattr__(self, name, value):
# 		pass #printx("EEEEEEEEEEEEEEEEEEEE---1")


# 	def __assign__(self, v):
# 		pass #print('called with %s' % v)



# TODO: improve
# def getWatchablesForFormulaMock(func):
# 	return ["name.first","name.last"]
def getWatchablesForFormula(func):
	return getAllObjects(getsource(dill.detect.code(func)))
	reg = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
	return re.search(reg, getsource(func)).groups()


def getAllObjects(given):
    given = given.split('<<=')[-1]
    regex = re.compile(r'(?P<xo>xo(\.\w+)*)')
    # regex = re.compile(r'(?P<name>xo.name\.[a-zA-Z]+)')
    # regex = re.compile(r'\\w+(?:\\.\\w+)+')

    def removeHiddenAtEnd(s):
        end = s.split('.')[-1]
        if not end.startswith('_'):
            return s
        else:
            return removeHiddenAtEnd('.'.join(s.split('.')[:-1]))

    return [removeHiddenAtEnd(x[0].lstrip("xo.")) for x in re.findall(regex, given)]




class Expando(object):
	"""docstring for Expando."""
	_hiddenAttr = ["value", "_val", "getattr", "show", "_id", "__dict__"]
	_rootName = "xo"

	__id = "xxx"

	

	
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
#### 		self._val = val
#### 		print("obj created! =",self._val)
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
		for a in self.__dict__:
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

	def kids(self):

				for a in self.__dict__:
					if not a.startswith("_") and a not in Expando._hiddenAttr:
						yield self[a]



	def children(self):
		# childs = []
		childs = {}
		for a in self.__dict__:
			if not a.startswith("_") and a not in Expando._hiddenAttr:
				# childs.append(self[a])
				childs[a]=self[a]
		return childs

	def reloadImport(self, module):
		return importlib.reload(module)
		
	def __init__(self, val = None, id = None, main = True, parent = None, **entries):####, wrapper = False, main = True):
	####expando.py
		#### def __init__(self):
		#### es=traceback.extract_stack()
		# super().__init__(id = id, val = val)
		super().__init__()
		pass #print("PPPPPPPPPPPPPP", id)
		#### self.name = self.GetName()

		self.__dict__.update(entries)
		if id is None:
			id = Expando._rootName
		self._name = id.split("/")[-1]
		self._id = id
		# self._birth = datetime.now()

		# self.__id = id
		# # print("........")
		# super().__init__(val=val, id=id)
		# # print("........ddd")

		# self.__id = id
		self._isRoot = False
		if parent is None:
			self._isRoot = True
		self._parent = parent
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
		self.__id__ = "hidden"
		self.__dict__.pop("__id__")
		self._val = val
		# print("obj created! =",self._val)
		self._zzz = 5
		#### print("******---",self.get_my_name())
		#### self["_id"] = self.get_my_name()[0]

		#### self.xxx.yyy.zzz = 13
		#### updateID = Thread(target = self.makeID, args = [list,])
		#### updateID.start()

		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
		for arg_name in entries:
			pass #print("AAAAAAAAAAAAA",arg_name)


# 		# Binding the object to the value
#		# global manager
# 		# self._manager = manager
# 		# self._val = manager.bind(self.__id, val, ref=[self])
	


	def __hash__(self):
		pass #print(hash(str(self)))
		return hash(str(self))

	def getID(self):
		return self.__id__


	def __set__(self, key, val):
		pass
		# print("eeeeeeeeeeeeeeeeeeeee")
		self.__dict__[key] = val
		return True

	def __get__(self,key):
		pass
		# print("eeeeeeeeeeeeeeeeeeeeeaaa")
		return self.__dict__[key]


	def __setattr__(self, name, value):
		pass ## print("EEEEEEEEEEEEEEEEEEEE1")
		if "str" not in str(type(name)):
			name = str(name)
		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr:#### and "__skip" in self.__dict__ and name not in self.skip:
			if "Expando" not in str(type(value)):
				pass ## print("_____________________",str(type(value)))
				if name not in self.__dict__:
					pass ## print("2222222222")
					# print("ppp33333",self._id)
					# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
					self[name] = Expando(id = self._id+"/"+name, val= value, parent = self)
				else:
					pass ## print("33333333")
					#### self.__set__(name,value)
					#### self.save(id = self._id+"/"+name, val= value)
					# if data binding
					# manager.save(channel = self._id+"/"+name, data=value)
					self[name]._val = value #?????
					self[name]._updateSubscribers_(value)
			else:
				pass ## print("44444")
				self.__dict__[name] = value

		else:
			pass ## print("555555555")
			self.__dict__[name] = value

	def __getitem__(self, name):
		if "str" not in str(type(name)):
			name = str(name)
		elif name == "value":
			# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
			# name = "_val"
			atr = object.__getattribute__(self, name)
			# return atr[0]
			return atr

		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
			# print("ppp44444")
			self.__dict__[name] = Expando(id = self._id+"/"+name, parent = self)

		if name in self.__dict__:
			#### print("FUUCKKKKKKKKKKKKKKKKKKKKKk")

			item = self.__dict__[name]
			return item

			atr = object.__getattribute__(self, name)
			return atr




	def __assign__(self, v):
		pass #print('called with %s' % v)

	def __setitem__(self, name, value):
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
					self.__dict__[name] = Expando(id = self._id+"/"+name, val = value, parent = self)
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

	def __getattribute__(self, name, loop = True):
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
	def __getattr__(self, name, loop = True):
		pass #print("getttt")
		if "str" not in str(type(name)):
			name = str(name)
		#### return name
		if not name.startswith("_") and "_val" in self.__dict__ and name not in Expando._hiddenAttr and name not in self.__dict__:
			pass #print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			pass #print("aaaaaaaaaaaaaa")
			# print("ppp66666",self)
			# self[name] = obj(id = self._id+"/"+name, parent = self)
			self[name] = Expando(id = self._id+"/"+name, parent = self)
		if name in self.__dict__:
			pass #print("bbbbbbbbbbbbbbb")
			atr = object.__getattribute__(self, name)

			return atr
		#### return 13
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		pass #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$xxxxxxxxxxxx")

	def _setValue(self, val):
		self._val = val
		self._updateSubscribers_(val)

	def __getstate__(self):
		pass #print ("I'm being pickled")
		pass #print(self.__dict__)
		pass #print()
		return False

	def __setstate__(self, d):
		pass #pprint ("I'm being unpickled with these values:", d)
		self.__dict__ = d
		#### self._val *= 3

	def __iter__(self):
		# print("ITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
		return self.kids()

	def __str__(self):
		# print(f"!!!!!!! {self._name}")
		if self._val is not None:
			if "formula" in self and True:  # TODO: check valid formula
				print("iiiiiiiiiiiiiiiiiiiiiiiiiiistr",self._lastLoaded,self._lastUpdated)
				if self._lastLoaded == self._lastUpdated:
					return str(self._val)
				return str(self._runFormula())
			return str(self._val)
		# [:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		return "{xobject "+str({str(self._id.replace("/", ".")): str(self._val)}
                         )[1:-1]+f" ::: children({len(self.children())})"
		# return "{xobject "+str({str(self._name):self._val[0]})[1:]#[:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		# return str({"_val":self._val})
		# return str(self._val)
		# return str(self.__get__())

	def __repr__(self):
		justShow = True
		if justShow:
			self.show(ret=False)
			print()
		# print("where are we ?")
		recursiveDict = False
		if self._val is not None:
			# self._setValue([[]])
			if "function" in str(type(self._val)):
				return str(self._val())
			if "formula" in self and True:  # TODO:`` check valid formula
				print("iiiiiiiiiiiiiiiiiiiiiiiiiiiRRRRRR")
				if self._lastLoaded == self._lastUpdated:
					return str(self._val)
				return str(self._runFormula())
		# ret = "{xobject "+str({str(self._name):self._val[0]})[1:-1]+f" ::: children({len(self.children())})"
		ret = "{xobject "+str({str(self._id.replace("/",".")): str(self._val)}
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
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		# print(final, final._id)
		for child in get.split("."):
			final = final[child]
		# print(final,final._id)
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
		# print("FFFFFFFFFFFFFFF")
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
			if follow is not None and follow._val is not None:
				# print(c,c,c,c,c,c,c,c,c,c);c+=100
				if "list" in str(type(follow._val)):
					if len(follow._val) > 0:
						if getValue:
							return follow._val[0]
						return follow
				if getValue:
					return follow._val
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
			# print("&&&",self._val, sub)
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
		


	# xo.trigger @= lambda Subscibe to changes
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
				return self._val
				# return self.formula.currentValue
			else:
				# formula = self.formula._val
				# newValue = formula()
				newValue = self.formula()
				# self.formula.currentValue = newValue
				# self._val = newValue
				# self = newValue
				self._lastLoaded = self._lastUpdated
				# print("xxxxxxxx", self, formula, getsource(formula))
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				# print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
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
		# self._val = currentValue
		# print("@@@@@@@@@ expando?",type(self))

		# self._setValue(lambda : self._runFormula())
		# self()
		

		# self._val = lambda : self._runFormula()
		# self.formula = lambda : self._parent() 
		# self._val = lambda : self._parent() if self._lastUpdated == self._lastLoaded else runFormula(self.formula)
		# setValue(self, currentValue)
		# self = lambda : self._val if self._lastUpdated == self._lastLoaded else self._formula()

		
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





	def __is__(self, other):
		return self.__eq__(other)

	def __and__(self, other):
		return self & other

	def __or__(self, other):
		return self | other

	def __contains__(self, key):
		return key in self.__dict__

	def __xor__(self, other):
		return self ^ other

	def __invert__(self, other):
		return ~self._val

	def __lshift__(self, other):
		return self << other

	def __rshift__(self, other):
		return self >> other

	def __bool__(self, other):
		return bool(self._val)

	def __abs__(self, other):
		return abs(self._val)

	def __abs__(self, other):
		return abs(self._val)

	#### by value of main
	def __eq__(self, other):
		if type(self._val) is not list:
			return None == other
		if "bool" in str(type(other)) and ("bool" in str(type(self._val)) or (self._val is not None and ("dict" in str(type(self._val[0])) or "dict" in str(type(self._val[0])) )and len(self._val) > 0 and "bool" in str(type(self._val[0])))):
			return self._val[0] == other
		if self.__isObj(other):
			return self._val[0] == other._val[0]
		elif "str" in str(type(other)):
			return str(self._val[0]) == other
		return self._val[0] == other

	def __ge__(self, other):
		if self.__isObj(other):
			return self._val[0] >= other._val[0]
		return self._val[0] >= other

	def __gt__(self, other):
		if self.__isObj(other):
			return self._val[0] > other._val[0]
		return self._val[0] > other

	def __le__(self, other):
		if self.__isObj(other):
			return self._val[0] <= other._val[0]
		return self._val[0] <= other

	def __lt__(self, other):
		if self.__isObj(other):
			return self._val[0] < other._val[0]
		return self._val[0] < other


	def __iadd__(self, other):
		self._val += other
		return self
		
	def __add__(self, other):
		if self._val is None:
			return other
		matchWith = other
		if self.__isObj(other):
			matchWith = other._val
			# print("$$$$$$$$$$$$$$$$$$$$$$1")
			# return self._val + other._val
		# if str(type(other)) != str(type(self._val[0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self._val[0])):
		# 		self._val[0] = [self._val[0]]
		# 	return self._val[0] + other
		return type(matchWith)(self._val) + matchWith

	def __radd__(self, other):
		if self._val is None:
			return other
		matchWith = other
		if self.__isObj(other):
			print("$$$$$$$$$$$$$$$$$$$$$$2")
			matchWith = other._val
		# if str(type(other)) != str(type(self._val[0])):
		# 	if "list" not in str(type(other)):
		# 		other = [other]
		# 	if "list" not in str(type(self._val[0])):
		# 		self._val[0] = [self._val[0]]
		# 	return other + self._val[0]
		return matchWith + type(matchWith)(self._val)

	def __pos__(self, other):
		#### # print("!!!!!!!!!")
		#### # print(type(other))
		#### # print()
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val + other

	def __sub__(self, other):
		#### print("!!!!!!!!!")
		pass  # print(type(other))
		pass  # print()
		if self.__isObj(other):
			return self._val[0] - other._val[0]
		elif "str" in str(type(other)):
			pass  # print("::::::::::::::xxxx:::::::::")
			return str(self._val[0]) - other
		return self._val[0] - other

	def __rsub__(self,other):
		pass ## print(type(other))
		pass ## print()
		if self.__isObj(other):
			return other._val[0] - self._val[0]
		elif "str" in str(type(other)):
			# print("::::::::::::::xxxx:::::::::")
			return other - str(self._val[0])
		return other - self._val[0]


	def __truediv__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val / other
		
	def __rtruediv__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return other / self._val

	def __floordiv__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val // other
		
	def __rfloordiv__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return other // self._val
		
	def __mod__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val % other

	def __rmod__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return other % self._val 

	def __pow__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val ** other

	def __rpow__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val ** other

	def __mul__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val * other

	def __rmul__(self, other):
		return self.__mul__(other)
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val * other

	def __div__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return self._val / other
		
	def __rdiv__(self, other):
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return str(self._val) + other
		return other / self._val

	def __neg__(self):
		return -self._val
		#### print("!!!!!!!!!")
		#### print(type(other))
		#### print()
		if self.__isObj(other):
			return self._val + other._val
		elif "str" in str(type(other)):
			return self._val + other

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

	def __call__(self, *vars, **kwargs):

		# for a in vars:
		# 	print(type(a),"AAAAAAAAAAAAAAA,", a)
		# for a in kwargs:
		# 	print(type(kwargs),type(a),"KKKKKKKKK,", a,"=", kwargs[a])
		# print(type(vars),type(*vars),"xxxxxxxxAAAAAAAAAAAAAAA,", vars)

		if self._id.endswith("learn"):
			newDict = {}
			appendToLearn = []
			for f in vars:
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
					print( f" ::: Learning new trick {owner.strip('/')}.{key} :D")
				else: #"function" in str(type(v)):
					# print( f" ::: New Element xo.{self._id.replace('/','.')}.{	key} = {v}")
					print( f" ::: New Element xo.{owner.strip('/')}.{	key} = {v}")
				self._parent[key] = v
				# print("SSSSSSSSSSSS",owner+key)

				# print(xo.GetXO(owner)+key, v,retXO=True)
			for a in appendToLearn:
				if self._parent is not None:
					self._parent.learned+=[a]
				else:
					print(" ::: WTF")
					self.value(ref=True).append(a)
				print( f" ::: New Element xo.{owner.strip('/')}.learned = {a}")

			return self._GetXO(owner)
			# print(vars)
			# print(".....")
			# print(kwargs)
		# print(":::::::::::::::::::::::",)
		# for v in vars:
		# 	print(v)
		retXO = False
		# if "function" in str(type(self._val)) or "method" in str(type(self._val)):
		if "function" in str(type(self._val)):
			# print("!!!!!!!!!!#####",str(type(self._val)))
			return self._val(*vars, **kwargs )
		if "formula" in self and True:  # TODO: check valid formula
			# print("ccccccccccccccccccccccccall",self._lastLoaded, self._lastUpdated)
			if self._lastLoaded == self._lastUpdated:
				# print("@@@@@@@")
				return self._val
			# print("+++++++",self._id)
			return self._runFormula()
		elif self._val is not None and len(self._val)>0 and "function" in str(type(self._val[0])):
			# print("!!!!!!!!!![0]")
			if "asyn" in kwargs and kwargs["asyn"] == True:
				xkwargs = {}
				for a in kwargs:
					if (a != "asyn" or "asyn" in self._id) and "retxo" not in a.lower():
						xkwargs[a] = kwargs[a]
					elif "retxo" in a.lower():
						retXO = True
				if not retXO:
					return self._startThread(self._val[0], vars, xkwargs)
				else:
					self._startThread(self._val[0], vars, xkwargs)
					return self
			if not retXO:
				return self._val[0](*vars, **kwargs)
			else:
				self._val[0](*vars, **kwargs)
				return self


		# print(" XXX CCC",self._id, self._val)
		if not retXO:
			if self._val is not None and ("ref" not in kwargs or kwargs["ref"] is not True):
				if "list" in str(type(self._val)) and len(self._val) == 1:
					return self._val[0]
			return self._val
			# return self._val[0](*vars, **kwargs)
		else:
			return self._val
			# self._val[0](*vars, **kwargs)
			# return self
		# print(":::::::::::::::::::::::")



	def show(self,t = "    ",count = 0, inLoop = False, ret = False):
		#### print("ssssssssssssssss..............")
		s = ""
		#### print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s
		tab = ""
		for i in range(count):
			tab+=t

		retList = []
		res = []
		p = tab+p
		if ret:
			retList.append(p)
		else:
			print(p.replace("\t","    "))
		for a in self.__dict__:
			# if "_" not in a:
			if not a.startswith("_"):
				if "Expando" in str(type(self.__dict__[a])):
					if ret:
						res = self.__dict__[a].show(count= count+1, ret = ret)
					else:
						self.__dict__[a].show(count= count+1, ret = ret)
		if count == 0 and inLoop:
			print("\n\nPress Ctrl+C to stop whileShow()\n")

		if ret:
			if count == 0:
				return str(retList + res)
			return retList +["\n"]+ res

	def show0(self,t = "    ",count = 0, inLoop = False):
		#### print("ssssssssssssssss..............")
		s = ""
		#### print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"
		p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s
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
		## print("///////////",self._val,type(self._val))

		if "str" in str(type(self._val)):
			s = "\'"


		if "list" in str(type(self._val[0])):

			fullid = ""
			for i in self._id.split("/")[1:]:
				fullid += i + " "
			fullid = fullid[:-1]
			#p = self._id.split("/")[-1] +" = "+ s+str(len(self._val[0]))+s + etab + str(self._val)
			p = fullid +"  = x"+ s+str(len(self._val[0])) + " times"
			l = len(p)%len(t)
			etab = ""
			for i in range((60 - len(t)*count) - len(p)):
				etab+=" "

			p += etab + "index: " + str(self._val)+s
		else:
			p = self._id.split("/")[-1] +" = "+ s+str(self._val)+s

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

	def value(self, ref=False):
		if ref:
			return self._val
		return self._val[0]


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
	ff = xo.ff._val
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


#xo.f = lambda : xo.self.name.first._val + "," + xo.self.name.last._val
#