import requests
import sys
import os
import time

platform = input("What platform is the player you are checking on?\n(1) Java (normal use of this script, uses usernames)\n(2) Bedrock (if you use Geyser and Floodgate, uses gamertags)\n> ")

# Bedrock
if platform == "2":
    gamertag = input("Please enter the gamertag of the player input\n> ")
    print("Fetching UUID from floodgate-uuid.heathmitchell1.repl.co\nThis may take a moment...")
    try:
        uuidResponse = requests.get(f"https://floodgate-uuid.heathmitchell1.repl.co/uuid?gamertag={gamertag.replace(' ','+')}").text
    except:
        print("Something went wrong\nPlease check your internet, otherwise the API may be unavalible\nCheck ./uuid/error.log for a full error log")
        error = open(os.path.dirname(os.path.abspath(__file__))+"\error.log", "w")
        error.write("All known info is as follows:\n")
        error.write("Platform request = Bedrock\n")
        error.write("Gamertag requested = "+gamertag+"\n")
        error.write("Tried URL = "+f"https://floodgate-uuid.heathmitchell1.repl.co/uuid?gamertag={gamertag.replace(' ','+')}\n")
        error.write("Error occured while attempting to fetch Floodgate UUID, please check the above URL to see if the API is online")
        error.close
        sys.exit(1)
    print(uuidResponse)

    outputType = input("Please specify the output type. Enter a single number out of the list below:\n(1) Hyphenated hexadecimal (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)\n(2) No output (closes script)\n> ")

    # Hyphen-hex
    if outputType == "1":
        uuid = uuidResponse[16+len(gamertag):]
        print("UUID is "+uuid)
        output = open(os.path.dirname(os.path.abspath(__file__))+"\hyphenhex.txt", "a")
        output.write("\n\nRequested UUID of \""+gamertag+"\":\n")
        output.write(uuid)
        output.close
        print("UUID has been printed to output file (at ./uuid/hyphenhex.txt)")

# Java
if platform == "1":
    username = input("Please enter the username of the player input\n> ")
    print("Fetching UUID from api.mojang.com\nThis may take a moment...")
    try:
        uuidResponse = requests.get(f"https://api.mojang.net/{username}").text
    except:
        print("Something went wrong\nPlease check your internet, otherwise the Mojang API may be unavalible")
        error = open(os.path.dirname(os.path.abspath(__file__))+"\error.log", "w")
        error.write("All known info is as follows:\n")
        error.write("Platform request = Java\n")
        error.write("Username requested = "+username+"\n")
        error.write("Tried URL = "+f"https://api.mojang.net/{username}\n")
        error.write("Error occured while attempting to fetch User UUID, please check the above URL to see if the API is online")
        error.close
        sys.exit(1)
    print(uuidResponse)

sys.exit(0)

### Exit Codes ###
# 0 = success
# 1 = Network error getting UUID