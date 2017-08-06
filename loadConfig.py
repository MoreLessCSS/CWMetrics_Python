import json

def getConfigFile():
    with open("config.json") as data_file:
        data = json.load(data_file)
        return data

