import json

def getConfig ():
    f = open('config.json')
    data = json.load(f)
    f.close()
    return data


def saveStatus(config):
    with open('status.json', 'w') as f:
        json.dump(config, f)
