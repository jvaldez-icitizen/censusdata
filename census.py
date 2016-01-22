import cgi
import urllib2
import csv
import sys
import json
import re
import requests

import census

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed

class Sex(ndb.Model):
    male = ndb.StringProperty()
    female = ndb.StringProperty()

class Age(ndb.Model):
    fiveyears = ndb.StringProperty()

class OneRace(ndb.Model):
    white = ndb.StringProperty()

class State(ndb.Model):
    """ Model for a listing of state items """
    state = ndb.StringProperty()
    year  = ndb.IntegerProperty()
    source = ndb.StringProperty()
    sex = ndb.StructuredProperty(Sex)
    age = ndb.StructuredProperty(Age)
    onerace = ndb.StructuredProperty(OneRace) 
    #date = ndb.DateTimeProperty(auto_now_add=True)

#### Main Thread ################


# Male and Female Pop each state 
resp1 = requests.get('http://api.census.gov/data/2014/acs1?get=NAME,B01001_002E,B01001_026E&for=state:*&key=a5078c224c10c1a5e6be6702543cfc8c9abdebac')

myjson = resp1.json()
headers = myjson[0]
print('yoooooooooooooooooo')
#json.dump(resp3.json(), j, sort_keys=True, indent=4)
for item in myjson:
    sex = Sex()
    sex.populate(male=item[0], female=item[1])
    sexkey = sex.put()
    getsex = sexkey.get()
    print(getsex.male, getsex.female)
    
print('JSON file successfully made!')

