import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_data(filename='network_speeds.csv'):
    timestamps, download_speeds, upload_speeds, pings = [], [], [], []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            timestamps.append(datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S.%fZ'))
            download_speeds.append(float(row[1]) / 1e6)  # Convert to Mbps
            upload_speeds.append(float(row[2]) / 1e6)    # Convert to Mbps
            pings.append(float(row[3]))
    return timestamps, download_speeds, upload_speeds, pings

def plot_data(timestamps, download_speeds, upload_speeds, pings):
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, download_speeds, label='Download Speed (Mbps)')
    plt.plot(timestamps, upload_speeds, label='Upload Speed (Mbps)')
    plt.plot(timestamps, pings, label='Ping (ms)')
    plt.xlabel('Time')
    plt.ylabel('Speed')
    plt.title('Network Speeds Over Time')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    timestamps, download_speeds, upload_speeds, pings = read_data()
    plot_data(timestamps, download_speeds, upload_speeds, pings)
