# from argparse import Namespace
# from dataclasses import dataclass, field, asdict
from xo.expando import Expando
from zeroless import Client, Server
# from xo.zmq import xoServer
import killport
from xo_zmq import xoClient

from threading import Thread
import traceback
import time, os
import json


class xodal(Expando):
	_rootName = "xodal"
	index = {}
	_auth = None
	# _id = xo

	def __init__(self, func=None, _xoT_=None, *args, **kwargs):
		# print("########", func, args, kwargs)
		super().__init__(_xoT_=_xoT_ if _xoT_ is not None else xodal, *args, **kwargs)
		# if func is None:
		# 	super().__init__(*args, **kwargs)
		# else:
		# 	super().__init__(self, *args, **kwargs)

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
		# if not self._isRoot:
		# 	# get = ".".join(self._id.replace("/",".").split(".")[1:] + get.split("."))
		# 	return self._getRoot().CallFunc(payload)

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
	_rootName = "microxo"
	_reqPort = 1970
	_pubPort = 19701

	def __init__(self, funcOrNamespace=None, reqPort=None, _xoT_=None, *args, **kwargs):
		# print("########", func, args, kwargs)
		func = None
		# namespace = self._rootName
		namespace = None
		if isinstance(funcOrNamespace,str):
			namespace = funcOrNamespace
		else:
			func = funcOrNamespace
			# get namespace from running filename
		
		super().__init__(func=func, _xoT_=_xoT_ if _xoT_ is not None else MicroXO, *args, **kwargs)
		# self._id = namespace

		if namespace is not None:
			pubPort = MicroXO._pubPort
			if reqPort is None:
				#Get port
				reqPort = MicroXO._reqPort
			else:
				pubPort = int(str(reqPort)+"1")				
			

			# self._reqServer = xoServer(port = int(str(port)+"1")) 
			killport.kill_ports(ports=[reqPort, pubPort])
			time.sleep(.2)
			# self._pubserver = Server(xoServer._pubPort)
			self._reqserver = Server(reqPort)
			self._reqport = reqPort
			self._pubport = pubPort

			def pushToSubs(topic: str):
				listen_for_push = self._pubserver.pull()
				for msg in listen_for_push:
					try:
						print(msg)
						topic, data = "updates", msg
						self._pubserver.pub()(topic, data)
					except:
						traceback.print_exc()
					finally:
						pass

			def listen(data, *args, **kwargs):
				reply, listen_for_request = self._reqserver.reply()
				c = 0
				for payload in listen_for_request:
					c += 1
					try:
						print(c, "::: INCOMING:", payload, "type:",type(payload))
						print("INDEX:",MicroXO.index)
						print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
						# f"ECHO! {msg}".encode()
						# reply(bytes("ECHO! "+str(msg)))
						payload = json.loads(payload)
						# payload = pk.loads(payload)
						target = payload["target"] if "target" in payload else None
						if target in MicroXO.index:
							print("!!!!!!!!!!!!!!!!!!!!!!!!", target, MicroXO.index[target])
							print("##########")
							res = None
							try:
								res = self.index[target](*payload["args"],**payload["kwargs"])
								print("@@@@@@@@@@@")
								res = json.dumps(res)
								print("@@@@@@@@@@@")
								res = res.encode()
							except:
								traceback.print_exc()
							if res is None:
								reply(bytes(True))
							else:
								# reply(bytes(json.dumps(res)))
								print("##########")
								# reply(json.dumps(res).encode())
								reply(res)
								print("##########")
						else:
							reply(f"ECHO! {target} was not found in index".encode())
		
						# reply(msg)
					except:
						traceback.print_exc()
					finally:
						pass
				# topic = topic[0] if isinstance(topic, list) else topic

				# # Initiate a subscriber client
				# # Assigns an iterable to wait for incoming messages with the topic 'sh'
				# listen_for_pub = self._hook.sub(topics=[topic.encode()])

				# for topic, msg in listen_for_pub:
				#     print(topic, ' - ', msg)
				#     self._setValue(msg)

			requests = Thread(target=listen, args=[self._id, ])
			requests.start()
			print(" ::: Requests Server Started {"+f" {namespace}"+"}"+f" port {self.MicroXO._reqPort}")
			# time.sleep(1)
			# pub = Thread(target=pushToSubs, args=[self._id, ])
			# pub.start()
			

	@staticmethod
	def register(namespace=None, port=None):
		if namespace is None:
			namespace = MicroXO.getNamespace()
		return MicroXO(funcOrNamespace=namespace, reqPort = port)

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
		print("PPPPPPP", payload)
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
				xoClient().request(namespace+"/"+target, * payload["args"], ** payload["kwargs"])


				
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
	# fin = json.dumps({"SARA IS AWESOME <3", args, kwargs})
	fin = {"res":"SARA IS AWESOME <3", "args": args, "kwargs":kwargs}
	print("$$$$$$$$$$")
	return fin
	# return "SARA IS AWESOME <3"


@MicroXO
def gpsLocation(*args, **kwargs):
	fin = {"location": {"lat": 37.422, "lng": -122.084}, "args": args, "kwargs":kwargs}
	return fin

# bar()
m = MicroXO()

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(m.index)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(type(d.index["xo/bar"]))
# d.index["xo/bar"]("NICEEEEEEEE!!!!!!!!!!!!!!")


# import MicRobee
# MicRobee = MicRobee.register("Webapi", 1970)


# def getLocation():
# 	return MicRobee.gps.location()


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

