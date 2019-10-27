# BookKeeperElite
 A local "web" tool to keep track of sorted data and capable of customizable algorithms. Designed for single user application  

# Implementation
 Using OneDrive server to sync SQLite files, therefore implement a private web database. Besides web server, another important feature would be file parsing. For now I'll try to write defination of grammar for this tool into a single json file so user can customize their grammar.  
 This tool is inspired by the need of a dictionary form class note, which can be not efficient in OneNote.  

# Architecture
 User interface: html page hosted by webpy  
 Database: SQLite  
 Web strage hosting: Microsoft OneDrive  
   
 It would work like a localhost webserver, providing webpage(s) to manipulate and display the content in a local SQL file stored in a user defined location.  
   
 init.py: driver code  
 modules/book.py: database toolset  
     mkLib(): create a new db file  
     mkBook(): create a new table in given database  
     addPage(): add a line of data in database, with specified format  
     rmPage(): remove a line of data, not a UI function  
     rmBook(): remove a book  
 modules/utils/configure.py: configuration toolset and storage  
     getMonday(): load startup configurations, including path to db file  
     reloadMonday(): reload startup configurations, in case future features modify Monday.json in running  
     updataTuesday(): modify metadata about database schemas (might be removed since SQLite files contain metadata)  

# Log  
