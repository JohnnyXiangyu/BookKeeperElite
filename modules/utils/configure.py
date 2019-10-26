import json
import os

# some terminologies
# monday: startup configurations
# tuesday: data about database structure


monday_file = open(os.getcwd() + "\\configs\\monday.json")
monday_config = json.load(monday_file)


def getMonday(config_key):
    '''
    Get the Monday configurations
    '''
    return monday_config[config_key]


def reloadMonday():
    '''
    Just in case the files can be legally changed one day, reload configuration file.
    '''
    global monday_file, monday_config
    monday_file = open(os.getcwd() + "\\configs\\monday.josn")
    monday_config = json.load(monday_file)


def getTuesdayNames():
    '''
    Get book names from Tuesday configuration
    '''
    # TODO: start
    return 0


def updateTuesday(new_book):
    '''
    This should be the only interface tuesday.json get modified.
    It'll read teusday into a dict and update tuesday["books"] section. 
    Then it'll override the file.
    '''
    # process added data
    tuesday_file = open(os.getcwd() + "\\configs\\tuesday.json")
    tuesday_dict = json.load(tuesday_file)
    tuesday_file.close()
    tuesday_dict["books"].update(new_book)

    # update the file
    tuesday_file = open(os.getcwd() + "\\configs\\tuesday.json", 'w')
    json.dump(tuesday_dict, tuesday_file, indent=4)

    return 0
