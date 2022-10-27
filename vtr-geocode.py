import requests
import urllib
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import time
import re

requests.urllib3.disable_warnings()
# urllib.parse.urlencode(geocode_post_vars)
locData = json.loads(open("hero-digital/locator/querystring/vtr/vtr.json", "r").read())
bingKey = "AoZktRDf56_rJu2MkwaO2mUnOLn5FgKAd5o4V5KKhWzK85flP9UhKcKljSL1a6qL"
locationsURL = "https://dev.virtualearth.net/REST/v1/Locations?"


def geocode(url):
    r = requests.get(url, verify=False)
    if r.ok:
        jdata = r.json()["resourceSets"][0]["resources"][0]
        jdata["foundResults"] = True
        return jdata
    else:
        return {"foundResults": False}


with open("hero-digital/locator/querystring/vtr/places.json", "w") as f:
    f.write("[]")
    f.close()

for n, loc in enumerate(locData):
    id = re.sub("\W", "", loc["Name"]) + "_" + str(n)
    loc["EntityID"] = id
    params = urllib.parse.urlencode(loc["geocodeData"])
    loc["geolocatedData"] = geocode(f"{locationsURL}{params}&o=json&key={bingKey}")
    jsonFile = json.loads(open("hero-digital/locator/querystring/vtr/places.json", "r").read())
    jsonFile.append(loc)
    open("hero-digital/locator/querystring/vtr/places.json", "w").write(json.dumps(jsonFile, indent=4))
    time.sleep(1)

print("DONE")
