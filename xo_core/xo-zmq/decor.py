from xodal import xodal

class decor(xodal):
	# index = {}
	def __init__(self,func = None,*args,**kwargs):
		print("########",func,args,kwargs)
		super().__init__(*args,**kwargs)
		self._func = func
		if func is not None:
			print(self._id,"!!!!!!!",func.__name__,type(func))
			# super().index[self._id+"/"+func.__name__] = self
			# decor.index[self._id+"/"+func.__name__] = [func, self]
			decor.index[self._id+"/"+func.__name__] = func

		# print(args, kwargs)
		# self._func = lambda : 1

	def __call__(self, *args, **kwargs):
		self._id
		print("DECORATOR", self._id, self._func, args, kwargs)
		if self._func is not None:
			return self._func(*args, **kwargs)
		# if isinstance(self.value, function):
		if "function" in str(type(self.value)):
			return self.value(*args, **kwargs)
		return self.value

# @decor
# def foo(*args, **kwargs):
# 	print("FOO", args, kwargs)

# @decor
# def bar(*args, **kwargs):
# 	print("BAR", args, kwargs)

# @decor
# def Sara(*args, **kwargs):
# 	print("SARA IS AWESOME <3", args, kwargs)


# # bar()
# d = decor()
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(d.index)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# # print(type(d.index["xo/bar"]))
# # d.index["xo/bar"]("NICEEEEEEEE!!!!!!!!!!!!!!")


# d.Sara(" And very loved by me :-*")
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# d.Sara("^^^^")