import urllib.request, urllib.error, urllib.parse
import logging

PDS_BASE = '/opt/PDS/'
DATA_FILE_LOCATION = '%s/distro_data' % PDS_BASE
LOG_FILE_LOCATION = '%s/log/pds.log' % PDS_BASE
MIN_DATA_FILE_SIZE = 50000
MAX_RECORDS_TO_CONCAT = 5000
MAX_RECORDS_TO_SEND = 100
CACHE_SIZE = 10
STATS_FILE_LOCATION = '/opt/PDS/stats'
proxy_user = 'proxy_user'
proxy_password = 'proxy_password'
proxy_server = 'proxy_server'
proxy_port = 'proxy_port'

enable_proxy_authentication = False
server_host = '0.0.0.0'
server_port = 5000

DISABLE_PAGINATION = False
STATS_SECRET='new123T'

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

SUPPORTED_DISTROS = {
    "zUbuntu": {
        "zUbuntu 16.04": "Ubuntu_16_04_Package_List.json",
        "zUbuntu 18.04": "Ubuntu_18_04_Package_List.json",
        "zUbuntu 20.04": "Ubuntu_20_04_Package_List.json",
        "zUbuntu 22.04": "Ubuntu_22_04_Package_List.json",
        "zUbuntu 24.04": "Ubuntu_24_04_Package_List.json",
        "zUbuntu 24.10": "Ubuntu_24_10_Package_List.json",
        "zUbuntu 25.04": "Ubuntu_25_04_Package_List.json"
    },
    "zSUSE Linux Enterprise Server": {
        "zSLES 12 SP3": "Suse_Linux_Enterprise_Server_12_SP3_Package_List.json",
        "zSLES 12 SP4": "Suse_Linux_Enterprise_Server_12_SP4_Package_List.json",
        "zSLES 12 SP5": "Suse_Linux_Enterprise_Server_12_SP5_Package_List.json",
        "zSLES 15": "Suse_Linux_Enterprise_Server_15_Package_List.json",
        "zSLES 15 SP1": "Suse_Linux_Enterprise_Server_15_SP1_Package_List.json",
        "zSLES 15 SP2": "Suse_Linux_Enterprise_Server_15_SP2_Package_List.json",
        "zSLES 15 SP3": "Suse_Linux_Enterprise_Server_15_SP3_Package_List.json",
        "zSLES 15 SP4": "Suse_Linux_Enterprise_Server_15_SP4_Package_List.json",
        "zSLES 15 SP5": "Suse_Linux_Enterprise_Server_15_SP5_Package_List.json",
        "zSLES 15 SP6": "Suse_Linux_Enterprise_Server_15_SP6_Package_List.json"
    },
    "zSUSE Package Hub": {
        "zSLES 15": "SUSE_Package_Hub_SLES_15.json",
        "zSLES 15 SP1": "SUSE_Package_Hub_SLES_15_SP1.json",
        "zSLES 15 SP2": "SUSE_Package_Hub_SLES_15_SP2.json",
        "zSLES 15 SP3": "SUSE_Package_Hub_SLES_15_SP3.json",
        "zSLES 15 SP4": "SUSE_Package_Hub_SLES_15_SP4.json",
        "zSLES 15 SP5": "SUSE_Package_Hub_SLES_15_SP5.json",
        "zSLES 15 SP6": "SUSE_Package_Hub_SLES_15_SP6.json"
    },
    "zRHEL": {
        "zRHEL 7.6": "RHEL_7_6_Package_List.json",
        "zRHEL 7.7": "RHEL_7_7_Package_List.json",
        "zRHEL 7.8": "RHEL_7_8_Package_List.json",
        "zRHEL 7.9": "RHEL_7_9_Package_List.json",
        "zRHEL 8.1": "RHEL_8_1_Package_List.json",
        "zRHEL 8.2": "RHEL_8_2_Package_List.json",
        "zRHEL 8.3": "RHEL_8_3_Package_List.json",
        "zRHEL 8.4": "RHEL_8_4_Package_List.json",
        "zRHEL 8.5": "RHEL_8_5_Package_List.json",
        "zRHEL 8.6": "RHEL_8_6_Package_List.json",
        "zRHEL 8.7": "RHEL_8_7_Package_List.json",
        "zRHEL 8.8": "RHEL_8_8_Package_List.json",
        "zRHEL 8.9": "RHEL_8_9_Package_List.json",
        "zRHEL 8.10": "RHEL_8_10_Package_List.json",
        "zRHEL 9.0": "RHEL_9_0_Package_List.json",
        "zRHEL 9.1": "RHEL_9_1_Package_List.json",
        "zRHEL 9.2": "RHEL_9_2_Package_List.json",
        "zRHEL 9.3": "RHEL_9_3_Package_List.json",
        "zRHEL 9.4": "RHEL_9_4_Package_List.json",
        "zRHEL 9.5": "RHEL_9_5_Package_List.json"
    },
    "xUbuntu": {
        "xUbuntu 16.04": "xUbuntu_16_04_Package_List.json",
        "xUbuntu 18.04": "xUbuntu_18_04_Package_List.json",
        "xUbuntu 20.04": "xUbuntu_20_04_Package_List.json",
        "xUbuntu 22.04": "xUbuntu_22_04_Package_List.json",
        "xUbuntu 24.04": "xUbuntu_24_04_Package_List.json",
        "xUbuntu 24.10": "xUbuntu_24_10_Package_List.json",
        "xUbuntu 25.04": "xUbuntu_25_04_Package_List.json"
    },
    "xSUSE Linux Enterprise Server": {
        "xSLES 12 SP3": "xSuse_Linux_Enterprise_Server_12_SP3_Package_List.json",
        "xSLES 12 SP4": "xSuse_Linux_Enterprise_Server_12_SP4_Package_List.json",
        "xSLES 12 SP5": "xSuse_Linux_Enterprise_Server_12_SP5_Package_List.json",
        "xSLES 15": "xSuse_Linux_Enterprise_Server_15_Package_List.json",
        "xSLES 15 SP1": "xSuse_Linux_Enterprise_Server_15_SP1_Package_List.json",
        "xSLES 15 SP2": "xSuse_Linux_Enterprise_Server_15_SP2_Package_List.json",
        "xSLES 15 SP3": "xSuse_Linux_Enterprise_Server_15_SP3_Package_List.json",
        "xSLES 15 SP4": "xSuse_Linux_Enterprise_Server_15_SP4_Package_List.json",
        "xSLES 15 SP5": "xSuse_Linux_Enterprise_Server_15_SP5_Package_List.json",
        "xSLES 15 SP6": "xSuse_Linux_Enterprise_Server_15_SP6_Package_List.json"
    },
    "xSUSE Package Hub": {
        "xSLES 15": "xSUSE_Package_Hub_SLES_15.json",
        "xSLES 15 SP1": "xSUSE_Package_Hub_SLES_15_SP1.json",
        "xSLES 15 SP2": "xSUSE_Package_Hub_SLES_15_SP2.json",
        "xSLES 15 SP3": "xSUSE_Package_Hub_SLES_15_SP3.json",
        "xSLES 15 SP4": "xSUSE_Package_Hub_SLES_15_SP4.json",
        "xSLES 15 SP5": "xSUSE_Package_Hub_SLES_15_SP5.json",
        "xSLES 15 SP6": "xSUSE_Package_Hub_SLES_15_SP6.json"
    },
    "xRHEL": {
        "xRHEL 7.6": "xRHEL_7_6_Package_List.json",
        "xRHEL 7.7": "xRHEL_7_7_Package_List.json",
        "xRHEL 7.8": "xRHEL_7_8_Package_List.json",
        "xRHEL 7.9": "xRHEL_7_9_Package_List.json",
        "xRHEL 8.1": "xRHEL_8_1_Package_List.json",
        "xRHEL 8.2": "xRHEL_8_2_Package_List.json",
        "xRHEL 8.3": "xRHEL_8_3_Package_List.json",
        "xRHEL 8.4": "xRHEL_8_4_Package_List.json",
        "xRHEL 8.5": "xRHEL_8_5_Package_List.json",
        "xRHEL 8.6": "xRHEL_8_6_Package_List.json",
        "xRHEL 8.7": "xRHEL_8_7_Package_List.json",
        "xRHEL 8.8": "xRHEL_8_8_Package_List.json",
        "xRHEL 8.9": "xRHEL_8_9_Package_List.json",
        "xRHEL 8.10": "xRHEL_8_10_Package_List.json",
        "xRHEL 9.0": "xRHEL_9_0_Package_List.json",
        "xRHEL 9.1": "xRHEL_9_1_Package_List.json",
        "xRHEL 9.2": "xRHEL_9_2_Package_List.json",
        "xRHEL 9.3": "xRHEL_9_3_Package_List.json",
        "xRHEL 9.4": "xRHEL_9_4_Package_List.json",
        "xRHEL 9.5": "xRHEL_9_5_Package_List.json"
    }
}

logging.basicConfig(format='%(asctime)s %(message)s', filename=LOG_FILE_LOCATION, level=DEBUG_LEVEL)

LOGGER = logging.getLogger('PDS_SERVER')
   
# In case application is hosted on server with proxy, set "enable_proxy_authentication = True" in config.py 
# and update the proxy details
def proxy_authentication():
    proxy = urllib.request.ProxyHandler({'http': 'http://%s:%s@%s:%s' % (proxy_user, proxy_password, proxy_server, proxy_port),
      'https': 'https://%s:%s@%s:%s' % (proxy_user, proxy_password, proxy_server, proxy_port)}
    )
    auth = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)