import time
import traceback
from xo import *
from xo_redis import Redis


from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask.helpers import send_from_directory
import logging
import json
from flask import (Response, jsonify, redirect, request, send_file, url_for)

# from flask.config import Config

#TODO: disable cors_allowed_origins at production



'''
##############################################################
##############################################################
#######                 BumbleBee                   ##########
#######            Robee WebAPI Service             ##########
#######                                             ##########
##############################################################
##############################################################
'''

app = Flask(__name__)
Robee = Redis()


# Robee.sensors.imu.data @= lambda data: print(f" ::: GOT IMU DATA ::: {time.time()} ::: {data}")
Robee.favicon.ico._setValue({})

Robee.f.foo = lambda *a, **kw: "BAR "+ str(xo.foo.count(xo.foo.count+1))
Robee.f.reboot = lambda *a, **kw: "STARTING REBOOT!"

@app.route('/<path:text>', methods=['POST',"GET"])
def route(text, ):
    try:
        xoID = text.replace(".", "/")
        print(f"!!!!!!!!!! Web API Request {text} !!!!!!!!!!! {xoID} !!!!!!!!!!!! {request.args.keys()}")
        res =  Robee._GetXO(xoID)()
        if "function" in str(type(res)) or "method" in str(type(res)):
            res = res()
        # print(res,"@@@@@@@@@@@@@@@")
        return jsonify(res)
    except:
        return jsonify({"Internal Exception":str(traceback.format_exc())})
    # return send_file('/var/www/PythonProgramming/PythonProgramming/static/images/python.jpg', attachment_filename='python.jpg')
    return send_file(f'uploads/{text}')


# @app.route('/upload/<path:text>', methods=['POST',"GET"])
# def upload(text):
#     print("!!!!!!!!!! SENDING FILE UPLOAD")
#     # return send_file('/var/www/PythonProgramming/PythonProgramming/static/images/python.jpg', attachment_filename='python.jpg')
#     return send_file(f'uploads/{text}')
# uploads/f_8Bau2hLrRZgVk6gQ4k8cDf.opus
# @app.route('/api/imu')
# def imu():
#     # x = SENSORS_CONTAINER.get_sensor('IMU').last_recorded()['temp']
#     return jsonify(Robee.sensors.imu.data.value)                                            # type: ignore



# sockets for keep alive status - it requires installation of gevent-websocket and gevent
socketio = SocketIO(app, cors_allowed_origins='*',
                    async_mode='gevent', logger=False)

print(" ::: STARTING WEB API ::: ")


@socketio.on('data')
def handle_message(data):
    print("DDDDDDDDDDDDDDDDDDDDDDDDDD",data)
    send(" ::: GOT DATA ::: " + str(data))

@socketio.on('connection')
def handle_messagec(data):
    print("DDDDDDDDDDDDDDDDDDDDDDDDDD",data)
    send(" ::: GOT DATA ::: " + str(data))

# logger.info('starting')
socketio.run(app, use_reloader=False, debug=True)
print("!!!!!!!!")
while True:
    time.sleep(1)
