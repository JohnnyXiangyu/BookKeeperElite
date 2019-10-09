import sqlite3

def addLib(lib_name):
    '''
    Add a sqlite file in configured path
    '''
    return 0

def mkBook(book_name, schema):
    '''
    A function used to create a new table in database, with name and schema defined in the args
    Book name should be also stored in a configure file
    '''
    command = 'CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (column_1 data_type PRIMARY KEY,column_2 data_type NOT NULL,column_3 data_type DEFAULT 0,table_constraints) [WITHOUT ROWID];'
    return 0

def addPage(book_name, contents):
    '''
    Add the content dict into given book name
    Should have error checking regarding recorded book names
    '''
    return 0


# DANGER ZONE
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