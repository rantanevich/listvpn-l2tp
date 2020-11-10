# ListVPN-L2TP
[![Build Status](https://travis-ci.org/rantanevich/listvpn-l2tp.svg?branch=main)](https://travis-ci.org/rantanevich/listvpn-l2tp)

It creates free L2TP VPN account on [listvpn.net](https://www.listvpn.net/).


## Requirements

  - requests (Python HTTP library)


## Installation

```sh
git clone https://github.com/rantanevich/listvpn-l2tp.git .
pip3 install --user requirements.txt
python3 signup.py
```


## Usage

```sh
usage: signup.py [-h] [-r REGION] [-u USERNAME] [-p PASSWORD]

Creates L2TP VPN account https://www.listvpn.net

optional arguments:
  -h, --help            show this help message and exit
  -r REGION, --region REGION
                        region of vpn server (default: unitedstates)
  -u USERNAME, --username USERNAME
                        username (from 5 to 10 characters)
  -p PASSWORD, --password PASSWORD
                        password (from 5 to 10 characters)
```


## Example

```sh
$ python3 signup.py \
    --region russia \
    --username matreshka \
    --password secret

server    : l2tpvpn-ru.server-listvpn.net
username  : matreshka
password  : secret
shared key: listvpn
port      : 1701


$ python3 signup.py

server    : l2tpvpn-us.server-listvpn.net
username  : listvpn.net-GBvgvW0Q
password  : 4Xrp61Ln
shared key: listvpn
port      : 1701
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
