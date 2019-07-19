# scaling-octo-waffle-webscraping
Scrape data to determine parcels under Rent Stabilization in the city of Los Angeles

## First
Run `create_pin_list.py` to create list of all the PINs in Los Angeles. This script also delete unnecessary columns to reduce file size.

## Second
Run `scrape_RSO_content.py` to capture PINs with under the Rent Stabilization (RSO) ordinance. As a courtesy there is a pause, `time.sleep(0.02)`, between each request.

## Content
Input CSV is found in the Resources folder. It is a subset of parcel data because of free repository file size limitations.
