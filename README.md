# Multipurpose GUI / Datalogger
GUI created to visualize testbench incoming data using arduino and serial ports. Future developing will be centered in the capacity to visualize telemetry data from rockets.

# How to install
To install required packages run the code below on cmd inside 'GUI-Datalogger_Multipurpose' folder.
```bash
pip install -r dependencies.txt
```

# How does it work?
## Communication
As there are 4 graphs at the moment incoming data from serial port needs to have the structure below.
```c++
[LoadCell_Data, Free_Data, Free_Data, Free_Data]
```
`Free_Data` can be whatever kind of data you want to visualize that is coming from arduino.

## Data saving
At the moment you can save data from every graph but not at the same time.

# Known bugs/problems
- Low performance
- Data saving only possible on one graph at a time. / WIP

# More info
Check out this [GUI project](https://github.com/el-NASA/CanSat-Ground-station) from Daniel Rodriguez which was very useful to developing our own.