from argparse import Namespace
from dataclasses import dataclass, field, asdict
from xo.expando import Expando
from xo.zmq import xoServer
class xodal(Expando):
	index = {}
	_auth = None

	def __init__(self, func=None, *args, **kwargs):
		# print("########", func, args, kwargs)
		super().__init__(*args, **kwargs)
		self._func = func
		if func is not None:
			# print(self._id, "!!!!!!!", func.__name__, type(func))
			xodal.index[self._id+"/"+func.__name__] = func

	
	@staticmethod
	def _checkAuth(payload):
		return True
		
	# Override the call method
	def __call__(self, *args, **kwargs):
		print("CALLING", self._id, args, kwargs)
		# if "args" not in kwargs:
		# 	print("args",type(args))
		# 	if isinstance(args,tuple):
		# 		kwargs["args"] = list(args)
				
		if "value" not in kwargs and self.value is not None:
			kwargs["value"] = self.value
		if "id" not in kwargs:
			kwargs["id"] = self._id
			
		
		return self.CallFunc(
			payload = {
						"pointer":self._id,
						"kwargs": kwargs,
						"args": list(args),
						"auth": self._auth
					})

	def DefaultFunc(self, payload):
		''' OVERLOAD THIS FUNCTION TO CHANGE DEFAULT BEHAVIOR '''
		print("DEFAULT", self._id, payload)
		return "NICE"

	def CallFunc(self, payload):
		# print("GGGGGGGGGGGGGGGGGetXO", self._id, get, getValue)
		# if "None" not in str(type(self._parent)):
		if not self._isRoot:
			# get = ".".join(self._id.replace("/",".").split(".")[1:] + get.split("."))
			return self._getRoot().CallFunc(payload)

		final = self
		if not isinstance(payload, dict) or not xodal._checkAuth(payload):
			return False
		
		# data should be kwargs {}
		data = payload["kwargs"] if "kwargs" in payload else None
		args = payload["args"] if "args" in payload else None
		auth = payload["auth"] if "auth" in payload else None
		pointer = payload["pointer"] if "pointer" in payload else None
		if pointer is not None and pointer in xodal.index:
			print(" CALLING EXISTING FUNC IN INDEX",
			      pointer, ":::", type(xodal.index[pointer]), ":", xodal.index[pointer])
			return xodal.index[pointer](*args, **data)
		else:
			print(" RUNNING DEFAULT FUNCTION ",self._id, payload)
			return self.DefaultFunc(payload)

	

	# def default(self, o):
	# 	return super().default(o)


	
class MicroXO(xodal):

	def __init__(self, funcOrNamespace=None, port=None, *args, **kwargs):
		# print("########", func, args, kwargs)
		func = None
		namespace = None
		if isinstance(funcOrNamespace,str):
			namespace = funcOrNamespace
		else:
			func = funcOrNamespace
			# get namespace from running filename

		super().__init__(func=func, _id = namespace, *args, **kwargs)

		if namespace is not None:
			if port is None:
				#Get port
				port = 1990
			# self._reqServer = xoServer(port = int(str(port)+"1")) 
			self._reqServer = xoServer(port = port) 
			

	@staticmethod
	def register(Namespace, port):
		return MicroXO(funcOrNamespace=Namespace, port = port)

	@staticmethod
	def getNamespace():
		return "microxo"

	@staticmethod
	def getPorts():
		return {""}
		
	_services = {"microxo": 1993,} # OVERLOAD THIS
	# _current_namespace = MicroXO.getNamespace()
	# _servers = getPorts()

	def DefaultFunc(self, payload):
		id = payload["kwargs"]["id"] if "kwargs" in payload and "id" in payload["kwargs"] else None
		namespace, target = None, None
		if id is not None:
			if len(id.split("/")) > 2:
				namespace = id.split("/")[1]
				target = "/".join(id.split("/")[2:])
				# print(" $$$$$$$ NAMESPACE $$$$$$$ ", namespace)
				# print(" $$$$$$$ TARGET $$$$$$$ ", target)

				# if MicroXO._current_namespace == namespace:
				# 	pass
				# 	BROADCAST PUSH 
				# else:
				# 	# REQUEST FROM SERVER
				# 	print(" $$$$$$$ REQUESTING FROM SERVER $$$$$$$ ", namespace)
				# 	SEND REQUEST TO SERVER

				
		print(":::::::::::::::::::::::::::", self._id, payload)
		if target is not None:
			print(f" ::: Sending Request to Server {namespace} ::: {target}")
			print(" $$$$$$$ TARGET $$$$$$$ ", target)
			# return self._getRoot().CallFunc(payload)
		return "NICE!!!!!!"


@MicroXO
def foo(*args, **kwargs):
	print("FOO", args, kwargs)


@MicroXO
def bar(*args, **kwargs):
	print("BAR", args, kwargs)


@MicroXO
def Sara(*args, **kwargs):
	print("SARA IS AWESOME <3", args, kwargs)


# bar()
m = MicroXO()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(m.index)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(type(d.index["xo/bar"]))
# d.index["xo/bar"]("NICEEEEEEEE!!!!!!!!!!!!!!")


import MicRobee
MicRobee = MicRobee.register("Webapi", 1970)


def getLocation():
	return MicRobee.gps.location()


m.Sara(" And very loved by me :-*")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

		# print(args, kwargs)
		# self._func = lambda : 1

	# def __call__(self, *args, **kwargs):
	# 	self._id
	# 	print("DECORATOR", self._id, self._func, args, kwargs)
	# 	if self._func is not None:
	# 		return self._func(*args, **kwargs)
	# 	# if isinstance(self.value, function):
	# 	if "function" in str(type(self.value)):
	# 		return self.value(*args, **kwargs)
	# 	return self.value

