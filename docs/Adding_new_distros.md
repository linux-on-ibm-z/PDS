# Adding new distributions to the tool

This documents details the steps to be performed in order to add a distribution support to PDS tool. 

_**General Notes:**_ 	

 * _A directory `/<DATA_FILE_LOCATION>/` defined in Step 6 of [Installation](Installation.md) document._

 * _A directory `/<PDS_BASE>/` defined in Step 6 of [Installation](Installation.md) document._

### Step 1. Create a JSON file with package data

**The data file should be saved in folder `<DATA_FILE_LOCATION>`:**

    The file name can be named as *.json
    NOTE: File should not be named as `cached_data.json`

**Here's sample file naming:**

    Ubuntu_14.04.json

The Content of the distribution data JSON file has to be in the following format:

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

### Step 2. Update the SUPPORTED_DISTROS variable in configuration file `/<PDS_BASE>/src/config/config.py`
This update in the configuration file is necessary to map the JSON files with relevent "Dispaly Name" of supported Distro and its versions.

SUPPORTED_DISTROS must have following structure
```
SUPPORTED_DISTROS = {
    '<Distro Name1>': {
        '<Distro Version 1': '<Json File Name>.json',
        '<Distro Version 2': '<Json File Name2>.json',
        '<Distro Version 3': '<Json File Name3>.json'
    },
    '<Distro Name2>': {
        '<Distro Version XX': '<Json File NameXX>.json',
        '<Distro Version YY': '<Json File NameYY>.json',
        '<Distro Version ZZ': '<Json File NameZZ>.json'
    }
}
```

**Here's an example:**
```
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
```

### Step 3. Delete the cached data file `<DATA_FILE_LOCATION>/cached_data.json`
The system needs to regenerate the cached_data after adding a new distro.  Hence delete the existing cache as follows:

```
cd <DATA_FILE_LOCATION>
rm -f cached_data.json
```

### Step 4. Restart the server by refering to the steps mentioned in [Installation](Installation.md) document.