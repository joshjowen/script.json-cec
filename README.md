# Send HDMI CEC commands through Kodi's JSON-RPC.


Kodi addon allowing HDMI-CEC control via Kodi's JSON-RPC.

Modified from [upstream](https://github.com/joshjowen/script.json-cec) to work with Kodi v18 (Leia).


## Installation

1. ``cd ~/.kodi/addons``
2. ``git clone https://github.com/jantman/script.json-cec.git``

## Accepted commands

* 'activate' - Wake up playing device via a CEC peripheral
* 'standby' - Put playing device on standby via a CEC peripheral
* 'toggle' - Toggle state of playing device via a CEC peripheral
* 'stop_and_standby' - Stop any playback and place the CEC peripheral on standby

#### Example JSON request:
```
http://localhost:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.json-cec","params":{"command":"activate"}},"id":1}
```

#### Example Curl Request

```
curl --header 'Content-Type: application/json' --data-binary '{"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.json-cec","params":{"command":"activate"}},"id":1}' http://kodi/jsonrpc
```
