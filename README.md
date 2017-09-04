# hue-controller
Qt application for controlling Hue lights using the phue library.

Currently the application will:
- Connect to the Hue Bridge
- Grab all of the lights from the Bridge by name
- Create a list of HueWidget objects and display them in a vertical layout
- Clicking a button will toggle the on/off state of the light
- Create 3 horizontal sliders in this order: hue, brightness and saturation

## Requirements
- Python 3
- phue (https://github.com/studioimaginaire/phue)
- pyqt4

## Known Issues
- The application expects that the inital setup with the phue library and the bridge has already been completed.
- The application only handles lights that have the colorspace set to 'hs'.

## To-Do
The todo list is obviously quite large at this point but some of the stuff to add would be:
- Implement config file
- Configurable Bridge IP address
- Initial Bridge setup (pressing the button on the Bridge)
- Scheduling
- Handle 'ct' and 'xy' colorspaces

## Acknowledgments

Thanks to [Nathanaël Lécaudé](https://github.com/natcl) and https://github.com/studioimaginaire for the phue library!

## License

MIT - http://opensource.org/licenses/MIT

"Hue Personal Wireless Lighting" is a trademark owned by Koninklijke Philips Electronics N.V., see www.meethue.com for more information.
I am in no way affiliated with the Philips organization.
