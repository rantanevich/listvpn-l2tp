# ListVPN.net
[![Build Status](https://travis-ci.org/rantanevich/listvpn-l2tp.svg?branch=main)](https://travis-ci.org/rantanevich/listvpn-l2tp)

It creates free L2TP/PPTP VPN account on [listvpn.net](https://www.listvpn.net/).


## Requirements

  - requests (Python HTTP library)


## Installation

```sh
git clone https://github.com/rantanevich/listvpn-l2tp.git .
pip3 install --user requirements.txt
python3 signup.py
```


## Usage

Available parameters:

| Argument           | Default        | Rule          | Description                                                                  |
|--------------------|----------------|---------------|------------------------------------------------------------------------------|
| `-t`, `--type`     | `l2tp`         | `(l2tp|pptp)` | preferable vpn type                                                          |
| `-r`, `--region`   | `unitedstates` | `[a-z0-9]`    | you have to choose region on listvpn.net and copy server name from url's end |
| `-u`, `--username` | random string  | `[a-zA-Z0-9]` | username should consist of letters and numbers (length: 5-10)                |
| `-p`, `--password` | random string  | `[a-zA-Z0-9]` | password should consist of letters and numbers (length: 5-10)                |

PPTP VPN uses AES-128 encryption.
L2TP VPN uses AES-256 encryption.


## Example

```sh
$ python3 signup.py \
    --type l2tp \
    --region russia \
    --username matreshka \
    --password secret

server    : l2tpvpn-ru.server-listvpn.net
username  : matreshka
password  : secret
shared key: listvpn
port      : 1701
expired   : 2020-12-31


$ python3 signup.py

server    : l2tpvpn-us.server-listvpn.net
username  : listvpn.net-GBvgvW0Q
password  : 4Xrp61Ln
shared key: listvpn
port      : 1701
expired   : 2020-12-31


$ python3 signup.py -t pptp

server    : pptpvpn-us.server-listvpn.net
username  : listvpn.net-zpxfjvK8
password  : 27s4NGdr
shared key:
port      : 1723
expired   : 2020-12-31
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
