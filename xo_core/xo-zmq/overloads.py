

class staticXO(Expando):
	shared = Expando()
	# overload all the functions

	@staticmethod
	def __call__(*args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__call__(*args, **kwargs)
		return self

	@staticmethod
	def __getattribute__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__getattr__(*args, **kwargs)
		return self

	@staticmethod
	def __getattr__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__getattr__(*args, **kwargs)
		return self

	@staticmethod
	def __setattr__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__setattr__(*args, **kwargs)
		return self

	@staticmethod
	def __delattr__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__delattr__(*args, **kwargs)
		return self

	@staticmethod
	def __getitem__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__getitem__(*args, **kwargs)
		return self

	@staticmethod
	def __setitem__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__setitem__(*args, **kwargs)
		return self

	@staticmethod
	def __delitem__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__delitem__(*args, **kwargs)
		return self

	@staticmethod
	def __iter__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__iter__(*args, **kwargs)
		return self

	@staticmethod
	def __next__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__next__(*args, **kwargs)
		return self

	@staticmethod
	def __len__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__len__(*args, **kwargs)
		return self

	@staticmethod
	def __contains__(name, *args, **kwargs):
		self = staticXO.shared
		print("STATIC", self._id, args, kwargs)
		super().__contains__(*args, **kwargs)
		return self


	def __getattr__(self, name):
		print("GETATTR", self._id, name)
		return self

	def __setattr__(self, name, value):
		print("SETATTR", self._id, name, value)
		super().__setattr__(name, value)

	def __delattr__(self, name):
		print("DELATTR", self._id, name)
		super().__delattr__(name)

	def __getitem__(self, name):
		print("GETITEM", self._id, name)
		return self	

	def __setitem__(self, name, value):
		print("SETITEM", self._id, name, value)
		super().__setitem__(name, value)

	def __delitem__(self, name):
		print("DELITEM", self._id, name)
		super().__delitem__(name)

	def __iter__(self):

		print("ITER", self._id)
		return self

	def __next__(self):
		print("NEXT", self._id)
		return self

	def __len__(self):
		print("LEN", self._id)
		return 0

	def __contains__(self, item):
		print("CONTAINS", self._id, item)
		return False

	def __enter__(self):
		print("ENTER", self._id)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		print("EXIT", self._id)
		return self

	def __bool__(self):
		print("BOOL", self._id)
		return False

	def __str__(self):
		print("STR", self._id)
		return ""

	def __repr__(self):
		print("REPR", self._id)
		return ""

	def __add__(self, other):
		print("ADD", self._id, other)
		return self

	def __sub__(self, other):
		print("SUB", self._id, other)
		return self

	def __mul__(self, other):
		print("MUL", self._id, other)
		return self

	def __truediv__(self, other):
		print("TRUEDIV", self._id, other)
		return self

	def __floordiv__(self, other):
		print("FLOORDIV", self._id, other)
		return self

	def __mod__(self, other):
		print("MOD", self._id, other)
		return self

	def __pow__(self, other):
		print("POW", self._id, other)
		return self

	def __lshift__(self, other):
		print("LSHIFT", self._id, other)
		return self

	def __rshift__(self, other):
		print("RSHIFT", self._id, other)
		return self

	def __and__(self, other):
		print("AND", self._id, other)
		return self

	def __xor__(self, other):
		print("XOR", self._id, other)
		return self

	def __or__(self, other):
		print("OR", self._id, other)
		return self

	def __radd__(self, other):
		print("RADD", self._id, other)
		return self

	def __rsub__(self, other):
		print("RSUB", self._id, other)
		return self	

	def __rmul__(self, other):
		print("RMUL", self._id, other)
		return self

	def __rtruediv__(self, other):
		print("RTRUEDIV", self._id, other)
		return self

	def __rfloordiv__(self, other):
		print("RFLOORDIV", self._id, other)
		return self

	def __rmod__(self, other):
		print("RMOD", self._id, other)
		return self

	def __rpow__(self, other):
		print("RPOW", self._id, other)
		return self

	def __rlshift__(self, other):
		print("RLSHIFT", self._id, other)
		return self

	def __rrshift__(self, other):
		print("RRSHIFT", self._id, other)
		return self

	def __rand__(self, other):
		print("RAND", self._id, other)
		return self

	def __rxor__(self, other):
		print("RXOR", self._id, other)
		return self

	def __ror__(self, other):
		print("ROR", self._id, other)
		return self

	def __iadd__(self, other):
		print("IADD", self._id, other)
		return self

	def __isub__(self, other):
		print("ISUB", self._id, other)
		return self

	def __imul__(self, other):
		print("IMUL", self._id, other)
		return self

	def __itruediv__(self, other):
		print("ITRUEDIV", self._id, other)
		return self

	def __ifloordiv__(self, other):
		print("IFLOORDIV", self._id, other)
		return self

	def __imod__(self, other):
		print("IMOD", self._id, other)
		return self

	def __ipow__(self, other):
		print("IPOW", self._id, other)
		return self

	def __ilshift__(self, other):
		print("ILSHIFT", self._id, other)
		return self

	def __irshift__(self, other):
		print("IRSHIFT", self._id, other)
		return self

	def __iand__(self, other):
		print("IAND", self._id, other)
		return self

	def __ixor__(self, other):
		print("IXOR", self._id, other)
		return self

	def __ior__(self, other):
		print("IOR", self._id, other)
		return self

	def __neg__(self):
		print("NEG", self._id)
		return self

	def __pos__(self):
		print("POS", self._id)
		return self

	def __abs__(self):
		print("ABS", self._id)
		return self

	def __invert__(self):
		print("INVERT", self._id)
		return self

	def __complex__(self):
		print("COMPLEX", self._id)
		return self

	def __int__(self):
		print("INT", self._id)
		return self

	def __float__(self):
		print("FLOAT", self._id)
		return self

	def __round__(self, n):
		print("ROUND", self._id, n)
		return self

	def __index__(self):
		print("INDEX", self._id)
		return self

	def __trunc__(self):
		print("TRUNC", self._id)
		return self

	def __floor__(self):
		print("FLOOR", self._id)
		return self

	def __ceil__(self):
		print("CEIL", self._id)
		return self

	def __enter__(self):
		print("ENTER", self._id)
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		print("EXIT", self._id, exc_type, exc_value, traceback)
		return self

	def __bool__(self):
		print("BOOL", self._id)
		return self

	def __len__(self):	
		print("LEN", self._id)
		return self

	def __getitem__(self, key):	
		print("GETITEM", self._id, key)
		return self

	def __setitem__(self, key, value):
		print("SETITEM", self._id, key, value)
		return self

	def __delitem__(self, key):
		print("DELITEM", self._id, key)
		return self

	def __missing__(self, key):
		print("MISSING", self._id, key)
		return self

	def __reversed__(self):
		print("REVERSED", self._id)
		return self

	def __getattribute__(self, name):
		print("GETATTRIBUTE", self._id, name)
		return self

	def __dir__(self):
		print("DIR", self._id)
		return self	

	def __get__(self, instance, owner):
		print("GET", self._id, instance, owner)
		return self

	def __set__(self, instance, value):
		print("SET", self._id, instance, value)
		return self

	def __delete__(self, instance):
		print("DELETE", self._id, instance)
		return self

	def __getinitargs__(self):
		print("GETINITARGS", self._id)
		return self

	def __getnewargs__(self):
		print("GETNEWARGS", self._id)
		return self

	def __getstate__(self):
		print("GETSTATE", self._id)
		return self

	def __setstate__(self, state):
		print("SETSTATE", self._id, state)
		return self

	def __reduce__(self):
		print("REDUCE", self._id)
		return self

	def __reduce_ex__(self, protocol):
		print("REDUCE_EX", self._id, protocol)
		return self

	def __sizeof__(self):
		print("SIZEOF", self._id)
		return self

	def __format__(self, format_spec):
		print("FORMAT", self._id, format_spec)
		return self

	def __hash__(self):
		print("HASH", self._id)
		return self

	def __instancecheck__(self, instance):
		print("INSTANCECHECK", self._id, instance)
		return self

	def __subclasscheck__(self, subclass):
		print("SUBCLASSCHECK", self._id, subclass)
		return self

	def __init_subclass__(self, **kwargs):
		print("INIT_SUBCLASS", self._id, kwargs)
		return self

	def __prepare__(self, name, bases, **kwargs):
		print("PREPARE", self._id, name, bases, kwargs)
		return self

	def __new__(cls, *args, **kwargs):
		print("NEW", cls, args, kwargs)
		return super().__new__(cls)


staticXO.a.b.c.d = "hello"
staticXO.a("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&", staticXO.a)
