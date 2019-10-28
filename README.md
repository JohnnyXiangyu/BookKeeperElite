# BookKeeperElite
 Localhost application that keeps records of user-specified schema, with htlml GUI.  

# Implementation
 Using OneDrive server to sync SQLite files, therefore implement a private web database.  
 At bottom level: database toolset, configuration toolset, html templates  
 Higher level: web.py server, user interface logics  

# Architecture
 User interface: html page hosted by webpy  
 Database: SQLite  
 Web strage hosting: Microsoft OneDrive  
   
 It would work like a localhost webserver, providing webpage(s) to manipulate and display the content in a local SQL file stored in a user defined location.  
   
 init.py: driver code  
 Toolsets:  
 modules/book.py: database toolset  
    * mkLib(): create a new db file  
    * mkBook(): create a new table in given database  
    * addPage(): add a line of data in database, with specified format  
    * rmPage(): remove a line of data, not a UI function  
    * rmBook(): remove a book  
 modules/utils/configure.py: configuration toolset and storage  
     getMonday(): load startup configurations, including path to db file  
     reloadMonday(): reload startup configurations, in case future features modify Monday.json in running  
     updataTuesday(): modify metadata about database schemas (might be removed since SQLite files contain metadata)  

# Log  
 10/27 organized existing functions and README  
 10/27 implemented getTuesdayNames(), tuesday file is removed from file structure  
 10/27 implemented getTuesdaySchema() and mkPage(), the later depends on the other * this feature is not tested  
