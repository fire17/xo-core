import time
from xo import *
from xo_redis import Redis


'''
##############################################################
##############################################################
#######                 BumbleBee                   ##########
#######           Robee Main Service                ##########
#######                                             ##########
##############################################################
##############################################################
'''


# Get Robee Hub
Robee = Redis()
print(":::::::",Robee)

# Subscribe to imu changes :)
Robee.sensors.imu.data @= lambda data: print(                                                                           # type: ignore
    f" ::: GOT IMU DATA ({Robee.sensors.imu.count.value}) ::: {time.ctime()} ::: \n{data}\n") if xo.debug else None     # type: ignore
	# f" ::: GOT IMU DATA ::: {time.ctime()} ::: \n{data}\n") if xo.debug else None
xo.debug = True

print(" ::: STARTING ROBEE MAIN ::: (awaiting sensor init)")

while True:
    time.sleep(1)

print("DONE")