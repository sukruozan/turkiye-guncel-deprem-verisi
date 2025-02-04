# main.py
# Author: Sukru Ozan
# Date: 04/02/2025
import sys
import os
import time 


# main function
def main():
    # todays year
    year = time.strftime("%Y")
    # check whether there is a folder for the year
    if not os.path.exists(year):
        os.makedirs(year)
    # check whether there is a folder for the month    

    return None

# main function
if __name__ == "__main__":
    main()