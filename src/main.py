#!/usr/bin/env python
import rospy
from autoforce_mixer.msg import NodeWeightArray, NodeWeight
import json

results = None
def callback(data):
	results = data

def main():
	with open('ambrose.json') as data_file:
		data = json.load(data_file)
		stages = data["stages"]
		pub = rospy.Publisher('autoforce_offb_controller', NodeWeightArray, queue_size=10)
		ros.init_node('autoforce_offb_controller')
		rate = rospy.Rate(10)

		current_stage = 0
		while current_stage < len(stages):
			stage = stages[current_stage]
			sub = rospy.Subscribe(stage['node'])
			out = []
			nodes = stage["then"]
			for node in nodes.keys():
				if node == "twist":
					
			while True:
				if results = None:
					continue
				if stage["type"] == "boolean":
					if results == stage["value"]:
						pub.
						break
				if stage["type"] == "range":
					if stage["min"] < results < stage["max"]:
						break
				rate.sleep()
			sub.shutdown()
			rate.sleep()

if __name__ == "__main__":
	main()
