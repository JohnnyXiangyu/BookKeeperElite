import json
import os
import sqlite3
import re

# some terminologies
# monday: startup configurations
# tuesday: mata data about database structure, not a file


# open and read monday file, and close it
monday_file = open(os.getcwd() + "\\configs\\monday.json")
monday_config = json.load(monday_file)
monday_file.close()


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
    monday_file.close()


def getTuesdayNames(lib_name='testbook.db'):
    '''
    Returns a list of names of tables in the given database
    '''
    # generate a sqlite command
    command = "SELECT name FROM sqlite_master WHERE type='table'"

    # commit the command
    filename = os.getcwd() + '\\books\\' + lib_name
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute(command)

    # construct result list
    namelist = []
    for name in cur.fetchall()[0]:
        namelist.append(name)
    conn.close()
    return namelist


# updateTuesday() is removed


def getTuesdaySchema(lib_name='testbook.db', book_name='dummy2'):
    command = "SELECT sql FROM sqlite_master WHERE type='table'"

    # commit the command
    filename = os.getcwd() + '\\books\\' + lib_name
    print(getMonday('db_location') + lib_name)
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute(command)
    resultlist = cur.fetchall()[0][0]
    if conn:
        conn.close()

    # parse result for a list of just column names (I reused the variable name)
    schema = re.findall(', [^ ]+ ', resultlist)
    resultlist = []
    for column in schema:
        temp_name = ''
        for char in column:
            if char != ',' and char != ' ':
                temp_name += char
        resultlist.append(temp_name)

    return resultlist
