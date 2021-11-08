# CockeBot
Automatic RSVP for Cocke Hall weight room. Multi-user support with automatic scripting through crontab. Requires implementation of slot when first assigned. Running on Raspberry Pi Zero

'''
    ***VERSION HISTORY***
    1.0 - Automatic Sign-up for a set user and specific gym slot
    1.1 - Allows input to detect which user to run script for. 
          Supports multiple manually inputted gym slots.
    1.11- Fixed command prompt input issues
    1.2 - Support for Raspberry Pi (Rasbian OS)
    1.3 - Offset value to automatically adjust event id's
	- Offset value determined through CHOffset.py
	- Fully automatic
'''

'''
    ***Windows Task Scheduler Settings***
    - Ensure running from user's account
    - Run with highest privilege 
    - Allow if user is logged in or not
    - Enable History
    - Windows 10 Server
    - Trigger with delay 0-2 seconds
    - All Batch Files located in: C:\Users\Samuel\Documents\CockeBots
    - Task Scheduler Script Files located in: C:\Windows\System32\Tasks
'''

''' 
    ***GOALS***
    - Add reminder system
    - Clean up multi-user support (utilize arrays/vectors)
'''

'''
    ***SLOT TRACKER***
    
    Sam:
        1300 Monday
        1300 Wednesday
        1300 Friday
        1300 Saturday
    Ethan:
        1300 Monday
    Riley:
        2000 Monday
        2000 Tuesday
        2000 Wednesday
        2000 Thursday
        2000 Friday
    Zach: 
        1800 Monday
        1800 Friday
    
'''

'''
    ***NOTES***
    driver.page.source
    driver.get("https://USERNAME:PASSWORD@www3.vmi.edu/cocke-hall/")
    driver.close -> for tab
    driver.quit() -> for browser
    driver.title -> title of page
    sudo crontab -e -> edit auto scripts on Pi
    crontab -l > backup_date.text to backup file
    crontab crontab.bak to import from backup

    git init #new directory
    git add <folder1> <folder2> <etc.>
    git commit -m "Your message about the commit"
    git remote add origin https://github.com/primetime728/CockeBot.git
    git push -u origin master
    git push origin master

    cd Documents
    git add CockeBots
    git commit -m "Latest Update"
    git push orgin master
'''

