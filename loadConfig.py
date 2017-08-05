import json

def getConfigFile():
    with open("D:\\repos_kib\\CWMetrics_Python\\config.json") as data_file:
        data = json.load(data_file)
        return data

