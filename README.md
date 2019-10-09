# BookKeeperElite
 A local "web" tool to keep track of sorted data and capable of customizable algorithms. Designed for single user application  

# Implementation
 Using OneDrive server to sync SQLite files, therefore implement a private web database. Besides web server, another important feature would be file parsing. For now I'll try to write defination of grammar for this tool into a single json file so user can customize their grammar.  
 This tool is inspired by the need of a dictionary form class note, which can be not efficient in OneNote.  

# Architecture
 User interface: html page run by webpy  
 Database: SQLite  
 Web hosting: Microsoft OneDrive  
   
 It would work like a localhost webserver, providing webpage(s) to manipulate and display the content in a local SQL file stored in a user defined location.  
