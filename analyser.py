import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import DateFormatter

FILE_NAME = "log.txt"

# Returns a list of dictionaries with date and duration as strings
def read_log():

    with open(FILE_NAME, 'r') as log_file:

       lines = log_file.readlines()
       data = []

       for line in lines:

           # create a dictionary as entry in list of data
           entry = {'date': '', 'duration': ''}

           # date and duration are separated by colon
           entry_as_list = line.split(':')

           # strip the strings of any newline characters and blank spaces
           entry['date'] = entry_as_list[0].strip()
           entry['duration'] = entry_as_list[1].strip()

           data.append(entry)

    return data

#decode the string values into numerical representations of time
def convert_to_numerical(data):

    new_data = []

    for point in data:

        # dictionary with more detailed numerical information
        entry = {'year': 0, 'month': 0, 'day': 0, 'hours': 0, 'minutes': 0, 'seconds': 0, 'date': point['date'], 'duration': point['duration']}

        # date is split in three parts by forward slashes
        date = point['date'].split('/')

        entry['day'] = int(date[0])

        entry['month'] = int(date[1])

        entry['year'] = int(date[2])

        # duration is divided first by h,
        duration = point['duration'].split('h')

        entry['hours'] = int(duration[0])

        # then by m,

        duration = duration[1].split('m')

        entry['minutes'] = int(duration[0])

        # and lastly the 's' is removed

        entry['seconds'] = int(duration[1][:-1])

        entry['duration'] = entry['hours'] * 60 + entry['minutes']

        new_data.append(entry)

    return new_data

#TODO:

#dictionary structure:
# for every entry, 'day' 'month' 'year', 'hours', 'minutes'

# ANALYSIS FUNCTIONS
def per_day_totals(data):

    per_day_data = []

    # iterate over the given data
    for old_entry in data:

        # switch variable triggered to false if date already exists in output list
        add = True

        # iterate over output list, checking if date matches existing date
        for entry in per_day_data:

            # date matching
            if old_entry['date'] == entry['date']:

                # trigger switch
                add = False

                # perform addition of times using modulo 60 to carry over minutes to hours
                # we discard seconds for now, later iterations may also carry over seconds
                sum_minutes = old_entry['minutes'] + entry['minutes']

                carry_hour = sum_minutes // 60

                remaining_min = sum_minutes % 60

                # record new duration (keep in mind that 'duration' key will now be useless...)
                entry['hours'] = old_entry['hours'] + carry_hour

                entry['minutes'] = remaining_min

                entry['duration'] = entry['hours'] * 60 + entry['minutes']

        # date has yet to be added to list, add to output list
        if add:
            per_day_data.append(old_entry)

    return per_day_data


def per_month_totals(data):

    per_month_data = []

    # iterate over the given data
    for old_entry in data:

        # switch variable triggered to false if month already exists in output list
        add = True

        # iterate over output list, checking if month matches existing month
        for entry in per_day_data:

            # month matching
            if old_entry['month'] == entry['month']:

                # trigger switch
                add = False

                # perform addition of times using modulo 60 to carry over minutes to hours
                # we discard seconds for now, later iterations may also carry over seconds
                sum_minutes = old_entry['minutes'] + entry['minutes']

                carry_hour = sum_minutes // 60

                remaining_min = sum_minutes % 60

                # record new duration (keep in mind that 'duration' key will now be useless...)
                entry['hours'] = old_entry['hours'] + carry_hour

                entry['minutes'] = remaining_min

                entry['duration'] = entry['hours'] * 60 + entry['minutes']

        # date has yet to be added to list, add to output list
        if add:
            per_month_data.append(old_entry)

    return per_month_data

def seven_day_average(data):
    pass

def monthly_average(data):
    pass

# TIME VALIDATION FUNCTIONS

# create constants for allowed hours of checking analysis

def get_current_weekday():
    pass

def get_current_time():
    pass

def validate_usage():
    pass

# PRINTING FUNCTIONS

def convert_to_datetime(data):
    for entry in data:
        entry["date"] = datetime.date(int(entry["year"]), int(entry["month"]), int(entry["day"]))
    return data

def show_graph(data, xfield, yfield):
    x = []
    y = []
    for entry in data:
        x.append(entry[xfield])
        y.append(entry[yfield])

    x = np.array(x)
    y = np.array(y)
    if xfield == "date":
        fig, ax = plt.subplots()
        formatter = DateFormatter('%d-%m-%y')
        plt.plot_date(x, y)
        ax.xaxis.set_major_formatter(formatter)
    else:
        plt.plot(x, y)
    plt.xlabel(xfield)
    plt.ylabel(yfield)
    plt.show()

def print_stats(data):
    for entry in data:
        print(entry['date'] + ": " + str(entry['hours']) + "h" + str(entry['minutes']) + "m")


#start of program
def analyze():

    # read data from file
    data = read_log()

    # decode strings to get dates and durations in integer values
    data = convert_to_numerical(data)

    # get data summed in days
    per_day_data = per_day_totals(data)

    # testing
    print_stats(per_day_data)

    # print per day data
    show_graph(convert_to_datetime(per_day_data), "date", "duration")

analyze()



