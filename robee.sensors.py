import time
import random
import traceback
from xo import *
from xo_redis import Redis


def getIMU(*args, **kwargs):
	''' Get IMU Data from DAL'''
	# if str(Robee.sensors.imu.ready()).lower() == "true":
	if Robee.sensors.imu.ready():             	 					# type: ignore	
		# ::: GETTING IMU DATA FROM DAL :::
		res = xo.dal.getIMU()             	 						# type: ignore

		Robee.sensors.imu.data = res             	 				# type: ignore
		Robee.sensors.imu.count += 1             	 				# type: ignore
		# Robee.sensors.imu.data(res)
		# Robee.sensors.imu.count(Robee.sensors.imu.count() + 1)
		return res
	else:
		print(" ::: Re-initialize sensors :::")
		xo.initSensors("imu")             	 						# type: ignore
		return None


def initSensors(sensors=None, *args, **kwargs):
	''' Initialize Robee Sensors'''

	currentSensors = xo.sensors
	if sensors is not None:
		if isinstance(sensors, str):
			sensors = [sensors] # Encapsulate in list incase str was given
	else: # If specific sensors were not given, all sensors in xo.sensors will be applied
		sensors = currentSensors.keys()             	 			# type: ignore
	
	robeeSensors = Robee.sensors # (Robee is the Redis Backed)
	noProblems = True
	for sensor in sensors:
		robeeSensor, currentSensor = robeeSensors[sensor], currentSensors[sensor]             	 				# type: ignore
		robeeSensor.count = 0
		if "init" in currentSensor:
			initSuccess = currentSensor.init()
			if not initSuccess:
				print(f" ::: COULD NOT INIT : {sensor} :::")
			robeeSensor.ready = initSuccess
		else: # Sensor doesn't need init apparently
			robeeSensor.ready = True

	if noProblems:
		robeeSensors.ready = True            	 				# type: ignore
	else:
		robeeSensors.ready = False            	 				# type: ignore
	


def initIMU(*args, **kwargs):
	print(f" ::: INITIALIZING IMU ::: ", (args, kwargs)
		  if len(args) > 0 or len(kwargs) > 0 else "")
	# TODO: really initialize imu
	return True


def mockIMU(*args, **kwargs):
	''' Get Mock IMU Data for testings'''
	return [
		[random.random(), random.random(), random.random(),
		 random.random()],  # Gyro          (x,y,z,q)
		[random.random(), random.random(), random.random(),
		 random.random()],  # Accelerometer (x,y,z,q)
		[random.random(), random.random(), random.random(),
		 random.random()],  # Magnetometer  (x,y,z,q)
	]


def sensorThread(_async=False, sampleEvery=0.0000001, delay = None):
	sensors = xo.sensors
	if _async:
		while True:
			for sensor in sensors:             	 											# type: ignore
				xo._async(sensors[sensor])             	 									# type: ignore
			time.sleep(sampleEvery)
	else:  # Use this if you want this to be blocking
		while True:
			try:
				for sensor in xo.sensors:             	 									# type: ignore
					sensors[sensor]()             	 										# type: ignore
					# raw = sensors[sensor]()
					# print(f" --- GOT IMU DATA --- \n{raw}\n -------------------\n")
				if delay is not None:
					time.sleep(delay)
			except Exception as e:
				print(" ::: Could not get imu data :::", traceback.print_exc())



'''
##############################################################
##############################################################
#######                 BumbleBee                   ##########
#######           Robee Sensors Service             ##########
#######                                             ##########
##############################################################
##############################################################
'''




# Get Robee Hub
Robee = Redis()

# init all sensors that have "init" (in xo.sensors)
xo.initSensors = initSensors
xo.sensors.imu = getIMU                	 						# type: ignore
xo.sensors.imu.init = initIMU                 	 				# type: ignore


xo.dal.getIMU = mockIMU             	 						# type: ignore


Robee.sensors.imu.count = 0	                 	 				# type: ignore
# Subscribe to imu changes :)
Robee.sensors.imu.data @= lambda data: print(              	 				# type: ignore
	f" ::: GOT IMU DATA ({Robee.sensors.imu.count.value}) ::: {time.ctime()} ::: \n{data}\n") if xo.debug else None   			# type: ignore

# Run Settings
xo.debug = False
xo.useAsync = True
xo.useDelay = None

if __name__ == "__main__":
	# Start Sensors Service (IMU,...)
	if xo.useAsync:
		xo._async(sensorThread, delay = xo.useDelay.value)             	 				# type: ignore
	else:
		sensorThread(delay = xo.useDelay.value)              	 						# type: ignore
	# TODO: currently using only Thread, but we can use asyncio, or timers
	while True:
		time.sleep(1)

	# TODO: replace MOCK with real sensors
	# from sensors_DI.sensors import SENSORS_CONTAINER, SensorNotRegisteredError
	# SENSORS_CONTAINER.turn_sensors_on()
	# from system_initializer import SystemInitializer
    # all initializations in background in the system initializer class
	# initializer = SystemInitializer()
	# initializer.start()
	# clock_updated_already = False
	# init_logging()
	# logger.info('starting')
