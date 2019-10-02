import requests
import json

request_post_code = requests.get('http://api.postcodes.io/postcodes/' + 'KT13PW')
#Get has path and arguments

print(request_post_code.headers)
#Header has metadata (information of information)

print(request_post_code.json())
#json method gets the data from the link - in the form of arrays (or dict)

print(request_post_code.json()['result']['country'] + ' ' + request_post_code.json()['result']['postcode'])
#using the dictionary key, we extract erquired values

json_var = request_post_code.json()
print(type(json_var))

print(json_var.keys())

result_var = (json_var['result'])
print(result_var.keys())


# Explore this requests package that is installed
# Explore this http://postcodes.io/

#use requests to make a GET request to http://postcode.io/ api
#search for a post code (can be your own or any)

#save response in variable

#Use json library to unpack it.