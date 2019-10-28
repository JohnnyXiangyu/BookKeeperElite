import sqlite3
import os
try:
    import modules.utils.configure as configs
except ModuleNotFoundError:
    import utils.configure as configs


# some terminologies
# book: collection of a sort of data
# page: an item in book


def mkLib(lib_name):
    '''
    Add a sqlite file in configured path
    '''
    filename = configs.getMonday('db_location') + lib_name
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


def rmLib(lib_name):
    '''
    Remove the specified db file.
    '''
    # TODO: make an identity check module here, don't let libs be easily deleted
    return 0


def mkBook(lib_name, book_name, schema, comment="no comment"):
    '''
    A function used to create a new table in database, with name and schema defined in the args
    Intersion_time will be prepended to the schema, so don't include it in argument
    '''
    # generate a sqlite command
    command = 'CREATE TABLE IF NOT EXISTS ' + \
        book_name + '(ID INT PRIMARY KEY AUTOINCREMENT, INSERT_TIME INT NOT NULL'
    items = {}
    for key, value in schema.items():
        items.update({key: value})
        command += ', ' + key + ' ' + value
    command += ');'

    # commit the command
    filename = configs.getMonday('db_location') + lib_name
    try:
        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        cur.execute(command)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

    # debug: show the updated list of tables
    current_books = configs.getTuesdayNames()
    debug_message = 'Updated list:'
    for name in current_books:
        debug_message += ' ' + name
    print(debug_message)


def rmBook(lib_name, book_name):
    '''
    Remove a book
    '''
    # TODO: add identity check for each table to be dropped
    command = 'DROP TABLE IF EXISTS ' + book_name + ';'
    # execute
    filename = configs.getMonday('db_location') + lib_name
    try:
        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        cur.execute(command)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return 0


def mkPage(lib_name='testbook.db', book_name='dummy2', contents = {}):
    '''
    Add the content dict into given book name
    contents argument should be dict containing key:value pairs, any field not specified will be null
    Should have error checking regarding recorded book names
    '''
    # TODO: this function is not debugged
    
    # load schema of book
    schema = configs.getTuesdaySchema(lib_name, book_name)

    # build command
    command = 'INSERT INTO ' + book_name + ' [(INSERT_TIME'
    values = []
    # add field names
    for field in schema:
        try:
            values.append(contents[field])
            command += ', ' + field
        except KeyError:
            # if this field is not given, let SQLite set it to null
            pass
    command += ')] VALUES ('
    # add field values
    # TODO: add timestamp
    for value in values:
        command += value + ', '
    command += ');'

    # execute
    filename = configs.getMonday('db_location') + lib_name
    try:
        conn = sqlite3.connect(filename)
        cur = conn.cursor()
        cur.execute(command)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return 0


def rmPage(page_id):
    '''
    Remove a page
    Arg should be dict containing enough data to identify a page
    '''

    return 0
