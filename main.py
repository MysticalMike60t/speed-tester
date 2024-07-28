import speedtest
import csv
import time
from datetime import datetime

def measure_speed():
    print("Measuring Speed...")
    try:
        print("Testing Speed...")
        s = speedtest.Speedtest()
        print("Testing Download Speed...")
        s.download()
        print("Testing Upload Speed...")
        s.upload()
        print(f"Results of scan: {s.results.dict()}")
        return s.results.dict()
    except speedtest.ConfigRetrievalError as e:
        print(f"Configuration retrieval error: {e}")
    except speedtest.SpeedtestException as e:
        print(f"Speedtest error: {e}")
    return None

def save_data(data, filename='network_speeds.csv'):
    print("Saving Data...")
    if data is not None:
        print("Checking Data...")
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            print("Writing data...")
            writer.writerow([data['timestamp'], data['download'], data['upload'], data['ping']])
            print(f"Wrote data: {data['timestamp'], data['download'], data['upload'], data['ping']}")

if __name__ == "__main__":
    while True:
        sleep_duration = 0
        print("Starting measure speed process...")
        speed_data = measure_speed()
        print("Measured Speed")
        print("Starting save data process...")
        save_data(speed_data)
        print("Saved data")
        print(f"Sleeping for {sleep_duration} seconds...")
        print("------------------------------")
        time.sleep(sleep_duration)
        print("Starting New Scan...")
