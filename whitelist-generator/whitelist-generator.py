import requests
import sys
import os
import time

gamertag = input("Please enter the gamertag of the player input\n> ")
uuidResponse = requests.get(f"https://floodgate-uuid.heathmitchell1.repl.co/uuid?gamertag={gamertag.replace(' ','+')}").text
print(uuidResponse)

outputType = input("Please specify the output type. Enter a single number out of the list below:\n(1) Hyphenated hexadecimal\n(2) No output\n> ")
if outputType == "1":
    uuid = uuidResponse[16+len(gamertag):]
    print("UUID is "+uuid)
    output = open(os.path.dirname(os.path.abspath(__file__))+"\hyphenhex.txt", "w")
    output.write("\n\nRequested UUID of \""+gamertag+"\":\n")
    output.write(uuid)
    output.close
    print("UUID has been printed to output file")

sys.exit(0)