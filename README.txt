Send CEC commands through XBMC's JSON-RPC.
XBMC Gotham is required because that is when these built in function were made available to add-ons.

Accepted commands are:

'activate' - Wake up playing device via a CEC peripheral
'standby' - Put playing device on standby via a CEC peripheral
'toggle' - Toggle state of playing device via a CEC peripheral

example JSON request:

http://localhost:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.json-cec","params":{"command":"activate"}},"id":1}

Installation

Method Zip

Download the project as zip and rename it as script.json-cec.zip and import it in Kodi

Method copying

Clone the project and copy it to kodi's addons directory, example: ~/.kodi/addons/
