#-------------------------------------------------------------------------
# File Name	: ImageOrganizer.py
# Purpose	:  This file
#				- lists all the image file
#				- extracts "date taken" information from meta data
#				- organizes file as per "date taken" information
#-------------------------------------------------------------------------
import os

#-------------------------------------------------------------------------
# Function 	: readConfigFile
#-------------------------------------------------------------------------
def readConfigFile(fileName):
	configDict = {}
	configFileHandle = open("./config.txt", "r")
	for entry in configFileHandle.readlines():
		if not entry.isspace():
			entry = entry.strip()
			data = entry.split(":")
			if data[0] == "rootDir":
				configDict["rootDir"] = os.path.abspath(data[1].strip())
			elif data[0] == "outDir":
				configDict["outDir"] = os.path.abspath(data[1].strip())
	return configDict


#read config file
configFile = "./config.txt"
configDict = readConfigFile(configFile)

for key, val in configDict.items():
	print(key, val)



