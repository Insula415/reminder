#!/usr/bin/env python3
import smtplib
import time
import math
from secrets import *
from colorama import Fore, Back, Style

class Emailsender:
    def __init__(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()


        print(Fore.MAGENTA + 'Please make sure less secure app access is turned on')
        print(Style.RESET_ALL)
        print("")

        # Get user input
        reciever = input("Please enter a reciever: ")
        text = input('What do you want to remind them? ')
        print("When do you want them to recieve this reminder?")
        hour = int(input('Input hour (enter 0 if none): '))
        min = int(input('Input minute (enter 0 if none): '))
        secs = int(input('Input seconds: '))
        print("")

        subject = "Reminder"


        message = 'Subject: {}\n\n{}'.format(subject, text)

        fin1 = hour * 3600
        fin2 = min * 60
        final = fin1 + fin2
        num = final + secs

        # Try to convert it to a float
        try:
            num = float(num)

        except ValueError:
            print('Please enter in a number.\n')



        half = num / 2
        quarter = num / 4

        try:
            server.login(sender, pw)
            print(Fore.GREEN + "Login success")
            print(Style.RESET_ALL)

        except:
            print(Fore.RED + "Error logging in")
            print(Style.RESET_ALL)

        print("Reminder will be sent in ", num , " seconds")
        print("Waiting...")
        time.sleep(half)
        print("Half way there...")
        time.sleep(quarter)
        print("Approaching the last quarter...")
        print("")


        try:
            time.sleep(quarter)
            server.sendmail(sender, reciever, message)
            print(Fore.GREEN + "Email has been sent to",reciever)
            print('The reminder was ' + '"' + text + '"')
            print('Sent email at: %s\n' % time.ctime())
            print(Style.RESET_ALL)


        except:
            print(Fore.RED + "Error sending email to",reciever)
            print(Style.RESET_ALL)


        another = input("Want to send another reminder? ")

        answer = {"Y", "y", "yes", "Yes", "YES"}
        if another in answer:
            print(Emailsender())

        else:
            print("Thanks for using my program ~ Fred415")
            print("Exiting")
            quit()

Emailsender()
