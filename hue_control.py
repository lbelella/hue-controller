#!/usr/bin/python
from PyQt4 import QtGui
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
        
        # Create a list of buttons using each light on the bridge
        buttons = [QtGui.QPushButton(l.name) for l in self.hc.lights]
        
        # Wire up the click handler and add to main layout
        for b in buttons:
            b.clicked.connect(lambda a, b=b: self.toggle_light(b.text()))
            self.mainLayout.addWidget(b)
        
        # Central widget
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        # Set central widget
        self.setCentralWidget(self.centralWidget)
            
    def toggle_light(self, name):
        """
        Toggles the on/off state of the light identified by name.
        Since the light buttons were created using the light names
        directly from the bridge this should be OK.
        """
        light = self.hc.bridge[name]
        if light.on == True:
            light.on = False
        else:
            light.on = True
        return
        
def main():
    app = QtGui.QApplication(sys.argv)
    hc = HueController()
    form = HueControlApp(hc)
    form.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
