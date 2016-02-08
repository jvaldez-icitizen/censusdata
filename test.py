from google.appengine.ext.remote_api import remote_api_stub
from census import census

remote_api_stub.ConfigureRemoteApiForOAuth('8ae6c23cc76eaa3294f70aaa7bdbcf1ce648.appspot.com',
                                           '/_ah/remote_api')

# Fetch the most recent 10 guestbook entries
entries = census.Greeting.all().order("-date").fetch(10)
# Create our own guestbook entry
census.Greeting(content="A greeting").put()
