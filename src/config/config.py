import urllib2
import logging
import json

PDS_BASE = '/opt/PDS/'
DATA_FILE_LOCATION = '%s/distro_data' % PDS_BASE
LOG_FILE_LOCATION = '%s/log/pds.log' % PDS_BASE
MIN_DATA_FILE_SIZE = 50000
MAX_RECORDS_TO_CONCAT = 5000

proxy_user = 'proxy_user'
proxy_password = 'proxy_password'
proxy_server = 'proxy_server'
proxy_port = 'proxy_port'

enable_proxy_authentication = False
server_host = '0.0.0.0'
server_port = 5000

DISABLE_PAGINATION = False

'''
Following are the various debug levels:
CRITICAL
ERROR
WARNING
INFO
DEBUG
NOTSET
Refer https://docs.python.org/2/library/logging.html for more information.
'''
DEBUG_LEVEL = logging.ERROR

'''
SUPPORTED_DISTROS dictionary provides details about supported distros.
The various distros provided form the 'Keys' of this dictionary
The value of this dctionary contains another dictionary whose keys are each versions of the distro and value contains the Json file having package data
Example:
To Support "Ubuntu 16.04", "Ubuntu 16.10" and "Ubuntu XX.yy" set the value of SUPPORTED_DISTROS as follows (Note the distro is "Ubuntu" here) ...  
SUPPORTED_DISTROS = {
    'Ubuntu': {
        'Ubuntu 16.04': 'Ubuntu_16_04_zzz.json',
        'Ubuntu 16.10': 'Ubuntu_16_10.json',
        'Ubuntu XX.yy': 'Ubuntu_ZXY.json'
    }
}

IMPORTANT: After making ANY change to SUPPORTED_DISTROS, ensure the following
    1) <PDS_BASE>/distro_data/cached_data.json file MUST BE deleted.  
    2) The PDS server MUST BE restarted.
'''

SUPPORTED_DISTROS = {
    'Ubuntu': {
        'Ubuntu 17.04': 'Ubuntu_16_04_Package_List.json',
        'Ubuntu 16.10': 'Ubuntu_16_10_Package_List.json',
        'Ubuntu 16.04': 'Ubuntu_17_04_Package_List.json'
    }, 
    'Suse Linux Enterprise Server': {
        'Suse Linux Enterprise Server 11 SP4': 'Suse_Linux_Enterprise_Server_11_SP4_Package_List.json',
        'Suse Linux Enterprise Server 12 SP1': 'Suse_Linux_Enterprise_Server_12_SP1_Package_List.json',
        'Suse Linux Enterprise Server 12 SP2': 'Suse_Linux_Enterprise_Server_12_SP2_Package_List.json'
    }
}

logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILE_LOCATION, level=DEBUG_LEVEL)

LOGGER = logging.getLogger('PDS_SERVER')

def DISTROS_WITH_BIT_REP():
    bit_value = '1'
    bitFlag = 1
    distroBitMap = {}
    distroRecord = {}
    for supportedDistroName in SUPPORTED_DISTROS.keys():
        for distroVersion in SUPPORTED_DISTROS[supportedDistroName].keys():
            if(not distroBitMap.has_key(supportedDistroName)):
                distroBitMap[supportedDistroName] = {}
            distroBitMap[supportedDistroName][distroVersion] = bitFlag
            bitFlag += bitFlag
    return distroBitMap
    
# In case application is hosted on server with proxy, set "enable_proxy_authentication = True" in config.py 
# and update the proxy details
def proxy_authentication():
    proxy = urllib2.ProxyHandler({'http': 'http://%s:%s@%s:%s' % (proxy_user, proxy_password, proxy_server, proxy_port),
      'https': 'https://%s:%s@%s:%s' % (proxy_user, proxy_password, proxy_server, proxy_port)}
    )
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
