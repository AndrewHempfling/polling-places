import json
from time import localtime, strftime, gmtime, strptime, mktime
from datetime import datetime
import re

jsonFile = json.loads(open("hero-digital/locator/querystring/vtr/places copy 2.json", "r").read())

for p in jsonFile:
    # p["pollingDays"] = []
    #    if p["electionDay"]:
    #        p["pollingDays"].append("electionDay")
    #    if p["earlyVoting"]:
    #        p["pollingDays"].append("earlyVoting")

    for h in p["hoursofOperation"]:
        h["close"] = h["open"].split("T")[0] + "T" + h["close"].split("T")[1]
        # strptime(h["open"], "%Y-%m-%dT%H:%M:%S.%fZ")


open("hero-digital/locator/querystring/vtr/places.json", "w").write(json.dumps(jsonFile, indent=4))
