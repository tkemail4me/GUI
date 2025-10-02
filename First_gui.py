'''
First PyQt5 (PySide5) app

Created by Phil J Sept 25

Note - no apparent distro for PySide 6 via pip - so cant install to use with Thonny, yet.

This will also run with Win11, assuming the PyQt5 lib files are installed with Thonny

resource - raspberrytips.com/pyqt-on-raspberry-pi

*****
      To begin run this script as is - after running the code, add comments to these
      uncommented lines (not the from or import), describing what happens
      
      Upload the completed code with comments to your github, provide the url in the DC Connect assignment box
*****
'''

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys



app = QApplication([])   # Opens GUI
win = QMainWindow()      # Places GUI in main window

#Now Uncomment this 2nd section and test - state what each line does with comments
win.setWindowTitle("A windows thing") # Adds a title to the top of the GUI
win.resize(500, 500) # Resizes the GUI window (made it larger)
win.move(400,200) # Moves the window


#Now uncomment this 3rd section and test - state what each line does with comments in these lines
label = QLabel("Some text", win) # Adds "Some text" to the top left corner of the GUI
label.move(50, 100) # Moves text down and to the right

#Now uncomment the 4th section and test - state what each line does with comments in these lines
def clickMethod():
    print("Button clicked")
 
button = QPushButton("Click here", win) # Creates a graphic button to be pushed (top left corner)
button.move(20,40) # Moves button down and to the right
button.clicked.connect(clickMethod) # Calls the function "clickMethod" which prints "Button clicked".


win.show()

sys.exit(app.exec_())

