
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

        entry['day'] = int(date[2])

        # duration is divided first by h,
        duration = point['duration'].split('h')

        entry['hours'] = int(duration[0])

        # then by m,

        duration = duration[1].split('m')

        entry['minutes'] = int(duration[0])

        # and lastly the 's' is removed

        entry['seconds'] = int(duration[1][:-1])

        new_data.append(entry)

    return new_data

#TODO:


# ANALYSIS FUNCTIONS
def per_day_totals(data):
    pass

def per_month_totals(data):
    pass

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



#start of program
def analyze():

    data = read_log()
    data = convert_to_numerical(data)


