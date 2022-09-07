# Cocke Hall Reservation Bot
Automatic RSVP for Cocke Hall weight room. Multi-user support with automatic scripting through crontab. Requires implementation of slot when first assigned. Running on Raspberry Pi Zero and utilizing Selenium (Python)


### _Version History_
    1.0 - Automatic Sign-up for a set user and specific gym slot
    
    1.1 - Allows input to detect which user to run script for. 
          Supports multiple manually inputted gym slots.
          
    1.11- Fixed command prompt input issues
    
    1.2 - Support for Raspberry Pi (Rasbian OS)
    
    1.3 - Offset value to automatically adjust event id's
    	- Offset value determined through CHOffset.py
    	- Fully automatic

### _Windows Task Scheduler Settings_
    - Ensure running from user's account
    - Run with highest privilege 
    - Allow if user is logged in or not
    - Enable History
    - Windows 10 Server
    - Trigger with delay 0-2 seconds
    - All Batch Files located in: C:\Users\Samuel\Documents\CockeBots
    - Task Scheduler Script Files located in: C:\Windows\System32\Tasks
