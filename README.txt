Send CEC commands through XBMC's JSON-RPC.
XBMC Gotham is required because that is when these built in function were made available to add-ons.

Accepted commands are:

'activate' - Wake up playing device via a CEC peripheral
'standby' - Put playing device on standby via a CEC peripheral
'toggle' - Toggle state of playing device via a CEC peripheral
'stop_and_standby' - Stop any playback and place the CEC peripheral on standby

Example JSON request:

http://localhost:8080/jsonrpc?request={"jsonrpc":"2.0","method":"Addons.ExecuteAddon","params":{"addonid":"script.json-cec","params":{"command":"activate"}},"id":1}

Installation

Method Zip

Download the project as Zip and rename it as script.json-cec.zip. Use the GUI interface to install it in Kodi.

Method Copying

Clone the project and copy it to Kodi's addons directory, example: ~/.kodi/addons/
