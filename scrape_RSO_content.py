# DESC: Scrape a website to find parcel's in the city of Los Angeles that are 
#       classified under the rent stabilization ordinace (RSO).

# Import libraries
import requests
from bs4 import BeautifulSoup
import json
from prep_pin import my_list
import time
import csv

# Open CSV
# set new line to '' to prevent extra carriage return
with open('Resources/output.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    for m in my_list:
        # specify the url containing content to scrape
        quote_page = requests.get('http://zimas.lacity.org/map.aspx?pin='+m+'&ajax=yes').text

        # create parser for text
        soup = BeautifulSoup(quote_page, "lxml")

        # Find all values
        soup.find_all('td', {'class': 'sorting_1'})

        # Loop through values
        count = 0
        for val in soup.find_all('td'):
            if val.get_text().startswith("Rent Stab"): # Grab td to work with
                count +=1
                if val.find_next_sibling("td").text == 'Yes':
                    print(m)
                    writer.writerow([m])
                    # pause for one second
                    time.sleep(.02)
            else:
                pass
print(count)