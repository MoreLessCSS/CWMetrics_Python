import json

def getConfigFile():
    with open('d:\\repo_kib\\CWMetrics_Python\\config\\MasterNode\\config.json') as data_file:
        data = json.load(data_file)
        return data

