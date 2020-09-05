# silent-work-logger
A silent and simple program for logging the time spent working on a project

### How to Use

Compile .cpp file using C++ compiler of choice. Run .exe file to start logging, and press enter to stop logger.

Run 'python analyser.py' to get information about the data collected. Currently displays time spent daily (as opposed to the recorded time spent per session)

### WORK IN PROGRESS: ANALYSIS

analysis.py is a separate file for executing and viewing analysis of data recorded by silent-work-logger. Currently under development.

### Philosophy

Having a discrete and subtle timer running in the background, that does not display how long you have worked at all times, may remove some of the performance anxiety and workaholic tendencies whilst still allowing for a tracking of past performance. This is a minimalist solution to this problem.

### Future Development

I intend to integrate the base logger with a data storage system in order to save the logged work sessions automatically, as well as functions to display a variety of statistics.
It is my intention that these statistics are hidden from the user and may only be checked at certain specific times to further remove anxiety and discourage a too frequent use.
For example, the statistics may only be accessed on monday mornings between certain times.
