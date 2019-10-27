import sqlite3
import os
try:
    from utils.configure import updateTuesday
except ModuleNotFoundError:
    from modules.utils.configure import updateTuesday

# some terminologies
# book: collection of a sort of data
# page: an item in book


def mkLib(lib_name):
    '''
    Add a sqlite file in configured path
    Should not be explictly called
    Should never be called
    '''
    filename = os.getcwd() + '\\books\\' + lib_name
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return 0


def mkBook(lib_name, book_name, schema, comment="no comment"):
    '''
    A function used to create a new table in database, with name and schema defined in the args
    Book name and structure should be also stored in a configuration file
    Insertion time is mandatory field
    '''
    # generate a sqlite command
    command = 'CREATE TABLE IF NOT EXISTS ' + \
        book_name + '(INSERTION_TIME INT PRIMARY KEY NOT NULL'
    items = {}
    for key, value in schema.items():
        items.update({key: value})
        command += ', ' + key + ' ' + value
    command += ');'

    # commit the command
    filename = os.getcwd() + '\\books\\' + lib_name
    conn = sqlite3.connect(filename)
    cur = conn.cursor()
    cur.execute(command)
    conn.close()

    # create a record in tuesday configuration
    newbook = {
        "name": book_name,
        "description": comment,
        "items": items
    }
    newbook = {book_name: newbook}
    updateTuesday(newbook)


def addPage(book_name, contents):
    '''
    Add the content dict into given book name
    Should have error checking regarding recorded book names
    '''

    return 0


# DANGER ZONE
# not implemented


def rmPage(page_id):
    '''
    Remove a page
    Arg should be dict containing enough data to identify a page
    '''
    return 0


def rmBook():
    '''
    Remove a book
    '''
    return 0
