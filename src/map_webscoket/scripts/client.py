#!/usr/bin/env python

import socketio
import rospy
from nav_msgs.msg import OccupancyGrid


class map_websocket():

    def __init__(self):
        
        #Variables
        self.map_json = ""

        #Websocketio
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:6000')
        self.sio.wait()

        #ROS
        rospy.init_node('map_websocket', anonymous=True)
        self.map_sub = rospy.Subscriber("map", OccupancyGrid, map_callback)
        rospy.spin()

    
    def map_callback(self,data):
        #Log
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

        #Create JSON data
        self.map_json = {'map':data.data}

        #Send to server
        self.sio.emit('map_data',self.map_json)

        
    @sio.event
    def connect(self):
        rospy.loginfo('connection established')


    @sio.event
    def my_message(self,data):
        print('message received with ', data)
    

    @sio.event
    def disconnect(self):
        rospy.loginfo('disconnected from server')



if __name__ == '__main__':
    map_websocket()

