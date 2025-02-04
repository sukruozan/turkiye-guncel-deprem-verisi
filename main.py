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
            date = parts[0]  # YYYY.MM.DD
            time = parts[1]
            latitude = parts[2]
            longitude = parts[3]
            depth = parts[4]
            md = parts[5] if parts[5] != "-.-" else None
            ml = parts[6] if parts[6] != "-.-" else None
            mw = parts[7] if parts[7] != "-.-" else None
            location = " ".join(parts[8:])

            # Convert date to extract year and month
            date_obj = datetime.datetime.strptime(date, "%Y.%m.%d")
            year_folder = str(date_obj.year)
            month_file = os.path.join(year_folder, f"{date_obj.strftime('%m')}.csv")

            earthquakes.append([date, time, latitude, longitude, depth, md, ml, mw, location, year_folder, month_file])

    # Process each month's data separately
    grouped_data = {}
    for row in earthquakes:
        year_folder, month_file = row[-2], row[-1]
        os.makedirs(year_folder, exist_ok=True)  # Ensure the folder exists

        if month_file not in grouped_data:
            grouped_data[month_file] = []

        grouped_data[month_file].append(row[:-2])  # Remove folder details before saving

    for month_file, data in grouped_data.items():
        df = pd.DataFrame(data, columns=["Date", "Time", "Latitude", "Longitude", "Depth", "MD", "ML", "Mw", "Location"])

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