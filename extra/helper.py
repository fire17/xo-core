
def processCMD(*args, **kwargs):
	print(f" ::: Processing Data from CMD ::: data length {len(str(args))}\n\n")

# REPOSIZE
# curl https://api.github.com/repos/fire17/AlphaENG 2> /dev/null | grep size | tr -dc '[:digit:]'

# TODO: Fix *args **kwargs
# def osCommand(cmd = ['ping -c100 www.google.com',False], callback = processCMD):
def osCommand(cmd = ["",'ping -c100 www.google.com',False, processCMD, "cmd.res"]):
	oneLine, location, cmd, asyn, callback, autoPub = cmd
	# location = "/home/magic/xo-gd/main"
	# cmd = "rm -rf fire17_AlphaENG && git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	# cmd = "git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG "
	if location and not asyn:
		currDir = os.getcwd()
		os.chdir(location)
		newDir = os.getcwd()
		print(" ::: CD TO",location)
	# print("RUNNING 1")
	# res =
	# print("ASYN", asyn)
	if not asyn or True:
		if not oneLine or True:
			cmd = cmd.strip(" ").split(' ')
			# print("bbbbbbbbbbbbbbbbbbb")
		else:
			cmd = [cmd.strip(" ")]
		res = []
		try:
			print (f" ::: Running Command ::: {' '.join(cmd)} \n ::: you can break (ctrl+c) and get the results :::  \n")
			for line in os_command(cmd, print_output=True):
				print(line)
				res.append(line)
		except Exception as e:
			traceback.print_exc()
			print(" ::: STOPING CMD !!! :::")
			pass #so you can break and also get the results

		if callback is not None:
			print(" ::: Sending results to callback !!! :::", callback)
			callback(res)
		if autoPub is not None and autoPub is not "":
			if "list" not in str(type(autoPub)):
				autoPub = [autoPub]
			for a in autoPub:
				x = xo.GetXO(a)
				if x:
					x.set(res)
		# xo.res = res
		return res
	# #######################################################################
	# Below Not Running

	res = []
	for cmdA in cmd.split(" && ")[1:]:
		if not oneLine:
			cmdA = cmdA.split(' ')
			# print("bbbbbbbbbbbbbbbbbbb")
		else:
			cmdA = [cmdA]
			# print("AAAAAAAAAAAAAAAAAAAAAAAAAAA",cmdA)
		resA = run_os_command(cmdA, print_output=False)
		# print("BBBBBBBBBBBBBBBBBBBBBBBBBBB",resA)
		res.append(resA)

	# print("RRRRRRRR",res)
	if location:
		os.chdir(currDir)
		resDir = os.getcwd()
		print(" ::: currDir == resDir",currDir == resDir," BACK TO ",resDir)

	if callback is not None:
		callback(res)
	if autoPub is not None and autoPub is not "" and autoPub is not []:
		if "list" not in str(type(autoPub)):
			autoPub = [autoPub]
		for a in autoPub:
			x = xo.GetXO(a)
			if x:
				x.set(res)
	# xo.res = res
	# print("RUNNING ASYNC DONE")
	# xo.res = line
	# # line = process.stdout.readline().rstrip()
	# # yield line
	# print("............DONE")
	return True


# def command(cmd = , asyn = False):
# def command(cmd = "ping 8.8.8.8",location ="", asyn = True):
# def command(cmd = "ping 8.8.8.8",location ="/home/magic/xo-gd/main", asyn = True):
# def command(cmd = "git clone https://github.com/fire17/AlphaENG.git /home/magic/xo-gd/main/fire17_AlphaENG ",location ="", asyn = True):
def command(cmd = "ping 8.8.8.8",location ="", oneLine=True, asyn = True):
	# print("XXXXXD")
	xo._osCMD = osCommand
	if asyn:
		xo._osCMD([oneLine, location, cmd, asyn, processCMD,"cmd.res"], asyn = asyn)
	else:
		xo._osCMD([oneLine, location, cmd, asyn, processCMD,"cmd.res"])