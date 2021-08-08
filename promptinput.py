import socket
import sys
import time
import os
import inspect
import pip
import random
import platform
import webbrowser
pip.main(['install', 'psutil'])
pip.main(['install', 'colorama'])
from colorama import init, Fore, Back, Style
init(convert=True)
import psutil
from datetime import datetime
__dirpath__ = os.path.dirname(os.path.abspath(globals().get("__file__", "./_")))
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
String1 = "\ "
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(Fore.RED + "PLEASE READ!!! TYPE 'help' FOR A LIST OF COMMANDS!")
print(Fore.WHITE + "")
res = input("Input: ")

def ifvar():
    print("\n")
    res = input("Input: ")
    if res == "info":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        info()
    if res == "close":
        print("closing in 5 secs")
        time.sleep(5)
        exit()
    if res == "exit":
        print("closing in 5 secs")
        time.sleep(5)
        exit()
    if res == "help":
        help()
    if res == "createtxt":
        createtxt()
    if res == "calculate":
        calculate()
    if res == "secret":
        secret()
    if res == "openlink":
        openlink()
    while res != "info" and res != "close" and res != "exit" and res != "help" and res != "createtxt" and res != "calculate" and res != "secret" and res != "openlink":
        print("Invalid Input")
        ifvar()

def help():
    print(Fore.CYAN + "Hello. You're using bean's terminal, here's a list of everything you can do:")
    print(Fore.BLUE + "info - displays system info.")
    print(Fore.BLUE + "close/exit - exits the program.")
    print(Fore.BLUE + "createtxt - create a txt file with custom text and name.")
    print(Fore.BLUE + "calculate - lets you calculate a sum, NOTE - DO NOT USE +=, ==, -=, <=, ETC, THEY WILL NOT WORK AND THE PROGRAM WILL CRASH.")
    print(Fore.BLUE + "secret - uses secret command.")
    print(Fore.BLUE + "openlink - opens specified link in input")
    print(Fore.BLUE + "help - shows this.")
    print(Fore.WHITE + "")
    ifvar()

def secret():
    webbrowser.open_new_tab("https://bit.ly/3jH4MBA")
    ifvar()

def openlink():
    link = input("Link: ")
    if "https://" not in link:
        webbrowser.open_new_tab("https://" + link)
        ifvar()
    else:
        webbrowser.open_new_tab(link)
        ifvar()

def createtxt():
    print("Type your text below:")
    fileinput = input("Text: ")
    print("Type your file name below:")
    filename = input("Text: ")
    file = open(filename + ".txt", "w")
    file.write(fileinput)
    file = open(filename + ".txt")
    ifvar()

def calculate():
    print("Input your calculation below:")
    calculation = input("Calculate: ")
    rawcalc = eval(calculation)
    print(rawcalc)
    ifvar()

def info():
    print("--SYSTEM INFO DEMO--")
    print("")
    print("")
    print("")
    print("")
    print(Fore.CYAN + "Host Info: ")
    print(Fore.CYAN + "Hostname = " + hostname)
    print(Fore.CYAN + "IpAddress = " + ip_address)
    print("")
    print(Fore.BLUE + "File info: ")
    print(Fore.BLUE + "Directory of file = " + __dirpath__ + String1[0] + os.path.basename(__file__))
    print("")
    print(Fore.GREEN + "System info: ")
    print(Fore.GREEN + "Computer was turned on at: " + str(bt.day) + "/" + str(bt.month) + "/" + str(bt.year) + " " + str(bt.hour) + ":" + str(bt.minute) + ":" + str(bt.second))
    print(Fore.GREEN + "Processor Name = " + platform.uname().processor)
    print(Fore.GREEN + "System (Windows, Apple, etc.) = " + platform.uname().system)
    print(Fore.GREEN + "Time: " + current_time)
    print("")
    print(Fore.YELLOW + "Txt section: ")
    print(Fore.YELLOW + "Creating text file with name 'log.txt' for test...")
    my_file = open("log.txt", "w")
    my_file.write("Here's the first line!\n")
    my_file.write("Here's the second line!\n")
    my_file.write("Maybe a third won't hurt.\n")
    my_file.write("Oh and here's a random number: " + str(random.randrange(0,10)))
    my_file = open("log.txt")
    print("Created!")
    print(Fore.WHITE + "")
    ifvar()

if res == "info":
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    info()
if res == "close":
    print("closing in 5 secs")
    time.sleep(5)
    exit()
if res == "exit":
    print("closing in 5 secs")
    time.sleep(5)
    exit()
if res == "help":
    help()
if res == "createtxt":
    createtxt()
if res == "calculate":
    calculate()
if res == "secret":
    secret()
if res == "openlink":
    openlink()
while res != "info" and res != "close" and res != "exit" and res != "help" and res != "createtxt" and res != "calculate" and res != "secret" and res != "openlink":
    print("Invalid Input")
    ifvar()
