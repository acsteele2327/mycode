#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    for x in resp['iss_position']:
        for y in resp['iss_position'][x]:
            print(y)
        #print(f"ISS Position:\nLat: {x['iss_position']['latitude']}\nLon: {x['iss_position']['longitude']}")










if __name__ == "__main__":
    main()
