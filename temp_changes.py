

	def __str__(self):
		# print(f"!!!!!!! {self._name}")
		if self._val is not None:
			if "formula" in self and True:  # TODO: check valid formula
				print("iiiiiiiiiiiiiiiiiiiiiiiiiiiRRRRRR")
				return str(self._runFormula())
			return str(self._val)
		return "{xobject "+str({str(self._name):self._val})[1:]#[:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		# return "{xobject "+str({str(self._name):self._val[0]})[1:]#[:-1]+f" Children({len(self.children())}) ::: {self.children()} "+"}"
		# return str({"_val":self._val})
		# return str(self._val)
		# return str(self.__get__())








	def __repr__(self):
		justShow = True
		if justShow:
			self.show(ret = False)
			print()
		# print("where are we ?")
		recursiveDict = False
		if self._val is None:
			self._setValue([[]])
		if "function" in str(type(self._val)):
			return str(self._val())
		if "formula" in self and True: # TODO: check valid formula
			print("iiiiiiiiiiiiiiiiiiiiiiiiiiiRRRRRR")
			return str(self._runFormula())
		# ret = "{xobject "+str({str(self._name):self._val[0]})[1:-1]+f" ::: children({len(self.children())})"
		ret = "{xobject "+str({str(self._name):self._val})[1:-1]+f" ::: children({len(self.children())})"
		childs = []
		if self.children() is not None and len(self.children()) > 0:
			if recursiveDict: #TODO DICT XXX
				ret += f" ::: {self.children()}"
			else:
				for c in self.children():
					# print("CCCCC",c)
					childs.append(c)
				ret += ":"+str(childs)
		ret +="}"
		return ret





        	





	def _needsUpdate(self):
		return self._lastUpdated == self._lastLoaded


	# def _lastUpdatedNow(self):
	# 	self._lastUpdated = time.time()
	def _runFormula(self):
		if True or "formula" in self:
			# if self._lastUpdated != self._lastLoaded:
			if self._needsUpdate():
				# formula = self.formula._val
				# newValue = formula()
				newValue = self.formula()
				self.formula.currentValue = newValue
				# self._val = newValue
				# self = newValue
				self._lastLoaded = self._lastUpdated
				# print("xxxxxxxx", self, formula, getsource(formula))
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", newValue)
				self._updateSubscribers_(newValue)
				return newValue
			else:
				return self.formula.currentValue
		return None