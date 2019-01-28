from urllib.request import urlopen
import os
from json import loads
import time
    
req_api = urlopen('https://api.truckersmp.com/v2/servers').read()  
api_loads = loads(req_api)

def checkserver(api_resp):
    for i in api_resp:
        print('\nGame:', i['game'], '\nName:', i['name'], '\nPlayers online: {}/{}'.format(i['players'], i['maxplayers']), '\nIP: {}:{}'.format(i['ip'], i['port']))
        if i['online'] == True:
            i['online'] = 'Online'
        else:
            i['online'] = 'Offline'
        print('Server Status:', i['online'])
    input()
    
def status(api_sts):
    if api_sts == 'false':
        print('The TruckersMP API is available. \n\nChecking Servers...')
        time.sleep(1.3)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        time.sleep(0.2)
        checkserver(api_loads['response'])
    else:
        print('The TruckersMP API seems to be offline. \n\nKindly, check the status at: https://stats.truckersmp.com/')
        input()

status(api_loads['error'])
