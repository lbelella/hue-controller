# hue-controller
Qt application for controlling Hue lights using the phue library.

Currently the application will only:
- Connect to the Hue Bridge
- Grab all of the lights from the Bridge by name
- Create a list of buttons with the light names
- Clicking a button will toggle the on/off state of the light

## Requirements
- phue (https://github.com/studioimaginaire/phue)
- pyqt4

## To-Do
The todo list is obviously quite large at this point but some of the stuff to add would be:
- Control hue and saturation of each light
- Scheduling
- Too many other things to list right now

##Acknowledgments

Thanks to [Nathanaël Lécaudé](https://github.com/natcl) and https://github.com/studioimaginaire for the phue library!

##License

MIT - http://opensource.org/licenses/MIT

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips Electronics N.V., see www.meethue.com for more information.
I am in no way affiliated with the Philips organization.
