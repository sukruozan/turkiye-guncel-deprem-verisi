# main.py
# Author: Sukru Ozan
# Date: 04/02/2025

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import os

# URL of the earthquake data
URL="http://www.koeri.boun.edu.tr/scripts/lst2.asp"

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
    data_lines = lines[header_index + 1:]

    earthquakes = []
    for line in data_lines:
        parts = line.split()

        if len(parts) >= 13:
            date = parts[0].replace(".", "-")
            time = parts[1]
            latitude = float(parts[2])
            longitude = float(parts[3])
            depth = float(parts[4])
            md = parts[5] if parts[5] != "-.-" else None
            ml = parts[6] if parts[6] != "-.-" else None
            mw = parts[7] if parts[7] != "-.-" else None
            location = " ".join(parts[8:])

            earthquakes.append([date, time, latitude, longitude, depth, md, ml, mw, location])

    df_new = pd.DataFrame(
        earthquakes,
        columns=[
            "Date",
            "Time",
            "Latitude",
            "Longitude",
            "Depth",
            "MD",
            "ML",
            "Mw",
            "Location",
        ],
    )

    # Determine the storage path (YYYY/MM.csv)
    now = datetime.datetime.now()
    year_folder = str(now.year)
    month_file = f"{now.strftime('%m')}.csv"
    os.makedirs(year_folder, exist_ok=True)
    file_path = os.path.join(year_folder, month_file)

    if os.path.exists(file_path):
        # Read the existing data
        df_existing = pd.read_csv(file_path)

        # Convert data types to match for proper comparison
        df_existing["Latitude"] = df_existing["Latitude"].astype(float)
        df_existing["Longitude"] = df_existing["Longitude"].astype(float)

        # Merge new and existing data, updating rows with same (Date, Time, Latitude, Longitude)
        df_combined = pd.concat([df_existing, df_new])
        df_combined.drop_duplicates(
            subset=["Date", "Time", "Latitude", "Longitude"], keep="last", inplace=True
        )
    else:
        df_combined = df_new

    # Save back to the CSV file
    df_combined.to_csv(file_path, index=False)
    print(f"Updated {file_path}")


if __name__ == "__main__":
    fetch_earthquake_data()
