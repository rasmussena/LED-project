Arduino LED Scrolling Message Board

This project allows you to create and control a scrolling LED message display using an Arduino and Python-based GUI. It uses the MD_Parola and MD_MAX72xx libraries for Arduino to control an LED matrix and a Python interface to input custom text messages.

Features:
-Scrolling text messages displayed on an LED matrix.
-Adjustable scrolling speed, direction, and pause settings.
-Input messages via a Python-based GUI using the PySimpleGUI library.
-Messages are sent from the GUI to the Arduino via a serial connection.

Requirements:
Hardware
-Arduino board (e.g., Uno, Mega, etc.).
-LED matrix with FC-16 hardware (configured for up to 11 devices).
-Potentiometer and switches for adjusting display settings (optional).
Software
-Arduino IDE with the following libraries:
  MD_Parola
  MD_MAX72xx
-Python 3.x with the following packages:
  PySimpleGUI
  pyserial

How It Works:
  Arduino Code:

The Arduino listens for text messages sent via the serial connection.
Displays the received text on an LED matrix as a scrolling message.
The scrolling speed and direction can be controlled through physical inputs (optional).

  Python GUI:

Provides an easy-to-use interface to input up to 6 phrases.
Sends the inputted text to the Arduino via a serial connection.

Setup and Installation:

1. Hardware Setup
Connect the LED matrix to the Arduino as follows:
CLK_PIN -> Pin 13
DATA_PIN -> Pin 11
CS_PIN -> Pin 10
(Optional) Connect a potentiometer and switches to control scrolling speed and direction.

2. Software Setup
Arduino Code:
  Install the required Arduino libraries:
  Open Arduino IDE.
  Go to Sketch > Include Library > Manage Libraries.
  Search for MD_Parola and MD_MAX72xx, then install them.
  Upload the provided Arduino code to your Arduino board.
Python Code:
  Install Python 3.x from the official site.
  Install the required Python libraries:

  pip install PySimpleGUI pyserial
Run the Python script:

python your_script_name.py

Usage:
  Connect the Arduino to your computer via USB.
  Ensure the correct serial port is set in the Python code (e.g., COM5).
  Run the Python GUI application.
  Enter your desired phrases into the input fields and click Submit.
  The Arduino will display the submitted phrases as a scrolling message.

Example GUI:
  The GUI allows users to input multiple phrases:

  Enter your messages into the input fields labeled Phrase 1 through Phrase 6.
  Click Submit to send the first message to the Arduino.
  Additional messages can be added and sent similarly.

Known Limitations:
  The current implementation only sends one phrase at a time to the Arduino. Additional functionality could be added to handle multiple phrases dynamically.
  Ensure the COM port is correctly configured in the Python script.

Future Improvements:
  Enable sending multiple phrases sequentially to the Arduino.
  Add controls for scrolling speed, direction, and pause settings within the GUI.
  Implement error handling for serial communication.
  Expand support for larger LED matrix displays.
References:
MD_Parola Library Documentation
MD_MAX72xx Library Documentation
PySimpleGUI Documentation
