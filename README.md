# ASDM  CLI Utility for Cisco ASA's

This is a cli asdm launcher I wrote. It will automatically add the ASA to the java exceptions list.

## Prerequisites
Must have Oracle Java installed. Please visit [here](https://java.com/en/download/help/linux_x64_install.xml) for more information.

## Installation
```shell
git clone git@github.com:rwendt-bw/asdm.git
```

### sym link executable

```
sudo ln -s ~/git/asdm/asdm.py /usr/local/bin/asdm
```

## Usage
```
usage: asdm [-h] -i IP [-p PORT]

optional arguments:
  -h, --help              show this help message and exit
  -i IP, --ip-address IP  hostname or IP address of ASA
  -p PORT, --port PORT    asdm port - default 8443
```

## Example run
```shell
asdm -i 192.168.1.1
```
