# coding: utf-8
import requests

host_url = 'http://localhost:8000/lang_id/'

# English
values = {'text' : "this be a test" }
r = requests.post (host_url, data = values)
print(r.text)

# French
values = {'text' : "cest un test" }
r = requests.post (host_url, data = values)
print(r.text)

# German
values = {'text' : "das ist ein Test" }
r = requests.post (host_url, data = values)
print(r.text)

# Portugese
values = {'text' : "isso é um teste" }
r = requests.post (host_url, data = values)
print(r.text)

# Spanish
values = {'text' : "esto es un examen" }
r = requests.post (host_url, data = values)
print(r.text)

# Itatian
values = {'text' : "questa è una prova" }
r = requests.post (host_url, data = values)
print(r.text)
