# main.py
# Author: Sukru Ozan
# Date: 04/02/2025

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

# URL of the earthquake data
URL = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"

# Directory where earthquake data will be stored
DATA_DIR = "earthquake_data"

def fetch_earthquake_data():
    response = requests.get(URL)
    response.encoding = "windows-1254"  # Ensure correct encoding

    if response.status_code != 200:
        print("Failed to retrieve data")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    pre_tag = soup.find("pre")

    if not pre_tag:
        print("Data format has changed.")
        return None

    lines = pre_tag.text.strip().split("\n")
    header_index = next(i for i, line in enumerate(lines) if "Tarih" in line)

    data_lines = lines[header_index + 1:]  # Extract data lines

    earthquakes = []
    for line in data_lines:
        parts = line.split()
        if len(parts) >= 10:
            date = parts[0]
            time = parts[1]
            latitude = parts[2]
            longitude = parts[3]
            depth = parts[4]
            md = parts[5] if parts[5] != "-.-" else None
            ml = parts[6] if parts[6] != "-.-" else None
            mw = parts[7] if parts[7] != "-.-" else None
            location = " ".join(parts[8:])

            earthquakes.append([date, time, latitude, longitude, depth, md, ml, mw, location])

    df = pd.DataFrame(earthquakes, columns=["Date", "Time", "Latitude", "Longitude", "Depth", "MD", "ML", "Mw", "Location"])

    # Get current year and month
    now = datetime.datetime.now()
    year_folder = os.path.join(DATA_DIR, str(now.year))
    os.makedirs(year_folder, exist_ok=True)  # Create year folder if not exists

    # Define monthly CSV file
    month_file = os.path.join(year_folder, f"{now.strftime('%m')}.csv")

    # Load existing data if file exists
    if os.path.exists(month_file):
        existing_df = pd.read_csv(month_file, dtype=str)
    else:
        existing_df = pd.DataFrame(columns=["Date", "Time", "Latitude", "Longitude", "Depth", "MD", "ML", "Mw", "Location"])

    # Merge new data, avoiding duplicates
    combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=["Date", "Time", "Latitude", "Longitude"], keep="last")

    # Save updated data
    combined_df.to_csv(month_file, index=False)
    print(f"Updated {month_file} with new earthquake data.")

if __name__ == "__main__":
    fetch_earthquake_data()
