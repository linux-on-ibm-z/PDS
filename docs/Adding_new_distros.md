# Adding new distributions to the tool:

This documents details the steps to be performed in order to add a distribution support to PDS tool. 

_**General Notes:**_ 	

* _A directory `/<pds_root>/` will be referred to in these instructions. This is a temporary writable directory anywhere you'd like to place it. For e.g. it can be set to `/opt/PDS/`_

### 1. Create a JSON file with package data:

All the distribution specific data files need to be added in the folder `/<pds_root>/distro_data`. 

**The data file should be named in following convention in folder `/<pds_root>/distro_data/`:**

    <Some_New_Distro>_<New_distro_version>_Package_List.json

`<Some_New_Distro>` - is distribution name in upper case.

`<New_distro_version>` - is the distribution version that gets added.

**Here's sample file naming:**

    Ubuntu_14.04_Package_List.json

The Content of the distribution data JSON file needs to be in format below:

```
[{
    "packageName": "<package_name_1>",
    "version": "<package_version_1>"
},{
    "packageName": "<package_name_2>",
    "version": "<package_version_2>"
},{
.
.
.
.
},{
    "packageName": "<package_name_n>",
    "version": "<package_version_n>"
}]
```

**Here's the sample data:**

```
[{
    "packageName": "ImageMagick-devel",
    "version": "6.4.3.6-7.20.1"
}, {
    "packageName": "KhmerOS-fonts",
    "version": "5.0-105.17"
}, {
    "packageName": "KhmerOS-fonts",
    "version": "5.0-105.17"
}, {
    "packageName": "LibVNCServer",
    "version": "0.9.1-156.1"
}]
```

### 2. Make an entry in the configuration file `/<pds_root>/src/config/config.py` as below:
The entry in the configuration file is to help generate a cache file `/<pds_root>/distro_data/cached_data.json` which will be then loaded by the server while starting and used for processing requests.

```diff
@@ -39,6 +39,8 @@ DISTROS_WITH_BIT_REP = {
         'Suse_Linux_Enterprise_Server__11_SP4': 0,
         'Suse_Linux_Enterprise_Server__12_SP1': 0,
         'Suse_Linux_Enterprise_Server__12_SP2': 0
+    }, '<Some_New_Distro>': {
+        '<Some_New_Distro>__<New_distro_version >': 0
     }
 }
```
`<Some_New_Distro>` - is distribution name to be added(naming case should be same as mentioned in file name).

`<distro_version>` - is the distribution version for the new distribution added.

### 3. Regenerate the cached data file `/<pds_root>/distro_data/cached_data.json`
Every time a new distribution is added the cache file needs to be regenerated for the new distribution data to be updated into the file. For this the cached file needs to be manually removed and the server needs to be restarted.

```
cd /<pds_root>/distro_data/
rm -f cached_data.json
```

Restart the server by refering to the steps mentioned in [Installation](Installation.md) document.

