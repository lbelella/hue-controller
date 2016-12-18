# hue-controller
Qt application for controlling Hue lights using the phue library.

Currently the application will only:
- Connect to the Hue Bridge
- Grab all of the lights from the Bridge by name
- Create a list of buttons with the light names
- Clicking a button will toggle the on/off state of the light

## Requirements
- phue
- pyqt4
