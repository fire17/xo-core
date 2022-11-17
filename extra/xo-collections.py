#xo-tupple.py
import collections
from collections import defaultdict
from typing import overload
import  time


# class xodefault(collections.defaultdict):


# class xxo('defaultdict[collections._KT, collections._VT]'):
class xxo(dict):
	_hiddenAttr = ["_val", "getattr", "show", "_id", "__dict__"]
	_rootName = "xo"
	_valueArg = "value"
	# value = None
	# , wrapper = False, main = True):
	def __init__(self, val=None, id=None, main=True, parent=None, **entries):
		####expando.py
		#### def __init__(self):
		#### es=traceback.extract_stack()
		# super().__init__(id = id, val = val)
		if id is None:
			id = xxo._rootName
		# super().__init__(*(None, val))
		# super().__init__(val)
		# super().__init__()
		pass  # print("PPPPPPPPPPPPPP", id)
		#### self.name = self.GetName()

		self.update(entries)
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
		# self.__id__ = "hidden"
		# self.__dict__.pop("__id__")
		# self._val = val
		if val is not None:
			# self._value = val
			self[xxo._valueArg] = val
		# self.__dict__["val"] = 3
		# print("obj created! =",self._val)
		self._zzz = 5
		#### print("******---",self.get_my_name())
		#### self["_id"] = self.get_my_name()[0]

		#### self.xxx.yyy.zzz = 13
		#### updateID = Thread(target = self.makeID, args = [list,])
		#### updateID.start()

		# print("AAAAAAAAAAA	AAA",entries,self.__name__)
		for arg_name in entries:
			pass  # print("AAAAAAAAAAAAA",arg_name)


# 		# Binding the object to the value
#		# global manager
# 		# self._manager = manager
# 		# self._val = manager.bind(self.__id, val, ref=[self])

	def __getattribute__(self, name, loop=True):
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

	def __setattr__(self, name, value):
		# print("EEEEEEEEEEEEEEEEEEEE1",self.__dict__)
		if "str" not in str(type(name)):
			name = str(name)
		# and "__skip" in self.__dict__ and name not in self.skip:
		if (not name.startswith("_") or name == xxo._valueArg) and name not in xxo._hiddenAttr:
			if "xxo" not in str(type(value)):
			# if type(value) is not xxo:
				print(f"____________{name}_________",str(type(value)))
				if name not in self:
					print("2222222222")
					# print("ppp33333",self._id)
					# self[name] = obj(id = self._id+"/"+name, val= value, parent = __objManager.getXO(self._id))
					if name == xxo._valueArg:
						self[name] = value
						object.__setattr__(self,name,value)
						self[name] = value
					else:
						print("........")
						#final .x = 
						res = xxo(id=self._id+"/"+name, val=value, parent=self)
						self[name] = res
						object.__setattr__(self, name, res)
				else:
					print("33333333")
					#### self.__set__(name,value)
					#### self.save(id = self._id+"/"+name, val= value)
					# if data binding
					# manager.save(channel = self._id+"/"+name, data=value)
					# self[name]._value = value  # ?????
					self[name][xxo._valueArg] = value  # ?????
					# self[name+"2"]._val = value  # ?????
					# self[name]._updateSubscribers_(value)
			else:
				print("44444")
				self[name] = value
				print("44444")

		else:
			print("555555555",name)
			# self.__dict__[name] = value
			# self[name] = value
			object.__setattr__(self, name,value)
		# time.sleep(.1)

	def __getattr__(self, name, loop=True):
		# print("getttt")	
		if "str" not in str(type(name)):
			name = str(name)
		#### return name
		if name == "value":
			# self[name] = xxo(id=self._id+"/"+name, parent=self)
			return self[name]

		# print(" ", name, name in self, ":::::::", dict(self), ":::::::" , self.__dict__)

		print(name in self.__dict__, name in self)
		# if not name.startswith("_") and "_val" in self.__dict__ and name not in xxo._hiddenAttr and name not in self.__dict__:
		if not name.startswith("_") and name not in dict(self) and name not in xxo._hiddenAttr:
			pass #print("OOOOO_ooooooooooooooooooooo",name)####,self.__dict__)
			print("aaaaaaaaaaaaaa",name,dict(self))
			# print("ppp66666",self)
			# self[name] = obj(id = self._id+"/"+name, parent = self)
			self[name] = xxo(id=self._id+"/"+name, parent=self)
			return self[name]
		if name in self:
			# atr = object.__getattribute__(self, name)
			atr = self[name]
			
			print("bbbbbbbbbbbbbbb",name,atr, type(atr))

			return atr
		print("!!!!!!!!!!!!!!!",name)
		return self[name]
	
x = xxo()
# x.a.b.c = 3
x.a = "aaaa"
x.a = 1
x.__dict__
print(dict(x))
# print(x.a)
print("@@@@@@@@@@@@@@@@@@@@")
print()
print()
print("@@@@@@@@@@@@@@@@@@@@")
x.a.b = 5
x.a.b = 7
x.a.b = 1000
# x.a = "aaaccccc"
# print(x)
# print(dict(x))
print("@@@@@@@@@@@@@@@@@@@@",x.a.b,x)


exit(0)
def fxo(arg):
	return defaultdict(lambda: fxo(arg))
	result = arg.upper()
	return result


def_dict = defaultdict(lambda: fxo('default value'))
print(dict(def_dict))
def_dict["a"]["b"]["c"] = 3


print((d))

# class Ext(defaultdict):
#     def __init__(self, *args, **kwarg):
#         super(Ext, self).__init__(*args, **kwarg)


# ext = Ext(Ext)
# ext.m
# print(ext)
# ext.a = 3
# # ext.b = 3
# ext.b.c = 3
