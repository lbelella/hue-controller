#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import sys
from phue import Bridge

class HueController():
    """
    Small wrapper class around the phue Bridge object.
    """
    def __init__(self):
        self.bridge = Bridge('192.168.2.102')
        self.bridge.connect()
        self.lights = self.bridge.get_light_objects()
        
class HueWidget(QtGui.QWidget):
    def __init__(self, light):
        super(HueWidget, self).__init__()
        
        print(light.name + " " + light.colormode)
        
        self.light = light
        self.displayName = light.name
        
        self.initUi()
    
    def initUi(self):
        # Layout our controls horizontally
        self.layout = QtGui.QHBoxLayout()
        self.layout.addStretch(1)
        
        # On/Off Toggle Button
        self.btnOnOff = QtGui.QPushButton(self.displayName)
        self.btnOnOff.setMinimumSize(200, 1)
        self.btnOnOff.clicked.connect(lambda: self.toggleLight())
        
        # Color slider
        self.sldColor = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sldColor.setMinimumSize(200, 1)
        self.sldColor.setTracking(False)
        self.sldColor.setMinimum(0)
        self.sldColor.setMaximum(65535)
        self.sldColor.setValue(self.light.hue)
        self.sldColor.valueChanged.connect(lambda: self.setColor(self.sldColor.value()))
        
        # Brightness slider
        self.sldBrightness = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sldColor.setMinimumSize(200, 1)
        self.sldBrightness.setTracking(False)
        self.sldBrightness.setMinimum(0)
        self.sldBrightness.setMaximum(254)
        self.sldBrightness.setValue(self.light.brightness)
        self.sldBrightness.valueChanged.connect(lambda: self.setBrightness(self.sldBrightness.value()))
        
        # Saturation slider
        self.sldSat = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.sldColor.setMinimumSize(200, 1)
        self.sldSat.setTracking(False)
        self.sldSat.setMinimum(0)
        self.sldSat.setMaximum(254)
        self.sldSat.setValue(self.light.saturation)
        self.sldSat.valueChanged.connect(lambda: self.setSaturation(self.sldSat.value()))
        
        # Add the controls to the horizontal layout
        self.layout.addWidget(self.btnOnOff)
        self.layout.addWidget(self.sldColor)
        self.layout.addWidget(self.sldBrightness)
        self.layout.addWidget(self.sldSat)
        
        # Set the layout for the widget to the horizontal layout
        self.setLayout(self.layout)
    
    def setSaturation(self, sat):
        self.light.on = True
        self.light.saturation = sat
        
    def setColor(self, color):
        self.light.on = True
        self.light.hue = color
        
    def setBrightness(self, brightness):
        """
        Turns on the light and sets the brightness to the value
        that was passed in.
        """
        self.light.on = True
        self.light.brightness = brightness
        
    def toggleLight(self):
        """
        Toggles the on/off state of the light that was passed into us.
        """
        if self.light.on == True:
            self.light.on = False
        else:
            self.light.on = True
        return
        
class HueControlApp(QtGui.QMainWindow):
    def __init__(self, hc):
        super(self.__class__, self).__init__()
        
        # Store the HueController object
        self.hc = hc
        
        # Create buttons and some other Qt stuff
        self.init_ui()
        
        # Set the window title
        self.setWindowTitle("Hue Control App")
        
    def init_ui(self):
        
        # Create the vertical layout
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addStretch(1)
        
        # Create a list of widgets using each light on the bridge
        widgets = [HueWidget(l) for l in self.hc.lights]

        # Add each widget to the main layout
        for w in widgets:
            self.mainLayout.addWidget(w)
        
        # Central widget
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # Set central widget
        self.setCentralWidget(self.centralWidget)
        
def main():
    app = QtGui.QApplication(sys.argv)
    hc = HueController()
    form = HueControlApp(hc)
    form.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
