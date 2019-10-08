#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author Παναγιώτης Πράττης/Panagiotis Prattis

"""
A program which uses the API from http://openweathermap.org/api 
to get weather conditions for a location specified using coordinates.
"""

import json
from urllib.request import urlopen

def is_rain(mainWeather):
    #check if there is rain
    if(mainWeather == 'rain'):
        return "I'm singing in the rain!"
    else:
        return False

def temp_response(temp):
    #check if temperatue is above 20
    if(temp > 20):
        return "nice..."
    elif(temp < 5):
        return "brrrr"
    else:
        return False
    
def is_number(numInput):
    #check if user input is number
    try:
        val = int(numInput)
    except ValueError:
        return False
    else:
        return True
    
    
def main():
    lat = input('Please enter the Latitude, e.g. 37.465465: ')
    while is_number(lat) == False
        lat = input('Please enter the Latitude, e.g. 37.465465: ')
    lon = input('Please enter the Longtitude, e.g. 40.50785: ') 
    while is_number(lon) == False:
        lon = input('Please enter the Longtitude, e.g. 40.50785: ')
    
    apikey = 'key'
    with(urlopen('http://api.openweathermap.org/data/2.5/weather?lat={la}&lon={lo}&APPID={apiid}'.format(la = lat, lo = lon, apiid = apikey))) as response:
        jsonObj = json.loads(response.read().decode('utf-8'))
        temp= is_rain(jsonObj.get('weather')[0].get('main')) #get weather condition
        print(rain) if rain != False else None
        temp = temp_response(jsonObj.get('main').get('temp')) #get temperature
        print(temp) if temp != False else None
    
if __name__ == "__main__": main()
