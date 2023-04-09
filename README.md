# Multipurpose GUI / Datalogger
GUI created to visualize and save incoming data from sensors connected to an arduino using serial communication.

![demo](https://i.imgur.com/FzNQVxr.gif)

## Capabilities
- Realtime plotting every 500 ms.
- Visualization of last 7.5 seconds of data.
- Data saving for up to 8 graphs at the same time.
- Test mode with data saving capabilites.
- Automatic Arduino detection.


# How to install
To install required packages run the code below on cmd inside 'GUI-Datalogger_Python' folder.
```bash
pip install -r requirements.txt
```

# How does it work?
## Communication
Software should automatically detect COM port when an Arduino is connected to the computer (**software needs to be restarted**). There's a manual way to select COM port inside `serialcomm.py` file. 

If the software doesn't detect an Arduino, test mode will start. Test mode status can be seen above `Start` and `Stop` buttons.

Incoming Arduino data needs to have a `baudrate` of 9600 and needs to be printed as a string with the following structure.
```c++
humidity, temperature, pressure, altitude, verticalaccel, magneticfield, otherdata1, otherdata2
```
Data plotting is made every 500 ms on the `main.py` file so incoming serial data doesn't need any timer for printing data.

## Data saving
To begin data saving just click the `Start` button, you can see elapsed time on the timer above the buttons, to stop data saving click `Stop`. 

Data will be saved on one or more csv files located on the `saves` folder, this depends on how many graphs you want to save data from. **Needs to be changed from code, default = 8**


# Known bugs/problems
- Graphs position and size changes when hidden and shown multiple times.


# More info
Check out this [GUI project](https://github.com/el-NASA/CanSat-Ground-station) from Daniel Rodriguez which was very useful to developing our own.