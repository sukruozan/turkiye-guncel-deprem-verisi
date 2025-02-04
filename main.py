# main.py
# Author: Sukru Ozan
# Date: 04/02/2025
import sys
import os
import time 
import requests

URL="http://www.koeri.boun.edu.tr/scripts/lst2.asp"

# main function
def main():
    # todays year
    year = time.strftime("%Y")
    # check whether there is a folder for the year
    if not os.path.exists(year):
        os.makedirs(year)
    # check whether there is a folder for the month

    response = requests.get(URL)
    response.encoding = "windows-1254"  # Ensure correct encoding
    
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None
    else:
        print("Data retrieved successfully")
        # write the data to a file
        with open(f"{year}/data.txt", "w") as file:
            file.write(response.text)
        
    return None

# main function
if __name__ == "__main__":
    main()