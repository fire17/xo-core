from .xodal import xodal
class MicroXO(xodal):
	_pubPort = 1970
	_reqPort = 19701
	_id = "_root_"
	
	def __init__(self, funcOrNamespace=None, port=None, *args, **kwargs):
		# print("########", func, args, kwargs)
		func = None
		x = xodal()
		
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
			killport.kill_ports(ports=[MicroXO._pubPort, MicroXO._reqPort])
			time.sleep(1)
			self._pubserver = Server(xoServer._pubPort)
			self._reqserver = Server(xoServer._reqPort)

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
				for msg in listen_for_request:
					c += 1
					try:
						print(c, "::: INCOMING:", msg)
						# f"ECHO! {msg}".encode()
						# reply(bytes("ECHO! "+str(msg)))
						reply(f"ECHO! {msg}".encode())
						# MERGE WITH MICROXO
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
			print(f" ::: Requests Server Started \{{namespace}\}")
		# time.sleep(1)
		# pub = Thread(target=pushToSubs, args=[self._id, ])
		# pub.start()
			

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

