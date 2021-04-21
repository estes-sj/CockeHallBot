'''
    File name: CockeHallReservation.py
    File Version: 1.11
    Author: Samuel Estes
    Date created: 3/10/2021
    Date last modified: 3/26/2021
    Python Version: 2020.3.4

    Automatic Sign-Up for Cocke Hall Reservation System.
    New Features: Supports multiple slots and users.

    Current Loaded Slots: 3/26: 3/29-4/3
'''
import sys

from datetime import datetime
from selenium import webdriver

# datetime object containing current date and time
now = datetime.now()
print("starting at...", now)

# Automated User Detection
print("Active User:")
user = input()
       
def main():

    # Location of Google Chrome Driver
    PATH = "/usr/lib/chromium-browser/chromedriver"

    driver = webdriver.Chrome(PATH)
    driver.maximize_window()

    # Continue running only if user has an assigned slot
    try:
        web_site = user_day_detection(user)
        login_site = web_site[:8] + login_credentials() + web_site[8:]
        driver.get(login_site)  # Load page with login credentials
    except BaseException:
        print("No Slot Established!\nTerminating Program...")
        sys.exit()

    main_page = driver.current_window_handle

    # Allow Page to Load
    driver.implicitly_wait(5)  # Seconds

    driver.switch_to.frame("trumba.spud.0.iframe")

    element = driver.find_element_by_link_text("Sign Up").click()

    # Changing the handles to access login page
    for handle in driver.window_handles:
        if handle != main_page:
            signup_page = handle

    # Change the control to signup page
    driver.switch_to.window(signup_page)

    # Get Name and Email based on User detection
    name = name_detection(user)
    email = email_detection(user)

    # Name
    driver.find_element_by_name('eaa$TextboxName').send_keys(name)
    # Email
    driver.find_element_by_name('eaa$TextboxEmail').send_keys(email)
    # Click the Confirm Button
    driver.find_element_by_id("eaa_ButtonOK").click()

    # Add Reminder
    # driver.find_element_by_id("eaa_btnAtmc").click()
    # driver.implicitly_wait(3)

    driver.quit()

    print("Cocke Bot Successful for User: " + user + "\n Confirmation Email Sending...")
    now = datetime.now()
    print("end task...", now)
    
def user_day_detection(user):
    # If-Else Based on Day of Week
    my_date = datetime.today().strftime('%A')
    if my_date == 'Sunday':
        # Wednesday Slot
        if user == "Sam":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452509"
        elif user == "Riley":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150453114"
        elif user == "Ethan":
            pass
    elif my_date == 'Monday':
        # Thursday Slot
        if user == "Sam":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452500"
        elif user == "Riley":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150453115"
        elif user == "Ethan":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452500"
    elif my_date == 'Tuesday':
        # Friday Slot
        if user == "Sam":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452511"
        elif user == "Riley":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150453116"
        elif user == "Ethan":
            pass
        elif user == "Zach":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452943"
    elif my_date == 'Wednesday':
        # Saturday Slot
        if user == "Sam":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452001"
        elif user == "Riley":
            pass
        elif user == "Ethan":
            pass
    elif my_date == 'Thursday':
        # Sunday Slot
        if user == "Sam":
            pass
        elif user == "Riley":
            pass
        elif user == "Ethan":
            pass
    elif my_date == 'Friday':
        # Monday Slot
        if user == "Sam":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452497"
        elif user == "Riley":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150453102"
        elif user == "Ethan":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452497"
        elif user == "Zach":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150452929"
    elif my_date == 'Saturday':
        # Tuesday Slot
        if user == "Sam":
            pass
        elif user == "Riley":
            return "https://www3.vmi.edu/cocke-hall/?trumbaEmbed=view%3Devent%26eventid%3D150453113"
        elif user == "Ethan":
            pass


def name_detection(user):
    if user == "Sam":
        return "Estes, Samuel"
    elif user == "Riley":
        return "Dodge, Riley"
    elif user == "Ethan":
        return "Gilmore, Ethan"
    elif user == "Zach":
        return "Branner, Zach"

def email_detection(user):
    if user == "Sam":
        return "estessj22@mail.vmi.edu"
    elif user == "Riley":
        return "dodgerj2213@mail.vmi.edu"
    elif user == "Ethan":
        return "gilmoreea22@mail.vmi.edu"
    elif user == "Zach":
        return "brannerzt22@mail.vmi.edu"

def login_credentials():
    return "estessj22:SaEs50567Z94C2!@"

if __name__ == "__main__":
    main()



