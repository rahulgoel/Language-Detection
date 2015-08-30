import urllib
import urllib2
import requests


values = {'text' : "this be a test" }
r = requests.post('http://localhost:8000/lang_id/',data = values)

print(r.text)
