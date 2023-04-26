# bayes-filter

TODO: All these instructions use COM port language and assume Windows as the operating system. Should make it more general or include language about Macs as well.
TODO @Kaanthi: Can you add brief instructions for how they would recalibrate the system or add another state?

A real-time state estimation algorithm implemented in Python for determining patient activity level from a continuous stream of x,y,z acceleration data.

This code requires an installation of Python 3.6.8, available [here](https://www.python.org/). The following supplementary libraries are also required:
- [matplotlib](https://matplotlib.org/stable/users/installing/index.html)
- [numpy](https://numpy.org/install/)
- [scipy](https://scipy.org/install/)
- [pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [pyserial](https://pypi.org/project/pyserial/)
- [termcolor](https://pypi.org/project/termcolor/)
The team recommends installing these libraries through pip, though Anaconda should also work.

To run the code, first connect the receiver board to the computer using a USB cable. The receiver will open a serial interface on the COM port it is plugged into.
The code assumes the receiver is connected to COM5, so if using a different COM port is necessary, modify line 39 of main.py to match the open COM port listed
in your computer's Device Manager.

Once the receiver is connected to the computer, turn on the transmitter PCB and run main.py.
The serial console should begin printing out the estimated patient activity state and the patient step count since the transmitter was turned on.

## main.py
Run this while the receiver is connected and receiving acceleration data to produce live predictions of patient activity state.

If no output is observed when running main.py, check the following things:
- Your current installation of Python is 3.6.8 or later, and all necessary libraries are installed
- The receiver board and transmitter PCB have the correct firmware uploaded for transmitting and receiving accelerometer and step data 
- The receiver is connected to the same COM port as listed on line 39 of main.py, COM5 by default. (Open Device Manager to see the current COM port)
- The transmitter is turned on, and if running on battery power that the battery is fully charged (3V)
- The transmitter is close to the receiver and line of sight is not obstructed by any conductive objects

If the code is still not working, try running serial_test.py or pointing a serial monitor at the receiver COM port at 115200 baud while the transmitter is broadcasting, 
and check if the receiver is outputting four comma-separated numbers corresponding to x, y, z acceleration and step count. If the receivier is not sending out that 
data, try turning it off and on, and serial data should start to appear as desired.

## realtimeBayes.py
The core loop for the real-time state estimator, implementing a statistical Bayes filter. This should be called by main.py during standard operation.

## PDFs.py
Functions for producing plots of observed or calibrated probability density functions (PDFs) associated with each patient activity state.

## constants.py
State transition matrix constants associated with the Bayes filter. These constants are determined through experiment and collected calibration data.

## serial_test.py
Prints out data received from the receiver over the serial interface.
Run this script if trying to debug the system and determine if the receiver and transmitter are properly connected.

By default, this script tries to open a serial connection on COM5 at 115200 baud. If connecting to a different COM port, modify line 4.

## A_Jog.csv
Calibration data for the jogging state.

## B_Walk.csv
Calibration data for the walking state.

## C_Sit.csv
Calibration data for the sitting state.
