#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Θέμα 4
Λήψη δεδομένων για τις καιρικές συνθήκες  από το API του http://openweathermap.org/api 
για μία περιοχή με βάση τις συντεταγμένες longtitute latitude που δίνονται στο πρόγραμμα.
Αρχικά εγγραφήκαμε για να αποκτήσουμε το απαραίτητο API KEY ώστε να καλέσουμε το API.
Τα δεδομένα που επιστρέφονται από το API τα διαχειριζόμαστε ως JSON.
"""
version = 1.0
developer = "Nikos Kontopoulos"

import json
from urllib.request import urlopen

def is_rain(mainWeather):
    """
    Ελέγχει εάν υπάρχει βροχή
    """
    if(mainWeather == 'rain'):
        return "I'm singing in the rain!"
    else:
        return False

def temp_response(temp):
    """
    Ελέγχει εάν η θερμοκρασία είναι άνω των 20 βαθμών κελσίου
    """
    if(temp > 20):
        return "nice..."
    elif(temp < 5):
        return "brrrr"
    else:
        return False
    
def is_number(numInput):
    """
    Ελέγχουμε εάν ο χρήστης μας έδωσε αριθμούς
    """
    try:
        val = int(numInput)
    except ValueError:
        return False
    else:
        return True
    
    
def main():
    lat = input('Please enter the Latitude, e.g. 37.465465: ') #λαμβάνουμε από το χρήστη το latitude
    while is_number(lat) == False: #εάν δεν μας δώσει αριθμό επαναλαμβάνουμε το ερώτημα
        lat = input('Please enter the Latitude, e.g. 37.465465: ')
    lon = input('Please enter the Longtitude, e.g. 40.50785: ') #λαμβάνουμε από το χρήστη το longtitude
    while is_number(lon) == False: #εάν δεν μας δώσει αριθμό επαναλαμβάνουμε το ερώτημα
        lon = input('Please enter the Longtitude, e.g. 40.50785: ')
    
    apikey = '237a5941a20b34e865b5290b8215efde' #είναι API ID που λάβαμε κατά την εγγραφή μας
    with(urlopen('http://api.openweathermap.org/data/2.5/weather?lat={la}&lon={lo}&APPID={apiid}'.format(la = lat, lo = lon, apiid = apikey))) as response:
        jsonObj = json.loads(response.read().decode('utf-8'))
        temp= is_rain(jsonObj.get('weather')[0].get('main')) #Γενική ένδειξη του καιρού που επικρατεί για να εξετάσουμε εάν λέει rain
        print(rain) if rain != False else None #εάν υπάρχει μήνυμα από τη συνάρτηση το επιστρέφει
        temp = temp_response(jsonObj.get('main').get('temp')) #Η θερμοκρασία που επικρατεί
        print(temp) if temp != False else None #εάν υπάρχει μήνυμα από τη συνάρτηση το επιστρέφει
    
if __name__ == "__main__": main()
