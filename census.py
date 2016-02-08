'''
 Connects with Census api and datastore instance
 creates entities in the datastore from the census data. 
 
 @author Jason Valdez

'''

# Tools for connections
import requests
import oauth2client
import getpass
import sys
from google.appengine.ext.remote_api import remote_api_stub

# Tools for the datastore
from google.appengine.api import users
from google.appengine.ext import ndb, db

# Grab all the available api calls and models
from api_calls import *
from census_models import *


######### Datastore Connection #########

# auth function used to return username and password if needed
# if just local testing, username and pass can be blank.
def auth_function():
    return('','')

# Remote Api config for remote connection
# replace SERVERNAME with Project ID
def remoteconnection():
    server = 'census-1197.appspot.com'

    remote_api_stub.ConfigureRemoteApiForOAuth(server,'/_ah/remote_api', secure=True)


# Remote Api config for local testing

# Run local server using below command from google_appengine dir.
# python dev_appserver.py --clear_datastore=yes --api_port=46464 census

def localconnection():
    server = 'localhost:42776'

    remote_api_stub.ConfigureRemoteApi(None, '/_ah/remote_api', auth_function, server)


def usage():
    print('Invalid number of Arguments')
    print('Usage: census.py local/remote')
    sys.exit(0)

#### Main Thread ################
if len(sys.argv) < 2:
    usage()
if sys.argv[1] == 'local':
    localconnection()
if sys.argv[1] == 'remote':
    remoteconnection()

# Make connection and get response
resp1 = requests.get(age_api_call)
resp2 = requests.get(race_api_call)

# Grab census json objects.
myjson = resp1.json()
myjson2 = resp2.json()

# Remove headers from json.
myjson.pop(0)
myjson2.pop(0)

# First Api call.
# Age and sex populations per state
state_keys = []

for item in myjson:
    sex = Sex()
    age = Age()
    sex.populate(male=int(item[1]), female=int(item[25]))
    age.populate(male_under_5=int(item[2]),
                    male_5_to_9=int(item[3]),
                    male_10_to_14=int(item[4]),
                    male_15_to_17=int(item[5]),
                    male_18_and_19=int(item[6]),
                    male_20=int(item[7]),
                    male_21=int(item[8]),
                    male_22_to_24=int(item[9]),
                    male_25_to_29=int(item[10]),
                    male_30_to_34=int(item[11]),
                    male_35_to_39=int(item[12]),
                    male_40_to_44=int(item[13]),
                    male_45_to_49=int(item[14]),
                    male_50_to_54=int(item[15]),
                    male_55_to_59=int(item[16]),
                    male_60_and_61=int(item[17]),
                    male_62_to_64=int(item[18]),
                    male_65_and_66=int(item[19]),
                    male_67_to_69=int(item[20]),
                    male_70_to_74 =int(item[21]),
                    male_74_to_79=int(item[22]),
                    male_80_to_84=int(item[23]),
                    male_over_85=int(item[24]),
                    female_under_5=int(item[26]),
                    female_5_to_9=int(item[27]),
                    female_10_to_14=int(item[28]),
                    female_15_to_17=int(item[29]),
                    female_18_and_19=int(item[30]),
                    female_20=int(item[31]),
                    female_21=int(item[32]),
                    female_22_to_24=int(item[33]),
                    female_25_to_29=int(item[34]),
                    female_30_to_34=int(item[35]),
                    female_35_to_39=int(item[36]),
                    female_40_to_44=int(item[37]),
                    female_45_to_49=int(item[38]),
                    female_50_to_54=int(item[39]),
                    female_55_to_59=int(item[40]),
                    female_60_and_61=int(item[41]),
                    female_62_to_64=int(item[42]),
                    female_65_and_66=int(item[43]),
                    female_67_to_69=int(item[44]),
                    female_70_to_74 =int(item[45]),
                    female_74_to_79=int(item[46]),
                    female_80_to_84=int(item[47]),
                    female_over_85=int(item[48])
                    )
    state = State(state = item[0], year=2014,
                    source='ACS 1-year', sex = sex,
                    age = age)
    statekey = state.put()
    state_keys.append(statekey)
    getstate = statekey.get()
    print(getstate.state,getstate.sex.male, getstate.sex.female)


# Second Api call
# Race populations per state
keycount = 0
for item in myjson2:
    race = Race()
    # Replace any None values with zero.
    for i in range(0, len(item)):
        if not item[i]:
            item[i] = 0
    race.populate(white = int(item[1]), black = int(item[2]),
                    american_indian_and_alaska_native = int(item[3]),
                    asian = int(item[4]),
                    native_hawaiian_and_other_pacific = int(item[5]),
                    other_race = int(item[6]),
                    hispanic_latino = int(item[7]))
    statekey = state_keys[keycount]
    state = statekey.get()
    state.race = race
    state.put()
    keycount += 1
  

print('Datastore successfully populated with new entities!!!')

